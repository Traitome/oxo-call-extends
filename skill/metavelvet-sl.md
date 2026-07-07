---
name: metavelvet-sl
category: assembly
description: "MetaVelvet-SL : An extension of Velvet assembler to de novo metagenomic assembler utilizing supervised learning"
tags: [metavelvet-sl, assembly, metagenomics, supervised-learning]
author: oxo-call-community
source_url: "http://metavelvet.dna.bio.keio.ac.jp/MSL.html"
---
## Concepts

- **Tool Overview**: MetaVelvet-SL v1.0 is an extension of the Velvet assembler that utilizes supervised learning for de novo metagenomic assembly.
- **Core Function**: Assembles metagenomic sequences using supervised learning techniques.
- **Supervised Learning**: Uses machine learning models to improve assembly accuracy.
- **De Novo Assembly**: Performs de novo assembly without reference sequences.
- **Input/Output**: Accepts FASTQ sequencing reads; outputs assembled contigs and scaffolds.
- **Meta-specific Optimization**: Optimized for metagenomic datasets with complex microbial communities.

## Pitfalls

- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Assembly of complex metagenomes can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Assembly quality depends on input read quality.
- **Training Data**: Requires high-quality training data for supervised learning models.

## Examples

### Assemble metagenome with supervised learning
**Args:** `metavelvet-sl -f reads.fastq -o assembly/`
**Explanation:** Assembles metagenomic short reads using supervised learning.

### With custom k-mer size
**Args:** `metavelvet-sl -f reads.fastq -k 51 -o assembly/`
**Explanation:** Uses k-mer size of 51 for assembly.

### Paired-end assembly
**Args:** `metavelvet-sl -f reads_1.fastq -r reads_2.fastq -o assembly/`
**Explanation:** Processes paired-end sequencing data.

### Train custom model
**Args:** `metavelvet-sl train -i training_data/ -o model.pkl`
**Explanation:** Trains a custom supervised learning model.

### Use trained model
**Args:** `metavelvet-sl -f reads.fastq -m model.pkl -o assembly/`
**Explanation:** Uses a pre-trained model for assembly.