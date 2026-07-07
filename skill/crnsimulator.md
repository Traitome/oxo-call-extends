---
name: crnsimulator
category: simulation
description: Simulate chemical reaction networks (CRNs) using ordinary differential equations (ODEs) with Python code generation
tags: [crnsimulator, CRN, ODE, chemical-reaction-network, simulation, systems-biology, biochemistry, python-code-generation]
author: oxo-call-community
source_url: "https://github.com/bad-ants-fleet/crnsimulator"
---

## Concepts

- **Tool Overview**: crnsimulator (v0.9) - A tool for simulating Chemical Reaction Networks (CRNs) using Ordinary Differential Equations (ODEs).
- **Core Function**: Converts CRN definitions into ODE systems, generates executable Python scripts for simulation, and produces various output formats including plots.
- **Algorithm**: (1) Parses CRN text format describing reactions with species and rate constants. (2) Builds ODE system mathematically from reaction stoichiometry. (3) Generates Python script using scipy/integrate for numerical solving. (4) Executes simulation with user-specified parameters and initial conditions.
- **Input**: CRN file (plain text format with reactions like `A + B -> C [k=0.1]`), command-line parameters for initial concentrations and simulation time.
- **Output**: Python executable script (`ozzy.py`), simulation results in various formats (text, numpy arrays), plot files (PDF, PNG).
- **Application**: Systems biology modeling, biochemical pathway analysis, synthetic biology circuit design, chemical kinetics simulation, population dynamics.
- **Installation**: `pip install crnsimulator` or `conda install -c bioconda crnsimulator`

## Pitfalls

- **Python Dependencies**: Requires Python with scipy, numpy, matplotlib installed for generated scripts to run.
- **Numerical Stability**: Stiff ODE systems may require solver tolerance adjustments or different integrators.
- **CRN Format**: Must follow correct CRN syntax - species names are case-sensitive, rate constants must be positive numbers.
- **Time Scale**: Simulation time units are arbitrary - ensure they match your biological system's timescale.
- **Initial Conditions**: Must specify initial species concentrations - system behavior is sensitive to these values.
- **Deterministic Only**: Default output is deterministic ODE solution - stochastic simulations require different tools.

## Examples

### Basic CRN simulation
**Args:** `crnsimulator -o ozzy < oscillator.crn`
**Explanation:** Read CRN from stdin and generate Python simulation script named ozzy.py.

### Run simulation with parameters
**Args:** `python ozzy.py --p0 A=0.1 B=1e-2 C=1e-3 --t8 10000 --pyplot ozzy.pdf`
**Explanation:** Run generated script with initial concentrations, time endpoint 10000, and output plot to PDF.

### Pipe CRN directly
**Args:** `cat oscillator.crn | crnsimulator -o my_sim`
**Explanation:** Pipe CRN file content directly to crnsimulator.

### Auto-run with parameters
**Args:** `crnsimulator --p0 A=0.1 B=1e-2 --t8 1000 -o sim < reaction.crn`
**Explanation:** Pass parameters directly to crnsimulator to auto-run simulation after code generation.

### Custom rate constants
**Args:** `crnsimulator -o sim --k "k1=0.5,k2=0.3" < model.crn`
**Explanation:** Override rate constants when generating the simulation script.

### List available species
**Args:** `crnsimulator --list < model.crn`
**Explanation:** Display all species names defined in the CRN without generating simulation.

### Multi-step time output
**Args:** `python ozzy.py --p0 A=1.0 B=0.5 --t8 500 --t8 1000 --t8 5000 --of text --oz output.txt`
**Explanation:** Generate output at multiple time points and save as text file.

### Stochastic simulation (using different tool)
**Args:** `crnsimulator --stochastic -o gillespie < model.crn`
**Explanation:** Note: crnsimulator is primarily for ODE-based deterministic simulation. For stochastic, consider using GillesPy or similar tools.

### Check generated code
**Args:** `cat ozzy.py | head -50`
**Explanation:** Inspect the generated Python code to understand the ODE system structure.

### Sensitivity analysis
**Args:** `python ozzy.py --p0 A=1.0 --param-scan k1=0.1:1.0:10 --of numpy --oz scan.npz`
**Explanation:** Run parameter scan over rate constant k1 range and save results as numpy arrays.

### Display version
**Args:** `crnsimulator --version`
**Explanation:** Show installed version.

### Show help
**Args:** `crnsimulator --help`
**Explanation:** Display all command-line options and usage information.
