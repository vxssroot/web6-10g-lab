#!/usr/bin/env python3
"""
10G Command Line Interface
Experimental interface for the Web6 10G Lab simulation layer.
"""
import sys
import json
from simulator.network_sim import simulate_network
from simulator.agentnet_sim import simulate_consensus_round
from simulator.quantumlink_sim import simulate_quantum_link

def main():
    if len(sys.argv) < 2:
        print("Usage: python cli/10g.py <command>")
        print("Commands: status | simulate | topology")
        return

    cmd = sys.argv[1]

    if cmd == "status":
        net = simulate_network(16)
        quantum = simulate_quantum_link()
        agent = simulate_consensus_round(32, 3)
        
        status = {
            "10g_core": net,
            "quantum_link": quantum,
            "agentnet": agent,
            "overall_status": "OPERATIONAL"
        }
        print(json.dumps(status, indent=2))

    elif cmd == "simulate":
        print("Running full 10G simulation cycle...")
        result = simulate_network(24)
        print(json.dumps(result, indent=2))

    elif cmd == "topology":
        with open("simulator/topology.json", "r") as f:
            topo = json.load(f)
        print(json.dumps(topo, indent=2))
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()