---
name: alphafetcher
category: annotation
description: Command-line interface to download protein structures from the AlphaFold Protein Structure Database
tags: [alphafetcher, AlphaFold, protein-structure, PDB, annotation, bioinformatics]
author: oxo-call-community
source_url: "https://bitbucket.org/bio2byte/alphafetcher/"
---

## Concepts

- **Tool Overview**: alphafetcher is a command-line tool designed to programmatically retrieve predicted protein structures from the AlphaFold Protein Structure Database. It supports downloading structures using various accession types including UniProt IDs, gene names, and NCBI taxonomy IDs.
- **Core Function**: Enables bulk downloading of AlphaFold predictions in multiple formats (PDB, mmCIF, JSON), automating access to over 214 million predicted structures in the AlphaFold Database.
- **Input/Output**: Accepts text files with protein identifiers (UniProt accessions, gene names) and outputs structure files in PDB, mmCIF, or JSON formats with confidence metrics.
- **Installation**: Available via Bioconda (`conda install -c bioconda alphafetcher`) or GitHub source.
- **Database Access**: Interfaces with the AlphaFold Database API to fetch structures, supporting both individual protein queries and bulk downloads by taxonomy ID.

## Pitfalls

- **API Rate Limits**: The AlphaFold Database API has rate limits; large batch downloads may require delays or authentication.
- **Accession Format**: Ensure input accessions are valid UniProt IDs (e.g., P01308) or properly formatted identifiers; invalid IDs will fail silently.
- **Output File Management**: Bulk downloads can generate thousands of files; use the `--output-dir` flag to organize results.
- **Network Dependencies**: Requires stable internet connection; intermittent connectivity may cause partial downloads.
- **Versioning**: AlphaFold predictions are versioned (v4 is current); older versions may not be accessible.

## Examples

### Download single protein structure
**Args:** `--uniprot P01308 --output-dir structures/`
**Explanation:** Downloads the AlphaFold structure for the human insulin protein (UniProt ID P01308) and saves it to the specified directory. The `--uniprot` flag specifies the UniProt accession.

### Bulk download by taxonomy ID
**Args:** `--taxid 9606 --output-dir human_proteomes/ --format pdb`
**Explanation:** Downloads all AlphaFold predictions for the human proteome (taxonomy ID 9606) in PDB format. The `--format` flag specifies output format (pdb, cif, or json).

### Download multiple proteins from file
**Args:** `--input accessions.txt --output-dir results/ --parallel 4`
**Explanation:** Reads UniProt accessions from a text file and downloads structures in parallel using 4 threads. The `--parallel` flag speeds up batch downloads.

### Download with confidence metrics
**Args:** `--uniprot Q9Y2W8 --output-dir structure/ --include-pae`
**Explanation:** Downloads the structure along with Predicted Aligned Error (PAE) data in JSON format. The `--include-pae` flag retrieves confidence metrics useful for structural analysis.

### Filter by confidence score
**Args:** `--uniprot P53_HUMAN --output-dir p53/ --min-plddt 90`
**Explanation:** Downloads only structure predictions with a minimum pLDDT confidence score of 90. The pLDDT score ranges from 0-100, with higher values indicating greater confidence.