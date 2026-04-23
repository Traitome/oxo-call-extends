---
name: centrifuge
category: metagenomics
description: Metagenomic sequence classifier using Burrows-Wheeler transform
tags: [centrifuge, metagenomics, classification, taxonomy, microbiome]
author: oxo-call-community
source_url: "https://github.com/DaehwanKimLab/centrifuge"
---

## Concepts

- **Tool Overview**: Centrifuge is a novel microbial classification engine that enables rapid, accurate, and sensitive labeling of reads and quantification of species in metagenomic samples. Uses a compressed FM-index for efficient memory usage.
- **Core Function**: Classifies metagenomic sequencing reads against a database of microbial genomes and assigns taxonomic labels with confidence scores.
- **Input/Output**: Input: FASTQ/FASTA files (paired or single-end). Output: Classification results (TAB or SAM format) and taxonomic reports.
- **Index-Based**: Requires pre-built index files (.cf files). Use `centrifuge-build` to create custom indexes or download pre-built indexes.
- **Threading**: Supports multi-threading with `-p/--threads` for parallel classification.
- **Memory Efficient**: Uses memory-mapped I/O (`--mm`) to share index across multiple instances.

## Pitfalls

- **Index Required**: Must have index files before classification. Download pre-built indexes or build from reference sequences.
- **Database Size**: Large databases (e.g., nt database) require significant memory. Use `--mm` for memory sharing.
- **Output Format**: Default is TAB format. Use `--out-fmt sam` for SAM output if needed for downstream tools.
- **Partial Hits**: Minimum hit length is 22 by default. Adjust `--min-hitlen` for shorter reads.
- **Multiple Assignments**: Use `-k` to control how many assignments are reported per read.

## Examples

### Classify paired-end reads
**Args:** `-x /path/to/index -1 reads_R1.fq -2 reads_R2.fq -S results.tsv --report-file report.tsv`
**Explanation:** Classifies paired-end reads against the specified index, outputs classification results to results.tsv and taxonomic report to report.tsv.

### Classify single-end reads with multiple threads
**Args:** `-x /path/to/index -U reads.fq -S results.tsv -p 8`
**Explanation:** Uses 8 threads to classify single-end reads, improving speed for large datasets.

### Output in SAM format
**Args:** `-x /path/to/index -1 R1.fq -2 R2.fq --out-fmt sam -S output.sam`
**Explanation:** Generates SAM format output for compatibility with downstream tools that expect SAM format.

### Build custom index from FASTA
**Args:** `centrifuge-build --conversion-table conv.txt --taxonomy-tree tree.txt genomes.fasta custom_index`
**Explanation:** Creates a custom centrifuge index from reference genomes with taxonomy information.

### Generate Kraken-style report
**Args:** `centrifuge-kreport -x /path/to/index results.tsv > kraken_report.txt`
**Explanation:** Converts centrifuge output to Kraken-style report for compatibility with Kraken tools.

### Inspect index contents
**Args:** `centrifuge-inspect -s /path/to/index`
**Explanation:** Prints summary of the index including reference names, lengths, and index properties.

### Classify with host filtering
**Args:** `-x /path/to/index -1 R1.fq -2 R2.fq --host-taxids 9606 -S results.tsv`
**Explanation:** Prefers human (taxid 9606) classification for host filtering in microbiome studies.

### Skip specific taxa
**Args:** `-x /path/to/index -U reads.fq --exclude-taxids 9606,10116 -S results.tsv`
**Explanation:** Excludes human (9606) and rat (10116) from classification to focus on microbial reads.

### Classify with minimum hit length
**Args:** `-x /path/to/index -1 R1.fq -2 R2.fq --min-hitlen 30 -S results.tsv`
**Explanation:** Requires minimum 30bp alignment for more stringent classification.
