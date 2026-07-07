---
name: phanotate
category: metagenomics
description: phanotate calls genes in phage genomes.
tags: [phanotate, metagenomics, phage, gene-calling]
author: oxo-call-community
source_url: "https://github.com/deprekate/PHANOTATE"
---

## Concepts

- **Tool Overview**: phanotate calls phage genes.
- **Core Function**: Predicts genes in phage genomes.
- **Algorithm**: Uses phage-specific gene prediction.
- **Input Format**: Accepts phage genome sequences.
- **Output**: Produces gene annotations.
- **Use Case**: Phage annotation, gene prediction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Gene Prediction**: May miss novel genes.
- **Phage Specificity**: Optimized for phage genomes.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phanotate --help`
**Explanation:** Shows available options and usage instructions.

### Call genes
**Args:** `phanotate -i phage.fasta -o genes.gff`
**Explanation:** Calls genes in phage genome.

### With parameters
**Args:** `phanotate -i phage.fasta -p params.yaml -o genes.gff`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phanotate -v -i phage.fasta -o genes.gff`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phanotate -t 4 -i phage.fasta -o genes.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phanotate -i phage.fasta -o genes.gtf --gtf`
**Explanation:** Outputs in GTF format.

### Generate report
**Args:** `phanotate -i phage.fasta -o genes.gff --report report.html`
**Explanation:** Generates HTML report.