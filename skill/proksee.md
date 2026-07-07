---
name: proksee
category: assembly
description: proksee provides assembly, annotation and visualization of microbial genomes.
tags: [proksee, assembly, genome-analysis, visualization]
author: oxo-call-community
source_url: "https://github.com/proksee-project/proksee-cmd"
---

## Concepts

- **Tool Overview**: proksee analyzes microbial genomes.
- **Core Function**: Genome assembly and annotation.
- **Algorithm**: Uses assembly methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces assembled genomes.
- **Use Case**: Microbial genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Assembly Quality**: May affect downstream analysis.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proksee --help`
**Explanation:** Shows available options and usage instructions.

### Run pipeline
**Args:** `proksee -i reads.fastq -o results`
**Explanation:** Runs assembly and annotation pipeline.

### With parameters
**Args:** `proksee -i reads.fastq -p params.yaml -o results`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proksee -v -i reads.fastq -o results`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proksee -t 4 -i reads.fastq -o results`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `proksee -i reads.fastq -o results --format fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `proksee -i reads.fastq -o results --report report.html`
**Explanation:** Generates HTML report.