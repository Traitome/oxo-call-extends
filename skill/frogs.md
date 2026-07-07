---
name: frogs
category: expression
description: FROGS is a workflow designed for metabarcoding sequence analysis.
tags: [frogs, metabarcoding, amplicon sequencing, biodiversity]
author: oxo-call-community
source_url: "https://github.com/geraldinepascal/FROGS"
---

## Concepts
- **Metabarcoding Analysis**: Processes amplicon sequencing data for biodiversity analysis.
- **ASV Generation**: Produces Amplicon Sequence Variants (ASVs) from raw reads.
- **Taxonomic Assignment**: Assigns taxonomy to ASVs.
- **Quality Control**: Includes comprehensive QC steps.
- **OTU Clustering**: Supports traditional OTU clustering and ASV approaches.

## Pitfalls
- **Amplicon Specific**: Designed for amplicon sequencing data.
- **Reference Database**: Requires appropriate reference database for taxonomy.
- **Computational Requirements**: Large datasets require significant resources.
- **Primer Removal**: Requires careful primer trimming.
- **Chimera Detection**: May miss some chimeric sequences.

## Examples
### Run complete FROGS workflow
**Args:** `frogs workflow --input reads/ --output results/ --reference ref_db/`
**Explanation:** Runs complete metabarcoding analysis workflow.

### Quality control
**Args:** `frogs qc --input reads.fastq --output qc_report.txt`
**Explanation:** Performs quality control on raw reads.

### ASV generation
**Args:** `frogs asv --input reads.fastq --output asvs.fasta`
**Explanation:** Generates ASVs from sequencing reads.

### Taxonomic assignment
**Args:** `frogs taxonomy --input asvs.fasta --reference ref_db/ --output taxonomy.txt`
**Explanation:** Assigns taxonomy to ASVs.

### Generate report
**Args:** `frogs report --input results/ --output report.html`
**Explanation:** Generates comprehensive HTML report.