---
name: gmap-fusion
category: fusion-transcript
description: gmap-fusion - Identify fusion transcripts from RNA-seq de novo transcriptome assembly.
tags: [gmap-fusion, fusion-transcript, RNA-seq, cancer]
author: oxo-call-community
source_url: "https://github.com/GMAP-fusion/GMAP-fusion/wiki"
---

## Concepts
- **Fusion Detection**: Identifies fusion transcripts.
- **Transcriptome Assembly**: Uses de novo assembly.
- **RNA-seq Analysis**: Analyzes RNA-seq data.
- **Cancer Research**: Important for cancer studies.
- **GMAP Integration**: Uses GMAP for alignment.

## Pitfalls
- **Assembly Quality**: Depends on assembly quality.
- **False Positives**: May have false positives.
- **Read Coverage**: Low coverage affects detection.
- **Validation**: Results require validation.
- **Computational Resources**: Requires resources.

## Examples
### Identify fusions
**Args:** `gmap-fusion -i transcripts.fasta -o fusions.txt`
**Explanation:** Identifies fusion transcripts.

### With reference
**Args:** `gmap-fusion -i transcripts.fasta -g genome -o fusions.txt`
**Explanation:** Uses reference genome.

### Filter results
**Args:** `gmap-fusion -i transcripts.fasta -r 0.1 -o fusions.txt`
**Explanation:** Uses support ratio filter.

### Generate report
**Args:** `gmap-fusion -i transcripts.fasta -o fusions.txt -report`
**Explanation:** Generates fusion report.

### Batch processing
**Args:** `gmap-fusion -l samples.txt -o ./fusions/`
**Explanation:** Processes multiple samples.