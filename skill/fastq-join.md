---
name: fastq-join
category: alignment
description: "Similar to audy's stitch program, but in C, more efficient and supports some automatic benchmarking and tuning. It uses the same 'squared distance for anchored alignment' as other tools."
tags: [fastq-join, alignment, paired-end, stitching, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/brwnj/fastq-join"
---

## Concepts

- **Tool Overview**: fastq-join is an efficient C-based tool for joining overlapping paired-end sequencing reads, similar to stitch but with improved performance.
- **Core Function**: Stitches overlapping paired-end reads into longer sequences using anchored alignment.
- **Input/Output**: Input: Paired-end FASTQ files. Output: Joined reads, unjoined reads.
- **Algorithm**: Uses squared distance for anchored alignment to find overlaps.
- **Key Features**: Efficient C implementation, automatic benchmarking, overlap detection, quality-aware joining, paired-end support.
- **Installation**: `conda install -c bioconda fastq-join`

## Pitfalls

- **Overlap Requirements**: Requires sufficient overlap between paired reads.
- **Memory Usage**: Large files may require significant memory.
- **Quality Threshold**: Low-quality reads may affect joining success.
- **Read Length**: Works best with reads of compatible lengths.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic read joining
**Args:** `fastq-join reads_1.fastq reads_2.fastq -o joined.fastq`
**Explanation:** Joins paired-end reads with overlapping regions.

### With quality filtering
**Args:** `fastq-join reads_1.fastq reads_2.fastq -o joined.fastq -q 20`
**Explanation:** Filters by minimum quality score.

### Minimum overlap
**Args:** `fastq-join reads_1.fastq reads_2.fastq -o joined.fastq -m 20`
**Explanation:** Sets minimum overlap length to 20.

### Output unjoined reads
**Args:** `fastq-join reads_1.fastq reads_2.fastq -o joined.fastq -u unjoined.fastq`
**Explanation:** Outputs unjoined reads separately.

### Verbose mode
**Args:** `fastq-join reads_1.fastq reads_2.fastq -o joined.fastq -v`
**Explanation:** Shows detailed progress information.