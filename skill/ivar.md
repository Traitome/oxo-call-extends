---
name: ivar
category: utility
description: iVar is a computational package that contains functions broadly useful for viral amplicon-based sequencing.
tags: [ivar, utility, virus, amplicon, sequencing]
author: oxo-call-community
source_url: "https://andersen-lab.github.io/ivar/html"
---

## Concepts

- **Tool Overview**: iVar (v1.4.4) - A comprehensive toolkit for analyzing viral amplicon sequencing data, including primer trimming, consensus calling, and variant detection.
- **Primer Trimming**: Removes primer sequences from amplicon reads using alignment-based approach.
- **Consensus Calling**: Generates consensus sequences with quality-based variant filtering.
- **Variant Calling**: Identifies SNVs and indels with support for both haploid and diploid calling.
- **Frequency Thresholds**: Filters variants based on minimum frequency in the population.
- **BAM Processing**: Works directly with aligned BAM files for efficient processing.
- **Phylogenetic Support**: Generates output formats compatible with downstream phylogenetic analysis.

## Pitfalls

- **Primer Mismatches**: Primer sequences must exactly match those used in sequencing.
- **PCR Duplicates**: High duplicate rates can skew variant frequencies.
- **Reference Bias**: Variant calling may be biased toward the reference sequence.
- **Low Coverage**: Regions with low coverage may miss true variants.
- **Indel Handling**: Complex indels may be incorrectly called or missed.
- **Ambiguity Codes**: Mixed bases in consensus may affect downstream analysis.

## Examples

### Trim primers from reads
**Args:** `ivar trim -b primers.bed -i input.bam -p output_prefix`
**Explanation:** Trims primer sequences from aligned reads using BED file of primer coordinates.

### Call consensus sequence
**Args:** `ivar consensus -i trimmed.bam -o consensus.fasta`
**Explanation:** Generates consensus sequence from trimmed BAM file.

### Call variants
**Args:** `ivar variants -i trimmed.bam -b reference.fasta -p variants`
**Explanation:** Calls variants relative to reference sequence and outputs to VCF.

### Set minimum frequency threshold
**Args:** `ivar variants -i trimmed.bam -b ref.fasta -p variants -t 0.05`
**Explanation:** Only reports variants with frequency ≥5%.

### Filter by quality
**Args:** `ivar variants -i trimmed.bam -b ref.fasta -p variants -q 20`
**Explanation:** Requires minimum Phred quality score of 20 for variant calls.

### Generate frequency table
**Args:** `ivar freq -i trimmed.bam -p frequency_table`
**Explanation:** Generates nucleotide frequency table at each position.