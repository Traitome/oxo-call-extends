---
name: hypro
category: annotation
description: HyPro - Extend hypothetical prokka protein annotations using additional homology searches
tags: [hypro, prokka, annotation, homology search]
author: oxo-call-community
source_url: "https://github.com/hoelzer-lab/hypro"
---

## Concepts

- **Tool Overview**: HyPro extends hypothetical protein annotations from Prokka using additional homology searches against larger databases.
- **Prokka Integration**: Works directly with Prokka annotation outputs.
- **Homology Search**: Performs BLAST searches against comprehensive protein databases.
- **Annotation Extension**: Updates annotations for hypothetical proteins with functional predictions.
- **Database Support**: Supports multiple databases including UniProt, RefSeq, and custom databases.
- **Installation**: `conda install -c bioconda hypro`

## Pitfalls

- **Prokka Requirement**: Requires prior Prokka annotation output.
- **Database Size**: Large databases require significant storage space.
- **Computation Time**: Comprehensive homology searches can be time-consuming.
- **E-value Threshold**: Appropriate e-value cutoff selection affects annotation quality.
- **False Positives**: Homology-based annotations may include false positives.
- **Database Updates**: Outdated databases may provide outdated annotations.

## Examples

### Extend annotations from Prokka output
**Args:** `hypro -i prokka_output/ -d uniprot.fasta -o extended_annotations/`
**Explanation:** Extends Prokka annotations using UniProt database.

### Custom e-value threshold
**Args:** `hypro -i prokka_output/ -d refseq.fasta -e 1e-5 -o extended/`
**Explanation:** Uses stricter e-value threshold of 1e-5.

### Multiple databases
**Args:** `hypro -i prokka_output/ -d uniprot.fasta -d refseq.fasta -o extended/`
**Explanation:** Searches against multiple databases sequentially.

### Thread configuration
**Args:** `hypro -i prokka_output/ -d uniprot.fasta -t 8 -o extended/`
**Explanation:** Runs with 8 threads for faster homology search.

### Output format
**Args:** `hypro -i prokka_output/ -d uniprot.fasta --gff3 -o extended/`
**Explanation:** Outputs annotations in GFF3 format.