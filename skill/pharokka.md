---
name: pharokka
category: metagenomics
description: pharokka provides fast phage genome annotation.
tags: [pharokka, metagenomics, phage, annotation]
author: oxo-call-community
source_url: "https://github.com/gbouras13/pharokka"
---

## Concepts

- **Tool Overview**: pharokka annotates phage genomes.
- **Core Function**: Provides fast phage annotation.
- **Algorithm**: Uses phage-specific annotation methods.
- **Input Format**: Accepts phage genome sequences.
- **Output**: Produces comprehensive phage annotations.
- **Use Case**: Phage annotation, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Database Quality**: Results depend on database quality.
- **Gene Prediction**: May miss novel genes.
- **Runtime**: Annotation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pharokka --help`
**Explanation:** Shows available options and usage instructions.

### Annotate genome
**Args:** `pharokka -i phage.fasta -o annotation_results/`
**Explanation:** Annotates phage genome.

### With database
**Args:** `pharokka -i phage.fasta -d phage_db.fasta -o annotation_results/`
**Explanation:** Uses specific phage database.

### Verbose mode
**Args:** `pharokka -v -i phage.fasta -o annotation_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pharokka -t 4 -i phage.fasta -o annotation_results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pharokka -i phage.fasta -o annotation_results/ --format gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `pharokka -i phage.fasta -o annotation_results/ --report report.html`
**Explanation:** Generates HTML report.