---
name: phast
category: population-genomics
description: phast performs phylogenetic analysis with space/time models.
tags: [phast, population-genomics, phylogeny, evolution]
author: oxo-call-community
source_url: "https://github.com/CshlSiepelLab/phast"
---

## Concepts

- **Tool Overview**: phast analyzes phylogenetics.
- **Core Function**: Uses space/time evolutionary models.
- **Algorithm**: Implements phylogenetic analysis methods.
- **Input Format**: Accepts genome and alignment files.
- **Output**: Produces phylogenetic analysis results.
- **Use Case**: Phylogenetics, evolutionary modeling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Model Selection**: Requires proper model choice.
- **Alignment Quality**: Results depend on alignment quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phast --help`
**Explanation:** Shows available options and usage instructions.

### Analyze phylogeny
**Args:** `phast -i alignment.fasta -o phylogenetic_results.txt`
**Explanation:** Performs phylogenetic analysis.

### With model
**Args:** `phast -i alignment.fasta -m space_time -o phylogenetic_results.txt`
**Explanation:** Uses space/time model.

### Verbose mode
**Args:** `phast -v -i alignment.fasta -o phylogenetic_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phast -t 4 -i alignment.fasta -o phylogenetic_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phast -i alignment.fasta -o phylogenetic_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phast -i alignment.fasta -o phylogenetic_results.txt --report report.html`
**Explanation:** Generates HTML report.