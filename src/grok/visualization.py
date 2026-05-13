"""
Visualization utilities for RML + CGCS results.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Optional

def plot_cgcs_vs_noise(
    noise_levels: List[float],
    cgcs_values: List[float],
    title: str = "CGCS vs Noise Level in Trisomy 21",
    save_path: Optional[str] = None
):
    """Plot CGCS degradation under increasing noise/dosage imbalance."""
    plt.figure(figsize=(8, 5))
    sns.lineplot(x=noise_levels, y=cgcs_values, marker='o', linewidth=2.5)
    
    plt.axhline(y=0.6, color='r', linestyle='--', alpha=0.7, label='Phase-Lock Threshold')
    plt.title(title)
    plt.xlabel("Noise / Dosage Imbalance Level")
    plt.ylabel("Constraint-Guided Coherence Score (CGCS)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()


def plot_dosage_impact():
    """Simple bar plot comparing normal vs Trisomy 21 CGCS."""
    labels = ['Normal (1.0x)', 'Trisomy 21 (1.5x)']
    cgcs_scores = [0.92, 0.48]  # Example values
    
    plt.figure(figsize=(7, 5))
    bars = plt.bar(labels, cgcs_scores, color=['#2ecc71', '#e74c3c'])
    
    plt.title("CGCS Comparison: Normal vs Trisomy 21")
    plt.ylabel("CGCS Score")
    plt.ylim(0, 1.0)
    
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                 f'{height:.2f}', ha='center')
    
    plt.grid(axis='y', alpha=0.3)
    plt.show()
