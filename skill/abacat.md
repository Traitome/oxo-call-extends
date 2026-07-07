---
name: abacat
category: annotation
description: Abacat - A Bacterial genome Comparison and Annotation Toolkit for working with bacterial whole genome sequencing data.
tags: [abacat, annotation, bacterial, genome, comparison, wgs, python]
author: oxo-call-community
source_url: "https://github.com/vinisalazar/abacat"
---

## Concepts

- **Tool Overview**: Abacat (pronounced "ABBA-cat") is a Python toolkit for working with bacterial whole genome sequencing (WGS) data. Version 0.0.4a.
- **Core Function**: Provides Python objects to represent elements common to WGS analysis workflows, including CDS files, genes, proteins, alignment methods, and sequence statistics.
- **Key Features**: Annotates freshly generated WGS data, parses existing NCBI data, indexes BLAST/HMM databases, performs ANI measurements, and tracks data provenance.
- **Installation**: Install via bioconda: `conda install -c bioconda abacat` or via pip: `pip install abacat`
- **Platform Support**: Python library (Python >= 3.6), platform-independent
- **Dependencies**: Requires Prodigal, FastANI, Biopython, and Pandas
- **Note**: This repository is archived and deprecated in favor of BioProv

## Pitfalls

- **Archived Project**: Abacat is no longer actively maintained and has been deprecated in favor of BioProv.
- **Python Library**: Primarily designed as a Python library/API, not a command-line tool.
- **Active Development**: During development phase, results were not guaranteed.
- **External Dependencies**: Requires Prodigal and FastANI to be installed separately.

## Examples

### Basic usage in Python script
**Args:** `from abacat import Project; project = Project("my_project")`
**Explanation:** Import the abacat library and create a new project object for managing WGS analysis.

### Annotate WGS data
**Args:** `project.annotate("assembly.fasta")`
**Explanation:** Annotate a bacterial genome assembly using Prodigal and other annotation tools.

### Parse NCBI data
**Args:** `project.parse_ncbi("genbank_file.gbff")`
**Explanation:** Parse and load existing NCBI GenBank annotations into the project.

### Calculate ANI between genomes
**Args:** `project.ani_comparison("genome1.fasta", "genome2.fasta")`
**Explanation:** Perform Average Nucleotide Identity (ANI) comparison between two genomes using FastANI.

### Index BLAST database
**Args:** `project.index_blastdb("sequences.fasta", "blast_db_name")`
**Explanation:** Create a BLAST database index for sequence alignment searches.