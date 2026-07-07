---
name: gaas
category: assembly
description: Suite of tools related to Genome Assembly Annotation Service tasks at NBIS.
tags: [gaas, genome annotation, assembly, NBIS]
author: oxo-call-community
source_url: "https://github.com/NBISweden/GAAS"
---

## Concepts
- **Genome Annotation**: Comprehensive genome annotation toolkit.
- **NBIS Service**: Part of NBIS Genome Assembly Annotation Service.
- **Assembly Quality**: Assesses assembly quality metrics.
- **Annotation Validation**: Validates genome annotations.
- **PASA Integration**: Integrates with PASA for annotation updates.

## Pitfalls
- **Complex Pipeline**: Multiple tools in the suite require coordination.
- **Database Dependencies**: Requires various annotation databases.
- **Memory Usage**: High memory usage for large genomes.
- **Time Consuming**: Full annotation pipeline can be time-consuming.
- **Expertise Required**: Requires bioinformatics expertise.

## Examples
### Run annotation
**Args:** `gaas_annotation.pl -genome assembly.fasta -species species_name`
**Explanation:** Runs genome annotation pipeline.

### Assess assembly quality
**Args:** `gaas_quality.pl -genome assembly.fasta`
**Explanation:** Assesses quality of genome assembly.

### Validate annotations
**Args:** `gaas_validate_annotations.pl -gff annotations.gff3`
**Explanation:** Validates genome annotations.

### Extract longest transcripts
**Args:** `gaas_extract_longest_transcripts.pl -gff annotations.gff3`
**Explanation:** Extracts longest transcript isoforms.

### Generate report
**Args:** `gaas_report.pl -project annotation_project/ -o report.html`
**Explanation:** Generates HTML report of annotation results.