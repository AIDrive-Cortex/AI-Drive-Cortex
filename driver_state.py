import torch
import torch.nn as nn

class DriverStateEncoder(nn.Module):
    """
    Encodes abstracted driver monitoring signals such as
    gaze direction, head pose, and attention indicators.

    No identity or biometric recognition is performed.
    """

    def __init__(self, input_dim=6):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, 64),
            nn.ReLU()
        )

    def forward(self, state):
        """
        state shape: (batch, time, features)
        """
        return self
