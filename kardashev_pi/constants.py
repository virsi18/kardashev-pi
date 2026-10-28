"""
Kardashev-Pi (K-314) Protocol Constants
Astrophysical, Relativistic, and Thermodynamic Foundations
"""

import math

# ==============================================================================
# ASTROPHYSICAL & UNIVERSAL CONSTANTS
# ==============================================================================
SPEED_OF_LIGHT = 299792458.0              # m/s (Lorentz causality propagation)
GRAVITATIONAL_CONSTANT = 6.67430e-11      # m^3 kg^-1 s^-2
BOLTZMANN_CONSTANT = 1.380649e-23         # J/K (Landauer informational entropy)
PLANCK_CONSTANT = 6.62607015e-34          # J*s
REDUCED_PLANCK = PLANCK_CONSTANT / (2.0 * math.pi)

# ==============================================================================
# KARDASHEV-PI GCV INVARIANT FORMULATION
# ==============================================================================
# The Global Consensus Value (GCV) is anchored as the Thermodynamic Invariant:
# GCV = floor(pi * 10^5) = 314,159.00 Thermodynamic Energy Units (TEU)
PI_MATHEMATICAL_CONSTANT = math.pi
GCV_SCALING_EXPONENT = 5
PI_GCV_INVARIANT = 314159.00              # Standard GCV anchor per 1.00 Pi

# 1 TEU (Thermodynamic Energy Unit) is formally equivalent to 10^9 Joules of 
# coherent quantum-computational work capacity at 2.725 K (Cosmic Microwave Background).
TEU_TO_JOULES_EQUIVALENCE = 1.0e9

# Kardashev Type-II Solar Luminosity Invariant (Sol Core Output: ~3.828e26 Watts)
SOLAR_LUMINOSITY = 3.828e26

# ==============================================================================
# PLANETARY NODE CLUSTER REFERENCE FRAMES (Minkowski Spacetime Metric)
# (Coordinates in meters relative to Solar System Barycenter, SSB)
# ==============================================================================
CELESTIAL_NODES = {
    "TERRA_PRIME": {
        "name": "Earth Terrestrial Core Network (Leap-Zero)",
        "type": "Planetary Surface & LEO Constellation",
        "distance_au": 1.000,
        "avg_light_latency_sec": 0.0,
        "gravitational_potential": -6.25e7, # J/kg (Earth surface)
        "velocity_relative_ssb": 29780.0,   # m/s orbital velocity
        "default_cluster_id": "0xTERRA-01"
    },
    "LUNA_GATEWAY": {
        "name": "Lunar L2 Deep-Space Relay Hub",
        "type": "Lagrange Point Orbital Gateway",
        "distance_au": 1.002,
        "avg_light_latency_sec": 1.282,
        "gravitational_potential": -2.82e6,
        "velocity_relative_ssb": 30800.0,
        "default_cluster_id": "0xLUNA-L2"
    },
    "ARES_MERIDIANI": {
        "name": "Mars Meridiani Planum Relativistic Anchor",
        "type": "Martian Surface Outpost & Phobos Relay",
        "distance_au": 1.524,
        "avg_light_latency_sec": 780.0,      # ~13 min average
        "gravitational_potential": -1.26e7,
        "velocity_relative_ssb": 24077.0,
        "default_cluster_id": "0xARES-01"
    },
    "SOL_DYSON_SWARM": {
        "name": "Helios Dyson-Ring Energy Collector Swarm",
        "type": "Sub-Mercury Dyson Orbit (0.15 AU)",
        "distance_au": 0.150,
        "avg_light_latency_sec": 499.0 * 0.85,
        "gravitational_potential": -8.90e8,
        "velocity_relative_ssb": 82000.0,
        "default_cluster_id": "0xSOL-DYSON-ALPHA"
    }
}

# ==============================================================================
# CONSENSUS PROTOCOL LIMITS
# ==============================================================================
MAX_LIGHT_CONE_DRIFT_SECONDS = 3600.0     # Maximum causal divergence tolerance
LORENTZ_TOLERANCE_EPSILON = 1e-12         # Spacetime curvature metric threshold
QUANTUM_ENTROPY_DECAY_RATE = 3.14159e-6   # Thermodynamic dissipation tensor factor
