---
name: lassensus
category: virology
description: Consensus sequence generation from Lassa virus sequencing data
tags: [lassensus, virology, Lassa-virus, consensus, sequencing, viral-genomics]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/lassensus"
---

## Concepts

- **Consensus Generation**: Creates consensus sequences from sequencing data
- **Lassa Virus Specific**: Optimized for Lassa virus data
- **Variant Calling**: Identifies variants within populations
- **Quality Trimming**: Includes read quality filtering
- **Genome Assembly**: Assembles viral genome from reads
- **High-quality Sequences**: Produces high-quality consensus sequences

## Pitfalls

- **Coverage Depth**: Low coverage produces incomplete consensus
- **Mixed Infections**: Multiple strains complicate consensus calling
- **Reference Bias**: Alignment to single reference may miss variants
- **Quality Scores**: Poor base quality affects accuracy
- **Ambiguous Bases**: Low coverage leads to N bases in consensus
- **Primer Regions**: PCR primers may cause artifacts

## Examples

### Generate consensus
**Args:** `lassensus -i reads.fastq -o consensus.fasta`
**Explanation:** Generates consensus sequence from reads.

### Specify reference
**Args:** `lassensus -i reads.fastq -r reference.gb -o consensus.fasta`
**Explanation:** Uses specific reference for alignment.

### Set coverage threshold
**Args:** `lassensus -i reads.fastq --min-cov 10 -o consensus.fasta`
**Explanation:** Requires minimum 10x coverage.

### Both segments
**Args:** `lassensus -i reads.fastq --segment S --segment L -o results/`
**Explanation:** Processes both genome segments.

### Filter variants
**Args:** `lassensus -i reads.fastq --min-freq 0.5 -o consensus.fasta`
**Explanation:** Only includes variants with 50% frequency.

### Export VCF
**Args:** `lassensus -i reads.fastq -o consensus.fasta --vcf variants.vcf`
**Explanation:** Also exports variant calls in VCF format.