---
name: mmannot
category: alignment
description: mmannot annotates reads, or quantifies the features. mmannot takes special care of multi-mapping reads.
tags: [mmannot, alignment, annotation]
author: oxo-call-community
source_url: "https://github.com/mzytnicki/mmannot"
---

## Concepts

- **Tool Overview**: mmannot v1.1 annotates reads and quantifies features.
- **Core Function**: Handles multi-mapping reads for accurate annotation.
- **Multi-mapping Handling**: Special care for reads mapping to multiple locations.
- **Feature Quantification**: Quantifies gene expression levels.
- **Input/Output**: Accepts alignments; outputs annotations.
- **RNA-seq Analysis**: Supports RNA-seq quantification workflows.

## Pitfalls

- **Alignment Required**: Requires aligned reads as input.
- **Computational Resources**: Processing may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal quantification.
- **Data Quality**: Results depend on alignment quality.
- **Annotation Dependence**: Requires gene annotations.

## Examples

### Annotate reads
**Args:** `mmannot -i alignments.bam -a annotation.gtf -o annotations.txt`
**Explanation:** Annotates aligned reads.

### Quantify features
**Args:** `mmannot -i alignments.bam -a annotation.gtf -q -o counts.txt`
**Explanation:** Quantifies gene expression.

### Handle multi-mapping
**Args:** `mmannot -i alignments.bam -a annotation.gtf -m -o annotations.txt`
**Explanation:** Special handling for multi-mapping reads.

### Batch processing
**Args:** `mmannot -i bam/ -a annotation.gtf -o results/`
**Explanation:** Processes multiple BAM files.

### Generate report
**Args:** `mmannot -i alignments.bam -a annotation.gtf -r report.html`
**Explanation:** Generates annotation report.