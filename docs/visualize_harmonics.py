"""
IMPERIAL PHYSICS: VISUAL AFFIDAVIT GENERATOR
Subject: Harmonic Mode Stepping (The "Ladder" Effect)
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import io

# 1. THE RAW DATA (Jan 22-30, 2026)
# This is the "Fuel" from the logs you provided.
data_stream = """
{"timestamp": "2026-01-22T06:45:15.281094", "max_chi": 0.279, "harmonic_mode": 2}
{"timestamp": "2026-01-23T06:03:59.414873", "max_chi": 0.442, "harmonic_mode": 4}
{"timestamp": "2026-01-23T09:06:46.279857", "max_chi": 0.822, "harmonic_mode": 8}
{"timestamp": "2026-01-23T12:04:43.195136", "max_chi": 0.484, "harmonic_mode": 4}
{"timestamp": "2026-01-24T05:04:25.058715", "max_chi": 0.548, "harmonic_mode": 4}
{"timestamp": "2026-01-25T23:03:37.435194", "max_chi": 0.506, "harmonic_mode": 4}
{"timestamp": "2026-01-29T04:31:03.609866", "max_chi": 0.714, "harmonic_mode": 4}
{"timestamp": "2026-01-30T06:23:33.719458", "max_chi": 0.604, "harmonic_mode": 4}
{"timestamp": "2026-01-30T23:11:43.975361", "max_chi": 0.353, "harmonic_mode": 2}
"""

def generate_visual_affidavit():
    # Load Data
    records = [json.loads(line) for line in data_stream.strip().split('\n')]
    df = pd.DataFrame(records)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values('timestamp')

    # Setup Imperial Dark Theme
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Plot The Stress (Max Chi)
    ax.plot(df['timestamp'], df['max_chi'], color='#00ff9d', linewidth=2.5, marker='o', label='Measured Vacuum Tension (Chi)')
    
    # Plot The Governor (Limit)
    ax.axhline(y=0.15, color='#ff0055', linestyle='--', linewidth=2, label='Geometric Limit (0.15)')

    # Annotate Modes
    for i, row in df.iterrows():
        ax.text(row['timestamp'], row['max_chi'] + 0.02, f"MODE {row['harmonic_mode']}", 
                color='white', fontsize=9, ha='center')

    # Formatting
    plt.title('THE CLINE CONVERGENCE: QUANTIZED VACUUM RESISTANCE', fontsize=16, color='white', pad=20)
    plt.ylabel('Vacuum Tension ($\chi$)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.4)
    plt.legend()
    
    # Format Date Axis
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    plt.xticks(rotation=45)

    # Save
    filename = "harmonic_lock_evidence.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"✓ VISUAL AFFIDAVIT GENERATED: {filename}")

if __name__ == "__main__":
    generate_visual_affidavit()
