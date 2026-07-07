---
name: gustaf
category: bioinformatics
description: Gustaf performs multi-split mapping of sequencing reads, enabling alignment across multiple genomic regions.
tags: [gustaf, read-mapping, multi-split, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/seqan/seqan"
---

## Concepts

- **Multi-split Mapping**: Gustaf maps reads that span multiple genomic regions.

- **Read Alignment**: Aligns sequencing reads to reference genomes.

- **Split Reads**: Handles reads that are split across exons or regions.

- **Chimeric Reads**: Identifies chimeric read mappings.

- **Structural Variants**: Aids in detection of structural variants.

- **Efficiency**: Optimized for fast processing of large datasets.

## Pitfalls

- **Memory Usage**: Mapping large datasets may require significant memory.

- **Reference Genome**: Requires well-indexed reference genome.

- **Read Quality**: Low-quality reads affect mapping accuracy.

- **Parameter Tuning**: Adjust parameters based on read characteristics.

- **Output Interpretation**: Interpret split mappings carefully.

## Examples

### Map reads
**Args:** `gustaf map -i reads.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Maps reads to reference genome with multi-split support.

### Paired-end mapping
**Args:** `gustaf map -i reads_1.fastq -i2 reads_2.fastq -r reference.fasta -o alignments.sam`
**Explanation:** Maps paired-end reads with multi-split support.

### Custom split size
**Args:** `gustaf map -i reads.fastq -r reference.fasta -s 50 -o alignments.sam`
**Explanation:** Sets minimum split size for mapping.

### Batch processing
**Args:** `for f in *.fastq; do gustaf map -i $f -r reference.fasta -o ${f%.fastq}_alignments.sam; done`
**Explanation:** Processes multiple read files.

### Generate statistics
**Args:** `gustaf stats -i alignments.sam -o stats.txt`
**Explanation:** Generates mapping statistics.

### Filter mappings
**Args:** `gustaf filter -i alignments.sam -q 30 -o filtered.sam`
**Explanation:** Filters mappings by quality score.

### Help command
**Args:** `gustaf --help`
**Explanation:** Shows available options and usage information.