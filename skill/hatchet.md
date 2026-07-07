---
name: hatchet
category: bioinformatics
description: HATCHet infers allele and clone-specific copy-number aberrations (CNAs) from sequencing data.
tags: [hatchet, copy-number, CNAs, bioinformatics]
author: oxo-call-community
source_url: "https://raphael-group.github.io/hatchet"
---

## Concepts

- **Copy-Number Aberrations**: HATCHet detects CNAs in genomic data.

- **Allele-Specific**: Considers allele-specific copy numbers.

- **Clone-Specific**: Identifies clone-specific CNAs.

- **Cancer Genomics**: Specialized for cancer genome analysis.

- **Segmentation**: Performs genomic segmentation.

- **Copy-Number Profiling**: Profiles copy-number across genome.

## Pitfalls

- **Tumor Purity**: Account for tumor purity in analysis.

- **Sample Heterogeneity**: Complex samples may be challenging.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Parameter Tuning**: Requires careful parameter optimization.

## Examples

### Infer CNAs
**Args:** `hatchet --input bam_files.txt --output cna_results/`
**Explanation:** Infers copy-number aberrations from BAM files.

### Allele-specific analysis
**Args:** `hatchet --input bam_files.txt --allele-specific --output cna_results/`
**Explanation:** Performs allele-specific CNA analysis.

### Batch processing
**Args:** `for sample in samples/*; do hatchet --input $sample/bam.txt --output $sample/cna_results/; done`
**Explanation:** Processes multiple samples.

### Generate report
**Args:** `hatchet --input bam_files.txt --report --output report.html`
**Explanation:** Generates comprehensive analysis report.

### Visualization
**Args:** `hatchet --input bam_files.txt --plot --output plot.pdf`
**Explanation:** Generates visualization of CNA results.

### Help command
**Args:** `hatchet --help`
**Explanation:** Shows available options and usage information.