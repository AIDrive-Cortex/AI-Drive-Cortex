import torch
import torch.nn as nn

from driver_cues import DriverCueEncoder
from driver_state import DriverStateEncoder
from social_behavior import SocialBehaviorEncoder

class HumanAwareDrivingModel(nn.Module):
    """
    Multimodal perception model incorporating human driver reactions
    and social driving context. Perception-only (no vehicle control).
    """

    def __init__(self):
        super().__init__()

        # Visual perception backbone
        self.vision = nn.Sequential(
            nn.Conv2d(3, 24, kernel_size=5, stride=2),
            nn.ReLU(),
            nn.Conv2d(24, 36, kernel_size=5, stride=2),
            nn.ReLU(),
            nn.Conv2d(36, 48, kernel_size=5, stride=2),
            nn.ReLU(),
        )

        self.driver_cues = DriverCueEncoder()
        self.driver_state = DriverStateEncoder()
        self.social = SocialBehaviorEncoder()

        self.lstm = nn.LSTM(
            input_size=(48 * 10 * 10) + 64 + 64 + 128,
            hidden_size=256,
            batch_first=True
        )

        self.head = nn.Linear(256, 1)

    def forward(self, images, cues, state, social):
        B, T, C, H, W = images.shape

        images = images.view(B * T, C, H, W)
        visual = self.vision(images)
        visual = visual.view(B, T, -1)

        cues = self.driver_cues(cues)
        state = self.driver_state(state)
        social = self.social(social)

        fused = torch.cat([visual, cues, state, social], dim=-1)
        lstm_out, _ = self.lstm(fused)

        return self.head(lstm_out[:, -1])
