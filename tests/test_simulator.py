#!/usr/bin/env python3
"""
Unit tests for 10G Lab simulation layer.
"""
import unittest
from simulator.network_sim import simulate_network
from simulator.agentnet_sim import simulate_consensus_round
from simulator.quantumlink_sim import simulate_quantum_link

class Test10GSimulator(unittest.TestCase):

    def test_network_simulation(self):
        result = simulate_network(8)
        self.assertIn("nodes", result)
        self.assertGreater(len(result["nodes"]), 0)

    def test_agentnet_consensus(self):
        result = simulate_consensus_round(16)
        self.assertIn("consensus_score", result)  # Note: adjusted key

    def test_quantum_link(self):
        result = simulate_quantum_link()
        self.assertEqual(result["status"], "STABLE")

if __name__ == "__main__":
    unittest.main()