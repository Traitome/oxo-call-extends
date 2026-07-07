---
name: salty
category: taxonomy
description: Staphylococcus aureus lineage typing from whole-genome sequencing data
tags: ["salty", "Staphylococcus aureus", "MLST", "lineage", "typing"]
author: oxo-call-community
source_url: "https://github.com/LanLab/salty"
---

## Concepts

- **Tool Overview**: SaLTy (v1.0.6) is a bioinformatics tool for assigning lineages to Staphylococcus aureus whole-genome sequencing data, enabling large-scale genomic epidemiology studies.
- **Core Function**: Determines the lineage of S. aureus isolates using SNP-based classification and MLST typing.
- **Algorithm**: Uses a curated database of S. aureus lineages and SNP markers for rapid lineage assignment.
- **Input Format**: Whole-genome sequencing reads (FASTQ) or assembled contigs (FASTA).
- **Output Format**: Lineage assignment report, MLST type, SNP profiles, visualization data.
- **Use Case**: Clinical microbiology, outbreak investigation, population genetics, antimicrobial resistance studies.

## Pitfalls

- **Database updates**: Requires regular database updates for new lineages.
- **Read quality**: Poor quality reads may affect typing accuracy.
- **Coverage depth**: Requires sufficient sequencing coverage for reliable results.
- **Mixed infections**: May struggle with mixed S. aureus populations.
- **Closely related lineages**: May have difficulty distinguishing closely related lineages.
- **Contamination**: High levels of contamination may interfere with results.

## Examples

### Basic lineage typing
**Args:** `salty -i reads.fastq -o report.txt`
**Explanation:** `-i` input FASTQ file; `-o` output report.

### With assembly
**Args:** `salty -i assembly.fasta -o report.txt --assembly`
**Explanation:** `--assembly` indicates input is assembled contigs.

### Paired-end reads
**Args:** `salty -1 reads_1.fastq -2 reads_2.fastq -o report.txt`
**Explanation:** `-1/-2` paired-end read files.

### MLST typing only
**Args:** `salty -i reads.fastq -o report.txt --mlst-only`
**Explanation:** `--mlst-only` performs only MLST typing.

### Verbose output
**Args:** `salty -i reads.fastq -o report.txt -v`
**Explanation:** `-v` verbose output with detailed analysis.

### Specify database
**Args:** `salty -i reads.fastq -o report.txt -d /path/to/database`
**Explanation:** `-d` path to custom database.

### Output JSON
**Args:** `salty -i reads.fastq -o report.json --format json`
**Explanation:** `--format json` outputs results in JSON format.