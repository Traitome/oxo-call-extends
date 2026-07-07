---
name: phigaro
category: metagenomics
description: phigaro predicts phages and prophages in genomic data.
tags: [phigaro, metagenomics, phage, prophage]
author: oxo-call-community
source_url: "https://github.com/bobeobibo/phigaro"
---

## Concepts

- **Tool Overview**: phigaro predicts phage regions.
- **Core Function**: Detects prophages in genomes.
- **Algorithm**: Uses phage prediction methods.
- **Input Format**: Accepts genome assemblies.
- **Output**: Produces phage region annotations.
- **Use Case**: Phage detection, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Phage Detection**: May miss novel phages.
- **Genome Quality**: Results depend on genome quality.
- **Runtime**: Prediction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phigaro --help`
**Explanation:** Shows available options and usage instructions.

### Predict phages
**Args:** `phigaro -i genome.fasta -o phage_regions.txt`
**Explanation:** Predicts phage regions.

### With parameters
**Args:** `phigaro -i genome.fasta -p params.yaml -o phage_regions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phigaro -v -i genome.fasta -o phage_regions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phigaro -t 4 -i genome.fasta -o phage_regions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phigaro -i genome.fasta -o phage_regions.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `phigaro -i genome.fasta -o phage_regions.txt --report report.html`
**Explanation:** Generates HTML report.