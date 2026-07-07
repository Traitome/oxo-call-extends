---
name: trim-galore
category: utility
description: Trim Galore! - Wrapper around Cutadapt for quality/adapter trimming of FASTQ reads, with RRBS-aware modes.
tags: [trim-galore, adapter-trimming, quality-control, sequencing, bioinformatics, rrbs, cutadapt]
author: oxo-call-community
source_url: "https://github.com/FelixKrueger/TrimGalore"
---

## Concepts

- **Tool Overview**: Trim Galore! is a Perl wrapper around [Cutadapt](https://cutadapt.readthedocs.io/) (and optionally FastQC) that automates quality trimming, adapter trimming, length filtering, and RRBS-specific bias removal in a single invocation.
- **Trimming Pipeline** (per file):
  1. Detect or accept an adapter sequence (default: first 13 bp of Illumina universal adapter `AGATCGGAAGAGC`).
  2. Trim low-quality 3' bases using a Phred threshold (default Q20).
  3. Trim adapter overlaps ≥ `--stringency` (default 1, extremely stringent).
  4. Optionally remove extra bases from the 5'/3' ends (`--clip_R1/R2`, `--three_prime_clip_R1/R2`).
  5. Discard reads shorter than `--length` (default 20 bp; lowered to 18 bp under `--small_rna`).
- **Adapter Auto-Detection**: If no `-a`/`--illumina`/`--nextera`/`--small_rna` is supplied, the first ~1 M reads are scanned and the most likely adapter (Illumina, Nextera, or Small RNA) is inferred from the terminal base composition.
- **RRBS Mode** (`--rrbs`): For MspI-digested RRBS libraries, after adapter trimming an extra 2 bp is removed from the 3' end to avoid the filled-in cytosine introduced during end-repair. In paired-end directional mode, `--rrbs` auto-sets `--clip_R2 2` to mask the corresponding 5' bias of read 2.
- **Non-Directional RRBS** (`--non_directional`): Requires `--rrbs`. Screens adapter-trimmed reads for `CAA` or `CGA` at the 5' end and clips 2 bp there; skips the 3' extra clip when a non-directional start is detected.
- **Paired-End Behavior**: With `--paired`, both reads are validated together. A pair is discarded entirely if **either** read falls below `--length`, unless `--retain_unpaired` is given (surviving single read → `*.unpaired_1.fq` / `*.unpaired_2.fq`).
- **2-Colour Chemistry** (`--2colour`/`--nextseq INT`): For NextSeq/NovaSeq data, calls without signal are emitted as high-quality G. `--nextseq INT` forwards the cutoff to Cutadapt's `--nextseq-trim=3'INT` and ignores G qualities during trimming; mutually exclusive with `-q`.
- **Input**: FASTQ (optionally gzipped). Single-end: one file; paired-end: two files passed in R1,R2 order.
- **Output**: `*_trimmed.fq.gz` (single-end) or `*_val_1.fq.gz` / `*_val_2.fq.gz` (paired-end), a `*_trimming_report.txt`, and (with `--fastqc`) FastQC reports. Use `--basename` for a custom output prefix.
- **Installation**: `conda install -c bioconda trim-galore` (bundles a compatible Cutadapt). Requires `pigz` to gain real speedup from `--cores >1`.
- **Use Case**: Preprocessing before alignment/methylation calling; RRBS/bisulfite-seq bias removal; NextSeq/NovaSeq poly-G trimming; small RNA library trimming.

## Pitfalls

- **Auto-detection is statistical, not authoritative**. The scanner picks the most likely of Illumina/Nextera/Small RNA based on the first ~1 M reads; low-contamination or short libraries can be misclassified. Always verify via the trimming report's "Adapter sequence" line and FastQC's overrepresented-sequence table. If you know the chemistry, pass `--illumina` / `--nextera` / `--small_rna` / `-a` explicitly.
- **`--stringency 1` is extremely aggressive**. A single trailing base matching the adapter is removed, which occasionally clips genuine genomic sequence (especially poly-A tails). For non-bisulfite-seq work, raising `--stringency` to 3–5 reduces false trimming at minimal cost.
- **`--paired` discards both reads if one is too short**. Without `--retain_unpaired`, even one short partner destroys the pair. Set `--retain_unpaired` (and tune `--length_1`/`--length_2`) when downstream tools accept unpaired FASTQ.
- **`--rrbs` is MspI-specific**. Do **not** use it for MseI-digested libraries (e.g., Tecan Ovision RRBS) or enzymatic methyl-seq (EM-seq). The extra 3' clip would corrupt valid methylation calls. For non-MspI bisulfite libraries, omit `--rrbs`.
- **`--non_directional` requires `--rrbs`**. It is not a standalone flag; invoking it alone raises an error. It only makes sense for non-directional MspI RRBS libraries that contain ligated `CAA`/`CGA` starts.
- **Phred encoding mismatch silently corrupts trimming**. Modern Illumina data is Phred+33 (`--phred33`, the default). Older Sanger/Solexa data may need `--phred64`. A wrong encoding makes Q scores off by 31 and triggers massive over- or under-trimming; verify via FastQC's "Per base sequence quality" before/after.
- **`--cores` requires Python 3 + `pigz`**. Trim Galore inspects the Cutadapt Python version; under Python 2 it silently forces `--cores 1`. Without `pigz`, gzip compression reverts to single-threaded `gzip` and erases the multi-core benefit; install `pigz` (`conda install -c bioconda pigz`).
- **`--small_rna` resets `--length` to 18 and sets `-a2`**. Users who explicitly override `--length` after `--small_rna` may unknowingly keep adapters in very short reads. Place `--small_rna` first, then override `--length` only if needed.
- **`--2colour` and `-q` are mutually exclusive**. For NextSeq/NovaSeq poly-G trimming use `--nextseq INT` (or `--2colour INT`); combining with `-q INT` will fail.
- **Output filenames change with `--basename`** but only for single-file or two-file runs; longer file lists ignore `--basename`. Use a shell loop if you need custom names for many files.
- **`--fastqc` runs FastQC after trimming only**. To compare before/after, run `fastqc reads.fq.gz` separately before invoking Trim Galore; `--fastqc_args "--nogroup"` is recommended for long-read libraries.
- **Trim Galore is a wrapper, not the engine**. Parameter interpretation and adapter-matching math come from the bundled Cutadapt; when in doubt about an option's semantics, consult `cutadapt --help` and the Cutadapt docs alongside the Trim Galore report.

## Examples

### Trim single-end Illumina reads with default adapter and Q20
**Args:** `trim_galore --quality 20 --output_dir trimmed/ reads.fastq.gz`
**Explanation:** `--quality 20` (synonym `-q 20`) trims 3' bases below Q20; the adapter is auto-detected (defaults to `AGATCGGAAGAGC` if detection is ambiguous); `--output_dir trimmed/` writes `reads_trimmed.fq.gz` and `reads.fastq.gz_trimming_report.txt` there.

### Trim paired-end reads and retain unpaired survivors
**Args:** `trim_galore --paired --retain_unpaired --length 25 --gzip -j 4 -o trimmed/ r1.fq.gz r2.fq.gz`
**Explanation:** `--paired` validates R1/R2 together; `--retain_unpaired` writes surviving single reads to `*.unpaired_1.fq`/`*.unpaired_2.fq` when a partner drops below `--length 25`; `--gzip` compresses outputs; `-j 4` requests 4 cores (effective only with Python 3 + `pigz`).

### Force Illumina universal adapter and custom stringency
**Args:** `trim_galore --illumina --stringency 3 -q 20 --length 20 reads.fq.gz -o out/`
**Explanation:** `--illumina` overrides auto-detection and uses `AGATCGGAAGAGC` (first 13 bp of Illumina universal adapter); `--stringency 3` requires ≥3 bp overlap before trimming, reducing false positives on poly-A tails.

### Trim Nextera transposase libraries
**Args:** `trim_galore --nextera --paired r1.fq.gz r2.fq.gz -o trimmed/`
**Explanation:** `--nextera` sets the adapter to `CTGTCTCTTATA` (first 12 bp of Nextera adapter), correct for ATAC-seq and Nextera DNA libraries.

### Trim small RNA libraries (single-end)
**Args:** `trim_galore --small_rna --length 18 --max_length 30 -o srna/ srr.fq.gz`
**Explanation:** `--small_rna` sets adapter to `TGGAATTCTCGG` (first 12 bp of Illumina Small RNA 3' Adapter) and lowers the default `--length` to 18; `--max_length 30` discards reads longer than 30 bp after trimming (mature miRNAs are ~22 nt), removing rRNA/tRNA fragments.

### Trim paired-end small RNA (auto-sets R2 adapter)
**Args:** `trim_galore --small_rna --paired srna_R1.fq.gz srna_R2.fq.gz -o srna/`
**Explanation:** `--small_rna` for paired-end auto-assigns `-a2 GATCGTCGGACT` (Illumina small RNA 5' adapter) unless overridden; `--length` defaults to 18 for both reads.

### Trim RRBS (MspI) directional library
**Args:** `trim_galore --rrbs --paired -q 20 -o rrbs_trim/ rrbs_R1.fq.gz rrbs_R2.fq.gz`
**Explanation:** `--rrbs` triggers MspI mode: after adapter/quality trimming, removes an extra 2 bp from the 3' end of adapter-trimmed reads (skipping quality-only-trimmed reads) to discard the end-repair filled-in cytosine; paired-end directional mode also auto-sets `--clip_R2 2` on R2.

### Trim non-directional RRBS library
**Args:** `trim_galore --rrbs --non_directional --length 20 -o rrbs_trim/ rrbs.fq.gz`
**Explanation:** `--non_directional` (requires `--rrbs`) screens adapter-trimmed reads for `CAA`/`CGA` starts; when found, clips 2 bp from the 5' end and skips the 3' extra clip. Correct only for non-directional MspI RRBS libraries.

### NextSeq/NovaSeq poly-G trimming
**Args:** `trim_galore --nextseq 20 --paired -o trimmed/ r1.fq.gz r2.fq.gz`
**Explanation:** `--nextseq 20` (synonym `--2colour 20`) forwards `--nextseq-trim=3'20` to Cutadapt, trimming 3' bases below Q20 while ignoring G qualities (which on 2-colour chemistry represent no-signal basecalls). Mutually exclusive with `-q`.

### Multi-core trimming with custom basename and FastQC
**Args:** `trim_galore --paired --basename sampleA --fastqc --fastqc_args "--nogroup" -j 8 -o out/ r1.fq r2.fq`
**Explanation:** `--basename sampleA` produces `sampleA_val_1.fq`/`sampleA_val_2.fq` instead of input-derived names; `--fastqc` runs FastQC on trimmed reads; `--fastqc_args` passes `--nogroup` to disable binning (recommended for long-read libraries); `-j 8` uses up to 8 cores.

### Clip fixed 5' bases (UMI removal) and 3' bias
**Args:** `trim_galore --paired --clip_R1 6 --clip_R2 6 --three_prime_clip_R1 2 --three_prime_clip_R2 2 -o out/ r1.fq r2.fq`
**Explanation:** `--clip_R1 6` / `--clip_R2 6` remove the first 6 bp of each read (a common inline UMI location); `--three_prime_clip_R1/R2 2` remove 2 bp from the 3' end **after** adapter/quality trimming, mitigating non-adapter end-call bias.

### Hard-trim to a fixed length (no adapter/quality trimming)
**Args:** `trim_galore --hardtrim5 50 reads.fq.gz -o out/`
**Explanation:** `--hardtrim5 50` simply truncates each read to 50 bp from the 5' end and exits, skipping adapter/quality trimming entirely. Useful for sub-sampling or matching a fixed read length for downstream tools.

### Filter reads with too many Ns
**Args:** `trim_galore --max_n 5 --paired r1.fq.gz r2.fq.gz -o out/`
**Explanation:** `--max_n 5` discards any read containing ≥5 N basecalls after trimming (paired: discards the pair). Useful for low-quality lanes with high unresolved-base rates.
