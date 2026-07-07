---
name: condiga
category: assembly
description: Contigs Directed Gene Annotation for metaproteomics database construction
tags: [condiga, metaproteomics, gene-annotation, metagenomics, database]
author: oxo-call-community
source_url: "https://github.com/metagentools/ConDiGA"
---

## Concepts

- **Tool Overview**: ConDiGA (Contigs Directed Gene Annotation) is a taxonomic annotation pipeline for metagenomic data designed to construct accurate protein sequence databases for deep metaproteomic coverage.
- **Core Function**: Annotates metagenomic contigs with taxonomic information and generates curated protein sequence databases optimized for metaproteomics analysis.
- **Algorithm**: Combines gene prediction, taxonomic classification, and quality filtering to create comprehensive protein databases.
- **Input**: Assembled metagenomic contigs in FASTA format.
- **Output**: Annotated protein sequence database with taxonomic labels.
- **Application**: Metaproteomics database construction, protein identification, and functional analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda condiga`

## Pitfalls

- **Assembly Quality**: Database quality depends on metagenome assembly completeness.
- **Taxonomic Resolution**: Classification accuracy varies with reference database coverage.
- **Gene Prediction**: May miss genes in poorly assembled regions.
- **Database Size**: Large databases increase search time in downstream proteomics.
- **Contamination**: May include contaminant sequences requiring filtering.

## Examples

### Build protein database
**Args:** `condiga -i contigs.fasta -o protein_db.fasta`
**Explanation:** Constructs annotated protein database from metagenomic contigs.

### With taxonomic filtering
**Args:** `condiga -i contigs.fasta -t bacteria -o protein_db.fasta`
**Explanation:** Filters database to include only bacterial taxa.

### With quality thresholds
**Args:** `condiga -i contigs.fasta -q 0.8 -o protein_db.fasta`
**Explanation:** Applies quality threshold of 0.8 for taxonomic assignments.

### Display help
**Args:** `condiga --help`
**Explanation:** Shows all available options and usage information.