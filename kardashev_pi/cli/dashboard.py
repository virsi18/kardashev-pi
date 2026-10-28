"""
Kardashev-Pi Neon Terminal UI & Telemetry Dashboard
Uses Rich to display real-time relativistic node telemetry,
interplanetary light-cone causal graphs, and GCV $314,159 thermodynamic flux.
"""

import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.text import Text
from rich.live import Live

from kardashev_pi.constants import (
    PI_GCV_INVARIANT,
    CELESTIAL_NODES,
    TEU_TO_JOULES_EQUIVALENCE
)
from kardashev_pi.consensus.dyson_mesh import DysonInterplanetaryMesh
from kardashev_pi.ledger.chain import KardashevChain
from kardashev_pi.physics.thermodynamics import ThermodynamicValueAnchor

BANNER = r"""
  _  __              _           _                   _____ _ 
 | |/ /             | |         | |                 |  __ (_)
 | ' / __ _ _ __  __| | __ _ ___| |__   _____   __  | |__) | 
 |  < / _` | '__/ _` |/ _` / __| '_ \ / _ \ \ / /  |  ___/ | 
 | . \ (_| | | | (_| | (_| \__ \ | | |  __/\ V /   | |   | | 
 |_|\_\__,_|_|  \__,_|\__,_|___/_| |_|\___| \_/    |_|   |_| 
   >> RELATIVISTIC THERMODYNAMIC CONSENSUS ENGINE (K-314) <<
"""

def generate_header_panel() -> Panel:
    text = Text()
    text.append("KARDASHEV-PI (PROJECT K-314) // ASTROPHYSICAL LEDGER\n", style="bold magenta")
    text.append("Invariant Global Consensus Value: ", style="cyan")
    text.append(f"1.00000000 Pi = {PI_GCV_INVARIANT:,.2f} TEU\n", style="bold yellow")
    text.append("Equivalent Coherent Work Capacity: ", style="cyan")
    text.append(f"{(PI_GCV_INVARIANT * TEU_TO_JOULES_EQUIVALENCE):.4e} Joules\n", style="bold green")
    text.append("Consensus Paradigm: 4D Minkowski Light-Cone Geodesic DAG\n", style="italic blue")
    return Panel(text, title="[bold white]ASTRO-ECONOMIC PROTOCOL MATRIX[/bold white]", border_style="bright_blue")

def generate_nodes_table(mesh: DysonInterplanetaryMesh) -> Table:
    table = Table(title="CELESTIAL NODE TELEMETRY & RELATIVISTIC FRAMES", border_style="cyan")
    table.add_column("Node Cluster", style="bold white")
    table.add_column("Classification", style="dim")
    table.add_column("Orbital Vel (m/s)", justify="right", style="cyan")
    table.add_column("Grav. Potential (J/kg)", justify="right", style="red")
    table.add_column("Light Delay", justify="right", style="yellow")
    table.add_column("GCV Volume (TEU)", justify="right", style="bold green")

    telemetry = mesh.get_mesh_telemetry()
    for nid, node in CELESTIAL_NODES.items():
        node_stats = telemetry["nodes"][nid]
        latency_str = f"{node['avg_light_latency_sec']:.2f}s" if node['avg_light_latency_sec'] < 60 else f"{node['avg_light_latency_sec']/60:.1f}m"
        table.add_row(
            nid,
            node["type"],
            f"{node['velocity_relative_ssb']:,.0f}",
            f"{node['gravitational_potential']:.2e}",
            latency_str,
            f"{node_stats['total_gcv_volume_teu']:,.2f}"
        )
    return table

def generate_thermodynamics_panel(thermo: ThermodynamicValueAnchor) -> Panel:
    telemetry = thermo.dyson_swarm_harvest_telemetry()
    text = Text()
    text.append("DYSON-RING SOLAR FLUX INTAKE:\n", style="bold yellow")
    text.append(f"  * Raw Solar Harvest Rate: {telemetry['harvested_power_watts']:.3e} Watts\n", style="white")
    text.append(f"  * Pi Minting Capacity:    {telemetry['pi_gcv_capacity_sec']:,.4f} Pi / second\n", style="bold green")
    text.append(f"  * Entropy Stability:     {telemetry['entropy_decay_stability'] * 100:.6f}%\n", style="cyan")
    text.append(f"  * Landauer Min Energy:    {thermo.landauer_limit_per_bit():.4e} J/bit @ 2.725 K\n", style="dim")
    return Panel(text, title="[bold yellow]THERMODYNAMIC HARVEST MATRIX[/bold yellow]", border_style="yellow")

def generate_chain_panel(chain: KardashevChain) -> Panel:
    stats = chain.get_aggregate_stats()
    text = Text()
    text.append("INTERPLANETARY BLOCKCHAIN STATUS:\n", style="bold green")
    text.append(f"  * Total Astral Blocks:       {stats['total_blocks']}\n", style="white")
    text.append(f"  * Total Pi Transacted:       {stats['total_pi_circulating']:,.4f} Pi\n", style="bold yellow")
    text.append(f"  * Aggregate GCV Settlement:   {stats['total_gcv_valuation_teu']:,.2f} TEU\n", style="bold cyan")
    text.append(f"  * Chain Geodesic Integrity:  {'OPTIMAL / VERIFIED' if stats['chain_validity'] else 'CORRUPTED'}\n", style="bold green")
    return Panel(text, title="[bold green]4D MINKOWSKI TIME-CHAIN[/bold green]", border_style="green")
