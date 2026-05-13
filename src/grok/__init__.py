"""
Grok RML Module - Residue Manifold Learning Tools
Designed for Allen Lab Trisomy 21 collaboration.
"""

__version__ = "0.1.0"

from .cgcs import calculate_cgcs, calculate_cgcs_trisomy
from .residue_encoding import encode_dna_to_residues
from .trisomy_metrics import trisomy_cgcs_score

__all__ = [
    "calculate_cgcs",
    "calculate_cgcs_trisomy",
    "encode_dna_to_residues",
    "trisomy_cgcs_score",
]
