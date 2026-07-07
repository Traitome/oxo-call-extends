---
name: phyluce
category: population-genomics
description: phyluce provides UCE phylogenomics software tools.
tags: [phyluce, population-genomics, uce, phylogenomics]
author: oxo-call-community
source_url: "https://github.com/faircloth-lab/phyluce"
---

## Concepts

- **Tool Overview**: phyluce performs UCE phylogenomics.
- **Core Function**: UCE phylogenomics toolkit.
- **Algorithm**: Uses UCE analysis methods.
- **Input Format**: Accepts UCE sequence files.
- **Output**: Produces phylogenomic analysis results.
- **Use Case**: Phylogenomics, UCE analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **UCE Quality**: Results depend on UCE quality.
- **Phylogenomic Analysis**: May have analysis errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phyluce --help`
**Explanation:** Shows available options and usage instructions.

### Analyze UCE
**Args:** `phyluce -i uce_sequences.fasta -o phylogenomic_results.txt`
**Explanation:** Analyzes UCE sequences.

### With parameters
**Args:** `phyluce -i uce_sequences.fasta -p params.yaml -o phylogenomic_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phyluce -v -i uce_sequences.fasta -o phylogenomic_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phyluce -t 4 -i uce_sequences.fasta -o phylogenomic_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phyluce -i uce_sequences.fasta -o phylogenomic_results.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `phyluce -i uce_sequences.fasta -o phylogenomic_results.txt --report report.html`
**Explanation:** Generates HTML report.