---
name: estscan
category: qc
description: "Detects coding regions in DNA sequences even if they are of low quality"
tags: [estscan, qc, coding-region-prediction, gene-finding, sequence-analysis]
author: oxo-call-community
source_url: "http://estscan.sourceforge.net"
---

## Concepts

- **Tool Overview**: ESTScan is a tool for detecting coding regions in DNA sequences, particularly effective for low-quality sequences such as expressed sequence tags (ESTs).
- **Core Function**: Identifies potential protein-coding regions by analyzing codon usage patterns and statistical characteristics of coding sequences.
- **Input/Output**: Input: DNA sequences (FASTA). Output: Predicted coding regions (FASTA, GFF), coding potential scores.
- **Algorithm**: Uses Markov models and codon usage statistics to distinguish coding from non-coding sequences.
- **Key Features**: Low-quality sequence tolerance, coding region prediction, frame detection, codon usage analysis, batch processing.
- **Installation**: `conda install -c bioconda estscan`

## Pitfalls

- **Species Specificity**: Codon usage models may need species-specific training.
- **Sequence Length**: Short sequences may produce unreliable predictions.
- **Frame Detection**: May incorrectly predict reading frames for fragmented sequences.
- **Parameter Tuning**: Default parameters may need adjustment for specific organisms.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic coding region prediction
**Args:** `estscan -i dna.fasta -o coding_regions.fasta`
**Explanation:** Predicts coding regions from DNA sequences.

### Output GFF format
**Args:** `estscan -i dna.fasta -g -o coding_regions.gff`
**Explanation:** Outputs predictions in GFF format.

### With training file
**Args:** `estscan -i dna.fasta -t training.txt -o coding_regions.fasta`
**Explanation:** Uses custom training file for codon usage.

### Frame detection
**Args:** `estscan -i dna.fasta -f -o frames.txt`
**Explanation:** Determines reading frame for each prediction.

### Batch processing
**Args:** `estscan -i sequences/ -o results/ --batch`
**Explanation:** Processes multiple sequence files in batch mode.