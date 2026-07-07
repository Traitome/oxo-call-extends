---
name: hmftools-bam-tools
category: formatting
description: Rapidly process BAM files for various tasks including convert, count, coverage, filter, merge, sort, split, and statistics.
tags: [hmftools-bam-tools, formatting, BAM, SAM, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/blob/master/bam-tools/README.md"
---

## Concepts

- **Tool Overview**: hmftools-bam-tools (v1.6) is a Java-based BAM processing toolkit from Hartwig Medical Foundation that provides rapid processing capabilities for BAM files through subcommands like convert, count, coverage, filter, header, index, merge, random, resolve, revert, sort, split, and stats.
- **Subcommand Architecture**: Each subcommand handles a specific operation (convert, count, coverage, filter, header, index, merge, random, resolve, revert, sort, split, stats) invoked as `bamtools <subcommand> [options]`.
- **Input/Output Formats**: Supports BAM, SAM, FASTQ, FASTA, BED, JSON, Pileup, and YAML formats for conversion operations.
- **Java-based Implementation**: Requires Java 8+ (OpenJDK >=8,<=21), runs as single-threaded commands.
- **Integration with WiGiTS Pipeline**: Part of the Hartwig Medical Foundation's WiGiTS (Whole Genome Toolkit Suite) for cancer genomics analysis.

## Pitfalls

- **CRITICAL: Single-threaded Execution**: All bamtools commands are single-threaded; setting multi-threaded SLURM parameters (--ntasks-per-node > 1) wastes resources.
- **Output Format Mismatch**: The -format flag must match supported formats (bed|fasta|fastq|json|pileup|sam|yaml); incorrect format causes failure.
- **Index Requirement**: Some operations (like merge with sorted inputs) require BAM index (.bai) files to be present.
- **Memory Management**: Large BAM files may require increased memory allocation for Java heap space.
- **Version Compatibility**: Different versions (1.3-1.6) may have subtle differences in behavior; bioconda packages version 1.6-0 and 1.5-0 are available.

## Examples

### Convert BAM to FASTQ format
**Args:** `convert -format fastq -in input.bam -out output.fastq`
**Explanation:** Extracts read sequences and qualities from a BAM file and converts them to FASTQ format. Useful for re-processing aligned reads through other pipelines.

### Count alignments in BAM file
**Args:** `count -in input_alignments.bam`
**Explanation:** Outputs the total number of alignments in the BAM file. This is a quick way to get basic statistics on sequencing depth.

### Generate coverage statistics
**Args:** `coverage -in input.bam -out coverage.txt`
**Explanation:** Prints coverage statistics from the input BAM file, including per-position depth information for downstream analysis.

### Filter alignments by length
**Args:** `filter -in input.bam -out filtered.bam -length 100`
**Explanation:** Filters the BAM file to retain only alignments with length >= 100 base pairs. The -length flag specifies the minimum read length threshold.

### Merge multiple BAM files
**Args:** `merge -in sample1.bam -in sample2.bam -in sample3.bam -out merged.bam`
**Explanation:** Combines multiple BAM files into a single output file. All input BAMs should ideally be sorted consistently.

### Create BAM index
**Args:** `index -in input.bam`
**Explanation:** Generates a BAM index file (input.bam.bai) required for efficient random access to aligned reads.

### Sort BAM file
**Args:** `sort -in input.bam -out sorted.bam`
**Explanation:** Sorts the BAM file by chromosomal coordinates. Sorted BAM is required for many downstream tools like GATK and for efficient viewing in IGV.

### Split BAM by read name
**Args:** `split -in input.bam -prefix split_`
**Explanation:** Splits a BAM file into multiple output files based on user-specified properties (like read name), creating separate BAM files for each group.

### Generate BAM statistics
**Args:** `stats -in input.bam -out stats.txt`
**Explanation:** Prints comprehensive statistics from the input BAM file including alignment counts, mapping quality distribution, and flag statistics.

### Print BAM header
**Args:** `header -in input.bam -out header.txt`
**Explanation:** Extracts and prints the header information from a BAM file, which contains metadata about the sequencing run and reference genome.
