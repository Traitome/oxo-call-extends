---
name: tracy
category: analysis
description: Tracy - Tool for analyzing tandem repeat expansions.
tags: [tracy, tandem-repeat, repeat-expansion, genomics, microsatellite]
author: oxo-call-community
source_url: "https://github.com/compbio/tracy"
---

## Concepts

- **Tool Overview**: Tracy - A tool for detecting and analyzing tandem repeat expansions from sequencing data.
- **Core Function**: Identifies tandem repeats and characterizes their expansion status.
- **Input**: Sequencing reads (FASTQ/BAM), reference genome, repeat annotations.
- **Output**: Repeat expansion calls, size estimates, quality metrics.
- **Installation**: `pip install tracy` or `conda install -c bioconda tracy`
- **Use Case**: Repeat expansion analysis, disease genetics, population studies.

## Pitfalls

- **Repeat Complexity**: Complex repeat structures may be difficult to resolve.
- **Coverage**: Requires sufficient coverage in repeat regions.

## Examples

### Detect expansions
**Args:** `tracy -i reads.fastq -r genome.fasta -o expansions/`
**Explanation:** Detect tandem repeat expansions from sequencing data.

### With BAM
**Args:** `tracy -b alignments.bam -o repeat_results/`
**Explanation:** Analyze repeat expansions from aligned reads.
