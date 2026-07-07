---
name: igdiscover
category: sequence-analysis
description: IgDiscover analyzes antibody repertoires and discovers novel V genes from high-throughput sequencing data, enabling creation of individualized germline gene databases.
tags: [igdiscover, sequence-analysis, antibody, VDJ, immunoglobulin, repertoire]
author: oxo-call-community
source_url: "https://igdiscover.se/"
---

## Concepts

- **Antibody Repertoire Analysis**: Processes high-throughput sequencing data from antibody libraries.
- **V Gene Discovery**: Identifies novel germline V genes from expressed antibody sequences.
- **Iterative Database Building**: Constructs individualized germline gene databases through iterative refinement.
- **IgBLAST Integration**: Uses IgBLAST for V/D/J gene assignment.
- **Cluster Analysis**: Identifies candidate V genes through sequence clustering.
- **ISCAPE-seq Support**: Analyzes plate-based single-cell antibody sequencing experiments.

## Pitfalls

- **Sequencing Depth**: Requires large datasets (hundreds of thousands of sequences) for comprehensive V gene discovery.
- **Library Type**: Works best with IgM libraries; IgG libraries may yield fewer germline sequences.
- **Primer Design**: Forward primers must be external to V gene sequences for accurate discovery.
- **Computational Time**: Analysis can take hours for large datasets.
- **Database Requirements**: Requires initial V/D/J gene database for iteration.

## Examples

### Initialize analysis directory
**Args:** `igdiscover init --db vdj_database/ --reads1 reads_R1.fastq.gz myexperiment`
**Explanation:** Creates and configures a new analysis directory with sequencing reads.

### Run complete analysis
**Args:** `igdiscover run`
**Explanation:** Executes the full IgDiscover pipeline for V gene discovery.

### Analyze single-end reads
**Args:** `igdiscover init --single-reads sequences.fasta.gz --db vdj_db/ analysis`
**Explanation:** Initializes analysis with single-end FASTA data.

### Discover new V genes
**Args:** `igdiscover discover --iterations 5`
**Explanation:** Runs V gene discovery with 5 iterations.

### ISCAPE-seq analysis
**Args:** `igdiscover iscape run --receptor IG --db vdj_db/ --R1-fastq reads_R1.fastq.gz --output-dir iscape_results/`
**Explanation:** Analyzes ISCAPE-seq single-cell antibody data.