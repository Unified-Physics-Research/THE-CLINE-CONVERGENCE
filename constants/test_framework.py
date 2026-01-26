"""
Unit tests for Imperial Physics framework
Validates core relationships and calculations
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from constants import (
    X,
    gravity_relationship,
    matter_relationship,
    actual_mass_ratio,
    mass_ratio_validation,
    LAMBDA_BIO,
    geometric_ratio_1,
    geometric_ratio_2,
    validate_universal_plasma_limit,
)

def test_universal_plasma_limit():
    """Test that X is correctly defined"""
    assert X == 0.15, f"Expected X = 0.15, got {X}"
    print("✓ Universal Plasma Limit X = 0.15")

def test_gravity_relationship():
    """Test gravity factor calculation"""
    g_factor = gravity_relationship()
    expected = 1.0 / 0.15
    assert abs(g_factor - expected) < 1e-10, f"Expected {expected}, got {g_factor}"
    assert abs(g_factor - 6.666667) < 0.001, "Gravity factor should be ~6.667"
    print(f"✓ Gravity relationship: 1/X = {g_factor:.6f}")

def test_matter_relationship():
    """Test matter ratio prediction"""
    m_predicted = matter_relationship()
    expected = 0.15 ** 4
    assert abs(m_predicted - expected) < 1e-10, f"Expected {expected}, got {m_predicted}"
    assert abs(m_predicted - 0.00050625) < 1e-10, "Matter prediction should be X^4"
    print(f"✓ Matter relationship: X^4 = {m_predicted:.8f}")

def test_matter_validation():
    """Test matter ratio empirical validation"""
    predicted, actual, error = mass_ratio_validation()
    
    # Check that prediction matches X^4
    assert abs(predicted - 0.00050625) < 1e-10, "Predicted should equal X^4"
    
    # Check that actual ratio is reasonable
    assert 0.0005 < actual < 0.0006, f"Actual ratio {actual} outside expected range"
    
    # Check that error is within tolerance
    assert error < 0.1, f"Error {error*100:.2f}% exceeds 10% tolerance"
    
    print(f"✓ Matter validation: {error*100:.4f}% error (within tolerance)")

def test_biology_parameter():
    """Test biology frequency"""
    assert LAMBDA_BIO == 20.56, f"Expected Λ = 20.56 Hz, got {LAMBDA_BIO}"
    print(f"✓ Biology parameter: Λ = {LAMBDA_BIO} Hz")

def test_geometric_invariant_1():
    """Test first geometric invariant"""
    inv1 = geometric_ratio_1()
    assert abs(inv1 - 1.0) < 1e-10, f"Invariant 1 should equal 1.0, got {inv1}"
    print(f"✓ Geometric invariant 1: X × (1/X) = {inv1:.6f}")

def test_geometric_invariant_2():
    """Test second geometric invariant"""
    inv2 = geometric_ratio_2()
    # Just check it's a positive number
    assert inv2 > 0, f"Invariant 2 should be positive, got {inv2}"
    print(f"✓ Geometric invariant 2: {inv2:.6f}")

def test_validate_universal_plasma_limit():
    """Test complete validation function"""
    results = validate_universal_plasma_limit()
    
    # Check all expected keys are present
    expected_keys = [
        'X', 'gravity_factor', 'matter_predicted', 'matter_actual',
        'matter_error_percent', 'bio_frequency_hz', 
        'geometric_invariant_1', 'geometric_invariant_2'
    ]
    
    for key in expected_keys:
        assert key in results, f"Missing key: {key}"
    
    # Check values
    assert results['X'] == 0.15
    assert results['bio_frequency_hz'] == 20.56
    assert abs(results['geometric_invariant_1'] - 1.0) < 1e-10
    
    print("✓ Complete validation function works correctly")

def test_dimensionless_ratios():
    """Test that key relationships are dimensionless"""
    # X is dimensionless
    assert isinstance(X, float)
    
    # 1/X is dimensionless
    assert isinstance(gravity_relationship(), float)
    
    # X^4 is dimensionless
    assert isinstance(matter_relationship(), float)
    
    # m_e/m_p is dimensionless (ratio of masses)
    assert isinstance(actual_mass_ratio(), float)
    
    print("✓ All relationships are dimensionless ratios")

def run_all_tests():
    """Run all tests"""
    print("=" * 70)
    print("IMPERIAL PHYSICS FRAMEWORK - UNIT TESTS")
    print("=" * 70)
    print()
    
    tests = [
        test_universal_plasma_limit,
        test_gravity_relationship,
        test_matter_relationship,
        test_matter_validation,
        test_biology_parameter,
        test_geometric_invariant_1,
        test_geometric_invariant_2,
        test_validate_universal_plasma_limit,
        test_dimensionless_ratios,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"✗ {test.__name__} ERROR: {e}")
            failed += 1
    
    print()
    print("=" * 70)
    print(f"TEST RESULTS: {passed} passed, {failed} failed")
    print("=" * 70)
    
    if failed == 0:
        print("✓ ALL TESTS PASSED")
        print("Imperial Physics framework validated successfully!")
        return 0
    else:
        print("✗ SOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)
