---
name: cressent
category: annotation
description: CRESS-DNA Extended aNnotation Toolkit for comprehensive ssDNA virus analysis including dereplication, decontamination, phylogenetics, and recombination detection
tags: [cressent, ssDNA-virus, virus-analysis, phylogenetics, motif-discovery, recombination-detection, CRISPR, stem-loop, viral-annotation, metagenomics]
author: oxo-call-community
source_url: "https://cressent.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: CRESSENT (CRESS-DNA Extended aNnotation Toolkit) v1.0.2 - A comprehensive and modular bioinformatic pipeline for ssDNA virus 'genome-to-analysis' and annotation.
- **Core Function**: Provides an integrated pipeline for ssDNA virus analysis with modules for: (1) Sequence dereplication/clustering, (2) Decontamination (kitome and other contaminants), (3) Phylogenetic analysis, (4) Motif discovery, (5) Stem-loop structure prediction, (6) Recombination detection. Each module can be used independently or in combination.
- **Algorithm**: Integrates multiple bioinformatics tools (BLAST, CD-HIT, MAFFT, IQ-TREE, MEME, etc.) into a modular workflow. Handles the full pipeline from raw sequences to publication-ready analyses.
- **Input**: Metagenomic sequences (FASTA), CAPS/REPS databases for annotation, taxonomy accession tables for custom database building.
- **Output**: Clustered/dereplicated sequences, ANI results, BLAST results, phylogenetic trees (NEWICK), motif annotations, recombination reports, cleaned assemblies.
- **Application**: ssDNA virus discovery in metagenomic data, virus annotation and classification, phylogenetic analysis of viral families, contamination detection in virome samples, comparative genomics of ssDNA viruses.
- **Installation**: `mamba create -n cressent -c bioconda -c conda-forge -c defaults cressent` or `pip install cressent`

## Pitfalls

- **Complex Dependencies**: Requires many dependencies (Bioconductor packages, BLAST, CD-HIT, MAFFT, IQ-TREE, MEME, MCL, etc.) - use conda/mamba to install all at once.
- **Database Download**: Database folders must be downloaded separately from Zenodo. Can also build custom DB using build_db module with taxonomy accession numbers.
- **Python Version**: Requires Python >=3.6 but some dependencies may have version conflicts.
- **Docker Alternative**: Use Docker image `docker pull ricrocha82/cressent` to avoid dependency issues.
- **Memory Usage**: Large-scale analyses may require substantial RAM, especially for phylogenetic tree building with many sequences.
- **Email Required**: Building custom database requires a valid email address for NCBI Entrez queries.

## Examples

### Display help message
**Args:** `cressent --help`
**Explanation:** Show all available commands and modules including cluster, db_builder, hmm, hmm_scan, contamination, annotate, phylogeny, recombination, and visualize.

### Dereplicate/cluster sequences
**Args:** `cressent cluster -i /path/to/sequences.fa -o ./output/cluster --keep_names`
**Explanation:** Cluster metagenomic sequences using CD-HIT and ANI calculations. The --keep_names flag preserves original sequence names (spaces replaced with underscores if not set).

### Build custom database
**Args:** `cressent db_builder -t ./DB/taxonomy_accession_number.csv -l Genus -s "Restivirus" "Lophivirus" -o ./my_DB -e your.email@gmail.com`
**Explanation:** Build a custom database from specific taxonomy groups using NCBI accession numbers. Requires valid email for Entrez queries.

### Detect contamination in samples
**Args:** `cressent contamination -i /path/to/sequences.fa -o ./decontamination_output`
**Explanation:** Screen sequences against contamination databases to identify and remove kitome and other laboratory contaminants from virome samples.

### Phylogenetic analysis
**Args:** `cressent phylogeny -i ./cluster/cluster_sequences.fa -o ./phylogeny_output --tree iqtree`
**Explanation:** Build phylogenetic trees from clustered sequences using IQ-TREE2 with automatic model selection. Supports multiple tree builders.

### Motif discovery
**Args:** `cressent hmm -i ./cluster/cluster_sequences.fa -o ./motif_output --tool meme`
**Explanation:** Discover conserved motifs (e.g., replication proteins, capsid proteins) using MEME or HMMER tools integrated in the pipeline.

### Recombination detection
**Args:** `cressent recombination -i aligned_viruses.fa -o ./recombination_output`
**Explanation:** Screen aligned ssDNA viral genomes for recombination events using 3Seq and GENECONV algorithms. Outputs recombinant domains and breakpoint locations.

### Run visualize module
**Args:** `cressent visualize -i ./phylogeny_output/tree.newick -o ./visualization --format pdf`
**Explanation:** Generate publication-ready visualizations of phylogenetic trees with annotation layers.

### Run full pipeline
**Args:** `cressent cluster -i input.fa -o cluster_out && cressent phylogeny -i cluster_out/cluster_sequences.fa -o phy_out`
**Explanation:** Chain multiple modules together for complete analysis. CRESSENT is designed for modular use.

### Annotate with CAPS/REPS databases
**Args:** `cressent annotate -i ./cluster/cluster_sequences.fa -db ./cressent_DB -o annotation_out`
**Explanation:** Annotate sequences using the built-in CAPS (capsid proteins) and REPS (replication-associated proteins) databases.
