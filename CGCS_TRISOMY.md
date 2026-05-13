# Adapted CGCS for Trisomy 21

## Formula
$$
\text{CGCS}_{\text{trisomy}} = \text{dosage coverage} \times \text{lane dosage alignment} \times \frac{1}{1 + \text{overexpression imbalance}} \times \frac{1}{1 + \text{global trans-dysregulation}} \times \text{redundancy penalty}
$$

## Component Definitions
- **dosage coverage**: Fraction of genes at expected vs observed copy number
- **lane dosage alignment**: How cleanly expression concentrates on biologically valid levels
- **overexpression imbalance**: Deviation from 1.0× (ideal) toward 1.5×
- **global trans-dysregulation**: Effects on non-chr21 genes
- **redundancy penalty**: Penalty for extra copy material

## Interpretation
- CGCS near 1.0 → High developmental coherence
- CGCS drop below threshold → Predicts increased developmental instability
