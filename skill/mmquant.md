---
name: mmquant
category: alignment
description: RNA-Seq quantification tool, with special handling on multi-mapping reads.
tags: [mmquant, alignment, rna-seq]
author: oxo-call-community
source_url: "https://bitbucket.org/mzytnicki/multi-mapping-counter/"
---

## Concepts

- **Tool Overview**: mmquant v1.0.9 is an RNA-Seq quantification tool.
- **Core Function**: Quantifies gene expression from RNA-Seq data.
- **Multi-mapping Handling**: Special handling for reads mapping to multiple locations.
- **Expression Quantification**: Counts reads per gene/transcript.
- **Input/Output**: Accepts aligned reads; outputs expression counts.
- **RNA-seq Analysis**: Supports gene expression analysis workflows.

## Pitfalls

- **Alignment Required**: Requires aligned reads as input.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal quantification.
- **Data Quality**: Results depend on alignment quality.
- **Annotation Dependence**: Requires gene annotations.
- **Computational Resources**: Quantification may require significant resources.

## Examples

### Quantify expression
**Args:** `mmquant -i alignments.bam -a annotation.gtf -o counts.txt`
**Explanation:** Quantifies gene expression from aligned reads.

### Handle multi-mapping
**Args:** `mmquant -i alignments.bam -a annotation.gtf -m -o counts.txt`
**Explanation:** Special handling for multi-mapping reads.

### With strand-specific data
**Args:** `mmquant -i alignments.bam -a annotation.gtf -s reverse -o counts.txt`
**Explanation:** Handles strand-specific RNA-seq data.

### Output in different formats
**Args:** `mmquant -i alignments.bam -a annotation.gtf -f tsv -o counts.tsv`
**Explanation:** Outputs counts in TSV format.

### Batch processing
**Args:** `mmquant -i bam/ -a annotation.gtf -o results/`
**Explanation:** Processes multiple BAM files.