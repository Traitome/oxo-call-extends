---
name: pathotypr
category: variant-calling
description: Pathotypr performs alignment-free genome classification using SNP markers and machine learning.
tags: [pathotypr, variant-calling, ml-classification, genomic-surveillance]
author: oxo-call-community
source_url: "https://github.com/PathoGenOmics-Lab/pathotypr"
---

## Concepts

- **Tool Overview**: Pathotypr classifies genomes using SNP markers and ML.
- **Core Function**: Performs alignment-free genome classification.
- **Algorithm**: Uses Random Forest for classification.
- **Input Format**: Accepts genome sequences or VCF files.
- **Output**: Produces lineage assignments and drug resistance predictions.
- **Use Case**: Genomic surveillance, MTBC analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Model Training**: Results depend on trained model.
- **Marker Quality**: Results depend on SNP marker quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pathotypr --help`
**Explanation:** Shows available options and usage instructions.

### Classify genome
**Args:** `pathotypr -i genome.fasta -o results/`
**Explanation:** Classifies genome using pre-trained model.

### With VCF
**Args:** `pathotypr -v variants.vcf -o results/`
**Explanation:** Uses VCF file for classification.

### Verbose mode
**Args:** `pathotypr -v -i genome.fasta -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pathotypr -t 4 -i genome.fasta -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pathotypr -i genome.fasta -o results.json --json`
**Explanation:** Outputs in JSON format.

### Train custom model
**Args:** `pathotypr train -i training_data/ -o model.pkl`
**Explanation:** Trains custom classification model.