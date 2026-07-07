---
name: funannotate
category: annotation
description: "funannotate: eukaryotic genome annotation pipeline."
tags: [funannotate, genome annotation, eukaryotic, gene prediction]
author: oxo-call-community
source_url: "https://github.com/nextgenusfs/funannotate"
---
## Concepts
- **Eukaryotic Annotation**: Pipeline for annotating eukaryotic genomes.
- **Gene Structure Prediction**: Predicts gene structures including exons and introns.
- **Non-coding RNA**: Identifies non-coding RNA genes.
- **GO Terms**: Assigns Gene Ontology terms to genes.
- **Comparative Annotation**: Uses comparative genomics for improved annotation.

## Pitfalls
- **Complex Setup**: Requires multiple dependencies and database setup.
- **Long Runtime**: Annotation of large genomes can be time-consuming.
- **Resource Intensive**: High CPU and memory requirements.
- **Database Updates**: Requires regular database updates for accurate annotations.
- **Expertise Required**: Requires knowledge of bioinformatics for optimal use.

## Examples
### Initialize annotation project
**Args:** `funannotate init -i genome.fasta -o project/`
**Explanation:** Initializes a new annotation project.

### Run annotation pipeline
**Args:** `funannotate annotate -i project/ -o final_annotation/`
**Explanation:** Runs the complete annotation pipeline.

### Predict genes with RNA-seq
**Args:** `funannotate predict -i genome.fasta -r rna_seq.fastq -o predictions.gff`
**Explanation:** Predicts genes using RNA-seq evidence.

### Add functional annotations
**Args:** `funannotate annotate -i project/ --iprscan --go`
**Explanation:** Adds InterProScan and GO term annotations.

### Export results
**Args:** `funannotate export -i project/ -o annotations.gff3`
**Explanation:** Exports annotations in GFF3 format.