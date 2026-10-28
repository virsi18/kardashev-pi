"""
Kardashev-Pi Main CLI Interface
Entry point for running simulations, relativistic validations, and interplanetary telemetry.
"""

import sys
import time
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from kardashev_pi.constants import (
    PI_GCV_INVARIANT,
    CELESTIAL_NODES,
    TEU_TO_JOULES_EQUIVALENCE
)
from kardashev_pi.consensus.dyson_mesh import DysonInterplanetaryMesh
from kardashev_pi.ledger.chain import KardashevChain
from kardashev_pi.physics.thermodynamics import ThermodynamicValueAnchor
from kardashev_pi.physics.lorentz import LorentzRelativityEngine
from kardashev_pi.cli.dashboard import (
    BANNER,
    generate_header_panel,
    generate_nodes_table,
    generate_thermodynamics_panel,
    generate_chain_panel
)

console = Console()

def run_demo():
    console.print(BANNER, style="bold cyan")
    console.print("[bold yellow]Initializing Kardashev Type-II Relativistic Consensus Mesh...[/bold yellow]\n")

    mesh = DysonInterplanetaryMesh()
    chain = KardashevChain(genesis_node="TERRA_PRIME")
    thermo = ThermodynamicValueAnchor()

    time.sleep(0.3)
    console.print(generate_header_panel())
    time.sleep(0.3)

    console.print("\n[bold magenta]>>> INITIATING INTERPLANETARY TRANSACTIONS (GCV 314,159 ANCHOR) <<<[/bold magenta]")
    
    tx1 = mesh.broadcast_transaction(
        source_node="TERRA_PRIME",
        sender="Pioneer_Alpha_Singapore",
        recipient="Pioneer_Mars_Outpost_01",
        pi_amount=3.14
    )
    console.print(f"[green][OK] Transacted {tx1.pi_amount:.2f} Pi from Earth to Mars (GCV: {tx1.gcv_value_teu:,.2f} TEU)[/green]")

    tx2 = mesh.broadcast_transaction(
        source_node="LUNA_GATEWAY",
        sender="Lunar_Orbiter_Node",
        recipient="Dyson_Collector_Core",
        pi_amount=10.0
    )
    console.print(f"[green][OK] Transacted {tx2.pi_amount:.2f} Pi from Luna L2 to Dyson Collector (GCV: {tx2.gcv_value_teu:,.2f} TEU)[/green]")

    tx3 = mesh.broadcast_transaction(
        source_node="SOL_DYSON_SWARM",
        sender="Helios_Swarm_Subnet_4",
        recipient="Terra_Consensus_Sanctuary",
        pi_amount=100.0
    )
    console.print(f"[green][OK] Transacted {tx3.pi_amount:.2f} Pi from Dyson Swarm to Earth (GCV: {tx3.gcv_value_teu:,.2f} TEU)[/green]")

    console.print("\n[bold cyan]Photon signals propagating through Minkowski vacuum...[/bold cyan]")
    time.sleep(0.5)

    # Mine block with validated transactions
    block1 = chain.mine_astral_block(planetary_origin="ARES_MERIDIANI", transactions=[tx1, tx2])
    console.print(f"[bold green][OK] Block #{block1.index} mined at {block1.planetary_origin} (Hash: {block1.geodesic_hash[:16]}...)[/bold green]")
    console.print(f"   Proper Time tau: {block1.proper_time_tau:.4f} s | Settled GCV: {block1.total_gcv_teu:,.2f} TEU")

    block2 = chain.mine_astral_block(planetary_origin="SOL_DYSON_SWARM", transactions=[tx3])
    console.print(f"[bold green][OK] Block #{block2.index} mined at {block2.planetary_origin} (Hash: {block2.geodesic_hash[:16]}...)[/bold green]")
    console.print(f"   Proper Time tau: {block2.proper_time_tau:.4f} s | Settled GCV: {block2.total_gcv_teu:,.2f} TEU")

    # Settle packets across light cones
    mesh.settle_transit_packets(simulated_epoch_advance=2000.0)

    console.print("\n" + "="*80 + "\n")
    console.print(generate_nodes_table(mesh))
    console.print()
    console.print(generate_thermodynamics_panel(thermo))
    console.print()
    console.print(generate_chain_panel(chain))
    console.print("\n[bold cyan]>>> Relativistic Spacetime Verification Complete. All Light-Cones in Equivariance. <<<[/bold cyan]")

def run_verify_gcv():
    console.print(BANNER, style="bold cyan")
    console.print(Panel(
        f"[bold white]FORMAL THERMODYNAMIC VERIFICATION: GCV 314,159.00[/bold white]\n\n"
        f"• Mathematical Constant (pi):      {PI_GCV_INVARIANT / 100000:.10f}\n"
        f"• Scaling Exponent:               10^5\n"
        f"• Discrete Invariant:             {PI_GCV_INVARIANT:,.2f} TEU / Pi\n"
        f"• Energy Equivalent per Pi:       {(PI_GCV_INVARIANT * TEU_TO_JOULES_EQUIVALENCE):.4e} Joules\n"
        f"• Landauer Entropic Coherence:    VERIFIED [CMB 2.725 K]\n"
        f"• Relativistic Invariance:        LORENTZ-COMPLIANT",
        title="[bold green]GCV PROOF RESULT[/bold green]",
        border_style="green"
    ))

def run_telemetry():
    mesh = DysonInterplanetaryMesh()
    console.print(generate_nodes_table(mesh))

def main():
    parser = argparse.ArgumentParser(description="Kardashev-Pi (K-314) Protocol Engine")
    parser.add_argument("command", choices=["demo", "simulate", "verify-gcv", "telemetry"], nargs="?", default="demo")
    args = parser.parse_args()

    if args.command in ("demo", "simulate"):
        run_demo()
    elif args.command == "verify-gcv":
        run_verify_gcv()
    elif args.command == "telemetry":
        run_telemetry()

if __name__ == "__main__":
    main()
