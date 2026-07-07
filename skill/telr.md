---
name: telr
category: analysis
description: TelR - Telomere detection using Long Reads for assembly validation.
tags: [telr, telomere, long-read, assembly-validation, nanopore, pacbio]
author: oxo-call-community
source_url: "https://github.com/guigozerve/telR"
---

## Concepts

- **Tool Overview**: TelR - A tool specifically designed to detect and validate telomeres in long-read assemblies.
- **Core Function**: Identifies telomere sequences at contig ends and validates assembly completeness by checking for telomere presence.
- **Input**: Assembled contigs or long-read data, reference genome (optional).
- **Output**: Telomere detection report, assembly quality metrics, telomere coordinates.
- **Installation**: `pip install telr` or `conda install -c bioconda telr`
- **Use Case**: Validating genome assemblies, ensuring telomere completeness in eukaryotic genome assemblies.

## Pitfalls

- **Assembly Required**: Works best with assembled contigs, not raw reads.
- **Incomplete Assemblies**: Telomeres at chromosome ends may be missing in draft assemblies.

## Examples

### Validate assembly telomeres
**Args:** `telr -i assembly.fasta -o telomere_validation.txt`
**Explanation:** Detect telomeres in assembled contigs and generate validation report.

### Compare to reference
**Args:** `telr -i contigs.fasta -r reference.fasta -o comparison/`
**Explanation:** Compare telomere detection between assembly and reference genome.
