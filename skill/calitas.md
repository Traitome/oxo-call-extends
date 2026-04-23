---
name: calitas
category: genome-editing
description: CRISPR/Cas-aware aligner for in silico off-target search
tags: [calitas, crispr, off-target, alignment, genome-editing]
author: oxo-call-community
source_url: "https://github.com/editasmedicine/calitas"
---

## Concepts

- **Tool Overview**: Calitas is a CRISPR/Cas-aware aligner for identifying off-target sites.
- **Core Function**: Aligns CRISPR-edited sequences considering guide RNA and PAM sequences.
- **Input**: FASTQ reads from CRISPR editing experiments and guide RNA sequences.
- **Output**: Aligned reads with on-target and off-target site identification.
- **Application**: CRISPR off-target analysis and genome editing validation.
- **Installation**: Install via bioconda: `conda install -c bioconda calitas`

## Pitfalls

- **CRISPR Specific**: Designed for CRISPR editing data; not for general alignment.
- **Guide RNA**: Must provide correct guide RNA sequence.
- **PAM Specification**: Specify correct PAM sequence for the Cas variant used.
- **Java Required**: Requires Java runtime environment.

## Examples

### Align CRISPR reads
**Args:** `java -jar calitas.jar -i reads.fq -g guide_sequence -p NGG -r reference.fa -o aligned.sam`
**Explanation:** Aligns CRISPR-edited reads with guide RNA and PAM awareness.

### Specify Cas variant
**Args:** `java -jar calitas.jar -i reads.fq -g guide -p NGG --cas9 -r ref.fa -o results/`
**Explanation:** Uses Cas9-specific parameters for off-target search.

### Display help
**Args:** `java -jar calitas.jar --help`
**Explanation:** Shows all available options and usage information.
