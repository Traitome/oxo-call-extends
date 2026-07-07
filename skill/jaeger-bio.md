---
name: jaeger-bio
category: hpc
description: A quick and precise pipeline for detecting phages in sequence assemblies.
tags: [jaeger-bio, hpc, phage, detection, assembly]
author: oxo-call-community
source_url: "https://readthedocs.org/projects/jaeger-docs/"
---

## Concepts

- **Tool Overview**: jaeger-bio (v1.1.30) - A high-performance pipeline for identifying prophages and phage sequences within bacterial genome assemblies.
- **Prophage Detection**: Identifies integrated phage sequences within bacterial chromosomes using computational approaches.
- **HPC Optimization**: Optimized for high-performance computing environments with parallel processing capabilities.
- **Multi-step Analysis**: Combines multiple detection algorithms including sequence similarity search, gene content analysis, and structural features.
- **Annotation Integration**: Integrates with databases like RefSeq and GenBank for phage classification.
- **Visualization Support**: Generates output files compatible with genome browsers for visual inspection.

## Pitfalls

- **False Positives**: May detect transposons or other mobile elements as phages.
- **Incomplete Assemblies**: Fragmented assemblies can lead to missed or partial phage detection.
- **Database Dependencies**: Detection accuracy depends on the completeness of reference phage databases.
- **Computational Requirements**: Large genomes require significant computational resources.
- **Boundary Detection**: Determining exact phage insertion boundaries can be ambiguous.
- **Strain Variation**: Highly divergent phage sequences may not be detected.

## Examples

### Detect phages in assembly
**Args:** `jaeger run --input assembly.fasta --output phage_results/`
**Explanation:** Runs phage detection pipeline on input FASTA assembly.

### Use custom database
**Args:** `jaeger run --input assembly.fasta --output results/ --database custom_phages.fasta`
**Explanation:** Uses custom phage database for detection instead of default.

### Specify threads
**Args:** `jaeger run --input assembly.fasta --output results/ --threads 16`
**Explanation:** Uses 16 threads for parallel processing.

### Include annotation
**Args:** `jaeger run --input assembly.fasta --output results/ --annotate`
**Explanation:** Adds functional annotation to detected phage sequences.

### Generate visualization
**Args:** `jaeger run --input assembly.fasta --output results/ --visualize`
**Explanation:** Generates visualization files for genome browsers.

### Filter by size
**Args:** `jaeger run --input assembly.fasta --output results/ --min-length 10000`
**Explanation:** Only reports phages longer than 10,000 bp.