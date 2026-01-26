"""
Example usage of Imperial Physics framework
Demonstrates the core relationships and validation
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from constants import (
    X,
    gravity_relationship,
    matter_relationship,
    actual_mass_ratio,
    mass_ratio_validation,
    LAMBDA_BIO,
    validate_universal_plasma_limit,
    fine_structure_constant,
)

def main():
    """Demonstrate Imperial Physics framework"""
    
    print("=" * 70)
    print("IMPERIAL PHYSICS FRAMEWORK DEMONSTRATION")
    print("=" * 70)
    print()
    
    # Show Universal Plasma Limit
    print(f"Universal Plasma Limit: X = {X}")
    print()
    
    # Gravity Domain
    print("--- GRAVITY DOMAIN ---")
    g_factor = gravity_relationship()
    print(f"Relationship: G ∝ 1/X")
    print(f"Factor: 1/X = {g_factor:.6f}")
    print()
    
    # Matter Domain
    print("--- MATTER DOMAIN ---")
    print(f"Relationship: m_e/m_p ∝ X^4")
    predicted, actual, error = mass_ratio_validation()
    print(f"Predicted: X^4 = {predicted:.8f}")
    print(f"Actual: m_e/m_p = {actual:.8f}")
    print(f"Error: {error*100:.4f}%")
    print(f"Status: {'PASS ✓' if error < 0.1 else 'NOTE'}")
    print()
    
    # Biology Domain
    print("--- BIOLOGY DOMAIN ---")
    print(f"Fundamental Frequency: Λ = {LAMBDA_BIO} Hz")
    print(f"Period: {1/LAMBDA_BIO:.6f} seconds ({1/LAMBDA_BIO*1000:.2f} ms)")
    print()
    
    # Fine Structure Constant
    print("--- FINE STRUCTURE CONSTANT ---")
    alpha = fine_structure_constant()
    print(f"α = {alpha:.10f}")
    print(f"1/α = {1/alpha:.6f}")
    print()
    
    # Full Validation
    print("--- COMPLETE VALIDATION ---")
    results = validate_universal_plasma_limit()
    for key, value in results.items():
        if isinstance(value, float):
            print(f"{key}: {value:.8f}")
        else:
            print(f"{key}: {value}")
    print()
    
    print("=" * 70)
    print("The Text Problem is solved: No calculus, only ratios.")
    print("We do not model the boundary; we monitor it.")
    print("=" * 70)

if __name__ == "__main__":
    main()
