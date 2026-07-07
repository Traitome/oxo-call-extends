---
name: hyplas
category: assembly
description: HyPlAs - Hybrid long-read short-read plasmid assembler
tags: [hyplas, plasmid assembly, hybrid assembly]
author: oxo-call-community
source_url: "https://github.com/cchauve/hyplas"
---

## Concepts

- **Tool Overview**: HyPlAs is a hybrid assembly pipeline specifically designed to assemble plasmids from hybrid bacterial sequencing datasets.
- **Contig Classification**: Incorporates prior classification of short-read contigs as chromosomal or plasmidic.
- **Multi-tool Integration**: Combines SPAdes, minimap2, miniasm, minigraph, racon, and platon for optimal results.
- **Long-read Support**: Works with Oxford Nanopore and PacBio long reads.
- **Plasmid Recovery**: Specialized in recovering complete plasmid sequences from bacterial genomes.
- **Installation**: `conda install -c bioconda hyplas`

## Pitfalls

- **Input Requirements**: Requires both short reads and long reads for hybrid assembly.
- **Reference Quality**: Plasmid classification accuracy depends on reference databases.
- **Memory Usage**: Assembling large plasmids may require significant memory.
- **Contamination**: Host DNA contamination can affect assembly quality.
- **Parameter Tuning**: Optimal parameters may vary by dataset.
- **Circularization**: Ensuring proper circularization of plasmids requires careful validation.

## Examples

### Basic hybrid plasmid assembly
**Args:** `hyplas --short1 reads_R1.fastq.gz --short2 reads_R2.fastq.gz --long long_reads.fastq.gz --output plasmids/`
**Explanation:** Assembles plasmids using both short and long reads.

### Long-read only assembly
**Args:** `hyplas --long long_reads.fastq.gz --output plasmids/ --no_short`
**Explanation:** Runs plasmid assembly using only long reads.

### Specify k-mer size
**Args:** `hyplas --short1 R1.fastq --short2 R2.fastq --long long.fastq -k 31 --output plasmids/`
**Explanation:** Uses k-mer size of 31 for assembly.

### Thread configuration
**Args:** `hyplas --short1 R1.fastq --short2 R2.fastq --long long.fastq -t 16 --output plasmids/`
**Explanation:** Runs assembly with 16 threads.

### Debug mode
**Args:** `hyplas --short1 R1.fastq --short2 R2.fastq --long long.fastq --debug --output plasmids/`
**Explanation:** Retains intermediate files for debugging.