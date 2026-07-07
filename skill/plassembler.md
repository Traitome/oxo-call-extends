---
name: plassembler
category: annotation
description: plassembler assembles plasmids from hybrid sequenced data.
tags: [plassembler, annotation, plasmid, assembly]
author: oxo-call-community
source_url: "https://github.com/gbouras13/plassembler"
---

## Concepts

- **Tool Overview**: plassembler assembles plasmids.
- **Core Function**: Hybrid plasmid assembly.
- **Algorithm**: Uses hybrid assembly methods.
- **Input Format**: Accepts FASTA sequence files.
- **Output**: Produces assembled plasmid sequences.
- **Use Case**: Bacterial genomics, plasmid analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Assembly Accuracy**: May have assembly errors.
- **Runtime**: Assembly may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plassembler --help`
**Explanation:** Shows available options and usage instructions.

### Assemble plasmids
**Args:** `plassembler -i reads.fasta -o plasmids.fasta`
**Explanation:** Assembles plasmids from hybrid sequenced data.

### With parameters
**Args:** `plassembler -i reads.fasta -p params.yaml -o plasmids.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plassembler -v -i reads.fasta -o plasmids.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plassembler -t 4 -i reads.fasta -o plasmids.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plassembler -i reads.fasta -o plasmids.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `plassembler -i reads.fasta -o plasmids.fasta --report report.html`
**Explanation:** Generates HTML report.