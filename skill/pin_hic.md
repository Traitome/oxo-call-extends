---
name: pin_hic
category: epigenomics
description: pin_hic provides Hi-C scaffolding methods.
tags: [pin_hic, epigenomics, hi-c, scaffolding]
author: oxo-call-community
source_url: "https://github.com/dfguan/pin_hic"
---

## Concepts

- **Tool Overview**: pin_hic performs Hi-C scaffolding.
- **Core Function**: Genome scaffolding using Hi-C data.
- **Algorithm**: Uses Hi-C interaction data.
- **Input Format**: Accepts Hi-C sequencing files.
- **Output**: Produces scaffolded genome results.
- **Use Case**: Genome assembly, scaffolding.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on Hi-C quality.
- **Scaffolding Errors**: May introduce misassemblies.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pin_hic --help`
**Explanation:** Shows available options and usage instructions.

### Perform Hi-C scaffolding
**Args:** `pin_hic -i hic_data.fastq -o scaffolded_genome.fasta`
**Explanation:** Scaffolds genome using Hi-C data.

### With parameters
**Args:** `pin_hic -i hic_data.fastq -p params.yaml -o scaffolded_genome.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pin_hic -v -i hic_data.fastq -o scaffolded_genome.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pin_hic -t 4 -i hic_data.fastq -o scaffolded_genome.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pin_hic -i hic_data.fastq -o scaffolded_genome.gfa --gfa`
**Explanation:** Outputs in GFA format.

### Generate report
**Args:** `pin_hic -i hic_data.fastq -o scaffolded_genome.fasta --report report.html`
**Explanation:** Generates HTML report.