---
name: needlr
category: variant-calling
description: needLR compares query structural variant VCFs to 1000 Genomes Project samples sequenced by Oxford Nanopore long-read sequencing.
tags: [needlr, variant-calling, sv, nanopore, long-reads]
author: oxo-call-community
source_url: "https://github.com/millerlaboratory/needLR"
---

## Concepts

- **Tool Overview**: needLR is a command-line tool for comparing structural variant VCFs against 1000 Genomes Project long-read sequencing data.
- **Core Function**: Uses Truvari merging to compare query SV calls with reference population data.
- **Algorithm**: Leverages Truvari for variant comparison and merging operations.
- **Input Format**: Accepts VCF files containing structural variant calls.
- **Output**: Produces comparison reports and filtered variant sets.
- **Use Case**: Structural variant validation, population genetics analysis, variant filtering.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Quality**: Performance depends on input VCF quality.
- **Reference Data**: Requires access to 1000 Genomes Project reference data.
- **Memory Usage**: Processing large VCF files requires significant memory.
- **Truvari Dependency**: Requires Truvari installation.
- **Format Compatibility**: VCF must follow standard structural variant conventions.

## Examples

### Display help
**Args:** `needlr --help`
**Explanation:** Shows available options and usage instructions.

### Compare SV VCF
**Args:** `needlr compare -i query.vcf -r reference.vcf -o comparison/`
**Explanation:** Compares query SV calls against reference VCF.

### Merge variants
**Args:** `needlr merge -i query.vcf -d database/ -o merged.vcf`
**Explanation:** Merges query variants with population database.

### Filter variants
**Args:** `needlr filter -i input.vcf -c 1000g -o filtered.vcf`
**Explanation:** Filters variants based on 1000 Genomes frequency.

### Generate report
**Args:** `needlr report -i query.vcf -r reference.vcf -o report.html`
**Explanation:** Generates HTML comparison report.

### Benchmark mode
**Args:** `needlr benchmark -i truth.vcf -q query.vcf -o results/`
**Explanation:** Runs benchmarking analysis for SV calls.

### Threads
**Args:** `needlr compare -i query.vcf -r ref.vcf -t 8 -o output/`
**Explanation:** Uses 8 threads for parallel processing.