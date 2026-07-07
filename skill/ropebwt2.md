---
name: ropebwt2
category: utility
description: Incremental construction of the FM-index (Burrows-Wheeler Transform with auxiliary arrays) for DNA sequences, designed for streaming insertion of new sequences and constant-memory indexing of large collections.
tags: ["ropebwt2", "fm-index", "bwt", "burrows-wheeler", "dna-indexing", "streaming"]
author: oxo-call-community
source_url: "https://github.com/lh3/ropebwt2"
---

## Concepts

- **Tool Overview**: ropebwt2 (r187, Heng Li) is a small, fast, constant-memory tool for incrementally constructing the FM-index of a set of DNA sequences. It is the predecessor of `ropebwt3` and uses a "rope" data structure (a balanced binary tree of BWT fragments) to enable O(log n) insertion of new sequences.
- **Core Function**: Takes a set of FASTA/FASTQ files (or stdin) and produces an FM-index file (`.fmd`) and a BWT file. The index is a memory-mapped, seekable representation that can be queried with the companion tool `ropebwt2 memmem` for exact-match search.
- **Algorithm**: A "rope" representation of the BWT — a binary tree where each leaf is a small BWT fragment, and internal nodes are concatenations. New sequences are inserted by finding the appropriate leaf (via a binary search on the cumulative length) and rebalancing. The auxiliary arrays (SA sampling, occurrence counts) are stored alongside the BWT in a single file.
- **Input Format**: One or more FASTA/FASTQ files, or stdin (piped from a list, e.g., `cat *.fa | ropebwt2`). The input is streamed; total input size can exceed RAM. Each sequence is treated as a separate "document" (a separate record in the index), separated by a special sentinel character.
- **Output Format**: A single `.fmd` file (the FM-index) and a `.bwt` file (the raw Burrows-Wheeler Transform). The `.fmd` is memory-mappable; the `.bwt` is the human-readable BWT. Optional `-s` flag emits a suffix array sample for faster `memmem` queries.
- **Use Case**: Building an FM-index of a large collection (e.g., all RefSeq bacterial genomes, all human transcripts) for exact-match queries, supporting long-read aligners that stream references (e.g., `minimap2`'s `ropebwt2` integration), and indexing a custom genome collection for downstream BWA-MEM or Bowtie2 mapping.

## Pitfalls

- **CRITICAL — ropebwt2 is DNA-only**: RNA sequences must be reverse-complemented and T-replaced-with-U (or U-replaced-with-T) before indexing. The tool does not handle ambiguous bases beyond A/C/G/T/N; non-ACGTN characters cause a silent skip.
- **CRITICAL — The `.fmd` file is platform-dependent**: The FM-index is byte-order and word-size dependent; an index built on a little-endian x86-64 machine is not portable to big-endian ARM. Use `ropebwt2 -d` (decompress) to recover the original BWT for portability.
- **`-m` is the maximum memory for the in-memory rope**: Default is 1 GB; reduce for memory-constrained machines (slower for large inputs), increase for faster indexing.
- **ropebwt2 is superseded by `ropebwt3`**: For new pipelines, use ropebwt3; ropebwt2 is maintained for compatibility with older `minimap2` versions.
- **No support for quality scores or read names**: The input is treated as a sequence stream; if a FASTQ's quality scores matter, the output is not useful (ropebwt2 only stores the BWT, not the quality).
- **`memmem` is for exact-match search only**: For approximate search (allowing mismatches/indels), use a dedicated aligner (BWA-MEM, Bowtie2, minimap2). The companion `memmem` is for finding exact k-mers in the index.

## Examples

### Build an FM-index from FASTA files
**Args:** `ropebwt2 -o index.fmd genome1.fa genome2.fa genome3.fa`
**Explanation:** `-o index.fmd` is the output FM-index file. Multiple input FASTA files are concatenated and indexed as a single collection. The output `.fmd` is memory-mappable and can be queried with `ropebwt2 memmem`.

### Build from stdin
**Args:** `cat *.fa | ropebwt2 -o index.fmd`
**Explanation:** Pipes the concatenation of all `*.fa` files to ropebwt2. Useful for indexing a large collection without writing an intermediate concatenation.

### Decompress to BWT
**Args:** `ropebwt2 -d -o bwt.txt index.fmd`
**Explanation:** `-d` decompresses the FM-index to the raw Burrows-Wheeler Transform text. Output `bwt.txt` is a single string of length equal to the total input size.

### Limit memory usage
**Args:** `ropebwt2 -m 500M -o index.fmd large_genome.fa`
**Explanation:** `-m 500M` sets the in-memory rope size to 500 MB. For very large inputs (e.g., a 3 Gbp human genome), this is 5–10× slower than the default 1 GB; reduce further for memory-constrained machines.

### Exact-match search
**Args:** `ropebwt2 memmem index.fmd "ACGTACGT"`
**Explanation:** `memmem` (a companion subcommand) finds exact occurrences of the pattern `ACGTACGT` in the index. Output is a list of (sequence_id, position) pairs. Useful for finding the location of a known sequence in a collection.

### Build a suffix array sample
**Args:** `ropebwt2 -s -o index.fmd *.fa`
**Explanation:** `-s` samples the suffix array for faster `memmem` queries. Increases the index size by ~10%, but speeds up exact searches by 5–10×.
