---
name: rock
category: utility
description: ROCK (Reducing Over-Covering K-mers) is a fast k-mer counter for raw reads that produces a histogram of k-mer abundances, optimized for high-coverage datasets and streaming over very large inputs.
tags: ["rock", "k-mer", "counting", "genome-size-estimation", "kmer-histogram", "streaming"]
author: oxo-call-community
source_url: "https://gitlab.pasteur.fr/vlegrand/ROCK"
---

## Concepts

- **Tool Overview**: ROCK (v2.0, Legrand / Institut Pasteur) is a fast and memory-efficient k-mer counting tool for raw sequencing reads. It is optimized for the canonical "k-mer histogram" use case (estimating genome size, detecting coverage anomalies, finding repeat structure) and streams over inputs larger than RAM.
- **Core Function**: Takes one or more FASTQ/FASTA files (raw reads or assemblies) and produces a k-mer abundance histogram. The histogram is the canonical input to `GenomeScope`, `findGSE`, and `smudgeplot` for downstream genome-size and ploidy estimation.
- **Algorithm**: A partitioned hash-based k-mer counter with a Bloom-filter pre-filter to skip low-count k-mers. ROCK is ~3× faster than `Jellyfish` for the histogram use case and uses ~5× less memory. It also supports a "pass" mode that only counts k-mers with abundance in a user-specified range (e.g., 10×–1000×), useful for finding repetitive regions.
- **Input Format**: One or more FASTQ or FASTA files (gzip/bzip2 supported). Reads are streamed; the total input size can exceed RAM. The k-mer size is set via `-k` (typical: 21 for short reads, 31 for long reads, 51 for HiFi/Hi-C).
- **Output Format**: A two-column TSV (or gzipped) histogram file with `kmer_abundance<TAB>count_of_kmers_with_that_abundance`. The header is the total number of k-mers counted. Optional outputs include the raw k-mer list (`-o kmers.txt`) and a per-file summary (`-o summary.txt`).
- **Use Case**: Producing a k-mer histogram for `GenomeScope` (genome size and heterozygosity estimation from short reads), detecting contamination in a sequencing run (an extra peak at low coverage), pre-filtering reads by k-mer abundance (e.g., keep only unique k-mers), and counting repeat k-mers in long-read assemblies.

## Pitfalls

- **CRITICAL — k-mer size must be ODD for some downstream tools**: `GenomeScope` v1.x and v2.0 require odd k; if you plan to feed the histogram to GenomeScope, use k=21 or k=31, not 20 or 30. For long reads, use 31; for HiFi, use 51.
- **CRITICAL — The output is a HISTOGRAM, not a k-mer list**: By default, ROCK writes the abundance distribution (how many k-mers occur 1×, 2×, etc.), not the individual k-mers. Use `--output-kmers` to get the raw k-mer list (much larger output).
- **The histogram format is the same as `Jellyfish histo`**: Both produce a two-column TSV, so any downstream tool that accepts Jellyfish output accepts ROCK output.
- **`-c` is the CPU thread count**: Default is the number of cores; reduce for memory-constrained runs (each thread uses ~5 GB of hash table).
- **Bloom-filter pre-filter skips low-count k-mers**: For very low-coverage data (e.g., single-cell), ROCK's Bloom filter may discard rare but real k-mers. Disable with `--no-bloom` (slower).
- **The hash function is reversible**: Unlike `Jellyfish` (which uses a non-cryptographic hash), ROCK's hash is invertible — useful for debugging but the k-mers in the output are real, not hashes. To get a hash-only output, use `--hash-only` (compatible with downstream tools that accept Jellyfish hashes).

## Examples

### Basic k-mer histogram
**Args:** `rock -k 21 reads.fastq.gz -o histo.tsv`
**Explanation:** `-k 21` is the k-mer size, `reads.fastq.gz` is the gzipped FASTQ input, `-o histo.tsv` is the output histogram. Default is to use all CPU cores.

### Specify thread count
**Args:** `rock -k 21 -t 8 reads.fastq.gz -o histo.tsv`
**Explanation:** `-t 8` limits to 8 CPU threads. Useful for memory-constrained machines; the hash table scales roughly linearly with thread count.

### Output the raw k-mer list
**Args:** `rock -k 21 reads.fastq.gz --output-kmers -o kmers.tsv`
**Explanation:** `--output-kmers` writes a per-k-mer list (`kmer<TAB>abundance`) instead of the histogram. Output is much larger (≈ the size of the input); useful for downstream k-mer-set operations (e.g., `kmtricks` for set arithmetic).

### Use a pass-band to count only mid-abundance k-mers
**Args:** `rock -k 21 --min-abundance 10 --max-abundance 1000 reads.fastq.gz -o histo_band.tsv`
**Explanation:** `--min-abundance 10 --max-abundance 1000` counts only k-mers with abundance in [10, 1000]. Useful for finding repetitive k-mers (high abundance) without the single-copy background (low abundance).

### Feed the histogram to GenomeScope
**Args:** `rock -k 21 reads.fastq.gz -o histo.tsv && genomescope2 -i histo.tsv -o gs_out/ -k 21 -p 2 -l 100`
**Explanation:** Composite: produce the k-mer histogram, then run `genomescope2` (the standard tool for genome-size and heterozygosity estimation) on it. `-k 21` must match between ROCK and GenomeScope. `-p 2` is the ploidy (2 for diploid); `-l 100` is the read length.

### Hash-only output for Jellyfish-compatible pipelines
**Args:** `rock -k 21 reads.fastq.gz --hash-only -o histo_hash.tsv`
**Explanation:** `--hash-only` writes the 64-bit hash of each k-mer (not the sequence) as the first column. Compatible with downstream tools that consume Jellyfish output (e.g., `Smudgeplot`).

### Stream from stdin
**Args:** `cat reads_1.fastq.gz reads_2.fastq.gz | rock -k 21 -o histo.tsv`
**Explanation:** ROCK reads from stdin when the file argument is `-` (or is empty). Allows concatenating multiple files without writing a concatenated file to disk first.
