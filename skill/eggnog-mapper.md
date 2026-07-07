---
name: eggnog-mapper
category: annotation
description: "Fast genome-wide functional annotation through orthology assignment."
tags: [eggnog-mapper, annotation, functional-annotation, orthology, eggNOG]
author: oxo-call-community
source_url: "https://github.com/eggnogdb/eggnog-mapper/wiki"
---

## Concepts

- **Tool Overview**: eggNOG-mapper is a tool for fast functional annotation of genes and proteins using orthology assignment.
- **Core Function**: Assigns functional annotations (GO terms, KEGG pathways, COGs) to sequences based on orthology.
- **Input/Output**: Input: Protein/DNA sequences (FASTA). Output: Annotation results with functional terms.
- **Algorithm**: Uses HMM-based searches against the eggNOG database for orthology detection.
- **Key Features**: Fast annotation, comprehensive database, multiple annotation sources, batch processing.
- **Installation**: `conda install -c bioconda eggnog-mapper`

## Pitfalls

- **Database Download**: Requires downloading large eggNOG database files.
- **Memory Usage**: Database loading requires significant RAM.
- **Sequence Quality**: Poor quality sequences affect annotation accuracy.
- **Database Updates**: Regular database updates recommended.
- **Computation Time**: Annotating many sequences can be time-consuming.

## Examples

### Basic annotation
**Args:** `emapper.py -i proteins.fa -o annotations`
**Explanation:** Annotates protein sequences using eggNOG database.

### With local database
**Args:** `emapper.py -i proteins.fa -o annotations --data_dir /path/to/eggnog_data`
**Explanation:** Uses locally installed eggNOG database.

### Include GO terms
**Args:** `emapper.py -i proteins.fa -o annotations --go_evidence all`
**Explanation:** Includes all GO evidence codes in output.

### Parallel processing
**Args:** `emapper.py -i proteins.fa -o annotations --cpu 8`
**Explanation:** Uses 8 CPU cores for parallel processing.

### Output in tabular format
**Args:** `emapper.py -i proteins.fa -o annotations --output_format tabular`
**Explanation:** Outputs annotations in tabular format.