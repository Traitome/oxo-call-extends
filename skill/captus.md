---
name: captus
category: assembly
description: Assembly of phylogenomic datasets from high-throughput sequencing data
tags: [captus, phylogenomics, assembly, target-capture]
author: oxo-call-community
source_url: "https://github.com/edgardomortiz/Captus"
---

## Concepts

- **Tool Overview**: Captus assembles phylogenomic datasets from target capture sequencing.
- **Core Function**: Extracts and assembles target loci from sequencing data.
- **Workflow**: Assembly → Extraction → Alignment → Phylogenetics.
- **Input**: FASTQ files from target capture experiments.
- **Output**: Aligned loci and concatenated supermatrix.
- **Installation**: Install via bioconda: `conda install -c bioconda captus`

## Pitfalls

- **Reference Probes**: Requires reference probe sequences for target extraction.
- **Coverage**: Low coverage may result in incomplete loci.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Run full pipeline
**Args:** `captus assembly -i reads/ -r probes.fa -o captus_results/`
**Explanation:** Assembles target loci from sequencing reads.

### Extract loci only
**Args:** `captus extract -i assembly.fa -r probes.fa -o extracted_loci/`
**Explanation:** Extracts target loci from assembled contigs.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
