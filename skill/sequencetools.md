---
name: sequencetools
category: variant-calling
description: sequencetools - Ancient DNA sequencing data processing tools
tags: ["sequencetools", "variant-calling", "ancient-DNA", "pileup"]
author: oxo-call-community
source_url: "https://github.com/stschiff/sequenceTools"
---

## Concepts

- **Tool Overview**: sequencetools (v1.6.0.0) provides tools for processing ancient DNA sequencing data.
- **Core Function**: Implements pileup-based variant calling for ancient DNA.
- **Algorithm**: Uses Bayesian approach for ancient DNA variant detection.
- **Input/Output**: Accepts BAM files and produces VCF output.
- **Ancient DNA**: Focuses on handling degraded DNA sequences.
- **Applications**: Ancient genomics, evolutionary biology, and paleogenomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Call variants
**Args:** `pileupCaller --bam input.bam --ref reference.fasta --out output.vcf`
**Explanation:** Calls variants from BAM file.

### With quality filter
**Args:** `pileupCaller --bam input.bam --ref reference.fasta -q 30 --out output.vcf`
**Explanation:** `-q 30` minimum quality score.

### Ancient DNA mode
**Args:** `pileupCaller --bam input.bam --ref reference.fasta --ancient --out output.vcf`
**Explanation:** `--ancient` enables ancient DNA specific processing.

### Verbose logging
**Args:** `pileupCaller -v --bam input.bam --ref reference.fasta --out output.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `pileupCaller --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `pileupCaller --version`
**Explanation:** Shows current version.

### Multiple samples
**Args:** `pileupCaller --bam sample1.bam --bam sample2.bam --ref reference.fasta --out output.vcf`
**Explanation:** Processes multiple BAM files.