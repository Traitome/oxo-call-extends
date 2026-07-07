---
name: ropebwt3
category: utility
description: Successor to ropebwt2; constructs the FM-index of a large DNA sequence collection using a hierarchical BWT with improved insertion performance and built-in exact-match search via `ropebwt3 memmem`.
tags: ["ropebwt3", "fm-index", "bwt", "burrows-wheeler", "dna-indexing", "hierarchical-bwt"]
author: oxo-call-community
source_url: "https://github.com/lh3/ropebwt3/blob/v3.10/README.md"
---

## Concepts

- **Tool Overview**: ropebwt3 (v3.10, Heng Li) is the successor to `ropebwt2` for incrementally constructing the FM-index of a large DNA sequence collection. It uses a hierarchical BWT (a multi-level rope) that is faster to insert and query, and includes a built-in `memmem` subcommand for exact-match search.
- **Core Function**: Takes a set of FASTA/FASTQ files (or stdin) and produces an FM-index file (`.fmd`) and a BWT file. The hierarchical design reduces the rebalancing overhead of the original rope, making it 2–5× faster on large collections (e.g., a multi-Gbp pangenome).
- **Algorithm**: A hierarchical BWT is a multi-level rope where each level is a balanced BWT of the level below. Insertion of a new sequence is O(log² n) instead of O(log n), and the per-level balancing is amortized. The auxiliary arrays (SA, occurrence) are stored per-level and merged at query time.
- **Input Format**: One or more FASTA/FASTQ files, or stdin (piped). The input is streamed; total input size can exceed RAM. Each FASTA record is a separate document in the index. Ambiguous bases (N) are stored as a separate "non-ACGT" class.
- **Output Format**: A single `.fmd` file (the FM-index) and a `.bwt` file (the raw BWT). The `.fmd` is memory-mappable. Optional `-s` flag emits a suffix array sample for faster `memmem`. The `ropebwt3 memmem` subcommand queries the index.
- **Use Case**: Building an FM-index of a large pangenome reference (the canonical use case for graph-based long-read aligners), indexing a custom genome collection for BWA-MEM / Bowtie2 mapping, supporting streaming long-read alignment with `minimap2` (which has a `ropebwt3` integration in recent versions), and constructing per-sample indexes for a metagenomic study.

## Pitfalls

- **CRITICAL — ropebwt3 is DNA-only**: RNA sequences must be reverse-complemented and T↔U substituted before indexing. The tool does not handle non-ACGTN characters; the entire record is silently skipped.
- **CRITICAL — The `.fmd` format is incompatible with `ropebwt2`**: An index built with ropebwt3 cannot be queried with ropebwt2's `memmem`, and vice versa. Pick one tool for the entire pipeline.
- **`-H` is the hierarchy depth**: Default is auto-detected from the input size; for very large inputs (> 100 Gbp), set `-H 5` explicitly. Each level adds ~5% overhead to queries but reduces insertion time.
- **`-m` is the maximum memory for the in-memory rope**: Default is 1 GB. For very large inputs (> 100 Gbp), increase to 4–8 GB (`-m 4G`) for faster indexing.
- **The index file is NOT sorted by default**: ropebwt3 preserves the input order; if you need the documents in alphabetical order (e.g., for some downstream tools that expect a sorted index), sort the input FASTA with `seqkit sort`.
- **No approximate matching**: `memmem` is exact-match only. For approximate matching (allowing mismatches/indels), use a dedicated aligner.

## Examples

### Build an FM-index from a directory of FASTA files
**Args:** `ropebwt3 -o pangenome.fmd *.fa`
**Explanation:** `-o pangenome.fmd` is the output FM-index. The glob `*.fa` includes all FASTA files in the current directory. For a pangenome reference (e.g., 100 bacterial genomes), the index is built in minutes.

### Build from stdin
**Args:** `find genomes/ -name "*.fa" -exec cat {} + | ropebwt3 -o pangenome.fmd`
**Explanation:** Concatenates all FASTA files in `genomes/` via `find` and pipes to ropebwt3. Useful for very large collections where a glob exceeds shell argument limits.

### Specify hierarchy depth
**Args:** `ropebwt3 -H 5 -o large.fmd all_genomes.fa`
**Explanation:** `-H 5` sets the hierarchy depth to 5. For inputs > 100 Gbp, this reduces insertion time by 30–50% at the cost of slightly slower `memmem` queries.

### Limit memory usage
**Args:** `ropebwt3 -m 500M -o index.fmd large.fa`
**Explanation:** `-m 500M` sets the in-memory rope size to 500 MB. Reduces RAM usage at the cost of slower indexing. For very small machines, reduce further to `-m 200M`.

### Decompress to BWT
**Args:** `ropebwt3 -d -o bwt.txt index.fmd`
**Explanation:** `-d` decompresses the FM-index to the raw BWT text. Output `bwt.txt` is a single string of length equal to the total input size.

### Exact-match search via memmem
**Args:** `ropebwt3 memmem index.fmd "ACGTACGT" 5`
**Explanation:** `memmem` finds exact occurrences of the pattern `ACGTACGT` in the index; the trailing `5` requests up to 5 hits. Output is a list of (sequence_id, position) pairs per line. Useful for finding the location of a known sequence in a pangenome.

### Build a suffix array sample
**Args:** `ropebwt3 -s -o index.fmd *.fa && ropebwt3 memmem index.fmd "ACGTACGT" 100`
**Explanation:** `-s` builds a suffix array sample for faster `memmem` queries. The composite example shows a search that returns up to 100 hits.
