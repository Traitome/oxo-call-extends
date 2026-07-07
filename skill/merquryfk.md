---
name: merquryfk
category: expression
description: Accelerated Merqury using FastK k-mer counter for faster assembly evaluation.
tags: [merquryfk, k-mer-analysis, assembly-validation]
author: oxo-call-community
source_url: "https://github.com/thegenemyers/MERQURY.FK"
---

## Concepts

- **Tool Overview**: MerquryFK is a faster version of Merqury using FastK.
- **Core Function**: Accelerated k-mer-based assembly evaluation.
- **FastK Integration**: Uses FastK for faster k-mer counting.
- **Performance**: Significantly faster than original Merqury.
- **Compatibility**: Compatible with Merqury workflows.
- **Installation**: `conda install -c bioconda merquryfk`

## Pitfalls

- **Memory Requirements**: Still requires significant memory.
- **FastK Dependencies**: Requires FastK installation.
- **Computation Time**: Still slow for very large datasets.
- **k-mer Size**: Optimal k-mer depends on data.
- **Output Format**: Output may differ from Merqury.
- **Version Compatibility**: May not support all Merqury features.

## Examples

### Evaluate assembly
**Args:** `merquryfk.sh assembly.fasta reads.fastq prefix`
**Explanation:** Evaluates assembly with FastK acceleration.

### Build FastK database
**Args:** `fastk -t 16 reads.fastq -k 21 -o kmer_db`
**Explanation:** Builds FastK k-mer database.

### Compute QV
**Args:** `merquryfk qv assembly.fasta kmer_db -o qv.txt`
**Explanation:** Computes quality value quickly.

### Threaded processing
**Args:** `merquryfk.sh -t 16 assembly.fasta reads.fastq prefix`
**Explanation:** Uses 16 threads for faster processing.

### Help documentation
**Args:** `merquryfk.sh --help`
**Explanation:** Displays available options.
