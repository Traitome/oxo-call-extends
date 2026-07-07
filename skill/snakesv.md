---
name: snakesv
category: variant-analysis
description: snakeSV - Flexible Snakemake framework for large-scale structural variant discovery
tags: [snakesv, variant-analysis, structural-variants, snakemake, pipeline]
author: oxo-call-community
source_url: "https://github.com/RajLabMSSM/snakeSV/"
---

## Concepts

- **Tool Overview**: snakesv (v0.8) - A Snakemake-based framework for structural variant (SV) discovery
- **Core Function**: Detects and analyzes structural variants from high-throughput sequencing data
- **Input/Output**: Accepts BAM/CRAM files; outputs VCF files with SV calls
- **Algorithm**: Integrates multiple SV callers for comprehensive variant detection
- **Installation**: `conda install -c bioconda snakesv`
- **Key Features**: Multi-caller integration, flexible configuration, large-scale processing

## Pitfalls

- **Input Requirements**: Requires properly aligned BAM/CRAM files
- **Reference Genome**: Must use compatible reference genome
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory for SV calling
- **Parameter Tuning**: Requires careful parameter adjustment
- **Caller Compatibility**: Different SV callers may have conflicting results

## Examples

### Display help
**Args:** `snakesv --help`
**Explanation:** Shows available options and usage information.

### Run pipeline
**Args:** `snakesv -c config.yaml -o results/`
**Explanation:** Run snakeSV pipeline with config file.

### Dry run
**Args:** `snakesv -c config.yaml --dryrun`
**Explanation:** Perform dry run to check pipeline.

### Specify threads
**Args:** `snakesv -c config.yaml -o results/ -t 8`
**Explanation:** Use 8 threads for parallel processing.

### Resume interrupted run
**Args:** `snakesv -c config.yaml -o results/ --resume`
**Explanation:** Resume previously interrupted pipeline run.

### Generate report
**Args:** `snakesv -c config.yaml -o results/ --report`
**Explanation:** Generate analysis report.

### With custom reference
**Args:** `snakesv -c config.yaml -r custom_reference.fasta -o results/`
**Explanation:** Use custom reference genome.

### Quality control only
**Args:** `snakesv -c config.yaml -o results/ --qc-only`
**Explanation:** Run only quality control steps.