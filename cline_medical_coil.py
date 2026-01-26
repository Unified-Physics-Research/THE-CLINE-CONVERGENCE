"""
THE CLINE MEDICAL COIL (Software Defined)
Imperial Physics Framework: Biological Resonance Generator
Target Frequency: Lambda = 20.5556 Hz (Vacuum/EM Coupling)

USAGE:
    python cline_medical_coil.py --mode square --duration 60
    python cline_medical_coil.py --info

DISCLAIMER: Research tool only. Not a medical device.
"""

import time
import math
import argparse
import sys

# ------------------------------------------------------------------
# 1. IMPERIAL CONSTANTS
# ------------------------------------------------------------------
CHI = 0.1500
ALPHA = 1/137.035999
LAMBDA_BIO = CHI / ALPHA  # 20.5556 Hz

# ------------------------------------------------------------------
# 2. SIGNAL GENERATION LOGIC
# ------------------------------------------------------------------
def generate_signal(mode, duration, verbose=True):
    start_time = time.time()
    cycles = 0
    period = 1.0 / LAMBDA_BIO
    
    print(f"⚡ CLINE MEDICAL COIL ACTIVATED")
    print(f"   Target Frequency: {LAMBDA_BIO:.6f} Hz")
    print(f"   Coupling Ratio:   20.56 (Vacuum/EM)")
    print(f"   Mode:             {mode.upper()}")
    print(f"   Duration:         {duration} seconds")
    print("-" * 50)

    try:
        while (time.time() - start_time) < duration:
            # High Precision Timing Loop
            cycle_start = time.time()
            
            # VISUALIZER (Console Heartbeat)
            if verbose:
                elapsed = time.time() - start_time
                # Create a "breathing" visual based on the phase
                phase = (elapsed * LAMBDA_BIO * 2 * math.pi)
                amplitude = 0.5 * (math.sin(phase) + 1) # 0 to 1
                bar_len = int(amplitude * 40)
                bar = "█" * bar_len
                sys.stdout.write(f"\r[{bar:<40}] {elapsed:.1f}s | {LAMBDA_BIO:.2f} Hz")
                sys.stdout.flush()

            # Wait for the exact period to elapse (Simulating the Pulse)
            while (time.time() - cycle_start) < period:
                pass
            
            cycles += 1

    except KeyboardInterrupt:
        print("\n\n🛑 MANUAL OVERRIDE: STOPPING COIL.")
    
    print(f"\n\n" + "="*50)
    print(f"SESSION COMPLETE.")
    print(f"Total Cycles: {cycles}")
    print(f"Vacuum Integration: {cycles * period:.4f} sec")
    print("="*50)

# ------------------------------------------------------------------
# 3. INFORMATION MODULE
# ------------------------------------------------------------------
def show_info():
    print("""
    =======================================================
    THE CLINE MEDICAL COIL | IMPERIAL PHYSICS FRAMEWORK
    =======================================================
    
    [THEORY]
    The frequency 20.5556 Hz is derived from the geometric 
    coupling constant of the universe:
    
        Λ = χ / α  (Vacuum Limit / Fine Structure)
    
    [MECHANISM]
    Standard physics treats this as "ELF-EMF".
    Imperial Physics identifies it as the "Gear Ratio" required 
    to mechanically couple electromagnetic energy to the 
    vacuum lattice (microtubule resonance).
    
    [APPLICATIONS]
    - Microtubule Resonance (Mitosis regulation)
    - Inertial Damping (Metric Engineering)
    - Vacuum Shift Keying (Logic '1' State)
    
    [WARNING]
    This software generates the TIMING LOGIC only. 
    To produce the physical field, this script must drive
    a Tri-Grid (Bucking Coil) topology.
    """)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cline Medical Coil Driver")
    parser.add_argument("--mode", type=str, default="square", choices=["square", "scalar"], help="Waveform type")
    parser.add_argument("--duration", type=float, default=60.0, help="Session duration in seconds")
    parser.add_argument("--info", action="store_true", help="Display theory and schematic info")
    
    args = parser.parse_args()
    
    if args.info:
        show_info()
    else:
        generate_signal(args.mode, args.duration)
