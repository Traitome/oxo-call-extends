---
name: burst
category: metagenomics
description: High-speed pairwise sequence aligner for NGS short reads against large reference databases
tags: [burst, alignment, metagenomics, 16s, database-search]
author: oxo-call-community
source_url: "https://github.com/knights-lab/BURST"
---

## Concepts

- **Tool Overview**: BURST is an optimal, high-speed pairwise sequence aligner for NGS reads against large databases.
- **Core Function**: Aligns short reads to reference sequences with optimal accuracy and speed.
- **Application**: 16S rRNA amplicon classification and metagenomics profiling.
- **Input**: FASTA/FASTQ reads and indexed reference database.
- **Output**: Alignment results and taxonomic classifications.
- **Installation**: Install via bioconda: `conda install -c bioconda burst`

## Pitfalls

- **Database Required**: Must build or download reference database before searching.
- **Memory Usage**: Large databases require significant memory.
- **Identity Threshold**: Set appropriate identity threshold for classification level.
- **Thread Count**: Use multiple threads for large datasets.

## Examples

### Build database
**Args:** `burst16s -db references.fa -o references.edb`
**Explanation:** Builds BURST database from reference sequences.

### Classify amplicon reads
**Args:** `burst16s -q reads.fa -db references.edb -o classified.tsv`
**Explanation:** Classifies 16S amplicon reads against reference database.

### Set identity threshold
**Args:** `burst16s -q reads.fa -db references.edb --id 0.99 -o classified.tsv`
**Explanation:** Uses 99% identity threshold for species-level classification.

### Multi-threaded search
**Args:** `burst16s -q reads.fa -db references.edb -t 8 -o classified.tsv`
**Explanation:** Uses 8 threads for parallel classification.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
