"""DNA base-pairing to modular residue encoding."""

import numpy as np
from typing import List


def encode_base(base: str) -> int:
    """Simple mapping: A=0, T=1, G=2, C=3"""
    mapping = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    return mapping.get(base.upper(), -1)


def encode_dna_to_residues(sequence: str, mod: int = 30) -> np.ndarray:
    """Encode DNA sequence to residue array mod N."""
    residues = [encode_base(b) for b in sequence if b.upper() in 'ATGC']
    return np.array(residues) % mod


def encode_sequence_list(sequences: List[str], mod: int = 30) -> List[np.ndarray]:
    """Encode multiple sequences."""
    return [encode_dna_to_residues(seq, mod) for seq in sequences]
