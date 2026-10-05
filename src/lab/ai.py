"""KπX-Labs AI utility kit."""

from collections.abc import Sequence
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    precision_recall_curve,
    auc,
    log_loss,
    matthews_corrcoef,
    average_precision_score,
)

def pred_eval(
    gts,
    preds,
    probas,
    criterion=log_loss,
    display: bool = True,
    plot: bool = True,
    labels: Sequence | None = None,
) -> tuple[dict[str, Any], np.ndarray | None]:
    """Evaluate predictions against ground truths.

    Knows nothing about the model, the split or the task: just gts, preds and
    probas in, metrics and optional visuals out.

    Args:
        gts: Ground truth labels, shape (n_samples,).
        preds: Predicted labels, shape (n_samples,), same label space as gts.
        probas: Predicted probabilities of the positive class, shape (n_samples,).
        criterion: Loss callable, signature criterion(gts, probas). Defaults to
            sklearn.metrics.log_loss.
        display: If True, print metrics and classification report.
        plot: If True, draw confusion matrix and PR curve.
        labels: Explicit class order. Inferred (sorted) when None.

    Returns:
        (results, axs).
            results: dict with keys "loss", "cm", "class_report", "mcc",
                "avg_pr", "pr_auc", "pr", "rec", "threshold", "labels".
            axs: ndarray of 2 Axes (cm + PR) when plot=True, else None.
    """
    # Class order shared by the confusion matrix, the report and the axes.
    # Without an explicit order, both label sets must agree before deriving it.
    if labels:
        labels = list(labels)
    else:
        classes_gts = set(gts)
        classes_preds = set(preds)
        if classes_gts != classes_preds:
            raise ValueError(
                "gts and preds must share the same classes, got "
                f"{sorted(classes_gts)} for gts and {sorted(classes_preds)} for preds. "
                "Pass labels= to force the class order explicitly."
            )
        labels = sorted(classes_gts)

    # Metrics, computed unconditionally so `results` stays complete when silent.
    loss = criterion(gts, probas)
    cm = confusion_matrix(gts, preds, labels=labels)
    class_report = classification_report(gts, preds, labels=labels, output_dict=True, zero_division=0)
    mcc = matthews_corrcoef(gts, preds)
    avg_pr = average_precision_score(gts, probas)
    pr, rec, threshold = precision_recall_curve(gts, probas)
    pr_auc = auc(rec, pr)

    results = {
        "loss": loss,
        "cm": cm,
        "class_report": class_report,
        "mcc": mcc,
        "avg_pr": avg_pr,
        "pr_auc": pr_auc,
        "pr": pr,
        "rec": rec,
        "threshold": threshold,
        "labels": labels,
    }

    if display:
        print("Loss:", loss)
        print("MCC:", mcc)
        print("AVG-PR:", avg_pr)
        print("PR-AUC:", pr_auc)
        print("Classification report")
        print(classification_report(gts, preds, labels=labels, zero_division=0))

    axs = None
    if plot:
        # Two panels: confusion matrix on the left, PR curve on the right.
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))

        sns.heatmap(cm, annot=True, ax=axs[0], xticklabels=labels, yticklabels=labels)
        axs[0].set_title("Confusion matrix")
        axs[0].set_xlabel("Predicted label")
        axs[0].set_ylabel("Ground truth")

        axs[1].plot(rec, pr, label="PR curve")
        axs[1].set_xlabel("recall")
        axs[1].set_ylabel("precision")
        axs[1].set_title("PR curve")
        axs[1].legend()

        plt.tight_layout()
        plt.show()

    return results, axs
