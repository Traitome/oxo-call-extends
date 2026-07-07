---
name: svpg
category: variant-calling
description: Pangenome-based structural variation caller for comprehensive SV detection.
tags: [svpg, structural-variants, pangenome, variant-discovery]
author: oxo-call-community
source_url: "https://github.com/coopsor/SVPG"
---

## Concepts

- **Tool Overview**: svpg (v1.4.1) discovers structural variants using pangenome approach.
- **Core Function**: Detects SVs by comparing reads against pangenome reference.
- **Algorithm**: Uses pangenome indexing for sensitive SV detection across diverse samples.
- **Input/Output**: Input: FASTQ/FASTA reads, pangenome; Output: VCF with SV calls.
- **Applications**: Population genetics, comparative genomics, SV discovery.
- **Installation**: `conda install -c bioconda svpg` or download from GitHub.

## Pitfalls

- **Reference Preparation**: Requires pangenome reference construction.
- **Memory Requirements**: Large pangenomes require significant memory.
- **Computational Time**: Pangenome alignment can be slow.
- **Parameter Tuning**: Incorrect parameters affect sensitivity.
- **Reference Diversity**: Performance depends on pangenome diversity.
- **Storage Requirements**: Pangenome indexes require significant storage.

## Examples

### Display help
**Args:** `svpg --help`
**Explanation:** Shows available options and usage information.

### Basic SV calling
**Args:** `svpg -i reads.fastq -p pangenome/ -o sv.vcf`
**Explanation:** Call SVs using pangenome reference.

### Build pangenome index
**Args:** `svpg build -r references/ -o pangenome/`
**Explanation:** Build pangenome index from multiple references.

### Verbose mode
**Args:** `svpg -i reads.fastq -p pangenome/ -o sv.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svpg -i reads.fastq -p pangenome/ -o sv.vcf --stats`
**Explanation:** Generate statistics about SV calling.

### Batch processing
**Args:** `svpg -i fastqs/ -p pangenome/ -o results/`
**Explanation:** Process multiple FASTQ files together.

### Filter by quality
**Args:** `svpg -i reads.fastq -p pangenome/ -o sv.vcf -q 20`
**Explanation:** Filter SVs by quality score.

### Include novel variants
**Args:** `svpg -i reads.fastq -p pangenome/ -o sv.vcf --novel`
**Explanation:** Report novel SVs not in pangenome.

### Generate report
**Args:** `svpg -i reads.fastq -p pangenome/ -o sv.vcf --report`
**Explanation:** Generate comprehensive HTML report.
