"""KπX-Labs AI utility kit."""

from collections.abc import Sequence
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import (
    auc,
    average_precision_score,
    classification_report,
    confusion_matrix,
    log_loss,
    matthews_corrcoef,
    precision_recall_curve,
)


def class_eval(
    gts,
    preds,
    probas,
    classes: Sequence | None = None,
    criterion=log_loss,
    display: bool = True,
    plot: bool = True,
    figsize: tuple[float, float] = (22, 7),
) -> tuple[dict[str, Any], np.ndarray | None]:
    """Evaluate predictions against ground truths for binary and multiclass.

    Knows nothing about the model, the split or the task: just gts, preds and
    probas in, metrics and visuals out. Everything is reported per label, and
    the same code path serves both binary and multiclass.

    Labels are contiguous integers 0..n-1. The task is read from the labels
    themselves: 2 labels means binary, 3 or more means multiclass.

    Args:
        gts: Ground truth labels, shape (n_samples,), values 0..n-1.
        preds: Predicted labels, shape (n_samples,), same value space.
        probas: Binary flat, shape (n_samples,): score of label 1
            (P(y=0) is then 1 - probas). Binary or multiclass matrix,
            shape (n_samples, n_classes): row-stochastic probabilities,
            column k being the score of label k.
        criterion: Loss callable, signature criterion(gts, probas). Defaults to
            sklearn.metrics.log_loss, which accepts both shapes.
        display: If True, print loss, MCC, macro scores, the classification
            report and the per-label score table.
        plot: If True, draw the confusion matrix, every PR curve and the
            per-label scores.
        figsize: Figure size passed to plt.subplots when plot=True.
            Defaults to (22, 7).
        classes: Optional class names, one per label, length n. Used for the
            report and the axis ticks only. Defaults to the label values.

    Returns:
        (results, axs).
            results: dict with keys "loss", "cm", "class_report", "mcc",
                "avg_pr", "pr_auc", "avg_pr_per_class", "pr_auc_per_class",
                "classes", "labels", "n_classes", "multiclass".
                "avg_pr" and "pr_auc" are the macro means of
                "avg_pr_per_class" and "pr_auc_per_class" respectively: the
                former is the step-wise average precision estimator, the latter
                is the area under the precision-recall curve. Per-label PR
                curve arrays are not stored in results (drawn when plot=True).
            axs: ndarray of 3 Axes (cm, PR curves, per-label scores) when
                plot=True, else None.
    """
    gts = np.asarray(gts).ravel()
    preds = np.asarray(preds).ravel()
    probas = np.asarray(probas)

    # The task is read from the labels themselves, never from the shape of
    # probas: 2 labels means binary, 3 or more means multiclass.
    labels = list(range(int(max(gts.max(), preds.max())) + 1))
    n_classes = len(labels)
    multiclass = n_classes > 2
    if classes is None:
        classes = labels

    # One score per label. Matrix → column k. Flat binary → P(y=1) given,
    # so P(y=0) = 1 - probas. Never reuse the same vector for both labels.
    if probas.ndim == 2 and probas.shape[1] == 1:
        probas = probas.ravel()
    scores_per_class = probas.T if probas.ndim == 2 else (1.0 - probas, probas)

    # Metrics, computed unconditionally so `results` stays complete when silent.
    cm = confusion_matrix(gts, preds, labels=labels)
    class_report = classification_report(
        gts, preds, labels=labels, target_names=classes, output_dict=True, zero_division=0
    )
    mcc = matthews_corrcoef(gts, preds)
    loss = criterion(gts, probas)

    curves = []
    for label, scores in zip(labels, scores_per_class, strict=True):
        scores = np.asarray(scores).ravel()
        positive = gts == label
        precisions, recalls, _ = precision_recall_curve(positive, scores)
        curves.append(
            {
                "label": label,
                "name": classes[label],
                "precisions": precisions,
                "recalls": recalls,
                "avg_pr": average_precision_score(positive, scores),
                "pr_auc": auc(recalls, precisions),
            }
        )

    avg_pr_per_class = np.array([curve["avg_pr"] for curve in curves])
    pr_auc_per_class = np.array([curve["pr_auc"] for curve in curves])
    avg_pr = float(np.mean(avg_pr_per_class))
    pr_auc = float(np.mean(pr_auc_per_class))

    results = {
        "loss": loss,
        "cm": cm,
        "class_report": class_report,
        "mcc": mcc,
        "avg_pr": avg_pr,
        "pr_auc": pr_auc,
        "avg_pr_per_class": avg_pr_per_class,
        "pr_auc_per_class": pr_auc_per_class,
        "classes": classes,
        "labels": labels,
        "n_classes": n_classes,
        "multiclass": multiclass,
    }

    if display:
        print("Loss:", loss)
        print("MCC:", mcc)
        print("AVG-PR:", avg_pr)
        print("PR-AUC:", pr_auc)
        print("Classification report")
        print(
            classification_report(gts, preds, labels=labels, target_names=classes, zero_division=0)
        )
        print(f"{'class':>12} {'avg_pr':>8} {'pr_auc':>8}")
        for curve in curves:
            print(f"{curve['name']:>12} {curve['avg_pr']:>8.4f} {curve['pr_auc']:>8.4f}")

    axs = None
    if plot:
        # Confusion matrix, every PR curve, and every per-label score family.
        # Same three panels for binary and multiclass: nothing is branched on.
        _, axs = plt.subplots(1, 3, figsize=figsize, squeeze=False)
        axs = axs[0]

        sns.heatmap(cm, annot=True, ax=axs[0], xticklabels=classes, yticklabels=classes)
        axs[0].set_title("Confusion matrix")
        axs[0].set_xlabel("Predicted label")
        axs[0].set_ylabel("Ground truth")

        for curve in curves:
            axs[1].plot(
                curve["recalls"],
                curve["precisions"],
                marker="o" if len(curves) < 4 else None,
                markersize=3,
                label=curve["name"],
            )
        axs[1].set_xlabel("recall")
        axs[1].set_ylabel("precision")
        axs[1].set_title("PR curves")
        axs[1].legend()

        families = {"avg_pr_per_class": avg_pr_per_class, "pr_auc_per_class": pr_auc_per_class}
        positions = np.arange(len(classes))
        width = 0.8 / len(families)
        for offset, (family, values) in enumerate(families.items()):
            shift = (offset - (len(families) - 1) / 2) * width
            axs[2].bar(positions + shift, values, width, label=family)
        axs[2].set_xticks(positions)
        axs[2].set_xticklabels(classes, rotation=45, ha="right", fontsize=8)
        axs[2].set_ylabel("score")
        axs[2].set_title("Per-class scores")
        axs[2].legend()

        plt.tight_layout()
        plt.show()

    return results, axs
