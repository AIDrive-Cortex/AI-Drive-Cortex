import torch
import torch.nn as nn

class SocialBehaviorEncoder(nn.Module):
    """
    Encodes surrounding vehicle behavior as social driving context.
    Examples include relative speed, distance, and motion patterns.
    """

    def __init__(self, vehicle_features=5):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(vehicle_features, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU()
        )

    def forward(self, x):
        """
        x shape: (batch, time, vehicles, features)
        """
        # Aggregate across nearby vehicles
        x = x.mean(dim=2)
        return self.encoder(x)
