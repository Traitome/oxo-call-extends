---
name: megalodon
category: variant-calling
description: Nanopore modified base and sequence variant detection tool.
tags: [megalodon, nanopore, modified-bases]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/megalodon"
---

## Concepts

- **Tool Overview**: Megalodon detects variants and modified bases from nanopore data.
- **Core Function**: Basecalling, variant calling, and modified base detection.
- **Modified Base Detection**: Identifies DNA modifications like 5mC.
- **Neural Networks**: Uses deep learning for basecalling.
- **Alignment-based**: Works with aligned nanopore reads.
- **Installation**: `conda install -c bioconda megalodon`

## Pitfalls

- **Data Requirements**: Requires high-quality nanopore data.
- **Computation Time**: Neural network processing is slow.
- **Memory Requirements**: High memory usage.
- **Model Selection**: Choosing right model is critical.
- **Modified Base Models**: Requires specific models for modifications.
- **Reference Dependence**: Needs reference genome for variant calling.

## Examples

### Basecall and call variants
**Args:** `megalodon raw_reads.fast5 --reference ref.fasta --output variants/`
**Explanation:** Basecalls and detects variants.

### Modified base detection
**Args:** `megalodon raw_reads.fast5 --reference ref.fasta --mod-motif 5mC CG --output mods/`
**Explanation:** Detects 5mC modifications.

### High accuracy mode
**Args:** `megalodon raw_reads.fast5 --reference ref.fasta --high-accuracy --output variants/`
**Explanation:** Uses high-accuracy basecalling.

### Threaded processing
**Args:** `megalodon raw_reads.fast5 --reference ref.fasta --threads 8 --output variants/`
**Explanation:** Uses 8 threads.

### Help documentation
**Args:** `megalodon --help`
**Explanation:** Displays available options.
