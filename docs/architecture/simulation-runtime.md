# Simulation Runtime Architecture

The 10G Lab simulator provides a high-fidelity digital twin of the autonomous networking stack.

## Components
- `network_sim.py` — Core packet routing and latency simulation
- `agentnet_sim.py` — Distributed agent consensus engine
- `quantumlink_sim.py` — Post-quantum channel health modeling

## Node Lifecycle States
- `BOOTING` → `ATTESTING` → `SYNCHRONIZED` → `OPERATIONAL`

Future work includes integration with real eBPF and formal verification.
