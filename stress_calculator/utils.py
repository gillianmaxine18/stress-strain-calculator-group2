"""
utils.py - Stress and Strain Calculation and Validation Utilities
Part of Task 6 Modular Package Integration
"""

import math

UNITS = ("N", "m²", "m", "Pa")

# 1. CORE CALCULATION UTILITIES
def calculate_stress(force: float, area: float) -> float:
    """Calculate normal stress: σ = F / A."""
    if area <= 0:
        raise ValueError("Cross-sectional area must be strictly greater than zero.")
    return force / area

def calculate_strain(original_length: float, change_in_length: float) -> float:
    """Calculate engineering strain: ε = ΔL / L₀."""
    if original_length <= 0:
        raise ValueError("Original length must be strictly greater than zero.")
    return change_in_length / original_length

def calculate_youngs_modulus(stress: float, strain: float) -> float:
    """Calculate Young's Modulus of Elasticity: E = σ / ε."""
    if math.isclose(strain, 0.0, abs_tol=1e-12):
        raise ValueError("Strain cannot be zero when calculating Young's Modulus.")
    return stress / strain

def calculate_factor_of_safety(yield_strength: float, stress: float) -> float:
    """Calculate factor of safety: FoS = σ_yield / σ_applied."""
    if stress <= 0:
        raise ValueError("Applied stress must be strictly positive to compute Factor of Safety.")
    return yield_strength / stress

# 2. VALIDATION UTILITIES
def validate_positive_number(value: float, parameter_name: str) -> float:
    """Validate that an input value is strictly greater than zero."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{parameter_name} must be a valid number.")
    if value <= 0:
        raise ValueError(f"{parameter_name} must be greater than zero, got {value}.")
    return float(value)

def validate_non_zero(value: float, parameter_name: str) -> float:
    """Ensure a denominator or change value is non-zero."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"{parameter_name} must be a valid number.")
    if math.isclose(value, 0.0, abs_tol=1e-12):
        raise ValueError(f"{parameter_name} cannot be zero.")
    return float(value)

def validate_input(force: float, area: float, original_length: float, change_in_length: float) -> bool:
    """Validate basic physical boundary conditions for specimen testing."""
    for name, val in [
        ("Force", force),
        ("Area", area),
        ("Original Length", original_length),
        ("Change in Length", change_in_length),
    ]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a valid number.")

    if area <= 0:
        raise ValueError("Cross-sectional area must be strictly greater than zero.")
    if original_length <= 0:
        raise ValueError("Original length must be strictly greater than zero.")
    if force < 0:
        raise ValueError("Force cannot be negative.")

    return True


# 3. CONVERSION UTILITIES
def pascals_to_megapascals(pa: float) -> float:
    """Convert Pascals (Pa) to MegaPascals (MPa)."""
    return pa / 1e6

def megapascals_to_pascals(mpa: float) -> float:
    """Convert MegaPascals (MPa) to Pascals (Pa)."""
    return mpa * 1e6
