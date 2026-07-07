---
name: array-as-vcf
category: variant-calling
description: Convert SNP array data to VCF format
tags: [array-as-vcf, variant-calling, VCF, snp-array, genotyping]
author: oxo-call-community
source_url: "https://github.com/LUMC/array-as-vcf"
---

## Concepts

- **Tool Overview**: array-as-vcf converts SNP array data to standard VCF (Variant Call Format) for compatibility with downstream bioinformatics tools. Version 1.1.0.
- **Core Function**: Transforms proprietary SNP array formats into standardized VCF format for variant analysis and comparison.
- **Array Support**: Supports multiple SNP array platforms (Illumina, Affymetrix, etc.) with proper genotype encoding.
- **VCF Compliance**: Generates VCF files compliant with VCF specification for tool interoperability.
- **Genotype Encoding**: Converts array genotypes to VCF genotype fields with proper phasing information.
- **Quality Scores**: Includes quality metrics from array platform in VCF INFO fields.
- **Input/Output**: Accepts SNP array data files and outputs VCF format variant calls.
- **Installation**: `conda install -c bioconda array-as-vcf` or install from GitHub.

## Pitfalls

- **Platform Specificity**: Different array platforms require specific configuration. Check platform compatibility.
- **Reference Genome**: Requires matching reference genome build (e.g., hg19, hg38). Incorrect build causes coordinate mismatches.
- **Genotype Encoding**: Array genotypes may use different encoding schemes. Verify conversion accuracy.
- **Missing Data**: Array platforms may have different missing data conventions. Handle appropriately.
- **Quality Metrics**: Array quality scores may not directly translate to VCF QUAL fields.

## Examples

### Display help
**Args:** `array-as-vcf --help`
**Explanation:** Shows all available command-line options and usage information.

### Convert Illumina array
**Args:** `array-as-vcf --platform illumina --input array_data.txt --output variants.vcf`
**Explanation:** Converts Illumina SNP array data to VCF format.

### Convert Affymetrix array
**Args:** `array-as-vcf --platform affymetrix --input array_data.txt --output variants.vcf`
**Explanation:** Converts Affymetrix SNP array data to VCF format.

### Specify reference genome
**Args:** `array-as-vcf --platform illumina --input array_data.txt --reference hg38 --output variants.vcf`
**Explanation:** Specifies reference genome build (hg38) for coordinate system.

### Include quality metrics
**Args:** `array-as-vcf --platform illumina --input array_data.txt --include-quality --output variants.vcf`
**Explanation:** Includes array quality metrics in VCF INFO fields.

### Filter by call rate
**Args:** `array-as-vcf --platform illumina --input array_data.txt --min-callrate 0.95 --output filtered.vcf`
**Explanation:** Filters SNPs with minimum 95% call rate.

### Batch conversion
**Args:** `array-as-vcf batch --input_dir array_files/ --output_dir vcf_files/ --platform illumina`
**Explanation:** Converts multiple array files in batch mode.