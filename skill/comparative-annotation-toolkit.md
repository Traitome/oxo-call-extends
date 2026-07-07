---
name: comparative-annotation-toolkit
category: alignment
description: End-to-end pipeline for comparative genome annotation transfer
tags: [comparative-annotation-toolkit, genome-annotation, hal, gff3, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/ComparativeGenomicsToolkit/Comparative-Annotation-Toolkit"
---

## Concepts

- **Tool Overview**: The Comparative Annotation Toolkit (CAT) is an end-to-end pipeline that transfers genome annotations from a reference genome to target genomes using HAL-format multiple whole genome alignments.
- **Core Function**: Takes a GFF3 annotation file from a high-quality reference assembly and produces GFF3 annotations on all target genomes in the HAL alignment.
- **Algorithm**: Uses genome alignment information to project annotations across species while accounting for evolutionary changes.
- **Input**: HAL-format multiple genome alignment, GFF3 annotation file for reference genome.
- **Output**: GFF3 annotation files for all target genomes.
- **Application**: Comparative genomics, annotation transfer, and multi-genome analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda comparative-annotation-toolkit`

## Pitfalls

- **Alignment Quality**: Annotation transfer quality depends on genome alignment accuracy.
- **Evolutionary Distance**: Distantly related species may have poor annotation transfer.
- **HAL Format**: Requires properly formatted HAL alignment files.
- **Reference Annotation**: Quality limited by reference annotation completeness.
- **Computational Resources**: Large genome alignments require significant resources.

## Examples

### Run annotation transfer
**Args:** `cat --hal-genome alignment.hal --reference-gff3 reference.gff3 --target-genomes human,chimp,gorilla --output-dir annotations/`
**Explanation:** Transfers annotations from reference to target genomes.

### With custom parameters
**Args:** `cat --hal-genome alignment.hal --reference-gff3 reference.gff3 --output-dir annotations/ --workers 8`
**Explanation:** Runs with 8 worker threads for parallel processing.

### Validate output
**Args:** `cat --validate --gff3 annotations/target.gff3`
**Explanation:** Validates transferred annotation quality.

### Display help
**Args:** `cat --help`
**Explanation:** Shows all available options and usage information.