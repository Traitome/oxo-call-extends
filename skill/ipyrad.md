---
name: ipyrad
category: assembly
description: Interactive assembly and analysis of RAD-seq data sets using de novo and reference-based approaches.
tags: [ipyrad, RAD-seq, assembly, population-genetics, phylogenetics]
author: oxo-call-community
source_url: "https://ipyrad.readthedocs.io/en/master"
---

## Concepts

- **Tool Overview**: ipyrad (v0.9.108) - A free and open source tool for assembling and analyzing restriction site-associated DNA sequence (RADseq) datasets.
- **Core Function**: Provides a modular workflow for processing RAD-seq data from raw reads to assembled loci.
- **Seven-Step Pipeline**: Demultiplexing, filtering, clustering, error estimation, consensus calling, cross-sample clustering, and output formatting.
- **Parallel Processing**: Designed for scalability with support for MPI and multi-core processing.
- **De novo and Reference-based**: Supports both de novo assembly and reference-guided mapping approaches.
- **Downstream Integration**: Outputs formatted files for phylogenetic and population genetic analysis tools.

## Pitfalls

- **Parameter Sensitivity**: Assembly results can be sensitive to parameter settings, particularly clustering threshold.
- **Missing Data**: RAD-seq data often has high missing data rates that need careful handling.
- **Computational Resources**: Large datasets require significant computational resources and memory.
- **Contamination**: Sample contamination can significantly affect assembly quality.
- **Barcode Mismatches**: Incorrect barcode assignment can lead to sample misidentification.
- **Reference Genome Quality**: Reference-based assembly depends heavily on reference genome quality.

## Examples

### Create new assembly project
**Args:** `ipyrad -n my_project`
**Explanation:** Creates a new assembly project with default parameters file.

### Run full assembly pipeline
**Args:** `ipyrad -p params-my_project.txt -s 1234567`
**Explanation:** Runs all seven steps of the RAD-seq assembly pipeline.

### Run specific steps
**Args:** `ipyrad -p params-my_project.txt -s 345`
**Explanation:** Runs only steps 3-5 (clustering, error estimation, consensus calling).

### Branch assembly with different parameters
**Args:** `ipyrad -p params-my_project.txt -b my_project_alt`
**Explanation:** Creates a branch of the assembly for testing alternative parameters.

### Parallel processing on cluster
**Args:** `ipyrad -p params-my_project.txt -s 3 -c 32 --MPI`
**Explanation:** Runs step 3 in parallel across 32 cores using MPI.

### Generate results summary
**Args:** `ipyrad -p params-my_project.txt -r`
**Explanation:** Generates a summary report of assembly statistics.