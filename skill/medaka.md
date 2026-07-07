---
name: medaka
category: variant-calling
description: Neural network-based consensus and variant calling for nanopore sequencing data.
tags: [medaka, nanopore, variant-calling]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/medaka"
---

## Concepts

- **Tool Overview**: Medaka creates consensus sequences from nanopore data.
- **Core Function**: Uses neural networks for basecalling and variant calling.
- **Deep Learning**: Trained neural networks for accurate base prediction.
- **Consensus Calling**: Generates high-quality consensus sequences.
- **Variant Detection**: Identifies variants from aligned reads.
- **Installation**: `conda install -c bioconda medaka`

## Pitfalls

- **Data Requirements**: Requires high-quality nanopore data.
- **Model Selection**: Choosing right model is critical.
- **Computation Time**: Neural network inference is computationally heavy.
- **Memory Requirements**: High memory usage for large datasets.
- **Reference Dependence**: Requires reference genome for variant calling.
- **Basecalling Quality**: Depends on initial basecalling quality.

## Examples

### Generate consensus
**Args:** `medaka_consensus -i reads.fastq -d ref.fasta -o consensus/`
**Explanation:** Creates consensus sequence from reads.

### Call variants
**Args:** `medaka_variant -i variants.vcf -d ref.fasta -o calls.vcf`
**Explanation:** Calls variants from aligned reads.

### Train model
**Args:** `medaka_train -i training_data/ -o model.hdf5`
**Explanation:** Trains custom neural network model.

### Use specific model
**Args:** `medaka_consensus -i reads.fastq -d ref.fasta -m r941_prom_high_g360 -o consensus/`
**Explanation:** Uses specific basecaller model.

### Help documentation
**Args:** `medaka --help`
**Explanation:** Displays available commands and options.
