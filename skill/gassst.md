---
name: gassst
category: sequence
description: GASSST is a high-performance DNA sequence aligner supporting gapped alignments with no restrictions on indel number.
tags: [gassst, alignment, sequence-alignment, ngs, fastq, genomics]
author: oxo-call-community
source_url: "https://www.irisa.fr/symbiose/projects/gassst/"
---

## Concepts

- **Tool Overview**: GASSST (Global Alignment Short Sequence Search Tool) is a fast DNA sequence aligner designed for efficient gapped alignment of next-generation sequencing data.
- **Core Function**: Performs sensitive local alignment of short reads against reference sequences with full support for insertions and deletions (indels).
- **Algorithm**: Uses a tiled dynamic programming approach with pre-computed lookup tables to accelerate seed-based alignment filtering. The method approximates full dynamic programming while discarding most false-positive alignments early.
- **Sensitivity**: Achieves high sensitivity across a wide range of configurations, outperforming BWA, BFAST, SSAHA2, and PASS in benchmarking.
- **Speed**: Faster overall execution time than other state-of-the-art aligners due to efficient multi-stage filtering.
- **Indel Support**: Unlike BWA-backtrack, GASSST places no restrictions on the number or length of indels in alignments.
- **Input Format**: Accepts FASTQ/FASTA read files and reference sequences in FASTA format.
- **Output Format**: Outputs alignments in SAM format for compatibility with downstream tools.
- **License**: Distributed under CeCILL free software license.

## Pitfalls

- **Reference Indexing**: First run requires building a reference index which can be time-consuming for large genomes. Index is reusable for subsequent runs.
- **Memory Usage**: Index and alignment algorithms require substantial RAM, especially for mammalian-sized genomes. 8GB+ recommended.
- **Paired-End Reads**: GASSST handles paired-end data but requires proper mate information in FASTQ read names.
- **Quality Scores**: Alignment quality scores depend on proper base quality encoding. Ensure Phred+33 or Phred+64 is correctly specified.
- **Seed Length**: Default seed parameters may need optimization for specific read lengths. Short seeds increase sensitivity but slow computation.
- **Output Sorting**: SAM output may need post-processing with samtools sort for tools requiring coordinate-sorted alignments.
- **Error Rate**: Higher error rates in reads (e.g., from long-read sequencing) may cause alignment failures if threshold not adjusted.

## Examples

### Build reference index
**Args:** `gassst -i reference.fasta -o reference_index`
**Explanation:** Creates indexed reference sequence for efficient subsequent alignments.

### Align single-end reads
**Args:** `gassst -i reference_index -q reads.fastq -o alignments.sam`
**Explanation:** Aligns single-end sequencing reads to reference and outputs SAM format alignments.

### Align paired-end reads
**Args:** `gassst -i reference_index -1 left.fastq -2 right.fastq -o paired_alignments.sam`
**Explanation:** Aligns paired-end read pairs and outputs SAM with proper mate information.

### Specify error threshold
**Args:** `gassst -i reference_index -q reads.fastq -e 0.05 -o alignments.sam`
**Explanation:** Sets maximum allowed error rate to 5% for filtered alignments.

### Convert to sorted BAM
**Args:** `gassst -i ref -q reads.fq -o aln.sam && samtools sort aln.sam -o aln.sorted.bam`
**Explanation:** Complete workflow from alignment to coordinate-sorted BAM file.

### Show help
**Args:** `gassst -h`
**Explanation:** Displays full list of command-line options and parameter descriptions.
