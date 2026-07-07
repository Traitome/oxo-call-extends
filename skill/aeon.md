---
name: aeon
category: programming
description: Python/Rust library for symbolic manipulation of Boolean networks using BDD-based methods
tags: [aeon, boolean-network, bdd, attractor, systems-biology, rust, python]
author: oxo-call-community
source_url: "https://github.com/sybila/biodivine-aeon-py"
---

## Concepts

- **Tool Overview**: AEON.py (biodivine-aeon) is a Python library with Rust backend for symbolic analysis of Boolean networks, using BDD-based methods for efficient computation.
- **Core Function**: Performs attractor detection, fixed-point enumeration, trap space analysis, and CTL model checking on Boolean networks.
- **Boolean Networks**: Supports both classical and partially specified Boolean networks with missing or unknown update functions.
- **File Formats**: Supports multiple network formats including .aeon, .sbml, .bnet, and .booleannet.
- **Symbolic Methods**: Uses BDDs (Binary Decision Diagrams) for efficient representation and manipulation of state spaces.
- **Installation**: Install via pip: `pip install biodivine-aeon` or conda: `conda install -c bioconda aeon`
- **Citation**: Beneš, N., Brim, L., Huvar, O., Pastva, S., Šafránek, D., & Šmijáková, E. (2022). AEON.py: Python library for attractor analysis in asynchronous Boolean networks. Bioinformatics, 38(21), 4978-4980.

## Pitfalls

- **Python Version**: Requires Python >= 3.9 for full functionality.
- **Model Validation**: Always validate network models before analysis to catch format errors early.
- **State Space Size**: Complex networks may produce large state spaces - use BDD optimization techniques.
- **Partial Specification**: Partially specified networks require careful handling of unknown update functions.
- **Performance**: Symbolic methods can be memory-intensive for very large networks.

## Examples

### Load and analyze a Boolean network
**Args:**
```python
from biodivine_aeon import BooleanNetwork

# Load network from file
bn = BooleanNetwork.from_file("model.bnet")

# Get network variables
print(bn.variables())

# Get regulatory graph
graph = bn.as_regulatory_graph()
```
**Explanation:** Loads a Boolean network from a .bnet file and accesses basic network properties.

### Find attractors in a network
**Args:**
```python
from biodivine_aeon import BooleanNetwork
from biodivine_aeon.attractors import find_attractors

bn = BooleanNetwork.from_file("model.sbml")

# Find all attractors using default method
attractors = find_attractors(bn)

for i, attractor in enumerate(attractors):
    print(f"Attractor {i}: size = {attractor.size()}")
```
**Explanation:** Performs attractor detection on a Boolean network and prints attractor information.

### Enumerate fixed points
**Args:**
```python
from biodivine_aeon import BooleanNetwork

bn = BooleanNetwork.from_file("model.aeon")

# Get all fixed points (steady states)
fixed_points = bn.fixed_points()

print(f"Found {fixed_points.count()} fixed points")
```
**Explanation:** Enumerates all fixed points (steady states) in the Boolean network.

### Compute trap spaces
**Args:**
```python
from biodivine_aeon import BooleanNetwork

bn = BooleanNetwork.from_file("model.bnet")

# Compute minimal trap spaces
min_trap = bn.minimal_trap_spaces()

# Compute maximal trap spaces  
max_trap = bn.maximal_trap_spaces()

print(f"Minimal trap spaces: {min_trap.count()}")
print(f"Maximal trap spaces: {max_trap.count()}")
```
**Explanation:** Computes minimal and maximal trap spaces for network analysis.

### CTL model checking
**Args:**
```python
from biodivine_aeon import BooleanNetwork
from biodivine_aeon.model_checking import ctl_model_check

bn = BooleanNetwork.from_file("model.sbml")

# Check CTL property: AG(p -> EF(q))
result = ctl_model_check(bn, "AG(p -> EF(q))")

print(f"Property holds: {result.is_true()}")
```
**Explanation:** Performs CTL model checking to verify temporal logic properties.

### Partially specified networks
**Args:**
```python
from biodivine_aeon import BooleanNetwork

# Load partially specified network
bn = BooleanNetwork.from_file("partial_model.bnet")

# Check which functions are partially specified
for var in bn.variables():
    func = bn.get_update_function(var)
    if func.is_partially_specified():
        print(f"{var} has partial specification")
```
**Explanation:** Handles partially specified Boolean networks with unknown update functions.

### Save network to file
**Args:**
```python
from biodivine_aeon import BooleanNetwork

bn = BooleanNetwork.from_file("input.bnet")

# Save in different formats
bn.to_file("output.aeon")
bn.to_file("output.sbml")
bn.to_file("output.bnet")
```
**Explanation:** Converts and saves Boolean networks in different supported formats.