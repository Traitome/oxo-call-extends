---
name: badread
category: utility
description: Badread - Long read simulator that can imitate many types of read problems
tags: [read-simulation, long-reads, nanopore, error-modeling]
author: oxo-call-community
source_url: "https://github.com/rrwick/Badread"
---

## Concepts

- **Tool Overview**: Badread simulates error-prone long reads (Oxford Nanopore, PacBio) with realistic error profiles, chimeric reads, and other artifacts for benchmarking and testing.

- **Error Modeling**: Generates reads with realistic error patterns including insertions, deletions, and substitutions matching real long-read data.

- **Chimeric Reads**: Can simulate chimeric reads where two unrelated sequences are joined, a common artifact in long-read data.

- **Read Length Distribution**: Supports custom read length distributions to match specific sequencing runs.

- **Quality Scores**: Generates realistic quality scores that correlate with actual error probabilities.

- **Junk Reads**: Can simulate junk reads (random sequences) that appear in real sequencing data.

## Pitfalls

- **Reference Required**: Needs a reference genome to simulate reads from. Cannot generate random sequences alone.

- **Error Profile**: Default error profiles may not match all sequencing chemistries. Adjust parameters for specific runs.

- **Output Size**: Simulated datasets can be very large. Monitor disk space during generation.

- **Not for Short Reads**: Designed for long-read simulation. Use other tools (e.g., ART) for short-read simulation.

## Examples

### Basic Nanopore simulation
**Args:** `badread --reference genome.fasta --quantity 50x --genome_size 5m --error_model nanopore --output reads.fastq`
**Explanation:** Simulates 50x coverage of Nanopore-like reads from reference genome.

### Custom read length
**Args:** `badread --reference genome.fasta --quantity 30x --genome_size 5m --error_model nanopore --read_length 15000,8000 --output reads.fastq`
**Explanation:** Simulates reads with mean length 15kb and standard deviation 8kb.

### Include chimeric reads
**Args:** `badread --reference genome.fasta --quantity 50x --genome_size 5m --error_model nanopore --chimeras 0.05 --output reads.fastq`
**Explanation:** Simulates 5% chimeric reads in addition to normal reads.

### Include junk reads
**Args:** `badread --reference genome.fasta --quantity 50x --genome_size 5m --error_model nanopore --junk_reads 0.02 --output reads.fastq`
**Explanation:** Simulates 2% junk reads (random sequences) mixed with normal reads.

### PacBio HiFi simulation
**Args:** `badread --reference genome.fasta --quantity 30x --genome_size 5m --error_model pacbio-hifi --read_length 15000,5000 --output reads.fastq`
**Explanation:** Simulates PacBio HiFi-like reads with higher accuracy and longer lengths.

### Custom error model
**Args:** `badread --reference genome.fasta --quantity 50x --genome_size 5m --error_model custom_model.tsv --output reads.fastq`
**Explanation:** Uses custom error model from TSV file for specific error profile simulation.
