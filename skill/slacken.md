---
name: slacken
category: metagenomics
description: A scalable implementation of the Kraken 2 metagenomic classification method based on Apache Spark
tags: [slacken, metagenomics, kraken2, spark, classification]
author: oxo-call-community
source_url: "https://github.com/JNP-Solutions/Slacken"
---

## Concepts

- **Tool Overview**: slacken (v2.0.0) - A distributed implementation of Kraken 2 for scalable metagenomic classification
- **Core Function**: Classifies metagenomic reads using k-mer matching, implemented on Apache Spark for horizontal scalability
- **Input/Output**: Accepts FASTQ files; outputs classification reports and Bracken-compatible results
- **Algorithm**: Implements Kraken 2 algorithm with distributed computing for large-scale processing
- **Installation**: Available via Docker or source installation; requires Spark cluster
- **Key Features**: Low RAM requirement, horizontal scalability, Bracken compatibility

## Pitfalls

- **Spark Cluster**: Requires properly configured Apache Spark cluster
- **Memory Management**: Ensure sufficient memory for large reference databases
- **Multi-sample Mode**: Best performance with multiple samples; single sample may be slower than Kraken 2
- **Database Building**: Requires time and resources to build Slacken-specific databases
- **Network Performance**: Distributed processing depends on fast network between nodes
- **Bracken Integration**: Requires separate Bracken installation for abundance estimation

## Examples

### Display help
**Args:** `slacken --help`
**Explanation:** Shows available options and usage information.

### Build database
**Args:** `slacken build -i reference_genomes/ -o slacken_db`
**Explanation:** Build a Slacken database from reference genomes.

### Classify reads
**Args:** `slacken classify -d slacken_db -i reads.fastq -o classification.txt`
**Explanation:** Classify metagenomic reads against the database.

### Multi-sample classification
**Args:** `slacken classify -d slacken_db -i sample1.fastq sample2.fastq -o results/`
**Explanation:** Classify multiple samples simultaneously for better performance.

### With Bracken output
**Args:** `slacken classify -d slacken_db -i reads.fastq -o classification.txt --bracken bracken_output.txt`
**Explanation:** Generate Bracken-compatible output for abundance estimation.

### Cluster mode
**Args:** `slacken classify --spark-master spark://master:7077 -d slacken_db -i reads.fastq -o results.txt`
**Explanation:** Run classification on a Spark cluster.

### Sample-tailored mode
**Args:** `slacken classify -d slacken_db -i reads.fastq -o results.txt --sample-tailored`
**Explanation:** Use sample-tailored minimizer libraries for improved specificity.