---
name: hybran
category: annotation
description: Comparative prokaryotic genome annotation
tags: [hybran, genome annotation, prokaryotic, comparative genomics]
author: oxo-call-community
source_url: "https://lpcdrp.gitlab.io/hybran"
---

## Concepts

- **Tool Overview**: Hybran is a hybrid reference-based and ab initio annotation pipeline for prokaryotic genomes.
- **Reference-based Annotation**: Uses RATT (Rapid Annotation Transfer Tool) to transfer annotations from reference genomes based on conserved synteny.
- **Ab Initio Prediction**: Supplements unannotated regions with Prokka for de novo gene prediction.
- **Gene Name Unification**: Clusters coding sequences and assigns reference gene names based on amino acid identity.
- **Multi-genome Support**: Can annotate one or many genomes simultaneously with improved accuracy using multiple references.
- **Installation**: `conda install -c bioconda hybran`

## Pitfalls

- **Reference Quality**: Annotation accuracy depends heavily on the quality of reference annotations.
- **Synteny Requirements**: RATT requires conserved synteny between reference and target genomes.
- **Multiple References**: Including more reference annotations improves accuracy but increases computational time.
- **Output Formats**: Generates both GenBank and GFF formats; ensure compatibility with downstream tools.
- **Gene Fusion Detection**: May detect gene fusions that require manual inspection.
- **Pseudogene Detection**: Pseudogenes identified during annotation require careful interpretation.

## Examples

### Basic annotation with single reference
**Args:** `hybran --genomes target.fasta --references reference.gbk --output results/ --organism "Escherichia coli"`
**Explanation:** Annotates a single genome using a reference annotation.

### Annotate multiple genomes
**Args:** `hybran --genomes genome1.fasta genome2.fasta --references ref1.gbk ref2.gbk --output results/ -n 4`
**Explanation:** Annotates multiple genomes with multiple reference annotations using 4 threads.

### Compare two annotations
**Args:** `hybran compare -a annotation1.gbk -b annotation2.gbk -o comparison/`
**Explanation:** Compares two annotations of the same genome to identify differences.

### Standardize gene names
**Args:** `hybran standardize -i annotated.gbk -o standardized.gbk`
**Explanation:** Removes generic gene names and restores original reference names.

### Process list of genomes
**Args:** `hybran --genomes genomes.fofn --references references/ --output results/`
**Explanation:** Processes multiple genomes listed in a File Of FileNames (FOFN).