---
name: dram
category: annotation
description: DRAM - Distilled and Refined Annotation of Metabolism for microbial and viral genomes.
tags: [dram, annotation, metabolism, microbial-genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/shafferm/DRAM/wiki"
---

## Concepts

- **Tool Overview**: DRAM is a comprehensive annotation tool for microbial and viral genomes that provides functional annotation and metabolic reconstruction.
- **Core Function**: Annotates protein-coding genes with functional information and reconstructs metabolic pathways.
- **Input/Output**: Input: FASTA genome sequences, protein sequences. Output: Annotated features, metabolic pathway predictions, quality reports.
- **Algorithm**: Integrates multiple databases (KEGG, Pfam, TIGRFAM, etc.) for comprehensive functional annotation.
- **Key Features**: Automated annotation, metabolic pathway reconstruction, genome quality assessment, customizable databases, comparative analysis.
- **Installation**: `conda install -c bioconda dram`

## Pitfalls

- **Input Requirements**: Requires properly formatted genome sequences; fragmented assemblies may affect annotation quality.
- **Database Updates**: Outdated databases can lead to incomplete annotations.
- **Memory Usage**: Large genomes or many genomes in batch may require significant RAM.
- **Annotation Confidence**: Some annotations may be uncertain; review low-confidence predictions.
- **Metabolic Reconstruction**: Depends on complete gene prediction; missing genes affect pathway completeness.
- **Time Requirements**: Full annotation can be time-consuming for large datasets.

## Examples

### Run basic annotation
**Args:** `dram annotate --input genome.fna --output dram_output`
**Explanation:** Runs complete annotation pipeline on a single genome.

### Annotate multiple genomes
**Args:** `dram annotate --input-dir genomes/ --output dram_output`
**Explanation:** Processes multiple genome files in batch mode.

### Skip gene calling
**Args:** `dram annotate --input genome.fna --output dram_output --skip-gene-calling`
**Explanation:** Uses pre-computed gene predictions instead of running Prodigal.

### Custom database directory
**Args:** `dram annotate --input genome.fna --output dram_output --databases custom_db/`
**Explanation:** Uses custom database directory instead of default databases.

### Generate metabolic models
**Args:** `dram distill --input dram_output/annotations.tsv --output metabolic_models/`
**Explanation:** Distills annotations into metabolic pathway predictions.

### Compare annotations
**Args:** `dram compare --input-dir dram_outputs/ --output comparison_report/`
**Explanation:** Compares annotations across multiple genomes.