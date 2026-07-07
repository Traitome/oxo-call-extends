---
name: metavelvet-sl-pipeline
category: utility
description: Perl libraries that run the full pipeline for metavelvet-sl
tags: [metavelvet-sl-pipeline, utility, pipeline]
author: oxo-call-community
source_url: "http://metavelvet.dna.bio.keio.ac.jp/MSL.html"
---

## Concepts

- **Tool Overview**: MetaVelvet-SL Pipeline v1.0 provides Perl libraries for running the complete MetaVelvet-SL assembly pipeline.
- **Core Function**: Executes the full supervised learning-based metagenomic assembly workflow.
- **End-to-End Pipeline**: Covers all steps from raw reads to assembled contigs.
- **Automated Processing**: Automates the entire assembly process with minimal user intervention.
- **Input/Output**: Accepts raw sequencing reads; outputs final assembled contigs and analysis reports.
- **Perl Implementation**: Implemented in Perl for pipeline orchestration.

## Pitfalls

- **Version Compatibility**: Designed specifically for MetaVelvet-SL.
- **Dependency Management**: Requires proper Perl environment and dependencies.
- **Memory Requirements**: Processing large datasets may require significant memory.
- **Runtime**: Complete pipeline execution can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Error Handling**: Pipeline errors may require careful debugging.

## Examples

### Run complete pipeline
**Args:** `metavelvet-sl-pipeline -i reads.fastq -o results/`
**Explanation:** Runs the complete MetaVelvet-SL assembly pipeline.

### With custom parameters
**Args:** `metavelvet-sl-pipeline -i reads.fastq -o results/ -k 51`
**Explanation:** Uses k-mer size of 51 for assembly.

### Paired-end analysis
**Args:** `metavelvet-sl-pipeline -i reads_1.fastq -r reads_2.fastq -o results/`
**Explanation:** Processes paired-end sequencing data.

### Generate report
**Args:** `metavelvet-sl-pipeline -i reads.fastq -o results/ -r report.html`
**Explanation:** Generates a comprehensive HTML report.

### Batch processing
**Args:** `metavelvet-sl-pipeline -i fastq/ -o results/`
**Explanation:** Processes multiple samples in batch mode.