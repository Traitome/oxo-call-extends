---
name: pyloh
category: utility
description: pyLOH deconvolves tumor purity and ploidy by integrating copy number alterations and loss of heterozygosity.
tags: [pyloh, utility, tumor, copy-number]
author: oxo-call-community
source_url: "https://github.com/uci-cbcl/PyLOH"
---

## Concepts

- **Tool Overview**: pyloh analyzes LOH in tumors.
- **Core Function**: Tumor purity/ploidy estimation.
- **Algorithm**: Uses statistical modeling.
- **Input Format**: Accepts VCF/BAM files.
- **Output**: Produces purity estimates.
- **Use Case**: Cancer genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large data requires memory.
- **Data Quality**: Results depend on input quality.
- **Tumor Content**: Affects accuracy.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyloh --help`
**Explanation:** Shows available options and usage instructions.

### Run LOH analysis
**Args:** `pyloh analyze -i tumor.bam -n normal.bam -r reference.fasta -o results/`
**Explanation:** Performs LOH analysis.

### With parameters
**Args:** `pyloh analyze -i tumor.bam -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyloh -v analyze -i tumor.bam -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyloh -t 4 analyze -i tumor.bam -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Plot results
**Args:** `pyloh plot -i results/ -o loh_plot.png`
**Explanation:** Generates LOH plot.

### Generate report
**Args:** `pyloh analyze -i tumor.bam -o results/ --report report.html`
**Explanation:** Generates HTML report.