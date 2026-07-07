---
name: spliceai
category: variant-calling
description: SpliceAI - Deep learning-based splice variant identification
tags: [spliceai, variant-calling, splicing, deep-learning, variant-annotation]
author: oxo-call-community
source_url: "https://github.com/Illumina/SpliceAI"
---

## Concepts

- **Tool Overview**: spliceai (v1.3.1) - A splice variant prediction tool
- **Core Function**: Identifies splice variants using deep learning
- **Input/Output**: Accepts BAM/VCF files; outputs splice variant predictions
- **Algorithm**: Deep learning model for splice site prediction
- **Installation**: `conda install -c bioconda spliceai`
- **Key Features**: Splice prediction, deep learning, variant annotation

## Pitfalls

- **Input Requirements**: Requires properly formatted BAM/VCF files
- **Read Quality**: Read quality affects prediction accuracy
- **Model Parameters**: Model parameters affect prediction sensitivity
- **Memory Usage**: Large datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Prediction Accuracy**: Accuracy depends on data quality and model

## Examples

### Display help
**Args:** `spliceai --help`
**Explanation:** Shows available options and usage information.

### Basic splice variant prediction
**Args:** `spliceai -I input.vcf -O output.vcf -R reference.fasta`
**Explanation:** Predict splice variants from VCF.

### With BAM input
**Args:** `spliceai -I input.bam -O output.vcf -R reference.fasta`
**Explanation:** Predict splice variants from BAM.

### With gene annotation
**Args:** `spliceai -I input.vcf -O output.vcf -R reference.fasta -A annotation.gtf`
**Explanation:** Use gene annotation for prediction.

### With distance cutoff
**Args:** `spliceai -I input.vcf -O output.vcf -R reference.fasta --distance 5000`
**Explanation:** Set distance cutoff for splice sites.

### Output detailed results
**Args:** `spliceai -I input.vcf -O output.vcf -R reference.fasta --detailed`
**Explanation:** Output detailed prediction information.

### Output scores
**Args:** `spliceai -I input.vcf -O output.vcf -R reference.fasta --scores`
**Explanation:** Output splice site scores.

### Output statistics
**Args:** `spliceai -I input.vcf -O output.vcf -R reference.fasta --stats`
**Explanation:** Output prediction statistics.

### Generate report
**Args:** `spliceai -I input.vcf -O output.vcf -R reference.fasta --report`
**Explanation:** Generate prediction report.

### With threads
**Args:** `spliceai -I input.vcf -O output.vcf -R reference.fasta -p 8`
**Explanation:** Use multiple threads for prediction.