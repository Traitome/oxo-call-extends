---
name: myloasm
category: assembly
description: Myloasm - High-resolution metagenome assembly for long reads
tags: [myloasm, assembly, metagenome, long-reads, nanopore, pacbio, hifi]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/myloasm"
---

## Concepts

- **Tool Overview**: Myloasm v0.5.1 is a high-resolution metagenome assembler designed specifically for modern long-read sequencing data (PacBio HiFi and Oxford Nanopore R10.4). It enables strain-level genome recovery from complex microbial communities.
- **Core Function**: Constructs high-resolution assembly graphs using polymorphic k-mers (SNPmers) to distinguish between highly similar genomes in metagenomes. Leverages differential abundance for graph simplification to resolve complex metagenome structures.
- **Algorithm**: Uses innovative "polymorphic k-mer" approach where SNPmers (k-mers with polymorphic middle bases) capture sequence variations within mixed populations. The string graph construction tolerates sequencing errors while preserving real polymorphisms.
- **Input Format**: Accepts raw long-read FASTQ files from PacBio HiFi or Oxford Nanopore (preferably R10.4 chemistry). Supports gzipped input for storage efficiency.
- **Output**: Produces assembled contigs in FASTA format, with improved recovery of complete circular genomes and strain-level variants. Can resolve genomes with >98% similarity.
- **Performance**: On real ONT data, assembles 3x more complete circular contigs than other assemblers. Makes ONT and HiFi achieve comparable assembly quality.
- **Use Case**: Human gut microbiome studies, environmental metagenomics, strain-level pathogen detection, and recovering complete genomes from complex microbial communities.

## Pitfalls

- **Read Quality**: Designed for modern long reads with accuracy >99% (HiFi) or R10.4 nanopore. Older high-error long reads may give poor results.
- **Computational Resources**: Assembly is memory-intensive for large metagenomes. Ensure adequate RAM for complex samples.
- **K-mer Parameter**: Default k-mer size works for most cases but may need adjustment for very complex or simple communities.
- **Coverage Requirements**: Low coverage genomes may not be assembled completely. Minimum depth recommendations depend on community complexity.
- **Similarity Resolution**: While able to resolve genomes with >98% similarity, very close strains (>99% identical) may still co-assemble.
- **Input Format**: Currently optimized for specific long-read formats. Illumina short reads are not directly supported.

## Examples

### Basic metagenome assembly
**Args:** `-i reads.fastq.gz -o assembly.fasta`
**Explanation:** Standard myloasm assembly workflow. Takes long reads and outputs assembled contigs.

### Specify k-mer size
**Args:** `-i nanopore_reads.fastq.gz -o assembly.fasta -k 31`
**Explanation:** Sets k-mer size to 31 for the assembly algorithm. Adjust based on read length and community complexity.

### Enable verbose logging
**Args:** `-i reads.fastq.gz -o assembly.fasta -v`
**Explanation:** Runs assembly with verbose output, showing progress and intermediate statistics.

### Set minimum read length filter
**Args:** `-i raw_reads.fastq.gz -o assembly.fasta -min_len 1000`
**Explanation:** Filters input reads to minimum 1000bp before assembly, removing short reads that may impact graph complexity.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options including advanced parameters for fine-tuning assembly.
