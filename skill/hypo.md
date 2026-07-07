---
name: hypo
category: polishing
description: HyPo - Super Fast and Accurate Polisher for Long Read Genome Assemblies
tags: [hypo, genome polishing, long reads]
author: oxo-call-community
source_url: "https://github.com/kensung-lab/hypo"
---

## Concepts

- **Tool Overview**: HyPo is a hybrid polisher that utilizes both short and long reads to polish long-read genome assemblies.
- **K-mer Based**: Exploits unique genomic k-mers to selectively polish segments of contigs.
- **Partial Order Alignment**: Uses partial order alignment of selective read-segments for accurate polishing.
- **Performance**: Significantly faster than Racon with lower memory requirements.
- **Hybrid Approach**: Combines the accuracy of short reads with the context of long reads.
- **Installation**: `conda install -c bioconda hypo`

## Pitfalls

- **Input Requirements**: Requires both short reads and long reads for hybrid polishing.
- **Assembly Quality**: Polishing effectiveness depends on initial assembly quality.
- **K-mer Selection**: Appropriate k-mer size selection is critical.
- **Memory Usage**: Still requires significant memory for large genomes.
- **Read Quality**: Low-quality reads can introduce errors during polishing.
- **Parameter Tuning**: May require parameter adjustment for optimal results.

## Examples

### Basic hybrid polishing
**Args:** `hypo -a assembly.fasta -l long_reads.fastq -s short_reads.fastq -o polished.fasta`
**Explanation:** Polishes assembly using both long and short reads.

### Long-read only polishing
**Args:** `hypo -a assembly.fasta -l long_reads.fastq -o polished.fasta`
**Explanation:** Polishes using only long reads.

### Short-read only polishing
**Args:** `hypo -a assembly.fasta -s short_reads.fastq -o polished.fasta`
**Explanation:** Polishes using only short reads.

### Custom k-mer size
**Args:** `hypo -a assembly.fasta -l long_reads.fastq -s short_reads.fastq -k 31 -o polished.fasta`
**Explanation:** Uses k-mer size of 31 for polishing.

### Thread configuration
**Args:** `hypo -a assembly.fasta -l long_reads.fastq -s short_reads.fastq -t 16 -o polished.fasta`
**Explanation:** Runs polishing with 16 threads.