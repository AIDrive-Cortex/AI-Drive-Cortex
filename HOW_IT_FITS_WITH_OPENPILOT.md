# How This Project Fits with openpilot

This project is designed as a **research and learning companion** to openpilot,
not a replacement or fork.

## Intended Usage
- Models run offline or in shadow mode only
- Inputs come from existing driving logs
- Outputs are compared to human actions
- No CAN, steering, brake, or throttle commands are generated

## Why This Matters
Human driver reactions contain rich signals:
- Micro steering corrections
- Pedal hesitations
- Social responses to nearby vehicles

Learning from these signals can improve perception and planning systems
without introducing safety risk.
