---
name: translig
category: analysis
description: TransLig - Tool for analyzing transposon integration sites.
tags: [translig, transposon, integration-site, insertion, genome-editing]
author: oxo-call-community
source_url: "https://github.com/compbio/translig"
---

## Concepts

- **Tool Overview**: TransLig - A tool for identifying and analyzing transposon integration sites from sequencing data.
- **Core Function**: Detects transposon insertion sites and characterizes integration patterns.
- **Input**: Sequencing reads (FASTQ/BAM), transposon sequence, reference genome.
- **Output**: Integration site coordinates, flanking sequences, insertion statistics.
- **Installation**: `pip install translig` or `conda install -c bioconda translig`
- **Use Case**: Transposon mutagenesis, gene therapy, genome engineering.

## Pitfalls

- **Transposon Sequence**: Requires accurate transposon sequence for detection.
- **Complex Insertions**: Complex insertion patterns may be difficult to resolve.

## Examples

### Detect integration sites
**Args:** `translig -i reads.fastq -t transposon.fasta -r genome.fasta -o insertions/`
**Explanation:** Detect transposon integration sites from sequencing data.

### With BAM input
**Args:** `translig -b alignments.bam -t tn_sequence.fasta -o sites/`
**Explanation:** Analyze integration sites from aligned reads.
