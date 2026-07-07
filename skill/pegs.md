---
name: pegs
category: utility
description: PEGS performs peak-set enrichment of gene sets.
tags: [pegs, utility, enrichment, gene-sets]
author: oxo-call-community
source_url: "https://github.com/fls-bioinformatics-core/pegs"
---

## Concepts

- **Tool Overview**: PEGS analyzes peak enrichment.
- **Core Function**: Performs gene set enrichment on peaks.
- **Algorithm**: Uses enrichment statistical methods.
- **Input Format**: Accepts peak and gene set files.
- **Output**: Produces enrichment results.
- **Use Case**: Peak analysis, gene set enrichment.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large peak sets require memory.
- **Peak Quality**: Results depend on peak quality.
- **Gene Set Definition**: Requires proper gene set definition.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pegs --help`
**Explanation:** Shows available options and usage instructions.

### Run enrichment
**Args:** `pegs -i peaks.bed -g gene_sets.txt -o enrichment.txt`
**Explanation:** Performs peak-set enrichment.

### With annotation
**Args:** `pegs -i peaks.bed -g gene_sets.txt -a annotation.gtf -o enrichment.txt`
**Explanation:** Uses gene annotation for enrichment.

### Verbose mode
**Args:** `pegs -v -i peaks.bed -g gene_sets.txt -o enrichment.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pegs -t 4 -i peaks.bed -g gene_sets.txt -o enrichment.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pegs -i peaks.bed -g gene_sets.txt -o enrichment.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pegs -i peaks.bed -g gene_sets.txt -o enrichment.txt --report report.html`
**Explanation:** Generates HTML report.