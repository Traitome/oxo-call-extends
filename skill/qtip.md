---
name: qtip
category: alignment
description: QTip predicts read alignment mapping qualities using a tandem simulation approach.
tags: [qtip, alignment, mapping-quality, simulation]
author: oxo-call-community
source_url: "https://github.com/BenLangmead/qtip"
---

## Concepts

- **Tool Overview**: qtip predicts mapping quality.
- **Core Function**: Quality prediction.
- **Algorithm**: Uses simulation.
- **Input Format**: Accepts SAM/BAM files.
- **Output**: Produces quality scores.
- **Use Case**: Alignment QC.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Simulation Parameters**: Must be configured.
- **Reference Genome**: Must be correct.
- **Runtime**: Simulation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qtip --help`
**Explanation:** Shows available options and usage instructions.

### Run prediction
**Args:** `qtip predict -i aligned.bam -o qualities.txt`
**Explanation:** Predicts mapping qualities.

### With parameters
**Args:** `qtip predict -i aligned.bam -p params.yaml -o qualities.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qtip -v predict -i aligned.bam -o qualities.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qtip -t 4 predict -i aligned.bam -o qualities.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `qtip predict -i aligned.bam -r reference.fasta -o qualities.txt`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `qtip predict -i aligned.bam -o qualities.txt --report report.html`
**Explanation:** Generates HTML report.