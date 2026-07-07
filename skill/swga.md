---
name: swga
category: primer-design
description: Select primer sets for selective whole genome amplification (SWGA).
tags: [swga, primer-design, whole-genome-amplification, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/eclarke/swga"
---

## Concepts

- **Tool Overview**: swga (v0.4.4) designs primer sets for selective whole genome amplification.
- **Core Function**: Identifies optimal primer combinations for targeted genome amplification.
- **Algorithm**: Uses greedy algorithm to select primers that amplify specific genomic regions.
- **Input/Output**: Input: Reference genome, target regions; Output: Primer sets.
- **Applications**: Metagenomics, target enrichment, diagnostic PCR.
- **Installation**: `conda install -c bioconda swga` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large genomes require significant memory.
- **Computational Time**: Primer selection can be computationally intensive.
- **Parameter Tuning**: Incorrect parameters affect primer quality.
- **Reference Quality**: Requires high-quality reference genome.
- **Primer Specificity**: May require validation experiments.
- **Target Complexity**: Complex genomes may be challenging.

## Examples

### Display help
**Args:** `swga --help`
**Explanation:** Shows available options and usage information.

### Basic primer selection
**Args:** `swga design -r reference.fasta -t targets.bed -o primers.txt`
**Explanation:** Design primers for target regions.

### With constraints
**Args:** `swga design -r reference.fasta -t targets.bed -o primers.txt -l 20`
**Explanation:** Use primer length of 20 nucleotides.

### Verbose mode
**Args:** `swga design -r reference.fasta -t targets.bed -o primers.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `swga design -r reference.fasta -t targets.bed -o primers.txt --stats`
**Explanation:** Generate statistics about primer design.

### Batch processing
**Args:** `for t in targets/*.bed; do swga design -r ref.fasta -t $t -o primers/${t%.bed}.txt; done`
**Explanation:** Design primers for multiple target sets.

### Filter by Tm
**Args:** `swga design -r reference.fasta -t targets.bed -o primers.txt -m 55 -M 65`
**Explanation:** Filter primers by melting temperature range.

### Include GC content
**Args:** `swga design -r reference.fasta -t targets.bed -o primers.txt -g 40 -G 60`
**Explanation:** Filter primers by GC content range.

### Generate report
**Args:** `swga design -r reference.fasta -t targets.bed -o primers.txt --report`
**Explanation:** Generate comprehensive primer design report.
