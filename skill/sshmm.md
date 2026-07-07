---
name: sshmm
category: rna-seq
description: ssHMM is an RNA motif finder that recovers sequence-structure motifs from RNA-binding protein data.
tags: [sshmm, rna-motif, clip-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.molgen.mpg.de/heller/ssHMM"
---

## Concepts

- **Tool Overview**: sshmm (v1.0.7) is a hidden Markov model-based tool for discovering RNA sequence-structure motifs from CLIP-Seq data.
- **Core Function**: Identifies conserved RNA motifs with associated secondary structures bound by RNA-binding proteins.
- **Algorithm**: Uses profile hidden Markov models (pHMMs) with structure constraints for motif discovery.
- **Input/Output**: Input: CLIP-Seq peaks or RNA sequences; Output: Consensus motifs with secondary structure predictions.
- **Structure Integration**: Combines sequence conservation with predicted RNA secondary structure.
- **Installation**: Download from GitHub repository and compile from source.

## Pitfalls

- **Input Quality**: Low-quality CLIP-Seq data leads to unreliable motif discovery.
- **Motif Complexity**: Highly degenerate motifs may not be recovered with default parameters.
- **Structure Prediction**: Incorrect secondary structure predictions affect motif accuracy.
- **False Positives**: Background sequences can produce spurious motifs.
- **Parameter Tuning**: Requires careful adjustment of HMM parameters for optimal results.
- **Computational Time**: Motif discovery for large datasets can be computationally intensive.

## Examples

### Display help
**Args:** `sshmm --help`
**Explanation:** Shows available options and usage information.

### Basic motif discovery
**Args:** `sshmm -i peaks.fasta -o motifs.txt`
**Explanation:** Discover RNA motifs from CLIP-Seq peaks.

### With structure prediction
**Args:** `sshmm -i peaks.fasta -o motifs.txt --structure`
**Explanation:** Enable RNA secondary structure prediction during motif discovery.

### Specify motif width
**Args:** `sshmm -i peaks.fasta -o motifs.txt -w 15`
**Explanation:** Set expected motif width to 15 nucleotides.

### Background correction
**Args:** `sshmm -i peaks.fasta -b background.fasta -o motifs.txt`
**Explanation:** Use background sequences for statistical significance calculation.

### Multiple iterations
**Args:** `sshmm -i peaks.fasta -o motifs.txt -n 5`
**Explanation:** Run 5 iterations of motif refinement.

### Output logo
**Args:** `sshmm -i peaks.fasta -o motifs.txt --logo motif_logo.png`
**Explanation:** Generate sequence logo for discovered motifs.

### Verbose mode
**Args:** `sshmm -i peaks.fasta -o motifs.txt --verbose`
**Explanation:** Run with detailed logging for debugging.
