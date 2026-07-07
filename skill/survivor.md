---
name: survivor
category: variant-calling
description: Toolset for SV simulation, comparison and filtering of structural variants.
tags: [survivor, structural-variants, sv-analysis, variant-comparison]
author: oxo-call-community
source_url: "https://github.com/fritzsedlazeck/SURVIVOR"
---

## Concepts

- **Tool Overview**: survivor (v1.0.7) is a toolset for SV simulation, comparison and filtering.
- **Core Function**: Analyzes and compares structural variant calls from multiple sources.
- **Algorithm**: Uses graph-based methods for SV comparison and merging.
- **Input/Output**: Input: SV VCF files; Output: Merged/filtered VCF, comparison statistics.
- **Applications**: SV benchmarking, variant calling validation, SV integration.
- **Installation**: `conda install -c bioconda survivor` or download from GitHub.

## Pitfalls

- **Input Format**: Requires specific SV VCF format.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect merging results.
- **SV Types**: May not support all SV types equally.
- **Coordinate System**: Requires consistent coordinate system.

## Examples

### Display help
**Args:** `SURVIVOR --help`
**Explanation:** Shows available options and usage information.

### Basic SV merging
**Args:** `SURVIVOR merge sv_calls/*.vcf 1000 1 1 0 0 50 merged.vcf`
**Explanation:** Merge multiple SV VCF files.

### SV comparison
**Args:** `SURVIVOR compare sv1.vcf sv2.vcf 1000 1 1 0 comparison.txt`
**Explanation:** Compare two sets of SV calls.

### Verbose mode
**Args:** `SURVIVOR merge sv_calls/*.vcf 1000 1 1 0 0 50 merged.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### SV simulation
**Args:** `SURVIVOR simulate reference.fasta 1000 0.1 0.1 0.1 0.1 0.1 simulated.vcf`
**Explanation:** Simulate structural variants.

### Batch processing
**Args:** `SURVIVOR merge vcfs/*.vcf 1000 1 1 0 0 50 merged.vcf`
**Explanation:** Merge VCF files from directory.

### Filter by size
**Args:** `SURVIVOR filter sv.vcf filtered.vcf 100 1000000`
**Explanation:** Filter SVs by size range.

### Include all SV types
**Args:** `SURVIVOR merge sv_calls/*.vcf 1000 1 1 1 0 50 merged.vcf`
**Explanation:** Include all SV types in merging.

### Generate report
**Args:** `SURVIVOR stats sv.vcf stats.txt`
**Explanation:** Generate statistics about SV calls.
