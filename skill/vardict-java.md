---
name: vardict-java
category: variant-calling
description: VarDictJava - Java implementation of VarDict variant caller.
tags: [vardict-java, variant-calling, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/AstraZeneca-NGS/VarDictJava"
---

## Concepts

- **Tool Overview**: VarDictJava - Java implementation of VarDict variant caller.
- **Core Function**: Calls variants from sequencing data.
- **Input**: BAM file, BED file.
- **Output**: VCF file.
- **Installation**: Install via conda or download from GitHub
- **Use Case**: Variant calling, cancer genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large BAM files.
- **Java Version**: Requires Java 8 or higher.

## Examples

### Call variants
**Args:** `java -jar VarDict.jar -G ref.fasta -f 0.01 -N sample -b sample.bam -R regions.bed`
**Explanation:** Call variants from BAM file.

### With options
**Args:** `java -jar VarDict.jar -G ref.fasta -f 0.01 -N sample -b sample.bam -R regions.bed -t 8`
**Explanation:** Use 8 threads.
