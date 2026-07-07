---
name: corgi
category: metagenomics
description: Classifier for ORganelle Genomes Inter alia
tags: [corgi, organelle, genome-classification, metagenomics, mitochondria]
author: oxo-call-community
source_url: "https://rbturnbull.github.io/corgi/"
---

## Concepts

- **Tool Overview**: CORGI (Classifier for ORganelle Genomes Inter alia) is a tool for identifying and classifying organelle genomes (mitochondria, chloroplasts) from sequencing data.
- **Core Function**: Classifies contigs as organellar or nuclear DNA, and further classifies organelle types.
- **Algorithm**: Uses machine learning and sequence composition features to identify organelle sequences.
- **Input**: Assembled contigs or raw reads in FASTA/FASTQ format.
- **Output**: Classification results indicating organelle type and confidence scores.
- **Application**: Metagenomics analysis, organelle genome assembly, contamination screening.
- **Installation**: Install via bioconda: `conda install -c bioconda corgi`

## Pitfalls

- **Sequence Length**: Short contigs may produce unreliable classifications.
- **Coverage Depth**: Low coverage can affect classification accuracy.
- **Organelle Diversity**: May not recognize highly divergent organelle sequences.
- **Contamination**: Nuclear contamination can affect results.
- **Training Data**: Performance depends on training dataset diversity.

## Examples

### Classify contigs
**Args:** `corgi classify -i contigs.fasta -o classification.txt`
**Explanation:** Classifies contigs as organelle or nuclear DNA.

### From raw reads
**Args:** `corgi classify --reads reads.fastq -o classification.txt`
**Explanation:** Classifies reads directly without assembly.

### Output detailed report
**Args:** `corgi classify -i contigs.fasta -o report.txt --detailed`
**Explanation:** Generates detailed classification report with confidence scores.

### Display help
**Args:** `corgi --help`
**Explanation:** Shows all available options and usage information.