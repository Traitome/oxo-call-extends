---
name: mirfix
category: alignment
description: MIRfix automatically curates miRNA datasets by improving alignments of their precursors, the consistency of the annotation of mature miR and miR* sequence, and the phylogenetic coverage. MIRfix produces alignments that are comparable across families and sets the stage for improved homology search as well as quantitative analyses.
tags: [mirfix, alignment, microrna]
author: oxo-call-community
source_url: "https://github.com/Bierinformatik/MIRfix"
---

## Concepts

- **Tool Overview**: MIRfix v2.1.1 curates and improves miRNA dataset alignments.
- **Core Function**: Improves miRNA precursor alignments and annotations.
- **Alignment Improvement**: Refines multiple sequence alignments of miRNAs.
- **Annotation Consistency**: Ensures consistent annotation of mature sequences.
- **Input/Output**: Accepts miRNA alignments; outputs curated datasets.
- **Phylogenetic Analysis**: Supports comparative miRNA genomics.

## Pitfalls

- **miRNA Specific**: Designed for miRNA data curation.
- **Computational Resources**: Processing large alignments may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Results depend on input alignment quality.
- **Phylogenetic Coverage**: Requires adequate taxonomic sampling.

## Examples

### Curate miRNA dataset
**Args:** `mirfix -i input_alignment.fasta -o curated_alignment.fasta`
**Explanation:** Improves miRNA precursor alignments.

### With reference
**Args:** `mirfix -i input_alignment.fasta -r reference.fasta -o curated_alignment.fasta`
**Explanation:** Uses reference sequence for alignment improvement.

### Detailed output
**Args:** `mirfix -i input_alignment.fasta -o curated_alignment.fasta -v`
**Explanation:** Generates detailed curation report.

### Batch processing
**Args:** `mirfix -i alignments/ -o curated/`
**Explanation:** Processes multiple alignment files.

### Generate statistics
**Args:** `mirfix -i input_alignment.fasta -o curated_alignment.fasta -s stats.txt`
**Explanation:** Generates curation statistics.