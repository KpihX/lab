import torch
import torch.nn as nn
import torch.nn.functional as F


class FocalLoss(nn.Module):
    def __init__(self, gamma: float = 1.5):
        super().__init__()
        self.gamma = gamma

    def forward(self, logits: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        ce_loss = F.cross_entropy(logits, targets, reduction="none")
        probs = torch.exp(-ce_loss)
        focal_loss = ((1.0 - probs) ** self.gamma) * ce_loss
        return focal_loss.mean()
