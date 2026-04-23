---
name: biopet-basecounter
category: expression
description: Count bases from genes and transcripts in exonic/intronic regions
tags: [rna-seq, base-counting, gene-expression]
author: oxo-call-community
source_url: "https://github.com/biopet/basecounter"
---

## Concepts
- **Tool Overview**: BaseCounter counts bases from genes and transcripts, reporting counts in exonic/intronic regions and sense/antisense strands.
- **Strand-Specific**: Reports sense and antisense strand counts separately.
- **Region Types**: Distinguishes exonic, intronic, and other genomic regions.
- **Applications**: RNA-seq quality control, gene body coverage analysis, strand specificity assessment.

## Pitfalls
- **Annotation Requirement**: Requires properly formatted GTF/GFF annotation file.
- **BAM Requirements**: BAM file must be aligned to same reference as annotation.

## Examples
### Count bases in genes
**Args:** `java -jar BaseCounter.jar -I aligned.bam -R annotation.gtf -o base_counts.tsv`
**Explanation:** Counts bases in exonic and intronic regions for each gene.
