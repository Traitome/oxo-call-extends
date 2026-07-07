---
name: aquila_umap
category: assembly
description: Umap generation tool for Aquila diploid genome assembly
tags: [aquila_umap, assembly, diploid-assembly, genome-assembly, Umap]
author: oxo-call-community
source_url: "https://github.com/maiziex/Aquila_Umap"
---

## Concepts

- **Tool Overview**: Aquila_Umap is a specialized tool for generating Umap (Unitig Overlap Map) data structures used in the Aquila diploid genome assembly pipeline. It processes sequencing reads to create an efficient representation for subsequent assembly steps.
- **Core Function**: Constructs unitig-based overlap maps from raw sequencing reads, enabling efficient graph-based assembly of diploid genomes.
- **Umap Data Structure**: A compact representation of read overlaps that facilitates haplotype-resolved assembly by maintaining phasing information.
- **Diploid Assembly Support**: Designed specifically for diploid genome assembly, preserving maternal and paternal allele information during the mapping process.
- **Input/Output**: Accepts FASTQ/FASTA reads as input; generates binary Umap files for use by Aquila assembler.
- **Installation**: `conda install -c bioconda aquila_umap` or build from source code on GitHub.

## Pitfalls

- **Read Quality**: Poor quality reads can lead to incorrect overlap detection. Consider preprocessing with quality filtering tools first.
- **Memory Requirements**: Generating Umap for large genomes requires significant memory. Monitor system resources during processing.
- **Input Format**: Supports FASTQ and FASTA formats. Compressed files (gzip) may require decompression first.
- **Paired-end Data**: Ensure proper read pairing when using paired-end sequencing data. Incorrect pairing affects overlap detection.
- **Output Directory**: Ensure output directory exists before running. Missing directories cause runtime errors.
- **Version Compatibility**: Umap format may change between versions. Use matching versions of Aquila_Umap and Aquila assembler.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options, including input/output parameters and advanced configuration settings.

### Basic Umap generation
**Args:** `-i reads.fastq -o umap_output`
**Explanation:** Generates Umap data structure from input FASTQ reads and writes output to umap_output directory. Creates binary index files for efficient access.

### Process paired-end reads
**Args:** `-1 reads_1.fastq -2 reads_2.fastq -o umap_output --pe`
**Explanation:** Processes paired-end sequencing data, treating read pairs as linked fragments. The `--pe` flag enables paired-end mode for improved overlap detection.

### Adjust k-mer size
**Args:** `-i reads.fastq -o umap_output -k 31`
**Explanation:** Sets k-mer size to 31 for overlap detection. Larger k-mers improve specificity but may reduce sensitivity for low-coverage regions.

### Enable verbose logging
**Args:** `-i reads.fastq -o umap_output -v --log umap.log`
**Explanation:** Runs with verbose output, logging detailed progress information and statistics to the specified log file. Useful for debugging and performance monitoring.

### Memory-efficient mode
**Args:** `-i reads.fastq -o umap_output --low_memory -t 4`
**Explanation:** Enables memory-efficient processing mode and limits thread usage to 4. Useful for systems with limited RAM or when running multiple processes simultaneously.