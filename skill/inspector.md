---
name: inspector
category: assembly
description: Accurate long-read de novo assembly evaluation tool that detects structural and small-scale errors, and can correct assembly errors based on consensus sequences.
tags: [inspector, assembly, evaluation, long-read, PacBio, Nanopore]
author: oxo-call-community
source_url: "https://github.com/ChongLab/Inspector"
---

## Concepts

- **Assembly Evaluation**: Inspector evaluates long-read de novo assemblies by mapping raw reads back to the assembly and identifying discrepancies.
- **Error Detection**: Identifies both structural errors (misassemblies, inversions, translocations) and small-scale errors (SNPs, indels).
- **Error Correction**: Can correct assembly errors using consensus sequences derived from raw reads covering erroneous regions.
- **Reference-free**: Operates without requiring a reference genome, making it suitable for novel genome assemblies.
- **Multi-platform Support**: Works with PacBio CLR, PacBio HiFi, Oxford Nanopore, and mixed sequencing platform data.

## Pitfalls

- **Read Quality**: Requires high-quality long reads for accurate error detection; poor quality reads may produce false positives.
- **Assembly Size**: Memory usage increases with assembly size; large genomes may require additional resources.
- **Computation Time**: Comprehensive evaluation can be time-consuming for large datasets.
- **Error Thresholds**: Default parameters may need adjustment based on specific sequencing platform characteristics.
- **Output Interpretation**: Detailed analysis requires understanding of assembly metrics and error types.

## Examples

### Basic assembly evaluation
**Args:** `inspector -c assembly.fasta -r reads.fastq -o inspector_output`
**Explanation:** Evaluates the assembly using raw long reads and generates detailed error reports.

### Evaluate with multiple read files
**Args:** `inspector -c assembly.fasta -r reads1.fastq reads2.fastq -o multi_read_output`
**Explanation:** Uses multiple read files for more comprehensive assembly evaluation.

### Enable error correction
**Args:** `inspector -c assembly.fasta -r reads.fastq -o corrected_assembly --correct`
**Explanation:** Detects and corrects assembly errors based on read consensus.

### Evaluate with reference genome
**Args:** `inspector -c assembly.fasta -r reads.fastq -ref reference.fasta -o ref_based_output`
**Explanation:** Uses a reference genome to enhance error detection and validation.

### Specify sequencing platform
**Args:** `inspector -c assembly.fasta -r reads.fastq -o nanopore_eval --platform nanopore`
**Explanation:** Optimizes evaluation parameters for Oxford Nanopore data.

### Generate visualization
**Args:** `inspector -c assembly.fasta -r reads.fastq -o vis_output --visualize`
**Explanation:** Generates visualizations of assembly errors and read alignments.