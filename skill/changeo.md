---
name: changeo
category: sequencing
description: Bioinformatics toolkit for processing high-throughput lymphocyte receptor sequencing data
tags: [changeo, immunology, repertoire-sequencing, bcr, tcr, bioinformatics]
author: oxo-call-community
source_url: "https://changeo.readthedocs.io"
---

## Concepts

- **Tool Overview**: Change-O is a bioinformatics toolkit for processing high-throughput lymphocyte receptor sequencing data (BCR/TCR).
- **Core Function**: Analyzes and annotates B-cell and T-cell receptor sequences from high-throughput sequencing.
- **Features**: V(D)J assignment, clonal grouping, sequence correction, and repertoire analysis.
- **Input**: FASTQ/FASTA sequence files from lymphocyte receptor sequencing.
- **Output**: Annotated sequences, clonal assignments, and repertoire statistics.
- **Application**: Immunology research, vaccine development, and cancer immunotherapy.
- **Installation**: Install via bioconda: `conda install -c bioconda changeo`

## Pitfalls

- **Sequence Quality**: Requires high-quality sequencing data for accurate V(D)J assignment.
- **Reference Database**: Must use appropriate germline reference database.
- **Clonal Assignment**: Clustering parameters affect clonal grouping results.
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Run IgBLAST analysis
**Args:** `igblastn -query sequences.fasta -db germline_db -out igblast.out`
**Explanation:** Runs IgBLAST for V(D)J assignment.

### Convert IgBLAST output
**Args:** `MakeDb.py -i igblast.out -s sequences.fasta -o results/`
**Explanation:** Converts IgBLAST output to Change-O database format.

### Clonal grouping
**Args:** `DefineClones.py -d database.tsv -o clones.tsv`
**Explanation:** Groups sequences into clonal families.

### Display help
**Args:** `MakeDb.py --help`
**Explanation:** Shows available options for database creation.