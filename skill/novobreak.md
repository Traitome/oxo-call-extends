---
name: novobreak
category: assembly
description: NovoBreak performs local assembly for breakpoint detection in cancer genomes.
tags: [novobreak, assembly, cancer-genomics, breakpoint-detection]
author: oxo-call-community
source_url: "https://github.com/czc/nb_distribution"
---

## Concepts

- **Tool Overview**: NovoBreak identifies structural variants through local assembly.
- **Core Function**: Detects breakpoints in cancer genomes using assembly approach.
- **Algorithm**: Implements local assembly around potential breakpoints.
- **Input Format**: Accepts BAM files and reference genome.
- **Output**: Produces breakpoint calls and assembled sequences.
- **Use Case**: Cancer genomics, structural variant detection, and SV analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Data Quality**: Results depend on sequencing quality.
- **Computational Cost**: Assembly can be computationally intensive.
- **Memory Usage**: Large datasets require memory.
- **False Positives**: May detect spurious breakpoints.
- **Validation**: Results should be experimentally validated.

## Examples

### Display help
**Args:** `novobreak --help`
**Explanation:** Shows available options and usage instructions.

### Run breakpoint detection
**Args:** `novobreak -i tumor.bam -r reference.fasta -o breakpoints.txt`
**Explanation:** Detects breakpoints in cancer genome.

### With normal sample
**Args:** `novobreak -i tumor.bam -n normal.bam -r reference.fasta -o breakpoints.txt`
**Explanation:** Uses matched normal for filtering.

### Output VCF
**Args:** `novobreak -i tumor.bam -r reference.fasta -o breakpoints.vcf --vcf`
**Explanation:** Outputs breakpoints in VCF format.

### Minimum support
**Args:** `novobreak -i tumor.bam -r reference.fasta -m 5 -o breakpoints.txt`
**Explanation:** Requires minimum 5 reads supporting breakpoint.

### Threads
**Args:** `novobreak -i tumor.bam -r reference.fasta -t 8 -o breakpoints.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `novobreak -i tumor.bam -r reference.fasta -v -o breakpoints.txt`
**Explanation:** Runs with verbose output.

### Assembly only
**Args:** `novobreak -i tumor.bam -r reference.fasta -a -o assemblies.fasta`
**Explanation:** Performs assembly without breakpoint detection.