---
name: amused
category: utility
description: Auditing Motifs Using Statistical Enrichment & Depletion
tags: [amused, motif, enrichment, depletion, statistics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Carldeboer/AMUSED"
---

## Concepts

- **Tool Overview**: AMUSED (Auditing Motifs Using Statistical Enrichment & Depletion) is a bioinformatics tool for analyzing sequence motifs to identify statistically significant enrichment or depletion patterns.
- **Core Function**: Identifies over-represented (enriched) and under-represented (depleted) sequence motifs within a set of sequences compared to a background or control set.
- **Statistical Methods**: Uses rigorous statistical tests to determine motif enrichment and depletion, similar to tools like AME (Analysis of Motif Enrichment).
- **Input/Output**: Inputs: Sequence files (FASTA format), motif databases; Outputs: Statistical reports with enrichment scores and significance values.
- **Installation**: Available via Bioconda (`conda install -c bioconda amused`). Requires Ruby (>=2.4), jemalloc, ruby-dna-tools, and zlib.
- **Key Features**: Motif auditing, statistical significance testing, enrichment/depletion analysis, support for custom motif databases.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format (FASTA for sequences, appropriate format for motif databases).
- **Ruby Dependencies**: Requires Ruby runtime environment and ruby-dna-tools gem.
- **Database Compatibility**: Motif databases must be in a format compatible with AMUSED.
- **Statistical Assumptions**: Results depend on proper selection of background/control sequences.
- **Memory Usage**: May require significant memory for large sequence datasets.

## Examples

### Display help
**Args:** `amused --help`
**Explanation:** Shows available options and usage information.

### Basic motif enrichment analysis
**Args:** `amused -i input_sequences.fasta -b background_sequences.fasta -m motifs.txt -o results.txt`
**Explanation:** Analyzes motif enrichment in input sequences compared to background sequences using motifs from the provided motif file.

### Motif depletion analysis
**Args:** `amused -i target_sequences.fasta -b control_sequences.fasta -m motif_database.meme -o depletion_results.txt --depletion`
**Explanation:** Focuses on identifying depleted motifs (under-represented) in target sequences compared to control sequences.

### Custom significance threshold
**Args:** `amused -i peaks.fasta -b genome.fasta -m jaspar_motifs.txt -o results.txt --pvalue 0.01`
**Explanation:** Sets custom p-value threshold of 0.01 for determining significant motif enrichment.

### Output detailed statistics
**Args:** `amused -i sequences.fasta -b background.fasta -m motifs.txt -o detailed_results.txt --verbose`
**Explanation:** Generates verbose output with detailed statistical information for each motif.

### Batch mode processing
**Args:** `amused -i batch_input/ -b background.fasta -m motifs.txt -o batch_output/`
**Explanation:** Processes multiple sequence files in batch mode from the input directory.