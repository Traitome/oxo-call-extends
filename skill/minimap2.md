---
name: minimap2
category: alignment
description: A versatile pairwise aligner for genomic and spliced nucleotide sequences.
tags: [minimap2, alignment, long-reads, sequencing, mapping]
author: oxo-call-community
source_url: "https://github.com/lh3/minimap2"
---

## Concepts

- **Tool Overview**: minimap2 (v2.30+) is a fast and versatile pairwise sequence aligner designed for mapping long reads (PacBio/ONT), short reads, and spliced sequences (RNA-seq) to reference genomes.
- **Core Function**: Aligns sequencing reads to reference sequences using a seed-and-chain approach with minimizer-based indexing for fast mapping.
- **Input/Output**: Input: FASTA/FASTQ reads, FASTA reference genome. Output: SAM/BAM/PAF alignment files.
- **Algorithm**: Uses minimizer sampling to find potential seed matches, then extends these into longer alignments using dynamic programming.
- **Key Features**: Supports long reads, short reads, spliced alignment (RNA-seq), structural variant detection, and multiple mapping modes.
- **Installation**: `conda install -c bioconda minimap2`

## Pitfalls

- **Preset Selection**: Choose the correct preset (-ax) for your data type (map-ont, map-hifi, sr, splice, etc.). Using the wrong preset can significantly reduce mapping accuracy.
- **Memory Usage**: Indexing large genomes requires significant memory. Consider using `-d` option to build index separately for very large genomes.
- **Output Format**: Default output is SAM. Use `-o` to specify output file and `-b` to output BAM directly.
- **Secondary Alignments**: By default, minimap2 reports multiple alignments per read. Use `-N 1` to report only the primary alignment.
- **Quality Values**: minimap2 ignores base quality values by default. Use `-k15` or adjust k-mer size for better sensitivity with noisy data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Map Oxford Nanopore reads
**Args:** `-ax map-ont reference.fa reads.fq > alignment.sam`
**Explanation:** Maps Oxford Nanopore reads to reference genome using the map-ont preset optimized for noisy long reads.

### Map PacBio HiFi reads
**Args:** `-ax map-hifi reference.fa reads.fq > alignment.sam`
**Explanation:** Maps PacBio HiFi reads using preset optimized for high-quality long reads.

### Map short paired-end reads
**Args:** `-ax sr reference.fa R1.fq R2.fq > alignment.sam`
**Explanation:** Maps short paired-end Illumina reads to reference genome.

### RNA-seq spliced alignment
**Args:** `-ax splice reference.fa reads.fq > alignment.sam`
**Explanation:** Performs spliced alignment for RNA-seq reads, detecting exon-intron boundaries.

### Generate PAF output format
**Args:** `-x map-ont reference.fa reads.fq -o alignment.paf`
**Explanation:** Outputs alignments in PAF (Pairwise mApping Format), a compact human-readable format.

### Build index for large genome
**Args:** `-d reference.mmi reference.fa`
**Explanation:** Builds a minimap2 index file (reference.mmi) for faster mapping of multiple read sets.

### Map using pre-built index
**Args:** `-ax map-ont reference.mmi reads.fq > alignment.sam`
**Explanation:** Maps reads using a pre-built index file for improved performance.

### Output sorted BAM directly
**Args:** `-ax map-ont reference.fa reads.fq | samtools sort -o alignment.bam`
**Explanation:** Maps reads and pipes output to samtools sort for sorted BAM output.