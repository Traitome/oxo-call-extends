---
name: bcftools-gtc2vcf-plugin
category: formatting
description: bcftools-gtc2vcf-plugin - Convert Illumina GTC and Affymetrix array data to VCF
tags: [bcftools-gtc2vcf-plugin, formatting, VCF, Illumina, Affymetrix, array-data]
author: oxo-call-community
source_url: "https://github.com/freeseek/gtc2vcf"
---

## Concepts

- **Tool Overview**: bcftools-gtc2vcf-plugin (v1.22) is a bcftools plugin that converts Illumina GTC (Genotyping Call Format) and Affymetrix array intensity data files into VCF format for variant analysis.
- **Core Function**: Converts array-based genotyping data to standard VCF format for downstream analysis.
- **Illumina GTC Support**: Handles Illumina GTC files containing genotype calls and intensity data.
- **Affymetrix Support**: Supports Affymetrix CEL and CHP files for SNP array data.
- **bcftools Integration**: Works as a plugin for the bcftools suite.
- **Input/Output**: Accepts GTC/CEL/CHP files; outputs VCF files.
- **Installation**: `conda install -c bioconda bcftools-gtc2vcf-plugin`.

## Pitfalls

- **bcftools Dependency**: Requires bcftools to be installed and configured.
- **Array Type**: Different array types require different processing parameters.
- **Reference Genome**: Requires matching reference genome for accurate variant coordinates.
- **Version Compatibility**: Ensure compatibility with bcftools version.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Convert GTC to VCF
**Args:** `bcftools +gtc2vcf -g sample.gtc -s sample_name -r reference.fasta -o output.vcf`
**Explanation:** Converts Illumina GTC file to VCF format.

### Multiple samples
**Args:** `bcftools +gtc2vcf -g sample1.gtc sample2.gtc -s sample1 sample2 -r reference.fasta -o output.vcf`
**Explanation:** Converts multiple GTC files to multi-sample VCF.

### With SNP manifest
**Args:** `bcftools +gtc2vcf -g sample.gtc -m manifest.csv -r reference.fasta -o output.vcf`
**Explanation:** Uses SNP manifest file for variant annotation.

### Affymetrix conversion
**Args:** `bcftools +gtc2vcf -c sample.cel -a chip_type -r reference.fasta -o output.vcf`
**Explanation:** Converts Affymetrix CEL file to VCF.

### Output compressed VCF
**Args:** `bcftools +gtc2vcf -g sample.gtc -r reference.fasta -o output.vcf.gz`
**Explanation:** Outputs compressed VCF file.

### Include intensity data
**Args:** `bcftools +gtc2vcf -g sample.gtc -r reference.fasta -i -o output.vcf`
**Explanation:** Includes intensity data in VCF output.

### Display help
**Args:** `bcftools +gtc2vcf --help`
**Explanation:** Shows all available command-line options and usage information.