---
name: centreseq
category: phylogeny
description: Fast core genome generation from bacterial genome assemblies using MMSeqs2 and Prokka
tags: [centreseq, core-genome, bacterial, phylogeny, pan-genome, mmseqs2, prokka]
author: oxo-call-community
source_url: "https://github.com/BFSSI-Bioinformatics-Lab/centreseq"
---

## Concepts

- **Tool Overview**: centreseq is a command-line tool for fast core genome generation from bacterial genome assemblies using MMSeqs2 and Prokka.
- **Core Function**: Builds an annotated core genome from multiple bacterial assemblies by performing annotation, self-clustering, pan-genome construction, and core genome identification.
- **Algorithm**: Uses Prokka for genome annotation, MMSeqs2 linclust for clustering, and generates reports for downstream phylogenetic analysis.
- **Input**: Directory containing multiple genome assemblies in FASTA format.
- **Output**: Core genome clusters, summary reports, pan-genome matrix, medoid sequences, phylogenetic tree input files.
- **Application**: Bacterial phylogenomics, outbreak investigation, population genetics, core genome MLST (cgMLST), microbial source tracking.
- **Installation**: `conda install -c bioconda centreseq` (Note: installation can be problematic, see pitfalls)

## Pitfalls

- **Complex Installation**: The conda installation is notoriously problematic due to Prokka dependencies. May need to manually install prokka after centreseq.
- **Perl Version Issue**: Prokka may require Perl downgrade: `conda install perl=5.22.0`
- **MMSeqs2 Version**: Version pinned at 9-d36de (10-6d92c contains bugs)
- **Memory Requirements**: Medoid picking step requires substantial RAM per CPU
- **Input Quality**: Results depend on assembly quality and annotation consistency

## Examples

### Generate core genome
**Args:** `centreseq core -f /path/to/assemblies -o /output/dir`
**Explanation:** Main command to generate core genome from a directory of genome assemblies.

### Generate core genome with medoid sequences
**Args:** `centreseq core -f /path/to/assemblies -o /output/dir --medoid-repseqs`
**Explanation:** Generates representative medoid nucleotide sequence for each core cluster (increases computation time).

### Adjust clustering similarity
**Args:** `centreseq core -f /path/to/assemblies -o /output/dir -m 0.95 -c 0.95`
**Explanation:** Sets minimum sequence identity (-m) and coverage (-c) for MMSeqs clustering (defaults 0.95).

### Generate pairwise comparisons
**Args:** `centreseq core -f /path/to/assemblies -o /output/dir --pairwise`
**Explanation:** Generates pairwise genome comparisons for interactive network visualization.

### Generate phylogenetic tree input
**Args:** `centreseq tree -s summary_report.csv -p /prokka/dir -o /output/dir`
**Explanation:** Processes core output to generate files for phylogenetic tree building software.

### Extract sequences from core cluster
**Args:** `centreseq extract -i /centreseq/core/dir -c cluster_id`
**Explanation:** Extracts ffn (nucleotide) and faa (amino acid) sequences from a specific core cluster.

### Subset summary report
**Args:** `centreseq subset -i samples.txt -s summary_report.tsv -o filtered_report.tsv`
**Explanation:** Filters summary report to only include specified sample IDs.
