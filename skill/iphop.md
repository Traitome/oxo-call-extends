---
name: iphop
category: viral-analysis
description: Integrated Phage Host Prediction - Machine learning framework for predicting host genus from phage genomes.
tags: [iphop, phage, host-prediction, machine-learning, metagenomics]
author: oxo-call-community
source_url: "https://bitbucket.org/srouxjgi/iphop/"
---

## Concepts

- **Tool Overview**: iPHoP (v1.4.2) - An integrated machine learning framework for phage host prediction.
- **Core Function**: Predicts host genus for uncultivated phages and archaeoviruses from metagenomic data.
- **Hybrid Approach**: Combines phage-based and host-based prediction methods for improved accuracy.
- **Machine Learning Integration**: Uses neural networks and random forests to integrate multiple prediction signals.
- **CRISPR Spacer Matching**: Incorporates CRISPR spacer matching for host prediction.
- **Database Support**: Includes comprehensive databases covering ~60,000 genomes and 1.39M CRISPR spacers.

## Pitfalls

- **Database Size**: Requires large reference database (~50GB) for optimal performance.
- **Computational Requirements**: Significant computational resources needed for large datasets.
- **Novel Phages**: Prediction accuracy may decrease for highly novel phage sequences.
- **Contig Quality**: Requires high-quality phage contigs (minimum ~1500bp recommended).
- **Memory Usage**: Memory-intensive operations may require careful resource allocation.
- **Confidence Threshold**: Default confidence thresholds may need adjustment for specific use cases.

## Examples

### Basic host prediction
**Args:** `iphop predict --fa_file phages.fna --db_dir /path/to/iphop_db --out_dir results/`
**Explanation:** Predicts hosts for phage sequences using the iPHoP database.

### Custom confidence threshold
**Args:** `iphop predict --fa_file phages.fna --db_dir /path/to/iphop_db --out_dir results/ --confidence 90`
**Explanation:** Predicts hosts with 90% confidence threshold, reducing false positives.

### Parallel processing
**Args:** `iphop predict --fa_file phages.fna --db_dir /path/to/iphop_db --out_dir results/ --num_threads 12`
**Explanation:** Uses 12 threads for parallel processing to speed up predictions.

### Build custom database
**Args:** `iphop build_db --custom_genomes my_mags/ --output custom_db/`
**Explanation:** Builds a custom host database from user-provided genome sequences.

### Batch mode
**Args:** `iphop batch --input_list samples.txt --db_dir /path/to/iphop_db --out_dir batch_results/`
**Explanation:** Processes multiple phage sequence files in batch mode.

### Filter low-quality predictions
**Args:** `iphop filter --input predictions.csv --output filtered.csv --min-confidence 80`
**Explanation:** Filters prediction results to retain only high-confidence host assignments.