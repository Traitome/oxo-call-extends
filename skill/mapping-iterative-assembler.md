---
name: mapping-iterative-assembler
category: alignment
description: Consensus calling or reference assisted assembly, chiefly of ancient mitochondria.
tags: [mapping-iterative-assembler, alignment, ancient-DNA, assembly]
author: oxo-call-community
source_url: "https://github.com/mpieva/mapping-iterative-assembler"
---

## Concepts

- **Tool Overview**: mapping-iterative-assembler v1.0 - Performs consensus calling and reference-assisted assembly, primarily designed for ancient mitochondrial DNA.
- **Core Function**: Iteratively maps reads to reference and builds consensus sequences for ancient DNA analysis.
- **Input/Output**: Input: FASTQ reads, reference genome; Output: Consensus sequence, alignment statistics.
- **Installation**: `conda install -c bioconda mapping-iterative-assembler`
- **Iterative Mapping**: Uses iterative mapping approach for improved consensus accuracy.
- **Ancient DNA Optimization**: Specifically optimized for ancient DNA data.

## Pitfalls

- **Read Quality**: Poor quality ancient DNA reads affect assembly.
- **Reference Bias**: Reference genome choice affects consensus.
- **Contamination**: Modern DNA contamination affects results.
- **Coverage**: Low coverage affects consensus accuracy.
- **Damage Patterns**: Ancient DNA damage patterns may affect base calling.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Run iterative assembly
**Args:** `mia -r ref.fa -f reads.fastq -o consensus.fasta`
**Explanation:** Performs iterative mapping and consensus calling.

### Paired-end reads
**Args:** `mia -r ref.fa -1 reads_1.fastq -2 reads_2.fastq -o consensus.fasta`
**Explanation:** Processes paired-end reads.

### With quality filtering
**Args:** `mia -r ref.fa -f reads.fastq -o consensus.fasta -q 30`
**Explanation:** Filters reads with quality < 30.

### Verbose mode
**Args:** `mia -r ref.fa -f reads.fastq -o consensus.fasta -v`
**Explanation:** Provides detailed logging during assembly.

### Multiple iterations
**Args:** `mia -r ref.fa -f reads.fastq -o consensus.fasta -i 10`
**Explanation:** Runs 10 iterations of mapping.

### Generate statistics
**Args:** `mia -r ref.fa -f reads.fastq -o consensus.fasta --stats stats.txt`
**Explanation:** Generates assembly statistics.