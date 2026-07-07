---
name: transcomb
category: analysis
description: TransComb - Tool for analyzing transposon recombination events.
tags: [transcomb, transposon, recombination, dna-repair, genome-stability]
author: oxo-call-community
source_url: "https://github.com/compbio/transcomb"
---

## Concepts

- **Tool Overview**: TransComb - A tool for analyzing transposon-mediated recombination events.
- **Core Function**: Identifies and characterizes recombination events involving transposons.
- **Input**: Sequencing reads (FASTQ/BAM), reference genome, transposon annotations.
- **Output**: Recombination events, breakpoints, structural variations.
- **Installation**: `pip install transcomb` or `conda install -c bioconda transcomb`
- **Use Case**: Genome stability analysis, transposon evolution, structural variation detection.

## Pitfalls

- **Complexity**: Complex recombination events may be difficult to detect.
- **Coverage**: Requires sufficient coverage at recombination breakpoints.

## Examples

### Detect recombination
**Args:** `transcomb -i reads.fastq -r genome.fasta -t transposons.gff -o recombination/`
**Explanation:** Detect transposon-mediated recombination events.

### Analyze BAM
**Args:** `transcomb -b alignments.bam -o events/`
**Explanation:** Analyze recombination events from aligned reads.
