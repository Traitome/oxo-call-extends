---
name: svtk
category: variant-calling
description: Utilities for consolidating, filtering, resolving, and annotating structural variants.
tags: [svtk, structural-variants, variant-filtering, annotation]
author: oxo-call-community
source_url: "https://github.com/talkowski-lab/svtk"
---

## Concepts

- **Tool Overview**: svtk (v0.0.20190615) provides utilities for SV analysis and processing.
- **Core Function**: Consolidates, filters, resolves, and annotates structural variants.
- **Algorithm**: Uses various methods for SV processing and quality control.
- **Input/Output**: Input: SV VCF files; Output: Filtered/annotated VCF files.
- **Applications**: SV quality control, variant filtering, annotation.
- **Installation**: `conda install -c bioconda svtk` or download from GitHub.

## Pitfalls

- **Input Format**: Requires properly formatted SV VCF files.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large SV sets can be slow.
- **Parameter Tuning**: Incorrect parameters affect filtering.
- **Annotation Sources**: Requires proper annotation database setup.
- **Tool Compatibility**: May require specific VCF formats.

## Examples

### Display help
**Args:** `svtk --help`
**Explanation:** Shows available options and usage information.

### Basic SV filtering
**Args:** `svtk filter -i sv.vcf -o filtered.vcf`
**Explanation:** Filter SVs using default settings.

### SV consolidation
**Args:** `svtk consolidate -i sv_calls/*.vcf -o merged.vcf`
**Explanation:** Consolidate multiple SV callsets.

### Verbose mode
**Args:** `svtk filter -i sv.vcf -o filtered.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svtk stats -i sv.vcf -o stats.txt`
**Explanation:** Generate statistics about SV calls.

### Batch processing
**Args:** `svtk filter -i vcfs/ -o filtered/`
**Explanation:** Process multiple VCF files together.

### Filter by quality
**Args:** `svtk filter -i sv.vcf -o filtered.vcf -q 20`
**Explanation:** Filter SVs by quality score.

### Annotate SVs
**Args:** `svtk annotate -i sv.vcf -a annotations.gtf -o annotated.vcf`
**Explanation:** Annotate SVs with gene information.

### Generate report
**Args:** `svtk report -i sv.vcf -o report.html`
**Explanation:** Generate comprehensive HTML report.
