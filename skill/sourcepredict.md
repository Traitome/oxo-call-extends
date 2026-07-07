---
name: sourcepredict
category: metagenomics
description: SourcePredict - Classification and prediction of metagenomic sample origin
tags: [sourcepredict, metagenomics, classification, prediction, source-tracking]
author: oxo-call-community
source_url: "https://github.com/maxibor/sourcepredict"
---

## Concepts

- **Tool Overview**: sourcepredict (v0.5.1) - A metagenomic source prediction tool
- **Core Function**: Predicts the origin of metagenomic samples
- **Input/Output**: Accepts metagenomic data; outputs source predictions
- **Algorithm**: Uses machine learning for source classification
- **Installation**: `conda install -c bioconda sourcepredict`
- **Key Features**: Source prediction, classification, metagenomics analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted metagenomic data
- **Training Data**: Requires proper training data for prediction
- **Database**: Requires source database for comparison
- **Memory Usage**: Large metagenomic datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Interpretation**: Results require biological interpretation

## Examples

### Display help
**Args:** `sourcepredict --help`
**Explanation:** Shows available options and usage information.

### Basic source prediction
**Args:** `sourcepredict -i metagenome.fastq -d sources.db -o predictions.tsv`
**Explanation:** Predict source of metagenomic sample.

### With multiple sources
**Args:** `sourcepredict -i metagenome.fastq -d sources.db -o predictions.tsv --sources source1 source2`
**Explanation:** Predict from multiple potential sources.

### With confidence threshold
**Args:** `sourcepredict -i metagenome.fastq -d sources.db -o predictions.tsv --threshold 0.8`
**Explanation:** Set confidence threshold for prediction.

### Output detailed results
**Args:** `sourcepredict -i metagenome.fastq -d sources.db -o predictions.tsv --detailed`
**Explanation:** Output detailed prediction results.

### Output statistics
**Args:** `sourcepredict -i metagenome.fastq -d sources.db -o predictions.tsv --stats`
**Explanation:** Output prediction statistics.

### Generate report
**Args:** `sourcepredict -i metagenome.fastq -d sources.db -o predictions.tsv --report`
**Explanation:** Generate prediction report.

### With threads
**Args:** `sourcepredict -i metagenome.fastq -d sources.db -o predictions.tsv -p 8`
**Explanation:** Use multiple threads for prediction.