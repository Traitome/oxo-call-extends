---
name: agc
category: formatting
description: Assembled Genomes Compressor for efficient compression of collections of de novo assembled genomes
tags: [compression, genomes, assembly, storage, fasta]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/agc"
---

## Concepts

- **Tool Overview**: AGC is a high-performance compression tool designed specifically for collections of assembled genomes of the same species, achieving high compression ratios.
- **Core Function**: Compresses multiple genome assemblies efficiently by exploiting sequence similarity between genomes, with fast random access to individual sequences.
- **Input/Output**: Input: FASTA files (multiple genomes). Output: Compressed AGC archive. Decompression: FASTA files for selected genomes/contigs.
- **Use Cases**: Pangenome storage, multiple strain assemblies, population-scale genome collections, viral genome databases.
- **Installation**: Install via bioconda: `conda install -c bioconda agc`

## Pitfalls

- **Reference Required**: First genome added becomes the reference - choose a high-quality assembly as the first input.
- **Memory Usage**: Large genome collections require substantial memory during creation - use appropriate batch sizes.
- **K-mer Selection**: Default k=31 works for most cases; adjust for very short genomes (viruses) or highly divergent sequences.
- **Output Size**: Compression ratio depends on sequence similarity - highly divergent genomes compress less.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows all available commands and general options.

### Create compressed archive
**Args:** `create -o genomes.agc reference.fa sample1.fa sample2.fa`
**Explanation:** Creates AGC archive from multiple genome assemblies using reference.fa as the base.

### Create with custom k-mer
**Args:** `create -k 25 -o viral.agc virus_ref.fa virus1.fa virus2.fa`
**Explanation:** Uses k=25 for short viral genomes, better for capturing short matches.

### Add genomes to existing archive
**Args:** `append -o expanded.agc genomes.agc new_sample.fa`
**Explanation:** Appends new genome assembly to existing AGC archive.

### Extract all genomes
**Args:** `getcol -o output_dir/ genomes.agc`
**Explanation:** Decompresses all genomes from archive to output directory.

### Extract specific sample
**Args:** `getset genomes.agc sample1 > sample1.fa`
**Explanation:** Extracts a single genome sample from the archive.

### Extract contig region
**Args:** `getctg genomes.agc chr1:1000-5000 > region.fa`
**Explanation:** Extracts specific region from a contig, useful for quick sequence access.

### List samples in archive
**Args:** `listset genomes.agc`
**Explanation:** Lists all sample names contained in the archive.

### Show archive statistics
**Args:** `info genomes.agc`
**Explanation:** Displays compression statistics including size, number of samples, and compression ratio.

### Multi-threaded compression
**Args:** `create -t 16 -o genomes.agc ref.fa *.fa`
**Explanation:** Uses 16 threads for faster compression of large genome collections.
