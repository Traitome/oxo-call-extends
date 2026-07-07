---
name: genion
category: structural-variation
description: Genion - Characterizing gene fusions using long transcriptomics reads.
tags: [genion, gene-fusion, long-reads, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/genion"
---

## Concepts
- **Gene Fusion Detection**: Detects gene fusion events from long reads.
- **Long-read Sequencing**: Analyzes long transcriptomic sequencing data.
- **Transcriptomics Analysis**: Analyzes transcriptomic data for fusion events.
- **Structural Variation**: Identifies structural variations in transcripts.
- **Fusion Characterization**: Characterizes fusion breakpoints and sequences.

## Pitfalls
- **Read Quality**: Requires high-quality long-read data.
- **Computational Resources**: Large datasets require significant resources.
- **False Positives**: May detect false fusion events.
- **Alignment Quality**: Depends on accurate read alignment.
- **Validation**: Fusion calls require experimental validation.

## Examples
### Detect gene fusions
**Args:** `genion -i reads.fastq -o fusions.txt`
**Explanation:** Detects gene fusion events from long reads.

### With reference genome
**Args:** `genion -i reads.fastq -r genome.fasta -o fusions.txt`
**Explanation:** Uses reference genome for improved fusion detection.

### Characterize fusions
**Args:** `genion -i reads.fastq -c -o fusion_sequences.fasta`
**Explanation:** Extracts fusion sequences from reads.

### Filter by confidence
**Args:** `genion -i reads.fastq -q 0.95 -o fusions.txt`
**Explanation:** Filters fusions by confidence score.

### Batch processing
**Args:** `genion -i ./fastq_files/ -o ./fusion_results/`
**Explanation:** Processes multiple long-read files in batch.