---
name: tepid
category: analysis
description: TEPID - Tool for Expression analysis of Plasmid Integration Devices.
tags: [tepid, plasmid, gene-expression, barcoding, transposon]
author: oxo-call-community
source_url: "https://github.com/ ARCHIVED /tepid"
---

## Concepts

- **Tool Overview**: TEPID (Tool for Expression analysis of Plasmid Integration Devices) - A tool for analyzing gene expression from transposon sequencing data, particularly for plasmid expression studies.
- **Core Function**: Quantifies gene expression from transposon insertion sites, specifically designed for studying plasmid-encoded genes and transposon integration events.
- **Input**: Transposon sequencing reads (FASTQ), reference genome with transposon annotation.
- **Output**: Gene expression counts, insertion site maps, differential expression results.
- **Installation**: `pip install tepid` or `conda install -c bioconda tepid`
- **Use Case**: Studying plasmid gene expression, transposon mutagenesis screens.

## Pitfalls

- **Transposon Annotation**: Requires accurate transposon sequence annotation.
- **Library Complexity**: Complex transposon libraries may require adjusted parameters.

## Examples

### Analyze expression
**Args:** `tepid analysis -i reads.fastq.gz -g genome.gbk -o expression_results/`
**Explanation:** Analyze gene expression from transposon sequencing data.

### Differential expression
**Args:** `tepid diff -c control_count.tsv -t treatment_count.tsv -o de_results/`
**Explanation:** Compare expression between conditions.
