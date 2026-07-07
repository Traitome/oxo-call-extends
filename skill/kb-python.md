---
name: kb-python
category: expression
description: Wrapper for the kallisto | bustools workflow for single-cell RNA-seq pre-processing.
tags: [kb-python, expression, single-cell, RNA-seq, kallisto, bustools]
author: oxo-call-community
source_url: "https://www.kallistobus.tools"
---

## Concepts

- **Tool Overview**: kb-python (v0.30.1) - Wrapper for kallisto | bustools single-cell RNA-seq workflow.
- **Single-Cell RNA-Seq**: Specialized for single-cell transcriptomics.
- **kallisto Integration**: Uses kallisto for pseudoalignment.
- **bustools Integration**: Uses bustools for unique molecular identifier (UMI) processing.
- **Workflow Automation**: Automates the entire scRNA-seq preprocessing pipeline.
- **Output Formats**: Generates outputs compatible with downstream analysis tools.

## Pitfalls

- **Memory Usage**: Requires significant memory for large datasets.
- **Reference Transcriptome**: Requires complete reference transcriptome.
- **UMI Handling**: Proper UMI handling is critical.
- **Barcode Whitelist**: Requires correct barcode whitelist.
- **Version Compatibility**: kallisto/bustools versions must be compatible.
- **Complexity**: Complex workflow requires understanding of scRNA-seq.

## Examples

### Run standard workflow
**Args:** `kb ref -d human -i index.idx -g t2g.txt`
**Explanation:** Downloads and builds reference index for human.

### Process single-cell data
**Args:** `kb count -i index.idx -g t2g.txt -x 10xv3 -o output/ reads_1.fastq reads_2.fastq`
**Explanation:** Processes 10x Genomics v3 data.

### Custom reference
**Args:** `kb ref -f transcripts.fasta -i index.idx -g t2g.txt`
**Explanation:** Builds index from custom transcriptome.

### Solo mode
**Args:** `kb count -i index.idx -g t2g.txt -x 10xv3 -o output/ --solo reads_1.fastq reads_2.fastq`
**Explanation:** Uses kallisto solo for processing.

### Multi-sample processing
**Args:** `kb count -i index.idx -g t2g.txt -x 10xv3 -o output/ --batch samples.txt`
**Explanation:** Processes multiple samples in batch.

### Generate reports
**Args:** `kb count -i index.idx -g t2g.txt -x 10xv3 -o output/ --report reads.fastq`
**Explanation:** Generates quality control report.