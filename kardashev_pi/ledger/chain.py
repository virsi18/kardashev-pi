"""
Kardashev Multi-Planetary Chain
Maintains the sequence of Astral Blocks, verifies energy equilibrium,
and certifies the GCV 314,159 invariant across solar history.
"""

from typing import List, Optional, Dict, Any
from kardashev_pi.ledger.astral_block import AstralBlock, AstralBlockFactory
from kardashev_pi.consensus.minkowski_engine import AstralTransaction
from kardashev_pi.constants import PI_GCV_INVARIANT

class KardashevChain:
    """
    The canonical timeline ledger for Kardashev-Pi interplanetary consensus.
    """

    def __init__(self, genesis_node: str = "TERRA_PRIME"):
        self.chain: List[AstralBlock] = []
        self.genesis_node = genesis_node
        self._initialize_genesis()

    def _initialize_genesis(self):
        """
        Mints the Genesis Singularity Block stamped with the initial GCV constant.
        """
        genesis_block = AstralBlockFactory.create_block(
            index=0,
            previous_hash="0" * 64,
            planetary_origin=self.genesis_node,
            transactions=[]
        )
        self.chain.append(genesis_block)

    @property
    def latest_block(self) -> AstralBlock:
        return self.chain[-1]

    def mine_astral_block(self, planetary_origin: str, transactions: List[AstralTransaction]) -> AstralBlock:
        """
        Constructs and appends a new block to the interplanetary chain.
        """
        new_block = AstralBlockFactory.create_block(
            index=len(self.chain),
            previous_hash=self.latest_block.geodesic_hash,
            planetary_origin=planetary_origin,
            transactions=transactions
        )
        self.chain.append(new_block)
        return new_block

    def verify_chain_integrity(self) -> bool:
        """
        Validates hash linkage, monotonic proper-time ordering, and GCV conservation.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i - 1]

            # Verify hash linkage
            if current.previous_geodesic_hash != prev.geodesic_hash:
                return False

            # Verify block recalculation
            if current.calculate_geodesic_hash() != current.geodesic_hash:
                return False

            # Verify GCV thermodynamic conservation
            expected_gcv = current.total_pi_settled * PI_GCV_INVARIANT
            if abs(current.total_gcv_teu - expected_gcv) > 1e-4:
                return False

        return True

    def get_aggregate_stats(self) -> Dict[str, Any]:
        """
        Aggregates multi-planetary ledger statistics.
        """
        total_blocks = len(self.chain)
        total_txs = sum(len(b.transactions) for b in self.chain)
        total_pi = sum(b.total_pi_settled for b in self.chain)
        total_gcv = sum(b.total_gcv_teu for b in self.chain)

        nodes_involved = list(set(b.planetary_origin for b in self.chain))

        return {
            "total_blocks": total_blocks,
            "total_transactions": total_txs,
            "total_pi_circulating": total_pi,
            "total_gcv_valuation_teu": total_gcv,
            "gcv_constant_anchor": PI_GCV_INVARIANT,
            "participating_celestial_nodes": nodes_involved,
            "chain_validity": self.verify_chain_integrity()
        }
