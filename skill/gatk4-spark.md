---
name: gatk4-spark
category: variant-calling
description: Spark-enabled GATK4 tools for parallelized execution on multi-core machines or Spark clusters.
tags: [gatk4-spark, spark, parallel, multithreading, gatk4, variant-calling, distributed]
author: oxo-call-community
source_url: "https://gatk.broadinstitute.org/"
---

## Concepts

- **Tool Overview**: GATK4-Spark refers to Spark-enabled versions of GATK4 tools that leverage Apache Spark for parallelized execution.
- **Core Function**: Enables GATK tools to run in parallel across multiple CPU cores on a single machine or across a Spark cluster.
- **Spark Architecture**: Spark is an Apache Software Foundation project for distributed computing. GATK uses it for multi-threading rather than traditional threading.
- **Local Spark Mode**: On regular machines (even laptops), Spark creates a virtual standalone cluster using available CPU cores without any cluster setup.
- **Spark Suffix Convention**: Tools with Spark versions have suffix "Spark" (e.g., `HaplotypeCallerSpark`, `MarkDuplicatesSpark`). Some tools only exist as Spark versions.
- **Performance Scaling**: Spark-enabled tools typically scale linearly with cores (e.g., MarkDuplicatesSpark is ~15% faster at 2 cores, scales to 16+ cores).
- **Memory Efficiency**: Spark handles data spilling to disk when memory is insufficient, providing graceful degradation.
- **No Cluster Required**: You do NOT need a Spark cluster to use Spark-enabled tools. Local mode uses all available cores by default.
- **Installation**: Same as gatk4: `conda install -c bioconda gatk4`

## Pitfalls

- **Spark vs Non-Spark Versions**: Not all tools have both versions. Using wrong version may cause errors or performance issues.
- **Executor Arguments Only Work on Clusters**: `--num-executors`, `--executor-memory` only apply when running on actual Spark clusters, not in local mode.
- **Queryname Sort Order**: MarkDuplicatesSpark is optimized for queryname-grouped input. Coordinate-sorted input incurs 2x slower processing for internal sorting.
- **Minimum Resources**: For 30x WGS BAM, minimum 16GB RAM recommended. Memory scales with library complexity.
- **UMI Not Supported**: Spark tools do not support UMI-based duplicate marking. Use Picard MarkDuplicates for UMI data.
- **Spark Master Selection**: `--spark-master local[*]` uses all cores. Specify `local[N]` to limit to N cores.
- **Java Options**: Set JVM memory with `--java-options "-Xmx4g"` before the tool name, not with Spark arguments.

## Examples

### Run MarkDuplicatesSpark locally
**Args:** `gatk MarkDuplicatesSpark -I input.bam -O marked_dup.bam -M metrics.txt`
**Explanation:** Runs duplicate marking in parallel using all local cores. `-M` produces metrics (optional but recommended).

### Specify core count for local Spark
**Args:** `gatk MarkDuplicatesSpark -I input.bam -O marked_dup.bam --spark-master local[8]`
**Explanation:** Limits Spark to 8 cores even if more are available. Useful for resource sharing.

### Run on Spark cluster
**Args:** `gatk MarkDuplicatesSpark -I input.bam -O marked_dup.bam --spark-master spark://master:7077 --num-executors 10 --executor-cores 4`
**Explanation:** Distributed execution on a Spark cluster with 10 executors of 4 cores each.

### ApplyBQSR with Spark
**Args:** `gatk ApplyBQSRSpark -I input.bam -O output.bam --bqsr-recal-file recal.table --spark-master local[*]`
**Explanation:** Parallelized BQSR application using all available cores.

### Check Spark availability
**Args:** `gatk --list | grep -i spark`
**Explanation:** Lists all available Spark-enabled GATK tools.

### Run HaplotypeCallerSpark
**Args:** `gatk HaplotypeCallerSpark -R reference.fa -I input.bam -O output.g.vcf.gz -ERC GVCF --spark-master local[*]`
**Explanation:** Parallel germline variant calling using Spark for faster processing on large BAMs.
