---
name: cannoli
category: distributed
description: Distributed execution of bioinformatics tools on Apache Spark
tags: [cannoli, spark, distributed, big-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bigdatagenomics/cannoli"
---

## Concepts

- **Tool Overview**: Cannoli enables distributed execution of bioinformatics tools on Apache Spark.
- **Core Function**: Wraps command-line bioinformatics tools for distributed processing on Spark clusters.
- **Integration**: Works with ADAM and other big data genomics frameworks.
- **Input**: Genomic data in ADAM or standard formats.
- **Output**: Processed results in ADAM or standard formats.
- **Application**: Scalable bioinformatics analysis on large datasets.
- **Installation**: Install via bioconda: `conda install -c bioconda cannoli`

## Pitfalls

- **Spark Required**: Requires Apache Spark cluster or local Spark installation.
- **Memory**: Distributed processing requires significant cluster memory.
- **Tool Compatibility**: Not all command-line tools are compatible.
- **Configuration**: Requires proper Spark configuration for optimal performance.

## Examples

### Run distributed tool
**Args:** `spark-submit --class org.bdgenomics.cannoli.Cannoli cannoli.jar --tool bwa-mem --input reads.adam --output aligned.adam`
**Explanation:** Runs BWA-MEM distributed on Spark cluster.

### Use with ADAM
**Args:** `spark-submit --class org.bdgenomics.cannoli.Cannoli cannoli.jar --tool samtools-sort --input aligned.adam --output sorted.adam`
**Explanation:** Runs SAMtools sort distributed on ADAM data.

### Display help
**Args:** `spark-submit --class org.bdgenomics.cannoli.Cannoli cannoli.jar --help`
**Explanation:** Shows all available options and usage information.