"""
Imperial Physics Constants
Universal Plasma Limit and Geometric Invariants

This module defines the core constants and relationships of the Imperial Physics framework.
X = 0.15 is the Universal Plasma Limit that unifies Gravity, Matter, and Biology.
"""

# Universal Plasma Limit - The fundamental dimensionless constant
X = 0.15

# Physical Constants (SI Units)
# Source: CODATA 2018 recommended values
SPEED_OF_LIGHT = 299792458.0  # m/s (exact)
PLANCK_CONSTANT = 6.62607015e-34  # J·s (exact)
ELEMENTARY_CHARGE = 1.602176634e-19  # C (exact)
ELECTRON_MASS = 9.1093837015e-31  # kg
PROTON_MASS = 1.67262192369e-27  # kg
GRAVITATIONAL_CONSTANT = 6.67430e-11  # m³/(kg·s²)
VACUUM_PERMITTIVITY = 8.8541878128e-12  # F/m
BOLTZMANN_CONSTANT = 1.380649e-23  # J/K

# Biology Parameter
LAMBDA_BIO = 20.56  # Hz - Fundamental biological frequency

# Derived Relationships based on X = 0.15
# These are dimensionless ratios that unify the physical domains

def gravity_relationship():
    """
    Gravity relationship: G ∝ 1/X
    Returns the proportionality factor for gravitational coupling
    """
    return 1.0 / X

def matter_relationship():
    """
    Matter relationship: m_e/m_p ∝ X^4
    Returns the predicted mass ratio based on X
    """
    return X ** 4

def actual_mass_ratio():
    """
    Actual electron-to-proton mass ratio from measurements
    """
    return ELECTRON_MASS / PROTON_MASS

def mass_ratio_validation():
    """
    Validates the matter relationship against empirical data
    Returns (predicted, actual, relative_error)
    """
    predicted = matter_relationship()
    actual = actual_mass_ratio()
    relative_error = abs(predicted - actual) / actual
    return predicted, actual, relative_error

def fine_structure_constant():
    """
    Fine structure constant α ≈ 1/137
    Dimensionless fundamental constant in quantum electrodynamics
    """
    alpha = (ELEMENTARY_CHARGE ** 2) / (4 * 3.14159265359 * VACUUM_PERMITTIVITY * 
                                        PLANCK_CONSTANT * SPEED_OF_LIGHT)
    return alpha

def plasma_frequency(n_e):
    """
    Plasma frequency given electron density n_e (electrons per m³)
    ω_p = sqrt(n_e * e² / (ε₀ * m_e))
    """
    import math
    omega_p = math.sqrt(n_e * ELEMENTARY_CHARGE ** 2 / 
                       (VACUUM_PERMITTIVITY * ELECTRON_MASS))
    return omega_p / (2 * math.pi)  # Convert to Hz

# Geometric Invariants
def geometric_ratio_1():
    """
    Primary geometric invariant: X relates to vacuum lattice structure
    """
    return X * gravity_relationship()  # Should equal 1

def geometric_ratio_2():
    """
    Secondary geometric invariant: Combines matter and gravity
    """
    return matter_relationship() * (gravity_relationship() ** 0.25)

# Universal Plasma Limit Validation
def validate_universal_plasma_limit():
    """
    Validates X = 0.15 against multiple physical constraints
    Returns a dictionary of validation metrics
    """
    results = {
        'X': X,
        'gravity_factor': gravity_relationship(),
        'matter_predicted': matter_relationship(),
        'matter_actual': actual_mass_ratio(),
        'matter_error_percent': mass_ratio_validation()[2] * 100,
        'bio_frequency_hz': LAMBDA_BIO,
        'geometric_invariant_1': geometric_ratio_1(),
        'geometric_invariant_2': geometric_ratio_2(),
    }
    return results

# Export all constants and functions
__all__ = [
    'X',
    'SPEED_OF_LIGHT',
    'PLANCK_CONSTANT',
    'ELEMENTARY_CHARGE',
    'ELECTRON_MASS',
    'PROTON_MASS',
    'GRAVITATIONAL_CONSTANT',
    'VACUUM_PERMITTIVITY',
    'BOLTZMANN_CONSTANT',
    'LAMBDA_BIO',
    'gravity_relationship',
    'matter_relationship',
    'actual_mass_ratio',
    'mass_ratio_validation',
    'fine_structure_constant',
    'plasma_frequency',
    'geometric_ratio_1',
    'geometric_ratio_2',
    'validate_universal_plasma_limit',
]
