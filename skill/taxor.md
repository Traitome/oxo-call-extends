---
name: taxor
category: metagenomics
description: Fast and space-efficient taxonomic classification of long reads using hierarchical interleaved XOR filters (HIXF).
tags: [taxor, metagenomics, long-reads, taxonomic-classification, nanopore, pacbio, hixf]
author: oxo-call-community
source_url: "https://github.com/JensUweUlrich/Taxor"
---

## Concepts

- **Tool Overview**: taxor (v0.2.1) - A taxonomic classification tool for long-read metagenomics using hierarchical interleaved XOR filters (HIXF). Provides fast, memory-efficient classification of nanopore or PacBio reads against large reference databases.
- **Core Functions**: Three main commands: `taxor-build` (create HIXF index from reference genomes), `taxor-search` (classify reads against index), `taxor-profile` (generate abundance profiles from search results).
- **Index Technology**: Uses HIXF (Hierarchical Interleaved XOR Filter) data structure for k-mer storage, reducing memory requirements by >50% compared to other methods while maintaining precision.
- **K-mer Strategy**: Supports both raw k-mers and syncmers (minimizer-based selection) for pseudoalignment. Syncmers provide better specificity with smaller index sizes.
- **Installation**: `conda install -c bioconda taxor` or `pixi global install taxor` or build from source with CMake and GCC.
- **Pre-built Databases**: Provides downloadable index files for Viruses (GenBank), Bacteria/Archaea (GTDB), and combined RefSeq databases.

## Pitfalls

- **Index Building Time**: Building HIXF index from large reference sets (like GTDB bacteria) is computationally intensive and can take hours for comprehensive databases.
- **Database Size**: While memory-efficient, pre-built databases are still large (71GB for GTDB). Ensure adequate disk space before downloading.
- **K-mer Size Trade-offs**: Smaller k-mers (like k=22) increase sensitivity but also false positive rate. Larger k-mers (k=30) are more specific but may miss short reads.
- **Syncmer Parameter**: The `--syncmer-size` must be smaller than `--kmer-size`. Typical values are k=22, s=12 for long reads.
- **Input Format**: Requires tab-separated file listing reference sequences with taxonomy IDs during index build - not just raw FASTA directories.
- **Threading Limits**: Maximum 32 threads supported, though diminishing returns may occur for I/O-bound operations.

## Examples

### Build index from reference genomes
**Args:** `taxor-build --input-file refs.tsv --input-sequence-dir ./ref_seqs/ --output-filename refdb.hixf --kmer-size 22 --threads 16`
**Explanation:** Build HIXF index from reference sequences. The input TSV should have columns for assembly accession and taxonomy ID.

### Search reads against database
**Args:** `taxor-search --index refdb.hixf --reads sample.fastq.gz --output results.tsv --threads 16`
**Explanation:** Classify long reads from FASTQ file against pre-built HIXF index. Output contains read assignments and taxonomic information.

### Generate taxonomic profile
**Args:** `taxor-profile --search-results results.tsv --output profile.tsv --method em`
**Explanation:** Convert search results into abundance profile. EM (expectation-maximization) method handles multi-matching reads better than simple binning.

### Build index with syncmers
**Args:** `taxor-build --input-file refs.tsv --output-filename refdb.hixf --kmer-size 22 --syncmer-size 12 --use-syncmer --threads 16`
**Explanation:** Use syncmers instead of raw k-mers for smaller index size. Recommended for very large reference databases.

### Search with verbose output
**Args:** `taxor-search --index refdb.hixf --reads sample.fastq.gz --output results.tsv --verbose`
**Explanation:** Enable verbose logging to see processing progress, read counts, and classification statistics during search.

### Search with filtering
**Args:** `taxor-search --index refdb.hixf --reads sample.fastq.gz --output results.tsv --min-score 0.9 --threads 16`
**Explanation:** Apply minimum score threshold to filter low-confidence classifications. Higher values increase precision but may reduce recall.

### Profile with genome size correction
**Args:** `taxor-profile --search-results results.tsv --output profile.tsv --genome-size-correction`
**Explanation:** Account for varying genome sizes when calculating abundances. Essential for accurate microbial load estimation.

### Use pre-built viral database
**Args:** `taxor-search --index genbank-viral-k22-s12.hixf --reads viral_reads.fastq.gz --output results.tsv`
**Explanation:** Downloaded pre-built index for viral genomes. Useful for pathogen detection in clinical samples.

### Multi-sample batch processing
**Args:** `for sample in sample1 sample2 sample3; do taxor-search --index refdb.hixf --reads ${sample}.fastq.gz --output ${sample}_results.tsv; done`
**Explanation:** Process multiple samples in parallel using shell loop. Each sample classified independently against same index.
