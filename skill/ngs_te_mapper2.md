---
name: ngs_te_mapper2
category: variant-calling
description: ngs_te_mapper2 identifies transposable element insertions from NGS data.
tags: [ngs_te_mapper2, variant-calling, transposable-elements, te-insertions]
author: oxo-call-community
source_url: "https://github.com/bergmanlab/ngs_te_mapper2"
---

## Concepts

- **Tool Overview**: ngs_te_mapper2 detects transposable element insertions from sequencing data.
- **Core Function**: Identifies TE insertion sites in the genome.
- **Algorithm**: Analyzes split reads and discordant pairs for TE detection.
- **Input Format**: Accepts BAM files and TE reference sequences.
- **Output**: Produces VCF files with TE insertion calls.
- **Use Case**: Transposable element analysis, genome variation, and evolutionary studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference TE Sequences**: Requires TE consensus sequences.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Parameter Tuning**: Requires careful parameter optimization.
- **False Positives**: May detect false insertions.

## Examples

### Display help
**Args:** `ngs_te_mapper2 --help`
**Explanation:** Shows available options and usage instructions.

### Run TE mapping
**Args:** `ngs_te_mapper2 -i alignment.bam -r reference.fasta -t te_consensus.fasta -o te_insertions.vcf`
**Explanation:** Detects TE insertions from aligned reads.

### Specify TE library
**Args:** `ngs_te_mapper2 -i alignment.bam -r reference.fasta -l te_library.txt -o te_insertions.vcf`
**Explanation:** Uses custom TE library.

### Minimum support
**Args:** `ngs_te_mapper2 -i alignment.bam -r reference.fasta -t te_consensus.fasta -m 5 -o te_insertions.vcf`
**Explanation:** Sets minimum read support threshold.

### Threads
**Args:** `ngs_te_mapper2 -i alignment.bam -r reference.fasta -t te_consensus.fasta -p 8 -o te_insertions.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Output BED
**Args:** `ngs_te_mapper2 -i alignment.bam -r reference.fasta -t te_consensus.fasta --bed -o te_insertions.bed`
**Explanation:** Outputs BED format.

### Verbose mode
**Args:** `ngs_te_mapper2 -i alignment.bam -r reference.fasta -t te_consensus.fasta -v -o te_insertions.vcf`
**Explanation:** Runs with verbose output.