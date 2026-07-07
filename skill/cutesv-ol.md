---
name: cutesv-ol
category: annotation
description: "cuteSV-OL: real-time structural variation detection for nanopore sequencing"
tags: [cutesv-ol, annotation, structural-variants, nanopore, real-time]
author: oxo-call-community
source_url: "https://github.com/gwmHIT/cuteSV-OL"
---
## Concepts

- **Tool Overview**: cutesv-ol (v1.0.2+) is a real-time structural variation detection tool optimized for nanopore sequencing data.
- **Core Function**: Detects structural variants from nanopore reads in real-time during sequencing.
- **Input/Output**: Input: Fast5 raw signal files or base-called FASTQ. Output: SV calls, real-time reports.
- **Algorithm**: Uses signal-level analysis and alignment-based methods for rapid SV detection.
- **Key Features**: Real-time analysis, optimized for nanopore data, supports live sequencing.
- **Installation**: `conda install -c bioconda cutesv-ol`

## Pitfalls

- **Nanopore Specific**: Designed specifically for nanopore sequencing data.
- **Real-Time Requirements**: Requires streaming data or fast processing pipelines.
- **Basecalling**: Raw signal analysis requires appropriate basecalling parameters.
- **Accuracy**: Real-time detection may have lower accuracy than post-sequencing analysis.
- **Memory Usage**: Real-time processing requires efficient memory management.

## Examples

### Real-time SV detection
**Args:** `cutesv-ol -i streaming_reads.fastq -r reference.fasta -o realtime_svs.vcf`
**Explanation:** Perform real-time structural variant detection during sequencing.

### Analyze base-called reads
**Args:** `cutesv-ol -i basecalled.fastq -r reference.fasta -o sv_calls.vcf`
**Explanation:** Detect SVs from base-called nanopore reads.

### Set confidence threshold
**Args:** `cutesv-ol -i reads.fastq -r reference.fasta -o svs.vcf --confidence 0.9`
**Explanation:** Filter SV calls to minimum confidence score of 0.9.
