---
name: npinv
category: structural-variation
description: npInv detects and genotypes inversions using multiple alignment long reads.
tags: [npinv, structural-variation, inversion, long-reads]
author: oxo-call-community
source_url: "https://github.com/haojingshao/npInv"
---

## Concepts

- **Tool Overview**: npInv detects and genotypes inversions from long-read alignments.
- **Core Function**: Identifies inversion breakpoints and determines genotypes.
- **Algorithm**: Uses multiple alignment approach for accurate inversion detection.
- **Input Format**: Accepts BAM files with long-read alignments.
- **Output**: Produces VCF with inversion calls and genotypes.
- **Use Case**: Structural variation analysis, inversion detection, and population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Long Reads**: Requires long-read sequencing data.
- **Alignment Quality**: Results depend on alignment quality.
- **Memory Usage**: Large datasets require memory.
- **Complex Inversions**: May miss complex nested inversions.
- **Validation**: Results should be experimentally validated.

## Examples

### Display help
**Args:** `npinv --help`
**Explanation:** Shows available options and usage instructions.

### Detect inversions
**Args:** `npinv -i alignments.bam -o inversions.vcf`
**Explanation:** Detects inversions from aligned reads.

### With reference
**Args:** `npinv -i alignments.bam -r reference.fasta -o inversions.vcf`
**Explanation:** Uses reference genome for analysis.

### Genotype inversions
**Args:** `npinv -i alignments.bam -g -o inversions.vcf`
**Explanation:** Genotypes detected inversions.

### Minimum support
**Args:** `npinv -i alignments.bam -m 5 -o inversions.vcf`
**Explanation:** Requires minimum 5 reads supporting inversion.

### Threads
**Args:** `npinv -i alignments.bam -t 8 -o inversions.vcf`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `npinv -i alignments.bam -v -o inversions.vcf`
**Explanation:** Runs with verbose output.