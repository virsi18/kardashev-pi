import unittest
from kardashev_pi.consensus.minkowski_engine import MinkowskiConsensusEngine
from kardashev_pi.ledger.chain import KardashevChain
from kardashev_pi.constants import PI_GCV_INVARIANT

class TestMinkowskiEngine(unittest.TestCase):
    def test_astral_transaction_gcv_enforcement(self):
        engine = MinkowskiConsensusEngine("TERRA_PRIME")
        tx = engine.create_astral_transaction("Pioneer_Earth", "Pioneer_Mars", 2.0)
        
        self.assertEqual(tx.pi_amount, 2.0)
        self.assertEqual(tx.gcv_value_teu, 2.0 * PI_GCV_INVARIANT)
        self.assertTrue(tx.signature_quantum.startswith("Q-ENTANGLE"))

        # Ingestion should succeed
        success = engine.ingest_transaction(tx)
        self.assertTrue(success)

    def test_chain_mining_and_integrity(self):
        chain = KardashevChain(genesis_node="TERRA_PRIME")
        self.assertEqual(len(chain.chain), 1)
        self.assertEqual(chain.latest_block.index, 0)

        engine = MinkowskiConsensusEngine("LUNA_GATEWAY")
        tx = engine.create_astral_transaction("Node_Luna", "Node_Dyson", 5.0)

        block1 = chain.mine_astral_block("LUNA_GATEWAY", [tx])
        self.assertEqual(block1.index, 1)
        self.assertEqual(block1.total_pi_settled, 5.0)
        self.assertEqual(block1.total_gcv_teu, 5.0 * PI_GCV_INVARIANT)
        self.assertTrue(chain.verify_chain_integrity())

if __name__ == "__main__":
    unittest.main()
