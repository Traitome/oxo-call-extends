---
name: mintie
category: expression
description: Method for Identifying Novel Transcripts and Isoforms using Equivalence classes, in cancer and rare disease.
tags: [mintie, expression, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/Oshlack/MINTIE"
---

## Concepts

- **Tool Overview**: MINTIE v0.4.3 identifies novel transcripts and isoforms.
- **Core Function**: Detects novel transcripts from RNA-seq data.
- **Equivalence Classes**: Uses equivalence class approach for transcript discovery.
- **Novel Isoforms**: Identifies previously unannotated transcript isoforms.
- **Input/Output**: Accepts RNA-seq alignments; outputs transcript predictions.
- **Cancer Transcriptomics**: Supports cancer and rare disease research.

## Pitfalls

- **RNA-seq Specific**: Designed for RNA-seq data analysis.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal discovery.
- **Data Quality**: Results depend on input data quality.
- **Annotation Dependence**: Relies on existing transcript annotations.

## Examples

### Identify novel transcripts
**Args:** `mintie -i alignments.bam -g genome.fasta -a annotation.gtf -o novel_transcripts.gtf`
**Explanation:** Identifies novel transcripts from RNA-seq data.

### With custom parameters
**Args:** `mintie -i alignments.bam -g genome.fasta -a annotation.gtf -o novel_transcripts.gtf -t 0.5`
**Explanation:** Uses custom expression threshold.

### Cancer-specific analysis
**Args:** `mintie -i tumor.bam -g genome.fasta -a annotation.gtf -o cancer_transcripts.gtf -c`
**Explanation:** Optimized for cancer transcriptomics.

### Batch processing
**Args:** `mintie -i bam/ -g genome.fasta -a annotation.gtf -o results/`
**Explanation:** Processes multiple BAM files.

### Generate statistics
**Args:** `mintie -i alignments.bam -g genome.fasta -a annotation.gtf -o novel_transcripts.gtf -s stats.txt`
**Explanation:** Generates transcript discovery statistics.