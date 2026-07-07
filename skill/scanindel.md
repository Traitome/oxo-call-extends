---
name: scanindel
category: variant-calling
description: ScanIndel - detection of insertions and deletions from NGS data by re-alignment
tags: ["scanindel", "variant-calling", "INDELs", "re-alignment"]
author: oxo-call-community
source_url: "https://github.com/cauyrd/ScanIndel"
---

## Concepts

- **Tool Overview**: ScanIndel (v1.3) is a Python program to detect indels (insertions and deletions) from NGS data by re-aligning and de novo assembling soft-clipped reads.
- **Core Function**: Identifies INDELs by analyzing soft-clipped reads and performing local de novo assembly.
- **Algorithm**: Uses soft-clipped read detection, local assembly, and re-alignment to accurately identify INDELs.
- **Input/Output**: Accepts BAM files and reference genome, produces VCF with INDEL calls.
- **Soft-clipped Reads**: Focuses on reads with soft-clipped regions that may indicate INDELs.
- **Applications**: Variant discovery, clinical genomics, and population genetics.

## Pitfalls

- **Soft-clipped Dependence**: Relies on soft-clipped reads for INDEL detection.
- **Read Depth**: Requires sufficient coverage for reliable detection.
- **Reference Genome**: Results depend on reference quality and completeness.
- **Computational Resources**: May require significant compute resources.
- **False Positives**: May report false INDELs from misaligned reads.
- **Parameter Tuning**: Requires careful adjustment for optimal performance.

## Examples

### Basic INDEL detection
**Args:** `scanindel -i alignments.bam -r reference.fasta -o variants.vcf`
**Explanation:** `-i` input BAM; `-r` reference genome; `-o` output VCF.

### With quality filtering
**Args:** `scanindel -i alignments.bam -r reference.fasta -q 20 -o variants.vcf`
**Explanation:** `-q 20` filters variants with quality below 20.

### Targeted regions
**Args:** `scanindel -i alignments.bam -r reference.fasta -t targets.bed -o variants.vcf`
**Explanation:** `-t` BED file with target regions.

### Minimum INDEL size
**Args:** `scanindel -i alignments.bam -r reference.fasta -min 5 -o variants.vcf`
**Explanation:** `-min 5` detects INDELs >= 5 bp.

### Maximum INDEL size
**Args:** `scanindel -i alignments.bam -r reference.fasta -max 100 -o variants.vcf`
**Explanation:** `-max 100` detects INDELs <= 100 bp.

### Verbose logging
**Args:** `scanindel -i alignments.bam -r reference.fasta -v -o variants.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Assembly mode
**Args:** `scanindel -i alignments.bam -r reference.fasta --assembly -o variants.vcf`
**Explanation:** `--assembly` enables local de novo assembly mode.