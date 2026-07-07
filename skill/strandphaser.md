---
name: strandphaser
category: variant-calling
description: Phase Strand-seq data for haplotype phasing.
tags: [strandphaser, haplotype-phasing, strand-seq, genomics]
author: oxo-call-community
source_url: "https://github.com/daewoooo/StrandPhaseR/"
---

## Concepts

- **Tool Overview**: strandphaser (v1.0.2) is a tool for phasing Strand-seq data to determine haplotypes.
- **Core Function**: Uses strand-specific sequencing data to phase genetic variants.
- **Algorithm**: Analyzes strand inheritance patterns to determine haplotype phase.
- **Input/Output**: Input: Strand-seq BAM file, variant calls; Output: Phased haplotypes.
- **Applications**: Haplotype phasing, population genetics, disease association studies.
- **Installation**: `conda install -c bioconda strandphaser` or download from GitHub.

## Pitfalls

- **Strand Bias**: Unequal strand coverage affects phasing accuracy.
- **Read Quality**: Low-quality reads affect variant calling.
- **Complex Regions**: Repetitive regions are hard to phase.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Phasing large genomes can be slow.
- **Reference Dependence**: Requires high-quality reference genome.

## Examples

### Display help
**Args:** `strandphaser --help`
**Explanation:** Shows available options and usage information.

### Basic haplotype phasing
**Args:** `strandphaser -i strandseq.bam -v variants.vcf -o haplotypes.txt`
**Explanation:** Phase variants using Strand-seq data.

### With reference genome
**Args:** `strandphaser -i strandseq.bam -v variants.vcf -r reference.fasta -o haplotypes.txt`
**Explanation:** Use reference genome for guided phasing.

### Verbose mode
**Args:** `strandphaser -i strandseq.bam -v variants.vcf -o haplotypes.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `strandphaser -i strandseq.bam -v variants.vcf -o haplotypes.txt --plot`
**Explanation:** Generate visualization of phased haplotypes.

### Custom parameters
**Args:** `strandphaser -i strandseq.bam -v variants.vcf -o haplotypes.txt -c 0.9`
**Explanation:** Minimum confidence threshold of 0.9.

### Batch processing
**Args:** `strandphaser -i batch/ -v variants.vcf -o results/`
**Explanation:** Process multiple Strand-seq samples together.

### Filter by quality
**Args:** `strandphaser -i strandseq.bam -v variants.vcf -o haplotypes.txt -q 30`
**Explanation:** Filter variants by quality score threshold.

### Generate report
**Args:** `strandphaser -i strandseq.bam -v variants.vcf -o haplotypes.txt --report`
**Explanation:** Generate comprehensive HTML report.
