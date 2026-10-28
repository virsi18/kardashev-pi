"""
Interplanetary Dyson Mesh Protocol
Simulates cosmic packet propagation, relativistic delay buffering,
and optimistic cross-planetary settlement under GCV $314,159.
"""

import time
import random
from typing import List, Dict, Any
from kardashev_pi.constants import CELESTIAL_NODES, SPEED_OF_LIGHT
from kardashev_pi.consensus.minkowski_engine import MinkowskiConsensusEngine, AstralTransaction

class DysonInterplanetaryMesh:
    """
    Coordinates peer-to-peer relativistic gossip between Earth, Lunar L2,
    Mars Outpost, and Dyson Ring solar energy harvesters.
    """

    def __init__(self):
        self.nodes: Dict[str, MinkowskiConsensusEngine] = {}
        for node_id in CELESTIAL_NODES:
            self.nodes[node_id] = MinkowskiConsensusEngine(node_id)
        self.transit_buffer: List[Dict[str, Any]] = []

    def broadcast_transaction(
        self,
        source_node: str,
        sender: str,
        recipient: str,
        pi_amount: float
    ) -> AstralTransaction:
        """
        Originates an Astral transaction from a specific celestial node and initiates
        interplanetary beam propagation across the solar system mesh.
        """
        if source_node not in self.nodes:
            raise ValueError(f"Unknown source celestial node: {source_node}")

        engine = self.nodes[source_node]
        tx = engine.create_astral_transaction(sender, recipient, pi_amount)
        engine.ingest_transaction(tx)

        # Broadcast packet across celestial mesh
        origin_info = CELESTIAL_NODES[source_node]
        current_time = time.time()

        for dest_node, dest_info in CELESTIAL_NODES.items():
            if dest_node == source_node:
                continue

            # Compute light travel time based on distance in Astronomical Units
            delta_au = abs(dest_info["distance_au"] - origin_info["distance_au"])
            meters = delta_au * 1.496e11
            latency_sec = max(dest_info["avg_light_latency_sec"], meters / SPEED_OF_LIGHT)
            arrival_epoch = current_time + latency_sec

            self.transit_buffer.append({
                "tx": tx,
                "from_node": source_node,
                "to_node": dest_node,
                "dispatched_at": current_time,
                "arrival_epoch": arrival_epoch,
                "latency_sec": latency_sec,
                "status": "IN_PHOTON_TRANSIT"
            })

        return tx

    def settle_transit_packets(self, simulated_epoch_advance: float = 1000.0) -> List[Dict[str, Any]]:
        """
        Advances the simulated spacetime coordinate and settles packets that have arrived
        at their destination planetary light-cones.
        """
        now = time.time() + simulated_epoch_advance
        settled = []

        remaining = []
        for packet in self.transit_buffer:
            if packet["arrival_epoch"] <= now:
                dest_engine = self.nodes[packet["to_node"]]
                success = dest_engine.ingest_transaction(packet["tx"])
                packet["status"] = "RECONCILED" if success else "REJECTED"
                settled.append(packet)
            else:
                remaining.append(packet)

        self.transit_buffer = remaining
        return settled

    def get_mesh_telemetry(self) -> Dict[str, Any]:
        """
        Returns full telemetry of the planetary node network.
        """
        node_status = {}
        for nid, engine in self.nodes.items():
            node_status[nid] = {
                "name": CELESTIAL_NODES[nid]["name"],
                "type": CELESTIAL_NODES[nid]["type"],
                "validated_txs_count": len(engine.validated_transactions),
                "total_gcv_volume_teu": sum(tx.gcv_value_teu for tx in engine.validated_transactions.values()),
                "orbital_velocity_mps": CELESTIAL_NODES[nid]["velocity_relative_ssb"],
                "gravitational_potential": CELESTIAL_NODES[nid]["gravitational_potential"]
            }

        return {
            "active_nodes_count": len(self.nodes),
            "packets_in_photon_transit": len(self.transit_buffer),
            "nodes": node_status
        }
