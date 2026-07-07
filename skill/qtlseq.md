---
name: qtlseq
category: variant-calling
description: QTL-seq is a pipeline to identify causative mutations responsible for a phenotype using bulk segregant analysis.
tags: [qtlseq, variant-calling, qtl, bulk-segregant]
author: oxo-call-community
source_url: "https://github.com/YuSugihara/QTL-seq"
---

## Concepts

- **Tool Overview**: qtlseq identifies causative mutations.
- **Core Function**: QTL mapping.
- **Algorithm**: Uses bulk segregant analysis.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces QTL regions.
- **Use Case**: Genetic mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Population Structure**: Must be considered.
- **Read Depth**: Must be sufficient.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qtlseq --help`
**Explanation:** Shows available options and usage instructions.

### Run QTL-seq
**Args:** `qtlseq run -i reads.fastq -r reference.fasta -o qtl_results/`
**Explanation:** Identifies causative mutations.

### With parameters
**Args:** `qtlseq run -i reads.fastq -p params.yaml -o qtl_results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qtlseq -v run -i reads.fastq -o qtl_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qtlseq -t 4 run -i reads.fastq -o qtl_results/`
**Explanation:** Uses 4 threads for parallel processing.

### With annotation
**Args:** `qtlseq run -i reads.fastq -a annotation.gff -o qtl_results/`
**Explanation:** Uses genome annotation.

### Generate report
**Args:** `qtlseq run -i reads.fastq -o qtl_results/ --report report.html`
**Explanation:** Generates HTML report.