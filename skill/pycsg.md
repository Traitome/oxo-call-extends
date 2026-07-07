---
name: pycsg
category: programming
description: pycsg is a Python port of csg.js for constructive solid geometry operations.
tags: [pycsg, programming, csg, 3d-modelling]
author: oxo-call-community
source_url: "https://github.com/pletzer/pycsg"
---

## Concepts

- **Tool Overview**: pycsg performs CSG operations.
- **Core Function**: Constructive solid geometry.
- **Algorithm**: Uses Boolean operations.
- **Input Format**: Accepts 3D models.
- **Output**: Produces combined models.
- **Use Case**: 3D modeling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex models require memory.
- **Data Quality**: Results depend on input quality.
- **Model Complexity**: May affect performance.
- **Runtime**: Operations may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pycsg --help`
**Explanation:** Shows available options and usage instructions.

### Union operation
**Args:** `pycsg union -i1 model1.stl -i2 model2.stl -o combined.stl`
**Explanation:** Performs CSG union operation.

### With parameters
**Args:** `pycsg union -i1 model1.stl -i2 model2.stl -p params.yaml -o combined.stl`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pycsg -v union -i1 model1.stl -i2 model2.stl -o combined.stl`
**Explanation:** Runs with verbose output.

### Intersection
**Args:** `pycsg intersect -i1 model1.stl -i2 model2.stl -o intersect.stl`
**Explanation:** Performs CSG intersection.

### Difference
**Args:** `pycsg difference -i1 model1.stl -i2 model2.stl -o diff.stl`
**Explanation:** Performs CSG difference.

### Generate report
**Args:** `pycsg union -i1 model1.stl -i2 model2.stl -o combined.stl --report report.html`
**Explanation:** Generates HTML report.