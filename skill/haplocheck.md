---
name: haplocheck
category: bioinformatics
description: HaploCheck detects in-sample contamination in mtDNA or WGS sequencing studies by analyzing mitochondrial content.
tags: [haplocheck, contamination-detection, mtDNA, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/genepi/haplocheck"
---

## Concepts

- **Contamination Detection**: HaploCheck detects sample contamination.

- **mtDNA Analysis**: Analyzes mitochondrial DNA content.

- **WGS Data**: Works with whole-genome sequencing data.

- **Heteroplasmy Detection**: Identifies mitochondrial heteroplasmy.

- **Quality Control**: Provides QC metrics for sequencing data.

- **Sample Validation**: Validates sample integrity.

## Pitfalls

- **mtDNA Coverage**: Requires sufficient mtDNA coverage.

- **Reference Genome**: Ensure compatibility with reference genome.

- **Contamination Level**: Very low contamination may be missed.

- **Data Quality**: Results depend on sequencing data quality.

- **Interpretation**: Carefully interpret contamination results.

## Examples

### Detect contamination
**Args:** `haplocheck -i input.bam -o contamination.txt`
**Explanation:** Detects contamination in sequencing data.

### With reference
**Args:** `haplocheck -i input.bam -r reference.fasta -o contamination.txt`
**Explanation:** Uses custom reference genome.

### mtDNA specific
**Args:** `haplocheck -i input.bam -m -o contamination.txt`
**Explanation:** Focuses on mitochondrial DNA analysis.

### Batch processing
**Args:** `for f in *.bam; do haplocheck -i $f -o ${f%.bam}_contamination.txt; done`
**Explanation:** Processes multiple BAM files.

### Generate report
**Args:** `haplocheck -i input.bam -report -o report.html`
**Explanation:** Generates comprehensive QC report.

### Visualization
**Args:** `haplocheck -i input.bam -plot -o plot.pdf`
**Explanation:** Generates visualization of contamination results.

### Help command
**Args:** `haplocheck --help`
**Explanation:** Shows available options and usage information.