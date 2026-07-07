---
name: svync
category: variant-calling
description: Tool to standardize VCF files from different structural variant callers.
tags: [svync, structural-variants, vcf-standardization, variant-calling]
author: oxo-call-community
source_url: "https://github.com/nvnieuwk/svync"
---

## Concepts

- **Tool Overview**: svync (v0.3.0) standardizes VCF files from different SV callers.
- **Core Function**: Converts SV VCF files to a standardized format.
- **Algorithm**: Normalizes SV representations across different callers.
- **Input/Output**: Input: SV VCF from various callers; Output: Standardized VCF.
- **Applications**: VCF harmonization, multi-caller SV integration.
- **Installation**: `conda install -c bioconda svync` or download from GitHub.

## Pitfalls

- **Input Format**: Requires properly formatted SV VCF files.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large SV sets can be slow.
- **Parameter Tuning**: Incorrect parameters affect standardization.
- **Tool Compatibility**: Not all SV callers may be supported.
- **Version Compatibility**: Different versions may have incompatible options.

## Examples

### Display help
**Args:** `svync --help`
**Explanation:** Shows available options and usage information.

### Basic VCF standardization
**Args:** `svync -i input.vcf -o standardized.vcf`
**Explanation:** Standardize SV VCF file.

### With reference
**Args:** `svync -i input.vcf -o standardized.vcf -r reference.fasta`
**Explanation:** Use reference genome for standardization.

### Verbose mode
**Args:** `svync -i input.vcf -o standardized.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svync -i input.vcf -o standardized.vcf --stats`
**Explanation:** Generate statistics about standardization.

### Batch processing
**Args:** `svync -i vcfs/ -o standardized/`
**Explanation:** Process multiple VCF files together.

### Filter by quality
**Args:** `svync -i input.vcf -o standardized.vcf -q 20`
**Explanation:** Filter SVs by quality score.

### Include all SV types
**Args:** `svync -i input.vcf -o standardized.vcf --all-types`
**Explanation:** Include all types of structural variants.

### Generate report
**Args:** `svync -i input.vcf -o standardized.vcf --report`
**Explanation:** Generate comprehensive HTML report.
