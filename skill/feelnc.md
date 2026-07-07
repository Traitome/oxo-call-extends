---
name: feelnc
category: utility
description: "FlExible Extraction of LncRNA"
tags: [feelnc, utility, lncRNA, non-coding-RNA, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/tderrien/FEELnc"
---

## Concepts

- **Tool Overview**: FEELnc (FlExible Extraction of LncRNA) is a tool for extracting and classifying long non-coding RNAs (lncRNAs) from transcriptome data.
- **Core Function**: Identifies and classifies lncRNA transcripts from RNA-seq data.
- **Input/Output**: Input: Transcriptome assembly (GTF/GFF). Output: lncRNA annotations, classification results.
- **Algorithm**: Uses machine learning and sequence features for lncRNA identification.
- **Key Features**: Flexible lncRNA extraction, lncRNA classification, antisense lncRNA detection, tissue-specific analysis, protein-coding potential assessment.
- **Installation**: `conda install -c bioconda feelnc`

## Pitfalls

- **Annotation Quality**: Requires high-quality transcriptome annotation.
- **Transcript Assembly**: Results depend on transcript assembly quality.
- **Training Data**: Classifier performance depends on training data.
- **Memory Usage**: Large datasets may require significant memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic lncRNA extraction
**Args:** `feelnc -i transcripts.gtf -o lncRNA_results/`
**Explanation:** Extracts lncRNAs from transcriptome.

### With classification
**Args:** `feelnc -i transcripts.gtf -o lncRNA_results/ --classify`
**Explanation:** Classifies extracted lncRNAs.

### Antisense detection
**Args:** `feelnc -i transcripts.gtf -o lncRNA_results/ --detect-antisense`
**Explanation:** Detects antisense lncRNAs.

### Training model
**Args:** `feelnc -i transcripts.gtf -o lncRNA_results/ --train-model`
**Explanation:** Trains classifier on data.

### Tissue-specific lncRNAs
**Args:** `feelnc -i transcripts.gtf -o lncRNA_results/ --tissue-analysis`
**Explanation:** Analyzes tissue-specific expression.