# AI-Drive-Cortex
Research project exploring human-aware, multimodal driving perception inspired by openpilot.
## Human-Reactive and Social Learning

This project explores how driving behavior can be learned from
human reactions and social context, not just road imagery.

Inputs include:
- Driver steering corrections and pedal taps
- Abstracted driver attention and facial cues
- Behavior of surrounding vehicles

All inputs are observational learning signals.
This project does not perform real-time vehicle control.
## Project Roadmap

### Phase 1 — Research & Architecture (Current)
- Define human-aware, multimodal perception models
- Separate perception from vehicle control
- Explore driver reactions and social context conceptually

### Phase 2 — Shadow-Mode Learning (Planned)
- Use recorded driving logs (e.g. openpilot logs)
- Learn from human steering corrections and interventions
- Compare model predictions against human behavior
- No vehicle actuation

### Phase 3 — Evaluation & Iteration (Future)
- Analyze when the model disagrees with human drivers
- Identify uncertainty and hesitation patterns
- Improve perception representations

This project intentionally avoids real-time vehicle control.
``
