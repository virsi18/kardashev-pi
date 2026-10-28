import unittest
import math
from kardashev_pi.physics.lorentz import LorentzRelativityEngine
from kardashev_pi.constants import SPEED_OF_LIGHT

class TestLorentzRelativity(unittest.TestCase):
    def test_lorentz_gamma(self):
        # At v = 0, gamma = 1
        self.assertEqual(LorentzRelativityEngine.calculate_gamma(0.0), 1.0)

        # At v = 0.6c, gamma = 1 / sqrt(1 - 0.36) = 1 / 0.8 = 1.25
        v = 0.6 * SPEED_OF_LIGHT
        self.assertTrue(math.isclose(LorentzRelativityEngine.calculate_gamma(v), 1.25, rel_tol=1e-5))

    def test_spacetime_interval_causality(self):
        # Timelike separation
        s2, causality = LorentzRelativityEngine.compute_spacetime_interval(
            t1=0.0, pos1=(0.0, 0.0, 0.0),
            t2=10.0, pos2=(1000.0, 0.0, 0.0)
        )
        self.assertEqual(causality, "TIMELIKE")
        self.assertGreater(s2, 0)

        # Spacelike separation
        s2_space, causality_space = LorentzRelativityEngine.compute_spacetime_interval(
            t1=0.0, pos1=(0.0, 0.0, 0.0),
            t2=0.000001, pos2=(1000000.0, 0.0, 0.0)
        )
        self.assertEqual(causality_space, "SPACELIKE")
        self.assertLess(s2_space, 0)

    def test_node_divergence(self):
        engine = LorentzRelativityEngine("TERRA_PRIME")
        res = engine.calculate_node_divergence("ARES_MERIDIANI", elapsed_seconds=3600.0)
        self.assertEqual(res["source_node"], "TERRA_PRIME")
        self.assertEqual(res["target_node"], "ARES_MERIDIANI")
        self.assertIn("clock_drift_microseconds", res)

if __name__ == "__main__":
    unittest.main()
