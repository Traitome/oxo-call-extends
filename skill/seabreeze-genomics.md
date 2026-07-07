---
name: seabreeze-genomics
category: variant-analysis
description: seabreeze-genomics - Analyzing Structural Variation Between Bacterial Genome Assemblies
tags: ["seabreeze-genomics", "variant-analysis", "structural-variation", "bacterial-genomics"]
author: oxo-call-community
source_url: "https://barricklab.github.io/seabreeze"
---

## Concepts

- **Tool Overview**: seabreeze-genomics (v1.5.0) analyzes structural variation between bacterial genome assemblies.
- **Core Function**: Identifies and characterizes structural variations in bacterial genomes.
- **Algorithm**: Uses alignment-based approach to detect structural differences.
- **Input/Output**: Accepts genome assemblies and produces variant calls.
- **Bacterial Focus**: Specifically designed for bacterial genome analysis.
- **Applications**: Comparative genomics, evolutionary biology, and strain typing.

## Pitfalls

- **Assembly Quality**: Results depend on input assembly quality.
- **Memory Usage**: High memory requirements for large genomes.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **False Positives**: May incorrectly identify variants.
- **Reference Bias**: Results may be biased by reference genome choice.

## Examples

### Basic analysis
**Args:** `seabreeze analyze -r reference.fasta -q query.fasta -o variants.vcf`
**Explanation:** `-r` reference genome; `-q` query genome; `-o` output VCF.

### With annotation
**Args:** `seabreeze analyze -r reference.fasta -q query.fasta -a annotation.gff -o variants.vcf`
**Explanation:** `-a` specifies annotation file.

### Verbose logging
**Args:** `seabreeze analyze -r reference.fasta -q query.fasta -v -o variants.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `seabreeze analyze -r reference.fasta -q query.fasta -t 8 -o variants.vcf`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Quality filtering
**Args:** `seabreeze analyze -r reference.fasta -q query.fasta -q 20 -o variants.vcf`
**Explanation:** `-q 20` filters variants by quality score.

### Generate report
**Args:** `seabreeze report -i variants.vcf -o report.pdf`
**Explanation:** Generates summary report.

### Help command
**Args:** `seabreeze --help`
**Explanation:** Shows available commands and options.