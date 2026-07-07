---
name: pepgenome
category: expression
description: pepgenome maps peptides to ENSEMBL genome coordinates.
tags: [pepgenome, expression, peptide, mapping]
author: oxo-call-community
source_url: "https://github.com/bigbio/pgatk/"
---

## Concepts

- **Tool Overview**: pepgenome maps peptide coordinates.
- **Core Function**: Maps peptides to genome positions.
- **Algorithm**: Uses ENSEMBL coordinate mapping.
- **Input Format**: Accepts peptide evidence files.
- **Output**: Produces genome coordinate mappings.
- **Use Case**: Proteomics, peptide mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large peptide sets require memory.
- **Peptide Quality**: Results depend on peptide quality.
- **ENSEMBL Version**: Requires proper ENSEMBL version.
- **Runtime**: Mapping may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pepgenome --help`
**Explanation:** Shows available options and usage instructions.

### Map peptides
**Args:** `pepgenome -i peptides.txt -g genome.fasta -o coordinates.txt`
**Explanation:** Maps peptides to genome coordinates.

### With ENSEMBL
**Args:** `pepgenome -i peptides.txt -e ensembl.gtf -o coordinates.txt`
**Explanation:** Uses ENSEMBL annotation for mapping.

### Verbose mode
**Args:** `pepgenome -v -i peptides.txt -g genome.fasta -o coordinates.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pepgenome -t 4 -i peptides.txt -g genome.fasta -o coordinates.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pepgenome -i peptides.txt -g genome.fasta -o coordinates.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pepgenome -i peptides.txt -g genome.fasta -o coordinates.txt --report report.html`
**Explanation:** Generates HTML report.