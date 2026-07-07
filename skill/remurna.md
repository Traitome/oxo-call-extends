---
name: remurna
category: formatting
description: RemuRNA measures Single-Nucleotide Polymorphism-induced changes of RNA conformation.
tags: [remurna, formatting, rna-structure, snp-analysis]
author: oxo-call-community
source_url: "https://www.ncbi.nlm.nih.gov/CBBresearch/Przytycka/software/remurna.html"
---

## Concepts

- **Tool Overview**: remurna measures RNA changes.
- **Core Function**: RNA conformation analysis.
- **Algorithm**: Uses structural methods.
- **Input Format**: Accepts SNP data.
- **Output**: Produces conformation changes.
- **Use Case**: RNA analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **SNP Quality**: Affects analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `remurna --help`
**Explanation:** Shows available options and usage instructions.

### Analyze RNA
**Args:** `remurna analyze -i snp_data.txt -r rna_structure.txt -o changes.txt`
**Explanation:** Measures SNP-induced RNA conformation changes.

### With parameters
**Args:** `remurna analyze -i snp_data.txt -p params.yaml -o changes.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `remurna -v analyze -i snp_data.txt -o changes.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `remurna -t 4 analyze -i snp_data.txt -o changes.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With structure
**Args:** `remurna analyze -i snp_data.txt -s structure.pdb -o changes.txt`
**Explanation:** Uses 3D structure file.

### Generate report
**Args:** `remurna analyze -i snp_data.txt -o changes.txt --report report.html`
**Explanation:** Generates HTML report.