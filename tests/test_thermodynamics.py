import unittest
from kardashev_pi.physics.thermodynamics import ThermodynamicValueAnchor
from kardashev_pi.constants import PI_GCV_INVARIANT, TEU_TO_JOULES_EQUIVALENCE

class TestThermodynamics(unittest.TestCase):
    def test_gcv_anchor_invariance(self):
        anchor = ThermodynamicValueAnchor()
        self.assertEqual(anchor.gcv_invariant_teu, 314159.0)

        joules = anchor.gcv_to_joules(1.0)
        self.assertEqual(joules, 314159.0 * 1e9)

        pi_recovered = anchor.joules_to_pi_gcv(joules)
        self.assertAlmostEqual(pi_recovered, 1.0, places=7)

    def test_landauer_limit(self):
        anchor = ThermodynamicValueAnchor(system_temperature_kelvin=300.0) # Room temp
        limit = anchor.landauer_limit_per_bit()
        self.assertGreater(limit, 0)
        self.assertTrue(2.8e-21 < limit < 3.0e-21)

    def test_dyson_harvest(self):
        anchor = ThermodynamicValueAnchor()
        res = anchor.dyson_swarm_harvest_telemetry(capture_fraction=1e-8)
        self.assertGreater(res["harvested_power_watts"], 0)
        self.assertGreater(res["pi_gcv_capacity_sec"], 0)
        self.assertEqual(res["gcv_fixed_anchor_teu"], 314159.0)

if __name__ == "__main__":
    unittest.main()
