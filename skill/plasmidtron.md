---
name: plasmidtron
category: annotation
description: plasmidtron assembles plasmids from NGS data.
tags: [plasmidtron, annotation, plasmid, assembly]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/plasmidtron"
---

## Concepts

- **Tool Overview**: plasmidtron assembles plasmids.
- **Core Function**: Plasmid assembly from NGS data.
- **Algorithm**: Uses sequence assembly methods.
- **Input Format**: Accepts NGS sequencing files.
- **Output**: Produces assembled plasmid sequences.
- **Use Case**: Phenotype analysis, plasmid sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Assembly Accuracy**: May have assembly errors.
- **Runtime**: Assembly may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plasmidtron --help`
**Explanation:** Shows available options and usage instructions.

### Assemble plasmids
**Args:** `plasmidtron -i reads.fastq -o plasmids.fasta`
**Explanation:** Assembles plasmids from NGS data.

### With parameters
**Args:** `plasmidtron -i reads.fastq -p params.yaml -o plasmids.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plasmidtron -v -i reads.fastq -o plasmids.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plasmidtron -t 4 -i reads.fastq -o plasmids.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plasmidtron -i reads.fastq -o plasmids.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `plasmidtron -i reads.fastq -o plasmids.fasta --report report.html`
**Explanation:** Generates HTML report.