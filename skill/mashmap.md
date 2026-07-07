---
name: mashmap
category: alignment
description: A fast approximate aligner for long DNA sequences using MinHash.
tags: [mashmap, alignment, MinHash, long reads]
author: oxo-call-community
source_url: "https://github.com/marbl/MashMap"
---

## Concepts

- **Tool Overview**: mashmap is a fast approximate aligner optimized for long DNA sequences using MinHash-based mapping.
- **Core Function**: Identifies homologous regions between query and reference sequences efficiently.
- **MinHash Sketches**: Uses MinHash to create compact representations of sequences for rapid similarity estimation.
- **Approximate Mapping**: Provides fast alignment by leveraging locality-sensitive hashing techniques.
- **Input/Output**: Accepts FASTA/Q files as input, produces SAM/BAM or PAF format alignments.
- **Installation**: `conda install -c bioconda mashmap` or `git clone https://github.com/marbl/MashMap.git`

## Pitfalls

- **Approximation Trade-off**: Speed comes at the cost of some sensitivity; may miss some alignments.
- **Memory Requirements**: High memory usage for large reference genomes; consider splitting large inputs.
- **Index Building**: Reference sequences must be indexed first with `mashmap -b` before mapping.
- **Sequence Length**: Optimal for long reads (>1kb); may not perform well on short reads.
- **Parameter Tuning**: Requires careful adjustment of `-k` (k-mer size) and `-s` (sketch size) for different data types.
- **Output Format**: Default output may need conversion for downstream tools like SAMtools.

## Examples

### Build reference index
**Args:** `mashmap -b ref.fasta -o ref_index`
**Explanation:** Builds MinHash index for reference sequences.

### Map long reads
**Args:** `mashmap -r ref.fasta -q reads.fastq -o alignments.paf`
**Explanation:** Maps query reads against reference, outputs PAF format.

### Output SAM format
**Args:** `mashmap -r ref.fasta -q reads.fastq -s -o alignments.sam`
**Explanation:** Produces SAM format output for compatibility with standard tools.

### Adjust k-mer size
**Args:** `mashmap -r ref.fasta -q reads.fastq -k 32 -o alignments.paf`
**Explanation:** Uses 32-mer size for MinHash computation.

### Parallel processing
**Args:** `mashmap -r ref.fasta -q reads.fastq -t 8 -o alignments.paf`
**Explanation:** Uses 8 threads for parallel mapping.

### Multiple query files
**Args:** `mashmap -r ref.fasta -q reads1.fq reads2.fq -o alignments.paf`
**Explanation:** Processes multiple query files simultaneously.
