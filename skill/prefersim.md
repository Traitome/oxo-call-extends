---
name: prefersim
category: utility
description: prefersim performs forward simulations under the PRF model.
tags: [prefersim, utility, simulation, population-genetics]
author: oxo-call-community
source_url: "https://github.com/LohmuellerLab/PReFerSim"
---

## Concepts

- **Tool Overview**: prefersim simulates population genetics.
- **Core Function**: Forward genetic simulation.
- **Algorithm**: Uses PRF model methods.
- **Input Format**: Accepts parameter files.
- **Output**: Produces simulated data.
- **Use Case**: Population genetics, evolutionary biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large simulations require memory.
- **Parameter Selection**: May affect results.
- **Computational Time**: Simulations may be slow.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `PReFerSim --help`
**Explanation:** Shows available options and usage instructions.

### Run simulation
**Args:** `PReFerSim -p params.txt -o output.txt`
**Explanation:** Performs forward simulation under PRF model.

### With parameters
**Args:** `PReFerSim -p params.txt -c config.yaml -o output.txt`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `PReFerSim -v -p params.txt -o output.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `PReFerSim -t 4 -p params.txt -o output.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `PReFerSim -p params.txt -o output.vcf --vcf`
**Explanation:** Outputs in VCF format.

### Generate report
**Args:** `PReFerSim -p params.txt -o output.txt --report report.html`
**Explanation:** Generates HTML report.