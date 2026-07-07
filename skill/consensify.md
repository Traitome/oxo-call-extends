---
name: consensify
category: qc
description: Generate consensus pseudohaploid genome sequences
tags: [consensify, consensus, pseudohaploid, ancient-dna, genomics]
author: oxo-call-community
source_url: "https://github.com/jlapaijmans/Consensify"
---

## Concepts

- **Tool Overview**: Consensify is a method for generating consensus pseudohaploid genome sequences from sequencing data, particularly useful for ancient DNA and low-coverage genomes.
- **Core Function**: Creates haploid consensus sequences by randomly selecting one allele at heterozygous sites, reducing bias in population genetic analyses.
- **Algorithm**: Uses random sampling at heterozygous positions while maintaining homozygous calls.
- **Input**: Aligned sequencing reads in BAM format, variant calls in VCF format.
- **Output**: Consensus pseudohaploid genome sequence in FASTA format.
- **Application**: Ancient DNA analysis, population genetics, and phylogenetic studies.
- **Installation**: Install via bioconda: `conda install -c bioconda consensify`

## Pitfalls

- **Coverage Requirements**: Requires sufficient coverage for reliable consensus calling.
- **Random Sampling**: Different runs may produce slightly different consensus sequences.
- **Heterozygosity Loss**: Intentionally loses heterozygosity information.
- **Reference Bias**: May inherit reference genome biases.
- **Damage Patterns**: Ancient DNA damage may affect consensus accuracy.

## Examples

### Generate consensus sequence
**Args:** `consensify -i input.bam -r reference.fasta -o consensus.fasta`
**Explanation:** Generates pseudohaploid consensus sequence from aligned reads.

### With random seed
**Args:** `consensify -i input.bam -r reference.fasta -s 42 -o consensus.fasta`
**Explanation:** Sets random seed for reproducible consensus generation.

### With minimum coverage
**Args:** `consensify -i input.bam -r reference.fasta -c 3 -o consensus.fasta`
**Explanation:** Requires minimum coverage of 3x for consensus calling.

### Display help
**Args:** `consensify --help`
**Explanation:** Shows all available options and usage information.