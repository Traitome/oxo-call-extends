---
name: satrap
category: assembly
description: SOLiD assembly translation program for color-space reads
tags: ["satrap", "assembly", "SOLiD", "color-space"]
author: oxo-call-community
source_url: "http://satrap.cribi.unipd.it/cgi-bin/satrap.pl"
---

## Concepts

- **Tool Overview**: Satrap (v0.2) is a SOLiD assembly translation program that converts color-space reads to nucleotide-space assemblies.
- **Core Function**: Translates SOLiD sequencing reads from color-space to nucleotide-space for downstream analysis.
- **Algorithm**: Uses color-space decoding algorithms to convert color calls (0-3) to nucleotide bases (A/C/G/T).
- **Input/Output**: Accepts color-space reads and produces standard nucleotide assemblies.
- **SOLiD Specific**: Designed specifically for Applied Biosystems SOLiD sequencing platform data.
- **Applications**: Preprocessing for SOLiD data, enabling compatibility with standard bioinformatics tools.

## Pitfalls

- **Platform Specific**: Only designed for SOLiD sequencing data.
- **Color-Space Artifacts**: May introduce errors during color-space to nucleotide conversion.
- **Read Quality**: Results depend on input read quality and color-space accuracy.
- **Deprecated Technology**: SOLiD platform is largely discontinued; tool may have limited utility.
- **Documentation**: Limited documentation available for newer users.
- **Performance**: May be slower than modern alternatives for data processing.

## Examples

### Basic translation
**Args:** `satrap -i color_space.fastq -o nucleotide.fastq`
**Explanation:** `-i` input color-space FASTQ; `-o` output nucleotide FASTQ.

### With quality filtering
**Args:** `satrap -i color_space.fastq -q 20 -o filtered.fastq`
**Explanation:** `-q 20` filters reads with quality below 20.

### Convert to FASTA
**Args:** `satrap -i color_space.fastq -f fasta -o output.fasta`
**Explanation:** `-f fasta` outputs in FASTA format.

### Batch processing
**Args:** `satrap -i ./color_space/ -o ./nucleotide/ -b`
**Explanation:** `-b` batch mode for processing multiple files.

### Verbose logging
**Args:** `satrap -i color_space.fastq -o output.fastq -v`
**Explanation:** `-v` enables verbose output for debugging.

### Quality report
**Args:** `satrap -i color_space.fastq --qc -o qc_report.txt`
**Explanation:** `--qc` generates quality control report.

### Custom color-space table
**Args:** `satrap -i color_space.fastq -c custom_table.txt -o output.fastq`
**Explanation:** `-c` specifies custom color-space to nucleotide mapping table.