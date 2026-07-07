---
name: cdna_cupcake
category: transcriptomics
description: Collection of Python and R scripts for analyzing sequencing data, especially Iso-Seq
tags: [cdna_cupcake, transcriptomics, iso-seq, sequencing-analysis, python]
author: oxo-call-community
source_url: "https://github.com/Magdoll/cDNA_Cupcake"
---

## Concepts

- **Tool Overview**: cDNA_Cupcake provides scripts for analyzing sequencing data, particularly Iso-Seq data processing.
- **Core Function**: Tools for Iso-Seq data analysis including cluster analysis, polishing, and visualization.
- **Scripts Included**: collapse_isoforms_by_sam.py, filter_by_count.py, ice_fusion_finder.py, and more.
- **Input**: Iso-Seq sequencing data in various formats (BAM, FASTA, FASTQ).
- **Output**: Processed isoforms, cluster reports, and visualization files.
- **Application**: Isoform-level transcriptomics analysis from PacBio sequencing.
- **Installation**: Install via bioconda: `conda install -c bioconda cdna_cupcake`

## Pitfalls

- **Iso-Seq Specific**: Primarily designed for PacBio Iso-Seq data.
- **Python/R Dependencies**: Requires Python and R environments.
- **Memory Usage**: Large datasets may require significant memory.
- **Quality Filtering**: Raw data should be pre-filtered for best results.

## Examples

### Collapse isoforms by SAM
**Args:** `collapse_isoforms_by_sam.py --input isoforms.fasta --sam alignments.sam --output collapsed/`
**Explanation:** Collapses redundant isoforms based on SAM alignment.

### Filter by read count
**Args:** `filter_by_count.py -i isoforms.fasta -c counts.txt -o filtered.fasta -m 2`
**Explanation:** Filters isoforms with minimum 2 supporting reads.

### Find fusion transcripts
**Args:** `ice_fusion_finder.py -i input.fasta -o fusions.txt`
**Explanation:** Identifies potential fusion transcripts from Iso-Seq data.

### Display help
**Args:** `collapse_isoforms_by_sam.py --help`
**Explanation:** Shows available options for isoform collapsing.