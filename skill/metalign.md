---
name: metalign
category: alignment
description: "Metalign: efficient alignment-based metagenomic profiling via containment min hash"
tags: [metalign, alignment, metagenomics, profiling]
author: oxo-call-community
source_url: "https://github.com/nlapier2/Metalign"
---
## Concepts

- **Tool Overview**: Metalign v0.12.5 is an efficient tool for alignment-based metagenomic profiling using containment min hash.
- **Core Function**: Profiles metagenomic samples by efficiently mapping reads to reference databases using min hash-based containment estimation.
- **Containment Min Hash**: Uses min hash signatures to quickly estimate sequence containment between reads and reference genomes.
- **Efficient Profiling**: Enables fast metagenomic profiling even for large reference databases.
- **Input/Output**: Accepts FASTQ sequencing reads; outputs taxonomic profiles with abundance estimates.
- **Reference Mapping**: Maps reads to reference sequences using efficient alignment strategies.

## Pitfalls

- **Database Completeness**: Profiling accuracy depends on reference database completeness.
- **Memory Requirements**: Building and loading min hash indexes may require significant memory.
- **k-mer Size Selection**: Choosing inappropriate k-mer sizes can affect sensitivity and specificity.
- **False Positives**: May produce false positive matches with similar sequences.
- **Low Abundance Detection**: May miss organisms present at very low abundance.
- **Computational Resources**: Processing large datasets may require significant computational resources.

## Examples

### Profile metagenomic sample
**Args:** `metalign -i reads.fastq -d reference_db/ -o profile.txt`
**Explanation:** Profiles metagenomic reads against reference database.

### Build min hash index
**Args:** `metalign build -i references.fasta -o index.mmh`
**Explanation:** Builds a min hash index from reference sequences.

### Use pre-built index
**Args:** `metalign -i reads.fastq -x index.mmh -o profile.txt`
**Explanation:** Uses pre-built min hash index for profiling.

### Paired-end analysis
**Args:** `metalign -i reads_1.fastq reads_2.fastq -d reference_db/ -o profile.txt`
**Explanation:** Processes paired-end sequencing data.

### Output detailed report
**Args:** `metalign -i reads.fastq -d reference_db/ -o profile.txt -v`
**Explanation:** Generates verbose output with detailed profiling information.