---
name: bandwagon
category: utility
description: Bandwagon - Simulate DNA band patterns for gel migration experiments
tags: [bandwagon, utility, gel-electrophoresis, dna-analysis, visualization]
author: oxo-call-community
source_url: "https://github.com/Edinburgh-Genome-Foundry/bandwagon/blob/v0.3.4/README.rst"
---

## Concepts

- **Tool Overview**: Bandwagon (v0.3.4) simulates DNA band patterns for gel migration experiments, helping visualize expected fragment separation.
- **Core Function**: Simulates DNA band patterns for gel electrophoresis experiments.
- **Gel Simulation**: Models DNA fragment migration based on size and gel properties.
- **Band Visualization**: Generates visual representations of expected band patterns.
- **Fragment Analysis**: Helps predict fragment separation based on size markers.
- **Input/Output**: Accepts sequence files or fragment size data; outputs gel images and analysis.
- **Installation**: `conda install -c bioconda bandwagon`.

## Pitfalls

- **Size Estimation**: Band positions are estimates and may vary based on gel conditions.
- **Resolution Limits**: Very similar fragment sizes may not be distinguishable.
- **Complex Mixtures**: Complex DNA mixtures may produce overlapping bands.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Simulate gel from sequence
**Args:** `bandwagon --sequence dna.fasta --output gel.png`
**Explanation:** Simulates gel migration pattern from DNA sequence file.

### Specify fragment sizes
**Args:** `bandwagon --fragments 100,200,500,1000 --output gel.png`
**Explanation:** Simulates gel with specified fragment sizes in base pairs.

### Add size marker
**Args:** `bandwagon --sequence dna.fasta --marker 100-1000 --output gel.png`
**Explanation:** Includes size marker ladder in gel simulation.

### Custom gel parameters
**Args:** `bandwagon --sequence dna.fasta --voltage 100 --time 60 --output gel.png`
**Explanation:** Specifies voltage and time for gel simulation.

### Batch processing
**Args:** `bandwagon --input-list samples.txt --output-dir results/`
**Explanation:** Processes multiple samples in batch mode.

### Generate report
**Args:** `bandwagon --sequence dna.fasta --report --output report.txt`
**Explanation:** Generates detailed analysis report with band positions.

### Display help
**Args:** `bandwagon --help`
**Explanation:** Shows all available command-line options and usage information.