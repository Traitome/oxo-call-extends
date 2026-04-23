---
name: adapterremovalfixprefix
category: qc
description: Fixes adapter removal prefixes to prevent clashing read names in AdapterRemoval output
tags: [adapter-removal, read-names, prefix, fastq, fix]
author: oxo-call-community
source_url: "https://github.com/apeltzer/AdapterRemovalFixPrefix"
---

## Concepts

- **Tool Overview**: AdapterRemovalFixPrefix fixes read name prefixes in AdapterRemoval output to ensure no clashing read names exist between paired files.
- **Core Function**: Renames reads with unique prefixes to prevent naming conflicts when merging or processing AdapterRemoval output files.
- **Input/Output**: Input: AdapterRemoval FASTQ output files. Output: FASTQ files with fixed, non-clashing read names.
- **Problem Solved**: AdapterRemoval may produce identical read names in paired files, causing issues in downstream tools.
- **Installation**: Install via bioconda: `conda install -c bioconda adapterremovalfixprefix`

## Pitfalls

- **Java Required**: Tool is distributed as a JAR file - requires Java runtime.
- **Input Format**: Expects AdapterRemoval output format - may not work with other trimming tools.
- **Paired-End Only**: The prefix fix is primarily needed for paired-end data where read names must be unique.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows available options for AdapterRemovalFixPrefix.

### Fix prefixes in paired files
**Args:** `-i R1.fastq -i2 R2.fastq -o R1_fixed.fastq -o2 R2_fixed.fastq`
**Explanation:** Fixes read name prefixes in paired FASTQ files from AdapterRemoval.

### Fix with custom prefix
**Args:** `-i R1.fastq -i2 R2.fastq -o R1_fixed.fastq -o2 R2_fixed.fastq --prefix custom_`
**Explanation:** Uses custom prefix instead of default for read name modification.

### Fix single-end file
**Args:** `-i trimmed.fastq -o fixed.fastq`
**Explanation:** Fixes read names in a single-end AdapterRemoval output file.

### Fix with gzip output
**Args:** `-i R1.fastq -i2 R2.fastq -o R1_fixed.fastq.gz -o2 R2_fixed.fastq.gz`
**Explanation:** Outputs fixed files in gzip-compressed format.
