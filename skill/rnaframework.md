---
name: rnaframework
category: utility
description: Modular toolkit for analysing RNA secondary-structure probing (SHAPE, DMS-MaPseq) and post-transcriptional modifications (m6A, pseudouridine, m5C) from HTS data.
tags: ["rnaframework", "shape", "dms-mapseq", "rna-modifications", "m6a", "pseudouridine", "transcriptome"]
author: oxo-call-community
source_url: "https://rnaframework-docs.readthedocs.io/"
---

## Concepts

- **Tool Overview**: RNA Framework (v2.9.6, incarnato-lab) is a Python toolkit for the analysis of RNA structure-probing experiments (SHAPE-seq, DMS-MaPseq, PARS) and post-transcriptional modification mapping (m⁶A, Ψ, m⁵C, m¹A). It provides a single entry point — `rf` — with several subcommands for read mapping, mutation counting, reactivity normalization, structure prediction, and modification calling.
- **Core Function**: Converts raw probing-Seq reads into per-base reactivity scores (or modification-aware mutation rates) and uses them to constrain RNA secondary structure prediction. The output is typically a `.shape` or `.map` reactivity file consumed by RNAfold (`RNAfold --shape`) or RNAstructure (`RNAstructure --SHAPE`).
- **Modular Components**: The six main subcommands are: `rf-index` (build a reference transcriptome index), `rf-map` (read mapping with optional read-quality / adapter trimming), `rf-count` (per-base mutation counting from mapped reads), `rf-norm` (reactivity normalization via the 2%/8% Winsorization method of Deigan et al. / Lavelle et al.), `rf-fold` (constrained folding with RNAfold or RNAstructure), and `rf-modcall` (modification-aware mutation calling, e.g., for m⁶A or Ψ).
- **Input Format**: A reference FASTA + GTF for `rf-index`, paired-end or single-end FASTQ files for `rf-map`, a BAM file (output of `rf-map`) for `rf-count`, and a count file (output of `rf-count`) for `rf-norm`. Modification detection additionally requires a list of candidate positions from `rf-modcall find` or external tools.
- **Output Format**: A combination of BAM (mapped reads), wiggle/BEDGraph (per-base signal), and `.shape`/`.map` reactivity files. RNAstructure and RNAfold consume the reactivity files directly via `--SHAPE` or `--shape`.
- **Use Case**: SHAPE-MaP experiments on SARS-CoV-2 or in-vitro-transcribed mRNAs (RNA vaccine design), DMS-MaPseq of ribosome-bound footprints, m⁶A-miCLIP analysis, and Ψ-induced mutation calling (Pseudo-seq). Also used in chemical probing-guided RNA structure modelling with `RNAfold --shape` or `RNAstructure --SHAPE`.

## Pitfalls

- **CRITICAL — Subcommand first, then options**: `rf` is a multi-tool dispatcher. Running `rf --help` shows the top-level usage, but the meaningful flags (e.g., `-ow` for `rf-norm`) only appear under `rf norm --help`. Always pass the subcommand (`index`, `map`, `count`, `norm`, `fold`, `modcall`) before any flag, otherwise `rf` will print a generic help and exit 1.
- **CRITICAL — `rf-map` requires the right read format for chemistry**: SHAPE-MaP uses 2'-acylation that causes reverse-transcriptase misincorporations; DMS-MaPseq uses double-strand RT-induced mutations. Both must be configured in `rf-map` with the correct mutation-detection parameters (e.g., `--mismatches-only`, `--max-mismatches`). Using the wrong preset silently produces flat reactivity profiles.
- **`rf-index` must be rebuilt for each new reference/GTF pair**: The index is a combined FASTA + GTF; reusing an old index after editing the GTF gives wrong per-transcript coverage statistics in `rf-count`.
- **`rf-norm` requires a minimum of 1000 reactive positions to fit the 2%/8% normalization**: Smaller data sets produce unstable normalization and downstream structures become unreliable. The default in `rf-norm` is to warn and abort; pass `--force` only with caution.
- **Memory in `rf-map` scales with read depth**: A 100M-read SHAPE-MaP library can use 30+ GB of RAM in `rf-map` due to the mutation-aware alignment. Set `--threads` (default 1) and run on a machine with sufficient RAM; on a typical 16-core server expect ~5 GB per thread.
- **`rf-fold` silently falls back to unconstrained folding on parse errors**: If the `.shape` file has a non-numeric token or a position beyond the transcript length, `rf-fold` logs a warning and folds the transcript as if no data were provided, producing the unconstrained MFE structure. Always validate the `.shape` file with `awk 'NF != 2 || $2 !~ /^-?[0-9.]+$/'` before folding.

## Examples

### Build a reference index
**Args:** `rf-index -o transcriptome_index --fasta gencode.v44.transcripts.fa --gtf gencode.v44.annotation.gtf`
**Explanation:** `-o transcriptome_index` is the output directory that will be created; `--fasta` is the transcriptome FASTA (one transcript per record); `--gtf` is the matching annotation GTF. The index is required by all downstream `rf-map` and `rf-count` steps.

### Map SHAPE-MaP reads
**Args:** `rf-map -ct transcriptome_index -ow map.bam -o map.log --mismatches-only reads_R1.fastq.gz reads_R2.fastq.gz`
**Explanation:** `-ct transcriptome_index` is the index from `rf-index`; `-ow` (output-with-overwrite) writes the BAM to `map.bam`; `--mismatches-only` keeps only reads carrying mismatches (the reactive signal), reducing file size 3–10×. Both mate files are required for paired-end SHAPE-MaP libraries.

### Per-base mutation counting
**Args:** `rf-count -ct transcriptome_index -i map.bam -o counts.tsv`
**Explanation:** `-i map.bam` is the BAM from `rf-map`; `-o counts.tsv` is a tab-separated file with per-base read depth, mutation count, and mutation rate across all transcripts. This file is the input to `rf-norm`.

### Reactivity normalization (2%/8% Winsorization)
**Args:** `rf-norm -cm counts.tsv -o normalized.shape --norm-method winsor-2-8`
**Explanation:** `-cm` is the counts file; `--norm-method winsor-2-8` selects the standard 2%/8% Winsorization that bounds the top 2% of reactivities and floors the bottom 8% at zero. Output `normalized.shape` is a two-column (position, reactivity) file consumable by RNAfold/RNAstructure.

### Constrained folding with RNAfold
**Args:** `rf-fold -cm normalized.shape -ct transcriptome_index -o folded_bp -p 8 --engine RNAfold`
**Explanation:** `--engine RNAfold` selects ViennaRNA's RNAfold for the constrained partition-function fold; `-p 8` runs 8 parallel transcript folders. The output `folded_bp` directory contains one CT file per transcript with the SHAPE-constrained MFE structure.

### Call m6A sites from miCLIP data
**Args:** `rf-modcall call -ct transcriptome_index -i bam/*.bam -o m6a_sites.bed --mod-type m6a`
**Explanation:** `--mod-type m6a` selects the m⁶A-specific crosslink-induced truncation-site model. Output `m6a_sites.bed` is a BED file with the DRACH motif context, mutation rate, and per-site q-value. Multiple BAMs can be passed as a glob.

### Find candidate positions for modification calling
**Args:** `rf-modcall find -ct transcriptome_index -i bam/*.bam -o candidates.bed`
**Explanation:** Pre-step for `rf-modcall call`: enumerates candidate modification positions from the crosslink sites across all BAMs. Useful when you want to run `call` on a restricted set of positions rather than scanning the entire transcriptome.

### Whole-pipeline in one script
**Args:** `rf-run.sh -i transcripts.fa -g annotation.gtf -r1 reads_R1.fq.gz -r2 reads_R2.fq.gz -o run/ --chemistry shape-map`
**Explanation:** `rf-run.sh` (provided in the rf-utils companion repo) chains `index`, `map`, `count`, `norm`, and `fold` into a single command. `--chemistry shape-map` auto-configures the mutation parameters for SHAPE-MaP. Equivalent to a Snakemake workflow but lives inside the framework.
