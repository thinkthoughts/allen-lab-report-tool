"""Core Constraint-Guided Coherence Score (CGCS) implementations."""

import numpy as np
from typing import Union, Dict

def calculate_cgcs(
    coverage: float = 1.0,
    lane_alignment: float = 1.0,
    redundancy_penalty: float = 1.0,
    dead_feature_penalty: float = 1.0,
    reconstruction_penalty: float = 1.0
) -> float:
    """Standard CGCS formula."""
    return (coverage *
            lane_alignment *
            redundancy_penalty *
            dead_feature_penalty *
            reconstruction_penalty)


def calculate_cgcs_trisomy(
    dosage_ratio: float = 1.5,
    overexpression_imbalance: float = 0.5,
    global_dysregulation: float = 0.35,
    redundancy_factor: float = 1.0,
    base_cgcs: float = 1.0
) -> float:
    """
    Adapted CGCS for Trisomy 21 dosage noise.
    """
    lane_alignment = 1.0 / dosage_ratio
    
    cgcs = (base_cgcs *
            lane_alignment *
            (1 / (1 + overexpression_imbalance)) *
            (1 / (1 + global_dysregulation)) *
            (1 / redundancy_factor))
    
    return float(np.clip(cgcs, 0.0, 1.0))
