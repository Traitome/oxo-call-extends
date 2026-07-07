---
name: baktfold
category: annotation
description: BakTFold - Rapid annotation of bacterial genomes using protein structural information
tags: [baktfold, annotation, protein-structure, bacterial-genomics, mag-annotation]
author: oxo-call-community
source_url: "https://baktfold.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: BakTFold provides rapid and standardized annotation of bacterial genomes, metagenome-assembled genomes (MAGs), and plasmids using protein structural information. Version 0.2.0.
- **Core Function**: Enhances genome annotation by incorporating protein structure prediction and comparison.
- **Structure-Based Annotation**: Uses AlphaFold2-derived structural predictions for improved functional annotation.
- **Structural Comparison**: Compares predicted protein structures against known structures in databases.
- **Functional Prediction**: Leverages structural similarity to infer protein function.
- **Integration**: Works alongside traditional sequence-based annotation for comprehensive results.
- **Input/Output**: Accepts genome assemblies in FASTA format, outputs annotated features in standard formats.
- **Installation**: `conda install -c bioconda baktfold`.

## Pitfalls

- **Computational Resources**: Structure prediction requires significant computational resources.
- **Database Requirements**: Requires structural databases for comparison.
- **Prediction Accuracy**: Structural predictions may have varying accuracy depending on sequence quality.
- **Runtime**: Structure-based annotation is computationally intensive and may take time.
- **Memory Usage**: Large genomes require substantial memory for structure prediction.

## Examples

### Basic genome annotation with structure
**Args:** `baktfold --input genome.fasta --output annotation/`
**Explanation:** Annotates bacterial genome using structural information.

### Use GPU acceleration
**Args:** `baktfold --input genome.fasta --output annotation/ --gpu`
**Explanation:** Uses GPU for accelerated structure prediction.

### Annotate MAG
**Args:** `baktfold --input mag.fasta --output annotation/ --min-contig-length 1000`
**Explanation:** Annotates metagenome-assembled genome with minimum contig length filter.

### Custom output formats
**Args:** `baktfold --input genome.fasta --output annotation/ --formats gff3,gbk`
**Explanation:** Outputs annotation in multiple formats.

### Increase threads
**Args:** `baktfold --input genome.fasta --output annotation/ --threads 8`
**Explanation:** Uses specified number of threads for parallel processing.

### Skip structure prediction
**Args:** `baktfold --input genome.fasta --output annotation/ --skip-structure`
**Explanation:** Performs annotation without structural information (faster).

### Use custom database
**Args:** `baktfold --input genome.fasta --output annotation/ --db custom_structural_db/`
**Explanation:** Uses custom structural database for comparison.

### Display help
**Args:** `baktfold --help`
**Explanation:** Shows all available command-line options and usage information.