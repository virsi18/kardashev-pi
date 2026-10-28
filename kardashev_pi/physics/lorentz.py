"""
Lorentz Spacetime & Relativistic Consensus Mechanics
Engineers relativistic time dilation, 4D Minkowski geodesics, and light-cone causality.
"""

import math
from typing import Tuple, Dict, Any
from kardashev_pi.constants import (
    SPEED_OF_LIGHT,
    CELESTIAL_NODES,
    LORENTZ_TOLERANCE_EPSILON
)

class LorentzRelativityEngine:
    """
    Computes relativistic corrections and Minkowski intervals for nodes operating
    across planetary and heliocentric orbital reference frames.
    """

    def __init__(self, reference_frame: str = "TERRA_PRIME"):
        if reference_frame not in CELESTIAL_NODES:
            raise ValueError(f"Unknown reference frame: {reference_frame}")
        self.reference_frame = reference_frame
        self.frame_data = CELESTIAL_NODES[reference_frame]

    @staticmethod
    def calculate_gamma(velocity_mps: float) -> float:
        """
        Calculates the Lorentz factor gamma:
        gamma = 1 / sqrt(1 - (v/c)^2)
        """
        beta = velocity_mps / SPEED_OF_LIGHT
        if abs(beta) >= 1.0:
            raise ValueError(f"Superluminal or luminal velocity not permitted in Lorentz frame: beta={beta}")
        return 1.0 / math.sqrt(1.0 - beta**2)

    @staticmethod
    def proper_time_dilation(coordinate_time_sec: float, velocity_mps: float, grav_potential: float) -> float:
        """
        Calculates proper time dTau considering both special relativistic kinematic
        dilation and general relativistic gravitational potential:
        dTau = dt * sqrt(1 - (v^2/c^2) + (2*Phi/c^2))
        """
        c2 = SPEED_OF_LIGHT ** 2
        kinematic_term = (velocity_mps ** 2) / c2
        gravitational_term = (2.0 * grav_potential) / c2
        metric_factor = 1.0 - kinematic_term + gravitational_term
        
        if metric_factor <= 0.0:
            return 0.0
        return coordinate_time_sec * math.sqrt(metric_factor)

    @classmethod
    def compute_spacetime_interval(
        cls, 
        t1: float, pos1: Tuple[float, float, float],
        t2: float, pos2: Tuple[float, float, float]
    ) -> Tuple[float, str]:
        """
        Computes 4D Minkowski spacetime interval s^2:
        ds^2 = c^2 * (dt)^2 - (dx^2 + dy^2 + dz^2)
        
        Returns:
            (interval_squared, causality_type)
            causality_type in ['TIMELIKE', 'LIGHTLIKE', 'SPACELIKE']
        """
        dt = t2 - t1
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]
        dz = pos2[2] - pos1[2]
        
        spatial_dist_sq = dx**2 + dy**2 + dz**2
        temporal_dist_sq = (SPEED_OF_LIGHT * dt) ** 2
        
        s2 = temporal_dist_sq - spatial_dist_sq
        
        if abs(s2) < LORENTZ_TOLERANCE_EPSILON:
            causality = "LIGHTLIKE"
        elif s2 > 0:
            causality = "TIMELIKE"
        else:
            causality = "SPACELIKE"
            
        return s2, causality

    def calculate_node_divergence(self, target_node: str, elapsed_seconds: float) -> Dict[str, Any]:
        """
        Calculates clock drift and relativistic phase variance between this node
        and another planetary cluster over a given elapsed coordinate period.
        """
        if target_node not in CELESTIAL_NODES:
            raise ValueError(f"Target node {target_node} not in celestial registry")
            
        target = CELESTIAL_NODES[target_node]
        tau_self = self.proper_time_dilation(
            elapsed_seconds, 
            self.frame_data["velocity_relative_ssb"],
            self.frame_data["gravitational_potential"]
        )
        tau_target = self.proper_time_dilation(
            elapsed_seconds,
            target["velocity_relative_ssb"],
            target["gravitational_potential"]
        )
        
        delta_tau = tau_target - tau_self
        drift_micros = delta_tau * 1.0e6
        
        return {
            "source_node": self.reference_frame,
            "target_node": target_node,
            "elapsed_coord_time_s": elapsed_seconds,
            "tau_source_s": tau_self,
            "tau_target_s": tau_target,
            "delta_tau_s": delta_tau,
            "clock_drift_microseconds": drift_micros,
            "lorentz_gamma_source": self.calculate_gamma(self.frame_data["velocity_relative_ssb"]),
            "lorentz_gamma_target": self.calculate_gamma(target["velocity_relative_ssb"])
        }
