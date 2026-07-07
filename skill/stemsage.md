---
name: stemsage
category: rna-analysis
description: Uncovering Stem-loop Motifs from RBP Binding Regions.
tags: [stemsage, rna-structure, rbp-binding, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/PrinceWang2018/stemsage"
---

## Concepts

- **Tool Overview**: stemsage (v0.8.8) is a tool for identifying stem-loop RNA motifs within RNA-binding protein (RBP) binding regions.
- **Core Function**: Predicts and analyzes stem-loop secondary structures enriched in RBP binding sites.
- **Algorithm**: Combines RNA secondary structure prediction with motif enrichment analysis.
- **Input/Output**: Input: RBP binding peaks (BED/BAM), RNA sequences; Output: Stem-loop motifs with enrichment statistics.
- **Applications**: Studying RBP-RNA interactions and regulatory mechanisms.
- **Installation**: `conda install -c bioconda stemsage` or `pip install stemsage`.

## Pitfalls

- **Sequence Quality**: Low-quality sequences affect structure prediction.
- **Binding Site Quality**: Poor ChIP-seq/CLIP-seq peaks produce false motifs.
- **Genome Version**: Incorrect genome assembly affects sequence retrieval.
- **Parameter Tuning**: Incorrect stem-loop parameters miss true motifs.
- **Multiple Testing**: Failure to correct for multiple testing produces false positives.
- **Computational Time**: Large datasets require significant computational resources.

## Examples

### Display help
**Args:** `stemsage --help`
**Explanation:** Shows available options and usage information.

### Basic motif discovery
**Args:** `stemsage -i peaks.bed -g genome.fasta -o motifs.txt`
**Explanation:** Discover stem-loop motifs in RBP binding regions.

### With custom parameters
**Args:** `stemsage -i peaks.bed -g genome.fasta -o motifs.txt -m 5 -M 20`
**Explanation:** Set minimum stem length to 5 and maximum to 20.

### Verbose mode
**Args:** `stemsage -i peaks.bed -g genome.fasta -o motifs.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `stemsage -i peaks.bed -g genome.fasta -o motifs.txt --plot`
**Explanation:** Generate visualization of discovered motifs.

### Statistical testing
**Args:** `stemsage -i peaks.bed -g genome.fasta -o motifs.txt --test`
**Explanation:** Perform statistical enrichment testing for motifs.

### Batch processing
**Args:** `stemsage -i batch/ -g genome.fasta -o results/`
**Explanation:** Process multiple peak files together.

### Filter by significance
**Args:** `stemsage -i peaks.bed -g genome.fasta -o motifs.txt -p 0.05`
**Explanation:** Filter motifs by p-value threshold of 0.05.

### Export to GFF
**Args:** `stemsage -i peaks.bed -g genome.fasta -o motifs.gff --gff`
**Explanation:** Output stem-loop positions in GFF format.
