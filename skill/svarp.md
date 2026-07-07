---
name: svarp
category: variant-calling
description: Pangenome-based structural variant discovery for comprehensive SV detection.
tags: [svarp, structural-variants, pangenome, variant-discovery]
author: oxo-call-community
source_url: "https://github.com/asylvz/SVarp"
---

## Concepts

- **Tool Overview**: svarp (v1.2.0) discovers structural variants using pangenome approach.
- **Core Function**: Detects SVs by comparing reads against multiple reference genomes.
- **Algorithm**: Uses pangenome indexing for sensitive SV detection across diverse samples.
- **Input/Output**: Input: FASTQ reads, pangenome reference; Output: SV calls.
- **Applications**: Population genetics, comparative genomics, SV discovery.
- **Installation**: `conda install -c bioconda svarp` or download from GitHub.

## Pitfalls

- **Reference Preparation**: Requires pangenome reference construction.
- **Memory Requirements**: Large pangenomes require significant memory.
- **Computational Time**: Pangenome alignment can be slow.
- **Parameter Tuning**: Incorrect parameters affect sensitivity.
- **Reference Diversity**: Performance depends on pangenome diversity.
- **Storage Requirements**: Pangenome indexes require significant storage.

## Examples

### Display help
**Args:** `svarp --help`
**Explanation:** Shows available options and usage information.

### Basic SV discovery
**Args:** `svarp discover -i reads.fastq -p pangenome/ -o sv.vcf`
**Explanation:** Discover SVs using pangenome reference.

### Build pangenome index
**Args:** `svarp build -r references/ -o pangenome/`
**Explanation:** Build pangenome index from multiple references.

### Verbose mode
**Args:** `svarp discover -i reads.fastq -p pangenome/ -o sv.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svarp discover -i reads.fastq -p pangenome/ -o sv.vcf --stats`
**Explanation:** Generate statistics about SV discovery.

### Batch processing
**Args:** `svarp discover -i fastqs/ -p pangenome/ -o results/`
**Explanation:** Process multiple FASTQ files together.

### Filter by quality
**Args:** `svarp discover -i reads.fastq -p pangenome/ -o sv.vcf -q 20`
**Explanation:** Filter SVs by quality score.

### Include novel variants
**Args:** `svarp discover -i reads.fastq -p pangenome/ -o sv.vcf --novel`
**Explanation:** Report novel SVs not in pangenome.

### Generate report
**Args:** `svarp discover -i reads.fastq -p pangenome/ -o sv.vcf --report`
**Explanation:** Generate comprehensive HTML report.
