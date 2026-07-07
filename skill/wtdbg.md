---
name: wtdbg
category: bioinformatics
description: wtdbg2 - Fast de novo assembler for long noisy reads (PacBio RSII/Sequel/CCS, Oxford Nanopore) using a Fuzzy Bruijn Graph.
tags: [wtdbg, wtdbg2, genome-assembly, long-read, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/ruanjue/wtdbg2"
---

## Concepts

- **Tool Overview**: wtdbg2 is a *de novo* sequence assembler for long noisy reads produced by PacBio (RSII, Sequel, CCS/HiFi) or Oxford Nanopore Technologies (ONT). It assembles raw reads without prior error correction and then derives consensus from intermediate layout output. Only runs on 64-bit Linux.
- **Core Algorithm — Fuzzy Bruijn Graph (FBG)**: wtdbg2 chops reads into 1024 bp segments, merges similar segments into a vertex, and connects vertices based on segment adjacency on reads. FBG is akin to a De Bruijn graph but permits mismatches/gaps and keeps read paths when collapsing k-mers. This is what distinguishes wtdbg2 from most other long-read assemblers.
- **Two Components**:
  - **`wtdbg2`** — the assembler. Reads raw long reads and produces a contig layout file `<prefix>.ctg.lay.gz` (and edge sequences).
  - **`wtpoa-cns`** — the consensus tool. Takes the layout file (or sorted SAM) and produces the final FASTA consensus. A faster but less accurate alternative `wtdbg-cns` is also bundled.
- **Standard Workflow**:
  1. `wtdbg2 -x <preset> -g <gsize> -i reads.fa.gz -fo <prefix>` — assemble.
  2. `wtpoa-cns -t <threads> -i <prefix>.ctg.lay.gz -fo <prefix>.ctg.fa` — derive consensus.
  3. Polish with long reads: `minimap2 -ax map-pb/-map-ont <prefix>.raw.fa reads.fa.gz | samtools sort > polish.bam`, then `wtpoa-cns -d <prefix>.raw.fa -i polish.bam -fo <prefix>.cns.fa`.
  4. (Optional) Polish with short reads: `bwa mem` + `wtpoa-cns -x sam-sr -d <prefix>.cns.fa -i - -fo <prefix>.srp.fa`.
- **Presets (`-x`)** — apply `-x` BEFORE other parameters since it sets multiple options:
  - `preset1` / `rsII` / `rs`: `-p 21 -S 4 -s 0.05 -L 5000` (PacBio RSII).
  - `preset2`: `-p 0 -k 15 -AS 2 -s 0.05 -L 5000`.
  - `preset3`: `-p 19 -AS 2 -s 0.05 -L 5000`.
  - `sequel` / `sq`: same as `preset3` (PacBio Sequel).
  - `nanopore` / `ont`: `preset2` for genome size <1G, `preset3` for >=1G.
  - `preset4` / `corrected` / `ccs`: `-p 21 -k 0 -AS 4 -K 0.05 -s 0.5` (PacBio CCS / corrected reads).
- **K-mer Selection**: wtdbg2 combines normal k-mers (`-k`, 0–23) and homopolymer-compressed (HPC) k-mers (`-p`, 0–23). Constraint: `k + p <= 25`. The seed is `<k-mer>+<p-homopolymer-compressed>`. Default `-p 21`. For ONT data the preset sets `-p 0 -k 15` (small genome) or `-p 19` (large genome).
- **K-mer Filtering and Subsampling**:
  - `-K <float>` (default `1000.05`): filters high-frequency k-mers (likely repetitive). Threshold: count >= 1000 AND index >= (1 − 0.05) × total_kmers.
  - `-S <float>` (default `4.00`): subsamples 1/S of all k-mers by hashcode. Greatly reduces memory and runtime at the cost of less matched length.
- **Read Length and Depth Controls**:
  - `-L <int>`: filter reads shorter than `<int>`; 5000 recommended for PacBio. Negative value also tidies read names.
  - `-g <number>`: approximate genome size (k/m/g suffix).
  - `-X <float>`: subsample to best `<float>` depth from input (default 50; effective only with `-g`).
- **Edge and Alignment Controls**: `-e <int>` (default 3) minimum read depth of a valid edge; `-s <float>` (default 0.05) minimum similarity (matched k-mer length / aligned length); `-l <float>` (default 2048) min alignment length; `-m <float>` (default 200) min matched length.
- **Low-Coverage Helpers**: `-A` keeps contained reads during alignment (helps low-coverage data at cost of performance); reducing `-S` increases matched length (but also memory).
- **Realignment Mode**: `-R` enables re-alignment using HPC k-mers (`--realn-kmer-psize=15`, `--realn-kmer-subsampling=1`, lower similarity threshold 0.1) for refining the graph.
- **`wtpoa-cns` Modes**:
  - Layout mode: `-i <prefix>.ctg.lay.gz` (default input).
  - SAM/reference mode: `-d <ref.fa> -i sorted.bam` — refines consensus using alignments.
  - Short-read polishing: `-x sam-sr -d <ref.fa> -i -` (reads SAM from stdin).
  - `-c 0` (default) run-length consensus; `-c 1` dp-call-cns mode.
- **Resource Usage (from official README)**: E. coli 20x PacBio ~1 GB RAM; C. elegans 80x ~11.6 GB; D. melanogaster 32x ONT ~17.3 GB; Human 36x ONT ~221.8 GB; Human 28x CCS ~112.9 GB; Axolotl 32x PacBio ~1788 GB.
- **Known Limitation**: For Nanopore data, wtdbg2 may produce an assembly smaller than the true genome size.
- **Citation**: Ruan & Li (2019) Fast and accurate long-read assembly with wtdbg2. *Nat Methods* doi:10.1038/s41592-019-0669-3.

## Pitfalls

- **`-x` preset must come first**: The `-x` flag sets multiple parameters (`-p`, `-k`, `-S`, `-s`, `-L`, etc.) and must be applied BEFORE other options, otherwise your overrides will be clobbered by the preset defaults.
- **ONT assemblies may be undersized**: wtdbg2 is known to produce assemblies smaller than the true genome for Nanopore data. Validate with QUAST or Merqury and consider hifiasm/Flye if contiguity is critical.
- **k-mer size constraint `k + p <= 25`**: Exceeding this hard limit will cause the assembler to fail or produce incorrect results. The preset values are within range; custom tuning must respect this.
- **Huge memory for large genomes**: A 3 Gb human ONT assembly needs ~220 GB RAM; the 32 Gb Axolotl genome needs ~1.8 TB. Plan node selection carefully, or use `-S` to subsample k-mers at the cost of sensitivity.
- **Input file order matters**: When mixing FASTA and FASTQ inputs, place FASTQ first, then FASTA. Otherwise wtdbg2 cannot detect `>` in FASTQ and will concatenate all FASTQ records into a single read.
- **`-X` only works with `-g`**: The depth subsampling option `-X` is effective only when `-g` is set. Without `-g`, all reads are used regardless of `-X`.
- **`-K` uses combined threshold**: k-mer filtering triggers when count >= 1000 AND the index fills past 95% of total k-mers. Adjust both `-K` integer (count) and the fractional part (index fraction) together.
- **No HiFi-specific optimization**: wtdbg2's `ccs` preset exists but the tool was designed for raw noisy reads. For PacBio HiFi, hifiasm or Verkko typically yield better T2T-grade assemblies.
- **`wtpoa-cns` reads from STDIN by default**: If you forget `-i`, it will hang waiting for input. Always specify `-i <file>` or pipe in.
- **`-d` for reference mode is mandatory for SAM polishing**: When using `wtpoa-cns -i sorted.bam`, you MUST also pass `-d <ref.fa>`; otherwise the consensus will be computed in layout mode with empty reference.
- **Consensus is not high-accuracy**: `wtpoa-cns` is intentionally tuned for speed; the README states it does not aim for high-accuracy consensus. Always follow with minimap2/Racon/Medaka polishing.
- **Negative `-L` renames reads**: `-L -5000` filters reads <5000 bp AND renames them to `S%010d` format. Use the positive form (`-L 5000`) if you want to preserve original read names.
- **`wtdbg2.pl` wrapper not always installed**: The convenience wrapper script `wtdbg2.pl` is part of the source tree but may not be copied to PATH by binary packages. Call `wtdbg2` and `wtpoa-cns` directly if the wrapper is missing.

## Examples

### Minimal ONT assembly (small genome <1G)
**Args:** `wtdbg2 -x ont -g 4.6m -i reads.fastq.gz -fo asm -t 16`
**Explanation:** `-x ont` selects the ONT preset (`-p 0 -k 15 -AS 2 -s 0.05 -L 5000` for small genomes); `-g 4.6m` estimates a 4.6 Mb genome (e.g., E. coli); `-fo asm` sets output prefix. Produces `asm.ctg.lay.gz`.

### PacBio Sequel assembly
**Args:** `wtdbg2 -x sq -g 125m -i reads.fastq.gz -fo asm -t 32 -L 5000`
**Explanation:** `-x sq` (alias for `preset3`: `-p 19 -AS 2 -s 0.05 -L 5000`); `-g 125m` targets a 125 Mb genome (e.g., A. thaliana); `-L 5000` explicitly drops reads shorter than 5 kb (recommended for PacBio).

### PacBio CCS / HiFi assembly
**Args:** `wtdbg2 -x ccs -g 3g -i hifi.fastq.gz -fo asm -t 32`
**Explanation:** `-x ccs` (alias `preset4`): `-p 21 -k 0 -AS 4 -K 0.05 -s 0.5`. Uses HPC k-mers only (no normal k-mer) with higher similarity (0.5) suited to high-accuracy CCS reads. Note: hifiasm/Verkko often outperform wtdbg2 on HiFi.

### Derive consensus from layout
**Args:** `wtpoa-cns -t 16 -i asm.ctg.lay.gz -fo asm.ctg.fa`
**Explanation:** Converts the wtdbg2 layout file into a FASTA consensus. This is step 2 of the standard workflow and is required after every `wtdbg2` run.

### Full workflow: assemble + consensus + long-read polish
**Args:** `wtdbg2 -x ont -g 3g -i reads.fastq.gz -fo asm -t 31 && wtpoa-cns -t 31 -i asm.ctg.lay.gz -fo asm.raw.fa && minimap2 -t 31 -ax map-ont -r2k asm.raw.fa reads.fastq.gz | samtools sort -@ 8 > asm.bam && samtools view -F0x900 asm.bam | wtpoa-cns -t 31 -d asm.raw.fa -i - -fo asm.cns.fa`
**Explanation:** Assembles (step 1), derives raw consensus (step 2), aligns raw reads back with `minimap2 -r2k` (step 3), and polishes with `wtpoa-cns -d` in reference mode (step 4). `-F0x900` filters secondary/supplementary alignments before consensus.

### Add short-read polishing
**Args:** `bwa index asm.cns.fa && bwa mem -t 16 asm.cns.fa sr.R1.fq sr.R2.fq | samtools sort -O SAM | wtpoa-cns -t 16 -x sam-sr -d asm.cns.fa -i - -fo asm.srp.fa`
**Explanation:** Indexes the consensus with `bwa index`, aligns paired-end short reads with `bwa mem`, pipes sorted SAM into `wtpoa-cns` with `-x sam-sr` (short-read preset). Output `asm.srp.fa` is the short-read-polished assembly.

### Subsample reads to best 30x depth
**Args:** `wtdbg2 -x ont -g 3g -X 30 -i reads.fastq.gz -fo asm -t 16`
**Explanation:** `-X 30` keeps only the best 30x of read depth (effective only with `-g`). Useful when coverage is excessively high (>60x) to save runtime and memory without sacrificing much contiguity.

### Custom k-mer tuning for low coverage
**Args:** `wtdbg2 -x ont -g 100m -S 2 -e 2 -A -i reads.fastq.gz -fo asm -t 32`
**Explanation:** `-S 2` increases k-mer sampling to 1/2 (from default 1/4) for more matched length; `-e 2` lowers the minimum edge depth from 3 to 2; `-A` keeps contained reads. Together these help low-coverage (<20x) datasets at the cost of memory and runtime.

### Estimate genome size from k-mer counts (pre-assembly sanity check)
**Args:** `kat hist -t 16 reads.fastq.gz -o kat_hist && kat plot spectra-hist kat_hist.stats.json -o kat_hist.png`
**Explanation:** While wtdbg2's `-g` is user-supplied, KAT (K-mer Analysis Toolkit) histogram lets you verify the true genome size from the haploid k-mer peak before running the assembler. Mismatch between `-g` and the KAT estimate will degrade assembly quality.

### Realignment mode for refined graph
**Args:** `wtdbg2 -x ont -g 3g -R -i reads.fastq.gz -fo asm -t 32`
**Explanation:** `-R` enables realignment mode, which uses additional HPC k-mers (`--realn-kmer-psize=15`, default subsampling 1) to refine the assembly graph. Slower but can resolve ambiguous overlaps.

### Run with memory-saving k-mer partitioning
**Args:** `wtdbg2 -x ont -g 3g --kbm-parts 4 -i reads.fastq.gz -fo asm -t 32`
**Explanation:** `--kbm-parts 4` splits total reads into 4 parts and indexes one at a time, reducing peak memory at the cost of longer runtime. Essential when available RAM is below the recommended for the genome size.

### Filter reads by length and tidy names
**Args:** `wtdbg2 -x rs -g 144m -L -5000 -i reads.fastq.gz -fo asm -t 32`
**Explanation:** `-L -5000` drops reads shorter than 5000 bp AND renames remaining reads to `S%010d` format (negative value enables renaming). Useful for PacBio RSII data with inconsistent naming.

### Compile from source
**Args:** `git clone https://github.com/ruanjue/wtdbg2.git && cd wtdbg2 && make -j16 && cp wtdbg2 wtpoa-cns wtdbg-cns ~/bin/`
**Explanation:** Clones the source and compiles with 16 parallel jobs. Copy `wtdbg2`, `wtpoa-cns`, and `wtdbg-cns` to a directory in PATH. Only works on 64-bit Linux.
