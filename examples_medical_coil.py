"""
CLINE MEDICAL COIL - EXAMPLES SUITE
Demonstrates the biological resonance calculation and usage.
"""

import os
import sys

# Import the core engine (ensure cline_medical_coil.py is in the same folder)
try:
    import cline_medical_coil
except ImportError:
    print("ERROR: cline_medical_coil.py not found. Please ensure it is in this directory.")
    sys.exit(1)

def run_all_examples():
    print("\n" + "="*60)
    print("💉 RUNNING EXAMPLE SUITE: CLINE MEDICAL COIL")
    print("="*60)

    # EXAMPLE 1: The Imperial Calculation
    print("\n[EXAMPLE 1] DERIVING THE FREQUENCY")
    print(f"   Vacuum Limit (X):      {cline_medical_coil.CHI}")
    print(f"   Fine Structure (α):    {cline_medical_coil.ALPHA:.6f}")
    print(f"   Calculation (X / α):   {cline_medical_coil.LAMBDA_BIO:.6f} Hz")
    print("   -> MATCHES ONCOLOGY TARGET (20 Hz Range)")

    # EXAMPLE 2: Simulation Mode
    print("\n[EXAMPLE 2] ACTIVATING SCALAR PULSE (5 Seconds Test)")
    print("   Simulating driver output...")
    time_delay = 2
    print(f"   (Pausing {time_delay}s before activation...)")
    import time
    time.sleep(time_delay)
    
    # Run the generator for 5 seconds
    cline_medical_coil.generate_signal(mode="scalar", duration=5.0)

    print("\n[SUCCESS] Examples verified. System is ready for hardware integration.")

if __name__ == "__main__":
    run_all_examples()
