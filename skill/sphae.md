---
name: sphae
category: microbiology
description: Sphae - Phage toolkit for bacteriophage analysis
tags: [sphae, microbiology, phage, bacteriophage, viral-analysis]
author: oxo-call-community
source_url: "https://github.com/linsalrob/sphae"
---

## Concepts

- **Tool Overview**: sphae (v1.5.4) - A phage analysis toolkit
- **Core Function**: Provides tools for bacteriophage genome analysis
- **Input/Output**: Accepts phage genomes; outputs analysis results
- **Algorithm**: Various phage analysis algorithms
- **Installation**: `conda install -c bioconda sphae`
- **Key Features**: Phage analysis, genome annotation, viral classification

## Pitfalls

- **Input Requirements**: Requires properly formatted phage genomes
- **Genome Quality**: Genome quality affects analysis accuracy
- **Database Coverage**: Database coverage affects classification
- **Memory Usage**: Large phage genomes require significant memory
- **Output Format**: Output format depends on configuration
- **Analysis Accuracy**: Accuracy depends on genome quality and database

## Examples

### Display help
**Args:** `sphae --help`
**Explanation:** Shows available options and usage information.

### Basic phage analysis
**Args:** `sphae -i phage_genome.fasta -o analysis_results.tsv`
**Explanation:** Analyze phage genome.

### With database
**Args:** `sphae -i phage_genome.fasta -d phage_db/ -o analysis_results.tsv`
**Explanation:** Use specific phage database.

### Multiple genomes
**Args:** `sphae -i phage1.fasta phage2.fasta -o analysis_results.tsv`
**Explanation:** Analyze multiple phage genomes.

### Genome annotation
**Args:** `sphae -i phage_genome.fasta -o annotation.gff --annotate`
**Explanation:** Annotate phage genome.

### Taxonomic classification
**Args:** `sphae -i phage_genome.fasta -o classification.tsv --classify`
**Explanation:** Classify phage taxonomically.

### Output detailed results
**Args:** `sphae -i phage_genome.fasta -o analysis_results.tsv --detailed`
**Explanation:** Output detailed analysis information.

### Output statistics
**Args:** `sphae -i phage_genome.fasta -o analysis_results.tsv --stats`
**Explanation:** Output analysis statistics.

### Generate report
**Args:** `sphae -i phage_genome.fasta -o analysis_results.tsv --report`
**Explanation:** Generate analysis report.

### With threads
**Args:** `sphae -i phage_genome.fasta -o analysis_results.tsv -p 8`
**Explanation:** Use multiple threads for analysis.