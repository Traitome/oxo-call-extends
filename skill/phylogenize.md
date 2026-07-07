---
name: phylogenize
category: population-genomics
description: phylogenize links microbial genes to environments using phylogeny.
tags: [phylogenize, population-genomics, microbial, environment]
author: oxo-call-community
source_url: "https://github.com/pbradleylab/phylogenize"
---

## Concepts

- **Tool Overview**: phylogenize links genes to environments.
- **Core Function**: Microbial gene-environment analysis.
- **Algorithm**: Uses phylogenetic analysis methods.
- **Input Format**: Accepts microbial gene files.
- **Output**: Produces gene-environment linkage results.
- **Use Case**: Microbial analysis, environmental genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Gene Quality**: Results depend on gene quality.
- **Phylogenetic Analysis**: May have analysis errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylogenize --help`
**Explanation:** Shows available options and usage instructions.

### Link genes to environments
**Args:** `phylogenize -i microbial_genes.fasta -e environment_data.txt -o linkage_results.txt`
**Explanation:** Links genes to environments.

### With parameters
**Args:** `phylogenize -i microbial_genes.fasta -e environment_data.txt -p params.yaml -o linkage_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylogenize -v -i microbial_genes.fasta -e environment_data.txt -o linkage_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylogenize -t 4 -i microbial_genes.fasta -e environment_data.txt -o linkage_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylogenize -i microbial_genes.fasta -e environment_data.txt -o linkage_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phylogenize -i microbial_genes.fasta -e environment_data.txt -o linkage_results.txt --report report.html`
**Explanation:** Generates HTML report.