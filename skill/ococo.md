---
name: ococo
category: utility
description: Ococo is an online consensus caller for generating consensus sequences from aligned reads.
tags: [ococo, utility, consensus-calling, sequence-analysis]
author: oxo-call-community
source_url: "http://github.com/karel-brinda/ococo"
---

## Concepts

- **Tool Overview**: Ococo generates consensus sequences from aligned sequencing reads.
- **Core Function**: Calls consensus bases from multiple aligned sequences.
- **Algorithm**: Uses majority voting and quality-based consensus calling.
- **Input Format**: Accepts BAM alignment files or FASTA sequences.
- **Output**: Produces consensus sequence in FASTA format.
- **Use Case**: Genome assembly finishing, consensus generation, and sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Quality**: Results depend on input alignment quality.
- **Ambiguity Handling**: May report ambiguous bases.
- **Memory Usage**: Large alignments require memory.
- **Computational Cost**: Processing can be computationally intensive.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `ococo --help`
**Explanation:** Shows available options and usage instructions.

### Generate consensus
**Args:** `ococo -i alignments.bam -o consensus.fasta`
**Explanation:** Generates consensus from BAM file.

### From FASTA
**Args:** `ococo -i sequences.fasta -o consensus.fasta`
**Explanation:** Generates consensus from multiple FASTA sequences.

### Minimum coverage
**Args:** `ococo -i alignments.bam -c 10 -o consensus.fasta`
**Explanation:** Sets minimum coverage threshold to 10.

### Quality threshold
**Args:** `ococo -i alignments.bam -q 30 -o consensus.fasta`
**Explanation:** Sets minimum quality score to 30.

### Output VCF
**Args:** `ococo -i alignments.bam -o variants.vcf --vcf`
**Explanation:** Outputs variants in VCF format.

### Verbose mode
**Args:** `ococo -i alignments.bam -v -o consensus.fasta`
**Explanation:** Runs with verbose output.