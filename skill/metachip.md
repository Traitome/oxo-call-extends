---
name: metachip
category: utility
description: HGT detection pipeline
tags: [metachip, utility, HGT, horizontal-gene-transfer, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/songweizhi/MetaCHIP"
---

## Concepts

- **Tool Overview**: MetaCHIP v1.10.13 is a comprehensive pipeline for detecting Horizontal Gene Transfer (HGT) events between microbial genomes.
- **Core Function**: Identifies potential HGT events by comparing genomic sequences and detecting anomalous patterns that suggest horizontal transfer.
- **Phylogenetic Analysis**: Uses phylogenetic trees to identify genes with evolutionary histories inconsistent with their host genome.
- **GC Content Analysis**: Detects regions with unusual GC content that may indicate foreign DNA acquisition.
- **Input/Output**: Accepts genome sequences in FASTA format; outputs HGT predictions with confidence scores and annotations.
- **Integration**: Combines multiple methods (phylogenetic, compositional, and syntenic) for robust HGT detection.

## Pitfalls

- **False Positives**: May detect false HGT events due to incomplete reference databases.
- **Phylogenetic Resolution**: Requires sufficient phylogenetic signal for accurate detection.
- **Computational Resources**: Large datasets may require significant computational resources.
- **Annotation Quality**: Depends on accurate gene annotations for reliable results.
- **Horizontal Gene Transfer vs. Vertical Inheritance**: Distinguishing between true HGT and other evolutionary processes can be challenging.
- **Database Completeness**: Reference database quality directly impacts detection accuracy.

## Examples

### Run HGT detection
**Args:** `MetaCHIP PI -i genomes/ -o hgt_results/`
**Explanation:** Runs the HGT detection pipeline on input genomes.

### With custom reference
**Args:** `MetaCHIP PI -i genomes/ -r reference.fasta -o hgt_results/`
**Explanation:** Uses a custom reference genome for comparison.

### Run with phylogenetic analysis
**Args:** `MetaCHIP PI -i genomes/ -p -o hgt_results/`
**Explanation:** Enables phylogenetic analysis for HGT detection.

### Specify output format
**Args:** `MetaCHIP PI -i genomes/ -o hgt_results/ -f csv`
**Explanation:** Outputs results in CSV format.

### Run with increased threads
**Args:** `MetaCHIP PI -i genomes/ -o hgt_results/ -t 8`
**Explanation:** Uses 8 threads for parallel processing.