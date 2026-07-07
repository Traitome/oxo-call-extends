---
name: saccharis
category: pipeline
description: SACCHARIS Bioinformatics Pipeline for carbohydrate-active enzyme analysis.
tags: ["saccharis", "CAZymes", "carbohydrate", "bioinformatics", "pipeline"]
author: oxo-call-community
source_url: "https://github.com/saccharis/SACCHARIS_2"
---

## Concepts

- **Tool Overview**: SACCHARIS (v2.0.5) is a comprehensive bioinformatics pipeline for the analysis of carbohydrate-active enzymes (CAZymes). It integrates multiple tools for annotation and analysis of CAZyme sequences.
- **Core Function**: Identifies and classifies carbohydrate-active enzymes from sequence data, predicts enzyme functions, and generates annotation reports.
- **Architecture**: Modular pipeline that combines sequence similarity searches, domain identification, and functional annotation tools.
- **Input Format**: Protein sequences in FASTA format, optionally with genomic context information.
- **Output Format**: CAZyme annotations, functional predictions, summary reports, visualization of enzyme families.
- **Use Case**: CAZyme annotation in genomic/metagenomic data, enzyme discovery, biotechnological applications, comparative genomics.

## Pitfalls

- **Database requirements**: Requires local CAZy database installation.
- **Computational resources**: Pipeline requires significant computational resources for large datasets.
- **Annotation quality**: Depends on database completeness and sequence similarity.
- **Memory usage**: Large sequence datasets require substantial memory.
- **Time consumption**: Full pipeline run can be time-consuming for large inputs.
- **Database updates**: CAZy database needs regular updates for accurate annotations.

## Examples

### Basic CAZyme annotation
**Args:** `saccharis run -i proteins.fasta -o results`
**Explanation:** `-i` input FASTA with protein sequences; `-o` output directory.

### With genomic context
**Args:** `saccharis run -i proteins.fasta -g genome.fasta -o results`
**Explanation:** `-g` genome sequence for context analysis.

### Specify database
**Args:** `saccharis run -i proteins.fasta -d /path/to/cazy/db -o results`
**Explanation:** `-d` path to local CAZy database.

### Parallel processing
**Args:** `saccharis run -i proteins.fasta -o results -t 16`
**Explanation:** `-t` number of threads for parallel processing.

### Quick mode
**Args:** `saccharis run -i proteins.fasta -o results --quick`
**Explanation:** `--quick` runs simplified analysis for faster results.

### Output visualization
**Args:** `saccharis run -i proteins.fasta -o results --visualize`
**Explanation:** `--visualize` generates visualizations of CAZyme distributions.

### Batch processing
**Args:** `saccharis batch -i sequences_dir -o results_dir`
**Explanation:** `batch` mode processes multiple FASTA files in a directory.
