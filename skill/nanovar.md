---
name: nanovar
category: variant-calling
description: NanoVar is a structural variant caller optimized for low-depth long-read sequencing data.
tags: [nanovar, variant-calling, structural-variation, nanopore, low-depth]
author: oxo-call-community
source_url: "https://github.com/cytham/nanovar"
---

## Concepts

- **Tool Overview**: NanoVar v1.8.3 is a structural variant caller optimized for low-coverage long-read sequencing data.
- **Core Function**: Detects structural variants from low-depth Nanopore or PacBio sequencing with high sensitivity.
- **Algorithm**: Uses a combination of split-read mapping, read-depth analysis, and assembly-based approaches.
- **Input Format**: Accepts aligned BAM files from long-read aligners like minimap2.
- **Output**: Produces VCF files with structural variant calls and confidence scores.
- **Use Case**: SV detection in low-coverage sequencing studies, population genetics, and rare disease research.

## Pitfalls

- **Low Coverage Limits**: Performance degrades significantly below 5x coverage.
- **Complex Regions**: May miss variants in highly repetitive or complex genomic regions.
- **Alignment Artifacts**: Requires careful alignment processing to avoid false positives.
- **Computational Cost**: Assembly-based calling can be computationally intensive.
- **Version Differences**: Options and output format may vary between versions.
- **Reference Requirements**: Needs high-quality reference assembly for accurate calls.

## Examples

### Display help
**Args:** `nanovar --help`
**Explanation:** Shows available options and usage instructions.

### Basic usage
**Args:** `nanovar -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Detects structural variants from low-depth long reads.

### Specify coverage
**Args:** `nanovar -i aligned.bam -r ref.fasta -c 5 -o variants.vcf`
**Explanation:** Optimizes for 5x coverage data.

### Output directory
**Args:** `nanovar -i aligned.bam -r ref.fasta -d output_dir -o variants.vcf`
**Explanation:** Creates output directory for intermediate files.

### Threads
**Args:** `nanovar -i aligned.bam -r ref.fasta -t 4 -o variants.vcf`
**Explanation:** Uses 4 threads for parallel processing.

### Minimum SV size
**Args:** `nanovar -i aligned.bam -r ref.fasta -m 100 -o variants.vcf`
**Explanation:** Sets minimum SV size to 100bp.