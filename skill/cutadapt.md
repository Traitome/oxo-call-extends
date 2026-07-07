---
name: cutadapt
category: qc
description: "Cutadapt (v5.2) removes adapter sequences, primers, poly-A tails and low-quality bases from high-throughput sequencing reads (FASTQ/FASTA, single- or paired-end, gzip/bz2/xz auto-detected)."
tags: [cutadapt, qc, adapter-trimming, fastq, fasta, paired-end, primer-trimming, quality-trimming, bioinformatics]
author: oxo-call-community
source_url: "https://cutadapt.readthedocs.io/"
---

## Concepts

- **Tool Overview**: cutadapt (v5.2+, by Marcel Martin) finds and removes adapter, primer, poly-A and low-quality sequences from high-throughput sequencing reads. It uses a dynamic-programming alignment with configurable error tolerance, supports IUPAC wildcards, and auto-detects gzip/bz2/xz compression from file extensions.
- **Core Function**: Per-read adapter matching and trimming. By default only the best-matching adapter (across multiple `-a/-g/-b` specifications) is removed per round; `-n/--times` runs additional rounds.
- **Input/Output**: Input: FASTQ or FASTA (`.fastq`, `.fq`, `.fasta`, `.fa`, with `.gz`/`.xz`/`.bz2`); `-` denotes stdin/stdout. Output: trimmed reads via `-o` (R1) and `-p` (R2); a textual report is always printed, and `--json` writes a machine-readable report.
- **Adapter Types**:
  - `-a ADAPTER`: 3' adapter (3' end of read). Append `$` to anchor at read end (e.g., `-a ADAPTER$`).
  - `-g ADAPTER`: 5' adapter (5' end of read). Prepend `^` to anchor at read start (e.g., `-g ^ADAPTER`).
  - `-b ADAPTER`: 5'/3' "anywhere" adapter (use only when adapter location is unknown).
  - Linked adapters: `-g ^FWD...REV$` trims a forward primer at start and reverse complement of reverse primer at end in one operation.
  - Non-internal: append `X` (3') or prepend `X` (5') to forbid internal matches.
- **Paired-end**: `-A`, `-G`, `-B`, `-U`, `-Q`, `-L` are the R2 counterparts of `-a`, `-g`, `-b`, `-u`, `-q`, `-L`. R1/R2 are always processed as a pair.
- **Quality Trimming**: `-q [5'CUTOFF,]3'CUTOFF` trims low-quality bases from ends (Phred+33 default; `--quality-base=64` for old Illumina). `--nextseq-trim=3'CUTOFF` handles NextSeq two-color chemistry (dark cycles appear as high-quality G).
- **Poly-A Trimming**: `--poly-a` (since v4.4) is the recommended method; older `-a "A{100}"` is slower and less accurate.
- **Filtering**: `-m LEN[:LEN2]` discards too-short reads; `-M` discards too-long; `--max-n`, `--max-ee`, `--max-aer` filter by N content / expected errors; `--discard-trimmed`/`--discard-untrimmed` partition reads by adapter presence.
- **Parallelism**: `-j CORES` (use `-j 0` for auto-detect). Multi-core uses multiprocessing and significantly speeds up large FASTQ files.
- **Installation**: `conda install -c bioconda cutadapt` or `pixi global install cutadapt` (also available via pip: `pip install --user --upgrade cutadapt`).
- **Citation**: Martin M. Cutadapt removes adapter sequences from high-throughput sequencing reads. EMBnet.Journal, 17(1):10-12, 2011. doi:10.14806/ej.17.1.200.

## Pitfalls

- **`-a` is required**: cutadapt refuses to run without at least one adapter (or `--cut`/`--quality-cutoff`/`--poly-a`/`--nextseq-trim`) specified. The error "You need to provide at least one adapter sequence" is the most common first-run failure.
- **Paired-end filter pairing**: Filtering options (`-m`, `-M`, `--discard-*`) always discard both reads of a pair, never just one. Use `--pair-filter={any,both,first}` to control which read triggers the discard.
- **Anchor notation**: `^` (5') and `$` (3') anchor the adapter to the read terminus. Omitting them allows partial internal matches; using them when the adapter is not actually terminal causes silent under-trimming.
- **Random matches at short overlap**: With the default `-O 3`, short adapters may match randomly. Raise `-O` (e.g., `-O 5` or higher) when adapter length permits, to reduce false-positive trimming.
- **Error rate is a fraction, not a count**: `-e 0.1` means 10% errors per alignment, not 0.1 errors. For short adapters use absolute form (`-e 1`) to allow exactly one error over the full length.
- **`-q` default applies to 3' end only**: A single value `-q 20` trims only the 3' end. To trim both ends use `-q 20,20` (5' cutoff first, then 3').
- **`--nextseq-trim` not for other platforms**: It is specifically for NextSeq/NovaSeq two-color chemistry where low-signal bases are called as high-quality G. Using it on HiSeq data wastes data.
- **`-n` may re-trim the same adapter**: When using `-n 2` with multiple `-a` options, the same adapter can be removed twice. Prefer linked adapters or pipe cutadapt twice for independent adapters.
- **Reverse complement not searched by default**: Use `--rc`/`--revcomp` to also search the read's reverse complement (e.g., for adapter dimers or unoriented reads).
- **Output file `{name}` is for demultiplexing only**: Using `{name}` in `-o` without named adapters (`-a name=ADAPTER`) results in an empty output file for unmatched reads.
- **Version drift**: v5.x removed/renamed some v3.x options (e.g., `--format` is mostly a no-op now because format is auto-detected). Always check `cutadapt --version` and `--help` for the installed version.

## Examples

### Trim a 3' adapter from single-end reads
**Args:** `-a AGATCGGAAGAGC -o trimmed.fastq.gz reads.fastq.gz`
**Explanation:** `-a` specifies the 3' Illumina TruSeq adapter; `-o` writes trimmed reads to a gzip file; cutadapt auto-detects `.gz` compression on both input and output. The textual summary report is printed to stderr/stdout.

### Trim paired-end adapters with quality cutoff and minimum length
**Args:** `-a AGATCGGAAGAGC -A GCTCTTCCGATCT -q 20 -m 25 -o r1.trim.fq.gz -p r2.trim.fq.gz r1.fq.gz r2.fq.gz`
**Explanation:** `-A` is the R2 3' adapter; `-q 20` trims 3' bases below Q20 on both reads; `-m 25` discards any pair where either read is <25 bp after trimming (pairs are always discarded together); `-p` is the R2 output.

### Trim anchored 5' primer and 3' adapter (linked)
**Args:** `-g ^ACGTACGTACGT...AGATCGGAAGAGC$ -o out.fq in.fq`
**Explanation:** `^` anchors the 5' primer to the read start; `...` links it to the 3' adapter; `$` anchors the 3' adapter to the read end. Linked adapters remove both primers in one operation without re-trimming.

### Trim amplicon primers from paired-end reads (anchored)
**Args:** `-g ^GTGYCAGCMGCCGCGGTAA -G ^GGACTACNVGGGTWTCTAAT --discard-untrimmed -o r1.fq -p r2.fq r1.in.fq r2.in.fq`
**Explanation:** `^` requires the primer at the start of each read (R1 via `-g`, R2 via `-G`); `--discard-untrimmed` drops pairs lacking the primer (useful for cleaning amplicon libraries where off-target reads should be removed). Anchored primers ensure only true primer sites are trimmed, avoiding internal false matches.

### Trim poly-A tails and quality-trim RNA-seq reads
**Args:** `--poly-a -q 20 -m 18 -o trimmed.fq.gz reads.fq.gz`
**Explanation:** `--poly-a` removes poly-A/poly-T tails (recommended since v4.4, faster and more accurate than `-a "A{100}"`); `-q 20` trims 3' low-quality bases; `-m 18` discards reads shorter than 18 bp. No `-a` adapter is needed because `--poly-a` itself satisfies the "at least one trimming operation" requirement.

### NextSeq two-color chemistry quality trimming
**Args:** `--nextseq-trim=20 -a AGATCGGAAGAGC -o out.fq in.fq`
**Explanation:** `--nextseq-trim=20` trims the 3' end using a NextSeq-aware algorithm that treats high-quality G calls at the end of reads as dark cycles (low signal) and trims them. Combined with `-a` for adapter removal. Use only for NextSeq/NovaSeq data.

### Multi-core trimming with JSON report and demultiplexing
**Args:** `-j 8 -a fwd=^ACGTACGT -a rev=ACGTACGT$ --pair-adapters -o out_{name}_R1.fq -p out_{name}_R2.fq --json report.json R1.fq R2.fq`
**Explanation:** `-j 8` uses 8 CPU cores; named adapters (`fwd=`, `rev=`) populate `{name}` in output filenames for demultiplexing; `--pair-adapters` treats `-a`/`-A` pairs as linked (either both or none are removed); `--json` writes a machine-readable report for pipeline integration.

### Separate trimmed from untrimmed reads (for QC tracking)
**Args:** `-a AGATCGGAAGAGC --untrimmed-output=untrimmed.fq.gz -o trimmed.fq.gz reads.fq.gz`
**Explanation:** `--untrimmed-output` writes reads without an adapter match to a separate file, useful for QC inspection or for re-running with relaxed parameters. Trimmed reads still go to `-o`. For paired-end data, add `--untrimmed-paired-output`.

### Remove multiple independent adapters by piping
**Args:** `cutadapt -g ^ATCGGATC reads.fq.gz | cutadapt -a GCTAGCTA - > trimmed.fq.gz`
**Explanation:** The first cutadapt removes the anchored 5' adapter and streams FASTQ to stdout; the second removes the 3' adapter and writes to a gzip output. This avoids `-n` re-trimming the same adapter and gives independent control over each step's parameters.

### Quickly test how cutadapt trims a single sequence
**Args:** `-a AGATCGGAAGAGC -o - <<< "@read\nAGATCGGAAGAGCAAAAAA\n+\nIIIIIIIIIIIIIIII"`
**Explanation:** Feeds a single dummy read via a bash here-string (`<<<`); `-o -` writes the trimmed read to stdout. Useful for verifying adapter syntax before running on a large file.
