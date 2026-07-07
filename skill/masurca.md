---
name: masurca
category: assembly
description: MaSuRCA genome assembler combining de Bruijn graph and overlap-layout-consensus approaches.
tags: [masurca, genome-assembly, hybrid-assembly]
author: oxo-call-community
source_url: "https://masurca.blogspot.co.uk"
---

## Concepts

- **Tool Overview**: MaSuRCA is a hybrid genome assembler combining multiple assembly approaches.
- **Core Function**: Assembles genomes using Illumina and optionally PacBio/Nanopore data.
- **Assembly Strategy**: Combines de Bruijn graph with overlap-layout-consensus.
- **Hybrid Assembly**: Supports Illumina-only and hybrid (Illumina + long reads) assembly.
- **Input/Output**: Accepts FASTQ reads, produces assembled contigs/scaffolds.
- **Installation**: `conda install -c bioconda masurca`

## Pitfalls

- **Configuration Complexity**: Requires detailed configuration file setup.
- **Memory Requirements**: High memory usage for large genomes.
- **Computation Time**: Very slow for complex genomes.
- **Data Quality**: Requires high-quality sequencing data.
- **Reference Dependencies**: May require reference-guided assembly options.
- **Output Size**: Large assemblies generate large output files.

## Examples

### Create configuration file
**Args:** `masurca -c config.txt`
**Explanation:** Creates template configuration file.

### Run assembly
**Args:** `bash assemble.sh`
**Explanation:** Runs MaSuRCA assembler using generated script.

### Hybrid assembly
**Args:** `masurca hybrid_config.txt`
**Explanation:** Configures hybrid assembly with Illumina and long reads.

### Illumina-only assembly
**Args:** `masurca illumina_config.txt`
**Explanation:** Assembles using only Illumina data.

### Specify genome size
**Args:** `masurca --genome-size 3000000000 config.txt`
**Explanation:** Sets expected genome size for assembly.

### Help documentation
**Args:** `masurca --help`
**Explanation:** Displays available options and parameters.
