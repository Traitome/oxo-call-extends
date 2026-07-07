---
name: stellar
category: alignment
description: STELLAR is a tool for finding pairwise local alignments between long genomic or very many short sequences.
tags: [stellar, sequence-alignment, local-alignment, seqan]
author: oxo-call-community
source_url: "https://github.com/seqan/seqan/tree/master/apps/stellar/README"
---

## Concepts

- **Tool Overview**: stellar (v1.4.9) is a fast local alignment tool optimized for finding pairwise alignments between long genomic sequences or many short sequences.
- **Core Function**: Performs rapid local alignment using advanced indexing and seed-based approaches.
- **Algorithm**: Uses a seed-and-extend strategy with efficient indexing for fast alignment searching.
- **Input/Output**: Input: FASTA sequences (query and reference); Output: SAM/BAM alignment file or custom format.
- **Performance**: Optimized for both long reads (PacBio/ONT) and short reads (Illumina).
- **Installation**: `conda install -c bioconda stellar` or compile from source with SeqAn.

## Pitfalls

- **Memory Requirements**: Large reference sequences require significant memory.
- **Sensitivity/Speed Tradeoff**: Higher sensitivity settings increase runtime.
- **Input Size**: Very large query sets may require batch processing.
- **Alignment Quality**: Poor quality sequences affect alignment accuracy.
- **Parameter Tuning**: Incorrect parameters affect alignment results.
- **Output Format**: Different output formats have different information content.

## Examples

### Display help
**Args:** `stellar --help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `stellar -i query.fasta -r reference.fasta -o alignment.sam`
**Explanation:** Align query sequences to reference genome.

### With quality filtering
**Args:** `stellar -i query.fasta -r reference.fasta -o alignment.sam -q 20`
**Explanation:** Filter alignments by quality score threshold.

### Multiple query files
**Args:** `stellar -i query1.fasta query2.fasta -r reference.fasta -o alignment.sam`
**Explanation:** Align multiple query files to same reference.

### Verbose mode
**Args:** `stellar -i query.fasta -r reference.fasta -o alignment.sam -v`
**Explanation:** Run with detailed logging for debugging.

### Output BAM format
**Args:** `stellar -i query.fasta -r reference.fasta -o alignment.bam --bam`
**Explanation:** Output alignment in BAM format.

### Custom seed size
**Args:** `stellar -i query.fasta -r reference.fasta -o alignment.sam -s 15`
**Explanation:** Set custom seed size for alignment.

### Threaded execution
**Args:** `stellar -i query.fasta -r reference.fasta -o alignment.sam -t 8`
**Explanation:** Use 8 threads for parallel processing.

### Report only best alignments
**Args:** `stellar -i query.fasta -r reference.fasta -o alignment.sam --best`
**Explanation:** Output only the best alignment per query.
