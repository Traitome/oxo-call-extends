---
name: salmid
category: taxonomy
description: Rapid taxonomic identification tool for Salmonella and related species
tags: ["salmid", "Salmonella", "taxonomy", "identification", "MLST"]
author: oxo-call-community
source_url: "https://github.com/hcdenbakker/SalmID"
---

## Concepts

- **Tool Overview**: SalmID (v0.1.23) is a rapid tool for taxonomic identification of Salmonella species and subspecies from sequencing data, also detecting common contaminants.
- **Core Function**: Identifies Salmonella serovars and detects contaminants (Listeria, Escherichia) from raw sequencing reads or assemblies.
- **Algorithm**: Uses k-mer based matching against a curated database of Salmonella genomes and common contaminants.
- **Input Format**: Raw sequencing reads (FASTQ), assembled contigs (FASTA), or pre-computed k-mer profiles.
- **Output Format**: Taxonomic identification report, confidence scores, contamination detection, MLST typing.
- **Use Case**: Clinical microbiology, food safety testing, outbreak investigation, environmental monitoring.

## Pitfalls

- **Database updates**: Requires regular database updates for new serovars.
- **Read quality**: Poor quality reads may affect identification accuracy.
- **Mixed samples**: May struggle with mixed bacterial populations.
- **Coverage depth**: Requires sufficient sequencing coverage for reliable identification.
- **Closely related species**: May have difficulty distinguishing closely related serovars.
- **Contamination**: High levels of contamination may interfere with results.

## Examples

### Basic identification
**Args:** `salmid -i reads.fastq -o report.txt`
**Explanation:** `-i` input FASTQ file; `-o` output report.

### With assembly
**Args:** `salmid -i assembly.fasta -o report.txt --assembly`
**Explanation:** `--assembly` indicates input is assembled contigs.

### Paired-end reads
**Args:** `salmid -1 reads_1.fastq -2 reads_2.fastq -o report.txt`
**Explanation:** `-1/-2` paired-end read files.

### MLST typing
**Args:** `salmid -i reads.fastq -o report.txt --mlst`
**Explanation:** `--mlst` enables multilocus sequence typing.

### Verbose output
**Args:** `salmid -i reads.fastq -o report.txt -v`
**Explanation:** `-v` verbose output with detailed analysis.

### Specify database
**Args:** `salmid -i reads.fastq -o report.txt -d /path/to/database`
**Explanation:** `-d` path to custom database.

### Threshold adjustment
**Args:** `salmid -i reads.fastq -o report.txt -t 0.8`
**Explanation:** `-t` confidence threshold (default: 0.7).