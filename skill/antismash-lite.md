---
name: antismash-lite
category: annotation
description: antiSMASH-lite - lightweight version of antibiotics and Secondary Metabolite Analysis SHell for rapid identification of secondary metabolite biosynthetic gene clusters
tags: [antismash-lite, antiSMASH, BGC, biosynthetic-gene-cluster, secondary-metabolite, genome-mining, antibiotics]
author: oxo-call-community
source_url: "https://docs.antismash.secondarymetabolites.org"
---

## Concepts

- **Tool Overview**: antiSMASH-lite (v8.0.1) - A lightweight version of antiSMASH for rapid genome-wide identification and annotation of secondary metabolite biosynthetic gene clusters (BGCs).
- **Core Function**: Identifies and annotates secondary metabolite biosynthesis gene clusters in bacterial and fungal genomes using profile hidden Markov models (HMMs).
- **Key Features**:
  - **BGC Detection**: Identifies all known classes of secondary metabolite gene clusters
  - **Supported Classes**: Polyketides (PKS), non-ribosomal peptides (NRPS), terpenes, aminoglycosides, lantibiotics, bacteriocins, siderophores, and many more
  - **ClusterBlast**: Compares identified clusters against known clusters in databases
  - **SubclusterBlast**: Identifies conserved subclusters involved in building block biosynthesis
  - **Input Formats**: GenBank (.gbk), EMBL (.embl), FASTA (.fasta, .fna)
  - **Output Formats**: HTML visualization, GenBank, JSON, and detailed annotation files
- **Installation**: `conda install -c bioconda antismash-lite`

## Pitfalls

- **Sequence Length**: Works best with well-assembled sequences; fragmented assemblies may miss complete clusters
- **Database Requirements**: Requires database download before first use
- **Computational Resources**: Large genomes may require significant memory and processing time
- **Annotation Quality**: FASTA input relies on Prodigal for gene prediction; pre-annotated GenBank/EMBL files recommended
- **Cluster Boundaries**: Predicted boundaries may need manual curation

## Examples

### Basic analysis
**Args:** `antismash genome.fasta --output results/`
**Explanation:** Runs basic antiSMASH analysis on a FASTA file and outputs results to the results directory.

### Full-featured run
**Args:** `antismash --cb-general --cb-knownclusters --cb-subclusters --asf --pfam2go genome.gbk -o results/`
**Explanation:** Runs comprehensive analysis with ClusterBlast against general and known clusters, SubclusterBlast, active site finding, and Pfam2GO mapping.

### With pre-computed gene predictions
**Args:** `antismash --genefinding-tool none annotated.gbk -o results/`
**Explanation:** Skips gene finding (uses existing annotations in GenBank file).

### Minimal run for quick screening
**Args:** `antismash --minimal genome.fasta -o quick_results/`
**Explanation:** Runs minimal analysis for rapid screening without ClusterBlast comparisons.

### Batch processing multiple genomes
**Args:** `for file in *.fasta; do antismash "$file" -o results/"${file%.fasta}"; done`
**Explanation:** Processes all FASTA files in a directory with individual output directories.

### Download databases
**Args:** `download-antismash-databases`
**Explanation:** Downloads required databases (run once before first use).