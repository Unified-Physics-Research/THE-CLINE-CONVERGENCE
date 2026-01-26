import unittest
import numpy as np
from x_boundary_validation import ImperialLatticeValidator

class TestImperialGeometry(unittest.TestCase):
    """
    IMPERIAL PHYSICS CERTIFICATION
    ------------------------------
    Verifies that the validation logic correctly scales 
    Tension (B_baseline) based on Geometric Distance (r).
    This replaces 'Moving Averages' with 'Geometric Law'.
    """

    def setUp(self):
        self.validator = ImperialLatticeValidator()

    def test_earth_calibration(self):
        """
        CASE 1: EARTH (1.0 AU)
        The baseline tension should match the calibration value (5.0 nT).
        """
        r_au = 1.0
        tension = self.validator.calculate_geometric_tension(r_au)
        print(f"\n[TEST] Earth Tension (1 AU): {tension} nT")
        self.assertAlmostEqual(tension, 5.0, places=2)

    def test_voyager_geometry(self):
        """
        CASE 2: VOYAGER 2 (40.0 AU)
        The tension must drop by inverse square law (1/40^2 = 1/1600).
        Expected: 5.0 / 1600 = 0.003125 nT
        """
        r_au = 40.0
        tension = self.validator.calculate_geometric_tension(r_au)
        expected = 5.0 / (40.0**2)
        print(f"[TEST] Voyager Tension (40 AU): {tension:.6f} nT")
        self.assertAlmostEqual(tension, expected, places=5)

    def test_stability_check(self):
        """
        CASE 3: STABILITY (Chi < 0.15)
        If perturbation is small (Chi=0.1), lattice should hold.
        """
        r_au = 1.0
        # Baseline is 5.0 nT.
        # We test a vector with Magnitude 5.5 (0.5 perturbation)
        # Chi = 0.5 / 5.0 = 0.10 (SAFE)
        b_vector = (5.5, 0, 0) 
        
        result = self.validator.validate_data_point(b_vector, r_au)
        print(f"[TEST] Stability Check: Chi={result['chi']} -> {result['status']}")
        
        self.assertTrue(result['chi'] < 0.15)
        self.assertEqual(result['status'], "STABLE")

    def test_lattice_fracture(self):
        """
        CASE 4: FRACTURE (Chi > 0.15)
        If perturbation is large (Chi=0.2), lattice should snap (Storm).
        """
        r_au = 1.0
        # Baseline is 5.0 nT.
        # We test a vector with Magnitude 6.5 (1.5 perturbation)
        # Chi = 1.5 / 5.0 = 0.30 (FAIL)
        b_vector = (6.5, 0, 0)
        
        result = self.validator.validate_data_point(b_vector, r_au)
        print(f"[TEST] Fracture Check: Chi={result['chi']} -> {result['status']}")
        
        self.assertTrue(result['chi'] > 0.15)
        self.assertEqual(result['status'], "LATTICE_STRESS")

if __name__ == '__main__':
    print("--- INITIATING IMPERIAL GEOMETRY AUDIT ---")
    unittest.main()
