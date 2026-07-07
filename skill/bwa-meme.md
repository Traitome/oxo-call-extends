---
name: bwa-meme
category: alignment
description: BWA-MEM emulated with a machine learning approach (learned-index) for accelerated alignment
tags: [bwa-meme, alignment, learned-index, machine-learning, fast]
author: oxo-call-community
source_url: "https://github.com/kaist-ina/BWA-MEME"
---

## Concepts

- **Tool Overview**: BWA-MEME is the first full-fledged short read alignment software that leverages learned indices for solving the exact match search problem for efficient seeding. It is a drop-in replacement for BWA-MEM2.
- **Learned Index (P-RMI)**: Replaces the FM-index lookup in the seeding phase with a Piecewise Recursive Model Index (P-RMI) that predicts the suffix array position of a k-mer, drastically reducing memory accesses. Training is required after indexing (`build_rmis_dna.sh`).
- **Performance**: Achieves up to 3.32x faster seeding throughput and up to 1.4x higher end-to-end alignment throughput compared to BWA-MEM2, by reducing instructions by 4.60x, memory accesses by 8.77x, and LLC misses by 2.21x.
- **Output Compatibility**: Generates 100% identical SAM output to BWA-MEM2 and bwa mem 0.7.17, making it a transparent drop-in replacement for existing pipelines.
- **Memory Modes**: Three binary variants with different memory/speed trade-offs: mode1 (38GB index, minimal acceleration), mode2 (88GB), and default mode3 (118GB, fastest). The `bwa-meme` binary auto-selects the best mode based on SIMD support (SSE, AVX2, AVX512).
- **Key Flag `-7`**: The `-7` flag activates BWA-MEME's learned-index seeding. Without `-7`, `bwa-meme mem` behaves identically to BWA-MEM2 (no learned index). This allows A/B testing within the same binary.
- **Installation**: `conda install -c conda-forge -c bioconda bwa-meme` (installs `bwa-meme` binary and `build_rmis_dna.sh` training script).

## Pitfalls

- **Memory Requirement**: Requires at least 64GB RAM for minimal mode (mode1: 38GB index). For WGS on human genome with >32 threads at full acceleration (mode3), 140-192GB RAM is recommended. Insufficient memory will cause swapping and negate speed benefits.
- **Two-Step Index Build**: Building the index is not sufficient; you must also run `build_rmis_dna.sh` to train the P-RMI model, which reads the suffix array generated during indexing. Skipping P-RMI training means `-7` cannot be used (falls back to BWA-MEM2 behavior).
- **Rust Dependency for Local Build**: Building from source requires Rust (for P-RMI training code) in addition to cmake and zlib-dev. The bioconda package bundles everything and is the recommended installation method.
- **Pipeline Bottleneck Shift**: Due to increased alignment throughput, the bottleneck often shifts to Samtools sorting. Use `mbuffer` or fast-compression BAM output to prevent CPU waste in the sorting stage.
- **Linux-64 Only**: Currently only available on linux-64 via bioconda. No macOS or Windows support.
- **`-K` for Reproducibility**: Use `-K 100000000` (process 100M bases per batch) for reproducible output across runs with different thread counts. Without `-K`, output order may vary with thread count.
- **Index Format Incompatibility**: BWA-MEME index (`-a meme`) is NOT compatible with standard BWA or BWA-MEM2 indices. You must rebuild the index specifically for BWA-MEME.

## Examples

### Build BWA-MEME index (requires P-RMI training)
**Args:** `bwa-meme index -a meme hg38.fa -t 32 && build_rmis_dna.sh hg38.fa`
**Explanation:** `-a meme` builds the BWA-MEME-specific index (includes suffix array needed for P-RMI training). The `build_rmis_dna.sh` script trains the learned index model (~15 min for human genome, single thread). Both the index files and `.rmi` model files must be in the same directory with the same prefix.

### Align reads with learned-index acceleration
**Args:** `bwa-meme mem -7 -Y -K 100000000 -t 32 hg38.fa reads_1.fq.gz reads_2.fq.gz -o aln.sam`
**Explanation:** `-7` enables learned-index seeding (BWA-MEME mode). `-Y` uses soft-clipping for supplementary alignments. `-K 100000000` processes 100M bases per batch for reproducible output. Without `-7`, runs as standard BWA-MEM2.

### Compare output with BWA-MEM2 (A/B test)
**Args:** `bwa-meme mem -7 -K 100000000 -t 32 hg38.fa reads.fq.gz -o meme.sam && bwa-meme mem -K 100000000 -t 32 hg38.fa reads.fq.gz -o mem2.sam && diff meme.sam mem2.sam`
**Explanation:** Runs the same alignment with (`-7`) and without learned index, then diffs the SAM outputs. The `diff` should return no differences, confirming 100% output compatibility. Use `diff-large-files` tool for large SAM files.

### Select minimal-memory mode (38GB index)
**Args:** `bwa-meme_mode1 mem -7 -Y -K 100000000 -t 16 hg38.fa reads.fq.gz > aln.sam`
**Explanation:** `bwa-meme_mode1` uses the 38GB index variant (minimal learned-index acceleration). Suitable for servers with limited RAM (~64GB total). Modes: mode1=38GB, mode2=88GB, mode3(default)=118GB. Check available modes with `bwa-meme version`.

### Pipeline with mbuffer to avoid sort bottleneck
**Args:** `bwa-meme mem -7 -K 100000000 -t 32 hg38.fa R1.fq.gz R2.fq.gz | mbuffer -m 20G | samtools sort -m 1G --output-fmt bam,level=1 -T ./sorttmp -@ 20 - > sorted.bam`
**Explanation:** Uses `mbuffer -m 20G` (20GB buffer = 20 threads x 1G per samtools thread) to absorb alignment throughput spikes and prevent Samtools sort from becoming a bottleneck. `--output-fmt bam,level=1` uses fast compression to keep pace.

### Build from source with Rust for P-RMI training
**Args:** `git clone https://github.com/kaist-ina/BWA-MEME.git && cd BWA-MEME && make -j32 && ./bwa-meme index -a meme ref.fa -t 32 && ./build_rmis_dna.sh ref.fa`
**Explanation:** Clones and compiles BWA-MEME. Requires Rust (`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`), cmake, and zlib-dev. The `make` step builds all three mode binaries (`bwa-meme`, `bwa-meme_mode1`, `bwa-meme_mode2`).

### Download prebuilt indices and P-RMI models
**Args:** `wget -r -np -nH --cut-dirs=1 -R "index.html*" https://web.inalab.net/~bwa-meme/hg38/`
**Explanation:** Downloads prebuilt BWA-MEME indices and trained P-RMI models for hg37/hg38 from the official server. The index files and `.rmi` model files must share the same prefix and reside in the same directory for `bwa-meme mem -7` to load them correctly.

### Display version and SIMD mode
**Args:** `bwa-meme version`
**Explanation:** Prints the version and the SIMD mode (SSE/AVX2/AVX512) of the compiled binary. The `bwa-meme` binary auto-selects the best mode based on CPU capabilities; explicit mode binaries (`bwa-meme_mode1`, `bwa-meme_mode2`) are available for manual selection.
