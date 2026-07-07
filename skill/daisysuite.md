---
name: daisysuite
category: alignment
description: DaisySuite - mapping-based pipeline for HGT detection
tags: [daisysuite, alignment, HGT, horizontal-gene-transfer, phylogeny]
author: oxo-call-community
source_url: "https://gitlab.com/eseiler/DaisySuite"
---

## Concepts

- **Tool Overview**: daisysuite (v1.3.0+) is a mapping-based pipeline for detecting horizontal gene transfer (HGT) events using sequencing data.
- **Core Function**: Identifies HGT candidates by mapping reads and analyzing phylogenetic incongruence.
- **Input/Output**: Input: Genome sequences, sequencing reads. Output: HGT predictions, phylogenetic trees.
- **Algorithm**: Combines read mapping, phylogenetic analysis, and statistical testing for HGT detection.
- **Key Features**: Automated HGT detection, supports multiple genomes, detailed reporting.
- **Installation**: `conda install -c bioconda daisysuite`

## Pitfalls

- **Reference Genomes**: Requires complete reference genomes for accurate mapping.
- **Phylogeny Quality**: HGT detection depends on quality of phylogenetic trees.
- **Coverage Requirements**: Low coverage regions may produce unreliable results.
- **False Positives**: Horizontal transfer between close relatives may be missed.
- **Runtime**: Full analysis can be time-consuming for large datasets.

## Examples

### Detect HGT events
**Args:** `daisysuite -i genomes/ -r reads/ -o hgt_results/`
**Explanation:** Run complete HGT detection pipeline.

### Use pre-built database
**Args:** `daisysuite -i genomes/ -r reads/ -d refdb/ -o results/`
**Explanation:** Run with pre-built reference database.

### Generate report
**Args:** `daisysuite -i genomes/ -r reads/ -o results/ --report`
**Explanation:** Generate detailed HTML report of HGT findings.
