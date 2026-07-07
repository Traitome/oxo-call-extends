---
name: poly-qtlseq
category: population-genomics
description: poly-qtlseq extends QTL-seq for polyploid F1 populations.
tags: [poly-qtlseq, population-genomics, qtl, polyploid]
author: oxo-call-community
source_url: "https://github.com/TatsumiMizubayashi/PolyploidQtlSeq"
---

## Concepts

- **Tool Overview**: poly-qtlseq analyzes polyploid QTLs.
- **Core Function**: QTL mapping in polyploid populations.
- **Algorithm**: Uses QTL-seq methodology.
- **Input Format**: Accepts sequencing reads and reference.
- **Output**: Produces QTL mapping results.
- **Use Case**: Plant genetics, polyploid breeding.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Mapping Accuracy**: May have QTL detection errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `poly-qtlseq --help`
**Explanation:** Shows available options and usage instructions.

### Run QTL analysis
**Args:** `poly-qtlseq -i reads.fastq -r reference.fasta -o qtl_results/`
**Explanation:** Performs QTL mapping for polyploid data.

### With parameters
**Args:** `poly-qtlseq -i reads.fastq -r reference.fasta -p params.yaml -o qtl_results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `poly-qtlseq -v -i reads.fastq -r reference.fasta -o qtl_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `poly-qtlseq -t 4 -i reads.fastq -r reference.fasta -o qtl_results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `poly-qtlseq -i reads.fastq -r reference.fasta -o qtl.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `poly-qtlseq -i reads.fastq -r reference.fasta -o qtl_results/ --report report.html`
**Explanation:** Generates HTML report.