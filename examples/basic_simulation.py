#!/usr/bin/env python3
"""
Basic 10G Lab Simulation Example
"""

from simulator.network_sim import NetworkSimulator

if __name__ == "__main__":
    sim = NetworkSimulator(node_count=12)
    sim.run_simulation(steps=30)
    sim.print_status()
