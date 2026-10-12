import torch
import torch.nn as nn
import torch.nn.functional as F


def init_kaiming(module: nn.Module) -> None:
    """Initialize network weights using He (Kaiming) normal initialization.

    Applies Kaiming normal distribution (mode='fan_out', nonlinearity='relu') to all
    convolutional and linear layers, preserving activation variance across deep ReLU
    networks. Sets BatchNorm2d affine weights to 1.0 and biases to 0.0.

    Usage:
        model.apply(init_kaiming)

    Args:
        module: A PyTorch module (nn.Module), called recursively by model.apply().
    """
    if isinstance(module, (nn.Conv2d, nn.Linear)):
        nn.init.kaiming_normal_(module.weight, mode="fan_out", nonlinearity="relu")
        if module.bias is not None:
            nn.init.constant_(module.bias, 0.0)
    elif isinstance(module, nn.BatchNorm2d):
        nn.init.constant_(module.weight, 1.0)
        nn.init.constant_(module.bias, 0.0)


class FocalLoss(nn.Module):
    """Multi-class Focal Loss with dynamic modulation factor (1 - p_t)^gamma.

    Down-weights easy examples during training to prevent their accumulated gradients
    from overwhelming hard or tail-class instances. Uses numerically stable formulation
    directly derived from negative log-likelihood (p_t = exp(-CE)).

    Args:
        gamma: Focusing parameter (default: 1.5). Setting gamma=0 recovers standard
            Cross-Entropy loss. Higher values focus more aggressively on hard errors.
    """

    def __init__(self, gamma: float = 1.5):
        super().__init__()
        self.gamma = gamma

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """Compute mean focal loss over a mini-batch.

        Args:
            logits: Unnormalized network predictions of shape (batch_size, num_classes).
            targets: Ground-truth class labels of shape (batch_size,).

        Returns:
            Scalar tensor representing the mean focal loss.
        """
        ce_loss = F.cross_entropy(logits, targets, reduction="none")
        probs = torch.exp(-ce_loss)
        focal_loss = ((1.0 - probs) ** self.gamma) * ce_loss
        return focal_loss.mean()
