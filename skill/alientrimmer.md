---
name: alientrimmer
category: qc
description: Tool for trimming contaminant oligonucleotide sequences like primers and adapters from sequencing reads
tags: [trimming, adapter, primer, fastq, contamination]
author: oxo-call-community
source_url: "https://gitlab.pasteur.fr/GIPhy/AlienTrimmer"
---

## Concepts

- **Tool Overview**: AlienTrimmer detects and trims contaminant oligonucleotide sequences (primers, adapters) from both ends of high-throughput sequencing reads.
- **Core Function**: Accurately removes known contaminant sequences from FASTQ files, improving downstream analysis quality.
- **Input/Output**: Input: FASTQ files and contaminant sequence file. Output: Trimmed FASTQ files and trimming statistics.
- **High Accuracy**: Uses sensitive alignment to detect contaminants even with mismatches and partial matches.
- **Installation**: Install via bioconda: `conda install -c bioconda alientrimmer`

## Pitfalls

- **Contaminant File**: Must provide file with known contaminant sequences - include all primers, adapters, and barcodes.
- **Partial Matches**: AlienTrimmer can detect partial contaminants at read ends - set appropriate parameters.
- **Quality Scores**: Trimming preserves quality scores but may affect downstream quality-based filtering.
- **Paired-End**: For paired-end data, run separately on each file or use paired mode if available.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows all available options and parameters for AlienTrimmer.

### Basic trimming with contaminant file
**Args:** `-i reads.fastq -a contaminants.fasta -o trimmed.fastq`
**Explanation:** Trims contaminant sequences from reads using provided contaminant FASTA file.

### Trim paired-end reads
**Args:** `-i R1.fastq -j R2.fastq -a adapters.fa -o R1_trimmed.fastq -p R2_trimmed.fastq`
**Explanation:** Trims adapters from both paired-end read files simultaneously.

### Set minimum overlap
**Args:** `-i reads.fastq -a adapters.fa -o trimmed.fastq -c 10`
**Explanation:** Requires minimum 10bp overlap between read and contaminant for trimming.

### Allow mismatches
**Args:** `-i reads.fastq -a adapters.fa -o trimmed.fastq -e 0.1`
**Explanation:** Allows up to 10% mismatch rate when detecting contaminants.

### Keep untrimmed reads
**Args:** `-i reads.fastq -a adapters.fa -o trimmed.fastq -u untrimmed.fastq`
**Explanation:** Saves reads without detected contaminants to separate file.

### Generate trimming statistics
**Args:** `-i reads.fastq -a adapters.fa -o trimmed.fastq -s stats.txt`
**Explanation:** Outputs detailed statistics about trimming efficiency and contaminant detection.

### Set quality threshold
**Args:** `-i reads.fastq -a adapters.fa -o trimmed.fastq -q 20`
**Explanation:** Only trims contaminants from reads with average quality ≥Q20.

### Preserve read order
**Args:** `-i reads.fastq -a adapters.fa -o trimmed.fastq --keep-order`
**Explanation:** Maintains original read order in output file for paired-end compatibility.
