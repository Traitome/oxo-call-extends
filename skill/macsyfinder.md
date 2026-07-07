---
name: macsyfinder
category: utility
description: "MacSyFinder: Detection of macromolecular systems in protein datasets using systems modelling and similarity search"
tags: [macsyfinder, utility, protein-analysis, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/gem-pasteur/macsyfinder"
---
## Concepts

- **Tool Overview**: macsyfinder v2.1.6 - A bioinformatics tool for detecting macromolecular systems (like secretion systems, flagella, etc.) in protein datasets using profile-based similarity searches and systems modeling.
- **Core Function**: Identifies complete or partial macromolecular systems by searching for functional modules and their components in genomic or metagenomic data.
- **Input/Output**: Input: Protein sequences in FASTA format; Output: Tab-separated files with detected systems and their components.
- **Installation**: `conda install -c bioconda macsyfinder` or `pip install macsyfinder`
- **System Models**: Uses predefined models (TXSScan, Sec-SPI, etc.) or user-defined models to search for specific systems.
- **Similarity Search**: Utilizes HMMER for profile hidden Markov model-based sequence similarity searches.

## Pitfalls

- **Model Selection**: Using incorrect or outdated system models can lead to false positives or missed detections.
- **Database Format**: Requires properly formatted HMM databases; incompatible formats cause errors.
- **Performance**: Running on large datasets without proper indexing can be slow.
- **False Positives**: Low-complexity regions or repetitive sequences may trigger spurious matches.
- **Model Customization**: User-defined models require careful validation to ensure specificity.
- **Memory Usage**: Analyzing large protein datasets may require significant memory resources.

## Examples

### Search for type III secretion systems
**Args:** `macsyfinder --db-type uniprot -d /path/to/db -m TXSScan -i proteins.fasta -o results`
**Explanation:** Searches for type III secretion systems using the TXSScan model.

### With custom model
**Args:** `macsyfinder --db-type uniprot -d /path/to/db -m /path/to/custom_model -i proteins.fasta -o results`
**Explanation:** Uses a user-defined model for system detection.

### With multiple models
**Args:** `macsyfinder --db-type uniprot -d /path/to/db -m TXSScan -m Sec-SPI -i proteins.fasta -o results`
**Explanation:** Searches for multiple system types simultaneously.

### Quick mode
**Args:** `macsyfinder --db-type uniprot -d /path/to/db -m TXSScan -i proteins.fasta -o results --quick`
**Explanation:** Runs in quick mode for faster analysis with reduced sensitivity.

### Verbose output
**Args:** `macsyfinder --db-type uniprot -d /path/to/db -m TXSScan -i proteins.fasta -o results -v`
**Explanation:** Provides detailed logging during analysis.

### Generate graphical output
**Args:** `macsyfinder --db-type uniprot -d /path/to/db -m TXSScan -i proteins.fasta -o results --plot`
**Explanation:** Generates visual representations of detected systems.