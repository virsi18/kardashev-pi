"""
Astral Block Specification
Represents a multi-planetary cryptographic state block containing
geodesic vectors, Minkowski light-cone Merkle proofs, and GCV thermodynamic proofs.
"""

import hashlib
import json
import time
from typing import List, Dict, Any
from dataclasses import dataclass, asdict
from kardashev_pi.consensus.minkowski_engine import AstralTransaction
from kardashev_pi.constants import PI_GCV_INVARIANT, CELESTIAL_NODES
from kardashev_pi.physics.lorentz import LorentzRelativityEngine

@dataclass
class AstralBlock:
    index: int
    previous_geodesic_hash: str
    planetary_origin: str
    timestamp_epoch: float
    proper_time_tau: float
    transactions: List[Dict[str, Any]]
    total_pi_settled: float
    total_gcv_teu: float
    thermodynamic_energy_proof: str
    merkle_light_cone_root: str
    geodesic_hash: str = ""

    def calculate_geodesic_hash(self) -> str:
        """
        Computes 4D topological block hash linking physical relativistic parameters
        with cryptographic state.
        """
        header = {
            "index": self.index,
            "prev": self.previous_geodesic_hash,
            "origin": self.planetary_origin,
            "t": self.timestamp_epoch,
            "tau": self.proper_time_tau,
            "merkle": self.merkle_light_cone_root,
            "gcv_teu": self.total_gcv_teu,
            "proof": self.thermodynamic_energy_proof
        }
        encoded = json.dumps(header, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

class AstralBlockFactory:
    """
    Synthesizes valid Astral Blocks with relativistic calibration.
    """

    @classmethod
    def create_block(
        cls,
        index: int,
        previous_hash: str,
        planetary_origin: str,
        transactions: List[AstralTransaction]
    ) -> AstralBlock:
        if planetary_origin not in CELESTIAL_NODES:
            raise ValueError(f"Unknown planetary origin: {planetary_origin}")

        now = time.time()
        engine = LorentzRelativityEngine(planetary_origin)
        node_info = CELESTIAL_NODES[planetary_origin]
        tau = engine.proper_time_dilation(
            now,
            node_info["velocity_relative_ssb"],
            node_info["gravitational_potential"]
        )

        total_pi = sum(tx.pi_amount for tx in transactions)
        total_gcv = total_pi * PI_GCV_INVARIANT

        # Compute Merkle Light-Cone Root
        tx_hashes = [tx.tx_id for tx in transactions] if transactions else ["0xGENESIS_SINGULARITY"]
        combined = "".join(tx_hashes).encode()
        merkle_root = hashlib.sha256(combined).hexdigest()

        # Thermodynamic Energy Proof (Proof of Post-Scarcity Dyson Flux)
        proof_payload = f"DYSON_FLUX::{total_gcv}::{planetary_origin}::{tau}"
        energy_proof = hashlib.sha3_256(proof_payload.encode()).hexdigest()

        serialized_txs = [asdict(tx) for tx in transactions]

        block = AstralBlock(
            index=index,
            previous_geodesic_hash=previous_hash,
            planetary_origin=planetary_origin,
            timestamp_epoch=now,
            proper_time_tau=tau,
            transactions=serialized_txs,
            total_pi_settled=total_pi,
            total_gcv_teu=total_gcv,
            thermodynamic_energy_proof=energy_proof,
            merkle_light_cone_root=merkle_root
        )
        block.geodesic_hash = block.calculate_geodesic_hash()
        return block
