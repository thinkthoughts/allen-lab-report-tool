"""
Trisomy-specific metrics and CGCS adaptations.
Focused on dosage imbalance, global dysregulation, and coherence recovery.
"""

import numpy as np
from typing import Dict, Tuple, Optional
from .cgcs import calculate_cgcs_trisomy


def trisomy_cgcs_score(
    dosage_ratio: float = 1.5,
    overexpression_imbalance: float = 0.5,
    global_dysregulation: float = 0.35,
    redundancy_factor: float = 1.0,
    return_components: bool = False
) -> Dict:
    """
    Compute CGCS score tailored for Trisomy 21 with optional component breakdown.
    """
    cgcs = calculate_cgcs_trisomy(
        dosage_ratio=dosage_ratio,
        overexpression_imbalance=overexpression_imbalance,
        global_dysregulation=global_dysregulation,
        redundancy_factor=redundancy_factor
    )
    
    if return_components:
        return {
            "cgcs": cgcs,
            "dosage_ratio": dosage_ratio,
            "lane_alignment": 1.0 / dosage_ratio,
            "overexpression_imbalance": overexpression_imbalance,
            "global_dysregulation": global_dysregulation,
            "redundancy_factor": redundancy_factor
        }
    
    return {"cgcs": cgcs}


def simulate_intervention_recovery(
    baseline_cgcs: float,
    recovery_strength: float = 0.3,
    max_recovery: float = 0.85
) -> float:
    """
    Model how interventions (therapy, pharmacology) improve CGCS.
    """
    recovered = baseline_cgcs + (1.0 - baseline_cgcs) * recovery_strength
    return min(recovered, max_recovery)
