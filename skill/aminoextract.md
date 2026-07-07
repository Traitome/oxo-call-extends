---
name: aminoextract
category: annotation
description: CLI tool to extract amino acid sequences from FASTA files based on GFF annotations
tags: [aminoextract, annotation, FASTA, GFF, protein-sequences, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/RIVM-bioinformatics/AminoExtract"
---

## Concepts

- **Tool Overview**: AminoExtract is a CLI tool and Python library for extracting amino acid sequences from nucleotide sequences based on GFF annotation files.
- **Core Function**: Parses GFF files to identify CDS (Coding Sequence) regions, extracts corresponding nucleotide sequences from FASTA files, translates them to amino acids, and writes results to output files.
- **Input/Output**: Inputs: Nucleotide FASTA file, GFF annotation file; Outputs: Amino acid FASTA files (single file or individual files per feature).
- **Installation**: Available via Bioconda (`conda install -c bioconda -c conda-forge aminoextract`) or PyPI (`pip install AminoExtract`).
- **Features**: Filtering of genomic features, support for multiple output formats, GFF data accessible via pandas DataFrame in Python API.

## Pitfalls

- **GFF Format**: Requires properly formatted GFF3 files; ensure GFF version is compatible.
- **FASTA Coordinates**: FASTA sequence IDs must match seqids in GFF file; coordinate mismatches cause errors.
- **CDS Features**: GFF must contain CDS features for translation; missing CDS features result in empty output.
- **Strand Handling**: Negative strand features require reverse complement before translation; tool handles this automatically.
- **Frame Information**: Ensure GFF contains correct frame information for proper translation start.

## Examples

### Extract amino acid sequences
**Args:** `aminoextract -f genome.fasta -g annotation.gff -o proteins.faa`
**Explanation:** Extracts all CDS regions from genome.fasta based on annotation.gff and writes translated amino acid sequences to proteins.faa.

### Output individual files per gene
**Args:** `aminoextract -f genome.fasta -g annotation.gff -o output_dir/ --split`
**Explanation:** Writes each protein sequence to a separate file in the output directory.

### Filter by feature type
**Args:** `aminoextract -f genome.fasta -g annotation.gff -o filtered.faa --feature-type gene`
**Explanation:** Filters and extracts sequences only for features of type 'gene'.

### Include metadata in output headers
**Args:** `aminoextract -f genome.fasta -g annotation.gff -o proteins.faa --include-metadata`
**Explanation:** Includes additional GFF metadata in FASTA headers for better traceability.

### Extract specific genes by ID
**Args:** `aminoextract -f genome.fasta -g annotation.gff -o selected.faa --gene-ids gene1 gene2 gene3`
**Explanation:** Extracts amino acid sequences only for the specified gene IDs.

### Use Python API
**Args:** Python usage
```python
from aminoextract import AminoExtract
extractor = AminoExtract('genome.fasta', 'annotation.gff')
proteins = extractor.extract()
proteins.to_csv('proteins.faa', sep='\n', index=False)
```
**Explanation:** Uses the Python API to programmatically extract and process amino acid sequences.