---
name: amplicontyper
category: utility
description: Tool for training model and classifying reads from environmental ONT amplicon sequencing
tags: [amplicontyper, ONT, nanopore, amplicon, classification, machine-learning]
author: oxo-call-community
source_url: "https://github.com/AntonS-bio/AmpliconTyper"
---

## Concepts

- **Tool Overview**: AmpliconTyper is a machine learning-based tool for genotyping Oxford Nanopore amplicon sequencing data, specifically designed for environmental surveillance applications.
- **Core Function**: Classifies ONT sequencing reads into target and non-target organisms with high specificity and sensitivity using machine learning models.
- **Input/Output**: Inputs: Nanopore sequencing reads (FASTQ), training data; Outputs: Classification results, HTML report with genotyping information.
- **Installation**: Available via Bioconda (`conda install -c bioconda amplicontyper`) or from source.
- **Workflow**: Train classification models using public and/or user-generated data, then classify ONT sequencing data using the trained model.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format (FASTQ for sequencing data).
- **Training Data Quality**: High-quality training data is essential for accurate classification.
- **Model Selection**: Choose appropriate model based on specific application requirements.
- **Computational Resources**: Large datasets may require significant computational resources.

## Examples

### Train classification model
**Args:** `amplicontyper train -i training_data/ -o model/`
**Explanation:** Trains a machine learning model using existing Nanopore data from training directory.

### Classify ONT sequencing data
**Args:** `amplicontyper classify -i reads.fastq -m model/ -o results/`
**Explanation:** Classifies ONT sequencing reads using a pre-trained model and generates results.

### Generate HTML report
**Args:** `amplicontyper classify -i reads.fastq -m model/ -o results/ --report`
**Explanation:** Classifies reads and generates an HTML report with detailed results.

### Display help
**Args:** `amplicontyper --help`
**Explanation:** Shows available options and usage information.

### Train with mixed data sources
**Args:** `amplicontyper train -i my_data/ -e ENA_accessions.txt -o model/`
**Explanation:** Trains model using both local data and public data from ENA.

### Classify with confidence threshold
**Args:** `amplicontyper classify -i reads.fastq -m model/ -o results/ -c 0.9`
**Explanation:** Sets minimum confidence threshold of 0.9 for classification.