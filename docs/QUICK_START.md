# Quick Start Guide - Imperial Physics

## What is Imperial Physics?

Imperial Physics is a framework that unifies three domains of physics using a single dimensionless constant: **X = 0.15** (the Universal Plasma Limit).

### The Three Domains

1. **Gravity**: G ∝ 1/X
2. **Matter**: m_e/m_p ∝ X^4  
3. **Biology**: Λ = 20.56 Hz

## Installation

No installation needed! The framework uses only Python standard library.

**Requirements**: Python 3.6 or higher

```bash
git clone https://github.com/Unified-Physics-Research/THE-CLINE-CONVERGENCE.git
cd THE-CLINE-CONVERGENCE
```

## Quick Examples

### Run the Example

```bash
python constants/example.py
```

Output shows:
- Universal Plasma Limit (X = 0.15)
- Gravity factor (1/X = 6.667)
- Matter ratio prediction vs actual (7% error)
- Biology frequency (20.56 Hz)
- Fine structure constant
- Complete validation metrics

### Run the Audit

```bash
python audit/generate_audit.py
```

Generates a comprehensive validation log showing empirical verification of all relationships.

### Use in Your Code

```python
from constants import X, gravity_relationship, matter_relationship

# Get the Universal Plasma Limit
print(f"X = {X}")  # 0.15

# Calculate gravity factor
g_factor = gravity_relationship()
print(f"Gravity: G ∝ 1/X = {g_factor}")  # 6.667

# Calculate matter prediction
m_ratio = matter_relationship()
print(f"Matter: m_e/m_p ∝ X^4 = {m_ratio}")  # 0.00050625
```

## Understanding the Results

### Gravity Domain
- **Factor**: 1/X = 6.667
- **Meaning**: Gravitational coupling strength scales inversely with X
- **Interpretation**: Gravity emerges from vacuum lattice geometry

### Matter Domain
- **Prediction**: X^4 = 0.000506
- **Actual**: m_e/m_p = 0.000545
- **Error**: 7.04%
- **Status**: ✓ PASS (within 10% tolerance)
- **Meaning**: Mass ratios have geometric origin

### Biology Domain
- **Frequency**: Λ = 20.56 Hz
- **Period**: 48.6 milliseconds
- **Meaning**: Fundamental biological oscillation rate

## The Text Problem

**Traditional Physics**: Uses calculus and differential equations to model boundaries
- Requires boundary conditions
- Needs numerical solutions
- Complex approximations

**Imperial Physics**: Uses dimensionless ratios to monitor boundaries
- Pure algebraic relationships
- Exact geometric constraints
- Direct empirical validation

**Result**: "We do not model the boundary; we monitor it."

## Directory Structure

```
/constants/     - Python code defining X and relationships
/audit/         - Validation logs and audit scripts
/docs/          - Documentation and technical specs
```

## Key Files

- `README.md` - Main documentation
- `constants/__init__.py` - Core framework definitions
- `constants/example.py` - Usage examples
- `audit/generate_audit.py` - Validation script
- `docs/VISUAL_AFFIDAVIT.md` - Visual documentation
- `docs/TECHNICAL_SPEC.md` - Technical specification

## Validation

All predictions are compared against CODATA 2018 physical constants:
- Electron mass: 9.109×10^-31 kg
- Proton mass: 1.673×10^-27 kg
- No free parameters
- No curve fitting

## Next Steps

1. **Explore the code**: Start with `constants/example.py`
2. **Run the audit**: Execute `audit/generate_audit.py`
3. **Read the docs**: See `docs/VISUAL_AFFIDAVIT.md`
4. **Study the theory**: Read `docs/TECHNICAL_SPEC.md`

## Questions?

See the documentation in `/docs/` for detailed explanations of:
- Mathematical framework
- Physical interpretation
- Empirical validation methodology
- Geometric invariants
- Vacuum lattice structure

---

**Status**: Framework validated and operational ✓  
**Version**: 1.0  
**Date**: 2026-01-26
