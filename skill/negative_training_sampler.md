---
name: negative_training_sampler
category: utility
description: Generates negative training samples with matched GC distribution to positive samples per chromosome.
tags: [negative_training_sampler, utility, machine-learning, genomics]
author: oxo-call-community
source_url: "https://github.com/kircherlab/negative_training_sampler"
---

## Concepts

- **Tool Overview**: Negative training sampler generates control regions matched for GC content.
- **Core Function**: Creates negative training samples with identical GC distribution as positive samples.
- **Algorithm**: Uses sliding window approach to find regions with matching GC content.
- **Input Format**: Accepts BED files of positive regions and genome FASTA.
- **Output**: Produces BED file of negative control regions.
- **Use Case**: Machine learning training set preparation, genomic feature analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Genome Requirements**: Requires genome FASTA with indexed chromosomes.
- **Memory Usage**: Processing large genomes requires memory.
- **Chromosome Matching**: Must ensure chromosome names match between inputs.
- **Window Size**: Results depend on window size parameter.
- **Overlap Handling**: May produce overlapping regions if not configured properly.

## Examples

### Display help
**Args:** `negative_training_sampler --help`
**Explanation:** Shows available options and usage instructions.

### Basic usage
**Args:** `negative_training_sampler -i positives.bed -g genome.fasta -o negatives.bed`
**Explanation:** Generates negative samples with matched GC content.

### Window size
**Args:** `negative_training_sampler -i positives.bed -g genome.fasta -w 1000 -o negatives.bed`
**Explanation:** Uses 1000bp window size for GC calculation.

### Masked regions
**Args:** `negative_training_sampler -i positives.bed -g genome.fasta -m mask.bed -o negatives.bed`
**Explanation:** Excludes masked regions from sampling.

### Multiple chromosomes
**Args:** `negative_training_sampler -i positives.bed -g genome.fasta -c chr1,chr2 -o negatives.bed`
**Explanation:** Limits sampling to specified chromosomes.

### Output statistics
**Args:** `negative_training_sampler -i positives.bed -g genome.fasta -s stats.tsv -o negatives.bed`
**Explanation:** Outputs GC matching statistics.