import numpy as np
import math

class ImperialLatticeValidator:
    """
    IMPERIAL PHYSICS VALIDATION ENGINE
    ---------------------------------
    Validates the Universal Plasma Limit (Chi <= 0.15) using
    Geometric Tension (Option C).
    """
    
    def __init__(self):
        self.CHI_LIMIT = 0.15
        self.TOLERANCE = 0.01  # Measurement noise floor
        
        # GEOMETRIC CONSTANTS (Solar System Calibration)
        self.B_TENSION_1AU = 5.0  # nT (nanoTesla)
        self.R_EARTH = 1.0        # AU

    def calculate_geometric_tension(self, r_au):
        """
        OPTION C: LOCAL EQUILIBRIUM (LATTICE TENSION)
        Formula: B_baseline = B_1AU * (1 / r^2)
        """
        if r_au is None or r_au <= 0:
            return self.B_TENSION_1AU
        return self.B_TENSION_1AU * (self.R_EARTH / r_au)**2

    def calculate_chi_3d(self, b_vector, r_au):
        """
        Audits the vacuum structure at a specific 3D coordinate.
        """
        # 1. GET THE DATA
        if isinstance(b_vector, (list, tuple, np.ndarray)):
            b_total_obs = np.linalg.norm(b_vector)
        else:
            b_total_obs = float(b_vector)

        # 2. GET THE LAW
        b_baseline_geo = self.calculate_geometric_tension(r_au)

        # 3. CALCULATE DELTA
        delta_b = abs(b_total_obs - b_baseline_geo)

        # 4. CALCULATE CHI
        if b_baseline_geo == 0:
            return 0.0
        return delta_b / b_baseline_geo

    def validate_data_point(self, b_vector, r_au):
        """
        The Enforcement Function.
        """
        chi = self.calculate_chi_3d(b_vector, r_au)
        is_stable = chi <= (self.CHI_LIMIT + self.TOLERANCE)
        
        return {
            "status": "STABLE" if is_stable else "LATTICE_STRESS",
            "chi": round(chi, 5),
            "limit": self.CHI_LIMIT,
            "tension_baseline": round(self.calculate_geometric_tension(r_au), 2),
            "observed_mag": round(np.linalg.norm(b_vector), 2)
        }
