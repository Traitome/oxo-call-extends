---
name: r2r
category: population-genomics
description: R2R generates aesthetic consensus RNA secondary structure depictions for visualization.
tags: [r2r, population-genomics, rna, visualization]
author: oxo-call-community
source_url: "http://breaker.research.yale.edu/R2R/"
---

## Concepts

- **Tool Overview**: r2r visualizes RNA structures.
- **Core Function**: RNA structure depiction.
- **Algorithm**: Uses consensus methods.
- **Input Format**: Accepts structure files.
- **Output**: Produces diagrams.
- **Use Case**: RNA analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Structure Quality**: Must be good.
- **Parameters**: Must be configured.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `r2r --help`
**Explanation:** Shows available options and usage instructions.

### Draw structure
**Args:** `r2r draw -i structure.sto -o structure.png`
**Explanation:** Draws RNA secondary structure.

### With parameters
**Args:** `r2r draw -i structure.sto -p params.cfg -o structure.png`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `r2r -v draw -i structure.sto -o structure.png`
**Explanation:** Runs with verbose output.

### Multiple structures
**Args:** `r2r draw -i struct1.sto,struct2.sto -o structures.png`
**Explanation:** Draws multiple structures.

### Consensus mode
**Args:** `r2r consensus -i align.sto -o consensus.png`
**Explanation:** Generates consensus structure.

### Generate report
**Args:** `r2r draw -i structure.sto -o structure.png --report report.html`
**Explanation:** Generates HTML report.