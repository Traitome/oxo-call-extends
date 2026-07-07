---
name: clinker
category: expression
description: Bioinformatics pipeline that generates a superTranscriptome from fusion finder outputs
tags: [clinker, fusion-genes, supertranscriptome, gene-expression, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Oshlack/Clinker"
---

## Concepts

- **Tool Overview**: Clinker is a bioinformatics pipeline that generates a superTranscriptome from outputs of popular fusion finders (JAFFA, tophatFusion, SOAP, deFUSE, Pizzly, etc).
- **Core Function**: Integrates fusion gene predictions from multiple tools to create a consensus superTranscriptome for visualization and downstream analysis.
- **Algorithm**: Combines and consolidates fusion calls from multiple sources into a unified representation.
- **Input**: Fusion finder outputs from various tools (JAFFA, tophatFusion, SOAP, deFUSE, Pizzly).
- **Output**: SuperTranscriptome in FASTA format and visualization plots.
- **Application**: Fusion gene analysis, cancer genomics, and transcriptome research.
- **Installation**: Install via bioconda: `conda install -c bioconda clinker`

## Pitfalls

- **Multiple Tools**: Requires outputs from multiple fusion detection tools.
- **Tool Compatibility**: Must use supported fusion finder formats.
- **Reference Genome**: Must match the reference used by fusion finders.
- **Computational Resources**: May require significant resources for large datasets.
- **Visualization**: Requires genome viewer like IGV for full analysis.

## Examples

### Generate superTranscriptome
**Args:** `clinker -i jaffa_results.txt topfusion_results.txt -o supertranscriptome.fasta`
**Explanation:** Generates superTranscriptome from multiple fusion finder outputs.

### With plotting
**Args:** `clinker -i fusion_results/ -o supertranscriptome.fasta --plot`
**Explanation:** Generates superTranscriptome and visualization plots.

### From single tool
**Args:** `clinker -i jaffa_results.txt -r reference.gtf -o supertranscriptome.fasta`
**Explanation:** Creates superTranscriptome from JAFFA output with annotation.

### Display help
**Args:** `clinker --help`
**Explanation:** Shows all available options and usage information.