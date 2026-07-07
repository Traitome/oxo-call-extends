---
name: cyrcular
category: variant-calling
description: Tool for calling circles from nanopore reads
tags: [cyrcular, variant-calling, nanopore, circular-DNA, extrachromosomal]
author: oxo-call-community
source_url: "https://github.com/tedil/cyrcular"
---

## Concepts

- **Tool Overview**: cyrcular (v0.3.0+) is a tool for detecting circular DNA molecules from nanopore sequencing reads.
- **Core Function**: Identifies circular DNA structures including plasmids, mitochondrial DNA, and extrachromosomal circular DNAs (eccDNAs).
- **Input/Output**: Input: FASTQ reads or BAM alignments. Output: Circular DNA predictions, breakpoint annotations.
- **Algorithm**: Uses signal-level analysis and alignment patterns to detect circular sequences.
- **Key Features**: Detects various circular DNA types, works directly with raw nanopore data, provides breakpoint resolution.
- **Installation**: `conda install -c bioconda cyrcular`

## Pitfalls

- **Nanopore Specific**: Designed specifically for nanopore sequencing data.
- **Basecalling**: Raw signal analysis requires appropriate basecalling parameters.
- **False Positives**: May detect false circular signals from repetitive sequences.
- **Reference Bias**: Performance may vary with different reference genomes.
- **Validation**: Circular DNA predictions should be validated experimentally.

## Examples

### Detect circular DNA from reads
**Args:** `cyrcular -i reads.fastq -o circular_calls.txt`
**Explanation:** Identify circular DNA molecules from nanopore reads.

### Use aligned BAM
**Args:** `cyrcular -i aligned.bam -r reference.fasta -o circular_calls.txt`
**Explanation:** Detect circular DNA from aligned reads with reference genome.

### Output breakpoints
**Args:** `cyrcular -i reads.fastq -o circular_calls.txt --breakpoints`
**Explanation:** Output detailed breakpoint information for circular DNA.
