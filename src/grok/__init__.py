"""
Grok RML Tools - Residue Manifold Learning + CGCS
For Allen Lab Trisomy 21 Collaboration
"""

__version__ = "0.1.0"
__author__ = "Your Name"

# Core modules
from .cgcs import (
    calculate_cgcs,
    calculate_cgcs_trisomy
)

from .residue_encoding import (
    encode_base,
    encode_dna_to_residues
)

from .trisomy_metrics import (
    trisomy_cgcs_score,
    simulate_intervention_recovery
)

from .visualization import (
    plot_cgcs_vs_noise,
    plot_dosage_impact
)

# Convenient combined imports
__all__ = [
    # CGCS
    "calculate_cgcs",
    "calculate_cgcs_trisomy",
    
    # Encoding
    "encode_base",
    "encode_dna_to_residues",
    
    # Trisomy specific
    "trisomy_cgcs_score",
    "simulate_intervention_recovery",
    
    # Visualization
    "plot_cgcs_vs_noise",
    "plot_dosage_impact",
]
