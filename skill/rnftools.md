---
name: rnftools
category: utility
description: "RNF (Reads N Fancy) framework for NGS: simulation of reads with explicit error models, evaluation of mappers, and conversion between RNF-compliant and standard alignment/sequence formats."
tags: ["rnftools", "rnf", "simulation", "evaluation", "ngs", "benchmarking"]
author: oxo-call-community
source_url: "http://karel-brinda.github.io/rnftools"
---
## Concepts

- **Tool Overview**: RNFtools (v0.4.0.0, Karel Brinda) is an integrative framework for next-generation sequencing simulation, evaluation, and format conversion in the RNF (Reads N Fancy) ecosystem. It unifies read simulation, alignment-format conversion, and mapper benchmarking under a single Python library and CLI.
- **Core Function**: Provides four main subcommands: `rnftools simulate` (generate synthetic reads from a FASTA reference with explicit error models), `rnftools mappers` (configure and run a list of mappers for benchmarking), `rnftools evaluate` (compute precision/recall from simulated-vs-true alignments), and `rnftools convert` (translate between RNF format and SAM/BAM/CRAM).
- **Algorithm**: The simulation engine wraps established simulators (wgsim, ART, Mason, DWGSIM) and exposes a unified interface; the evaluation engine uses a "true alignment" file (the simulator's ground truth) to compute per-mapper precision/recall via `rnftools evaluate`. Mapper configuration is YAML-based and supports per-mapper parameter sweeps.
- **Input Format**: (1) A reference FASTA (input to simulate); (2) a list of mapper configurations (YAML, input to `mappers`); (3) the simulated reads in RNF format (FASTA-like but with truth in the header). The CLI is `rnftools <subcommand> <args>`.
- **Output Format**: (1) Simulated reads in FASTA with truth information in the headers; (2) a SAM/BAM per mapper; (3) an evaluation HTML report with precision/recall curves; (4) a per-mapper TSV with the global metrics. The evaluation report is suitable for inclusion in a methods paper.
- **Use Case**: Standardized benchmarking of new mappers (BWA, Bowtie2, Minimap2, HISAT2) on a specific reference, validating an alignment pipeline against a known truth set, generating training data for a machine-learning alignment model, and producing reproducible benchmarks for a paper's supplement.

## Pitfalls

- **CRITICAL — The RNF format is not FASTA-compatible**: RNF reads have truth coordinates in the header line (e.g., `>read1 ref=chr1:100-200 strand=+`). Piping them to a tool that expects standard FASTA will produce silent misalignment because the truth annotation is ignored. Use `rnftools convert` to translate to standard FASTA when needed.
- **CRITICAL — Mapper binaries must be on PATH and compatible with the RNF I/O spec**: The RNF "mappers" subcommand assumes the mapper can read FASTA/FASTQ from stdin and write SAM to stdout. BWA, Bowtie2, and Minimap2 all support this; custom mappers may need a wrapper.
- **Simulation error models do NOT cover all platform quirks**: The default wgsim model is reasonable for Illumina but does not model indel patterns from long reads. For PacBio/Nanopore, use Mason or a custom error model.
- **The evaluation depends on a true alignment file**: If the simulation is run without ground truth (e.g., the user picks `--no-truth`), the evaluation step is meaningless. Always keep ground truth for benchmark purposes.
- **The default mapper list is small**: RNFtools includes pre-configured wrappers for BWA, Bowtie2, HISAT2, and Minimap2, but for newer mappers (STAR, GMAP) you must add a YAML config manually.
- **Large simulations are slow and I/O-heavy**: A 10× coverage simulation of a 3 Gbp human genome produces ~3 Gbp of reads; storage and time both scale linearly. Use `rnftools simulate --coverage 5` for a quick sanity check before the full run.

## Examples

### Simulate reads with default wgsim model
**Args:** `rnftools simulate --reference genome.fa --coverage 10 --read-length 100 --format fastq --output simulated.fa`
**Explanation:** `--reference` is the genome FASTA, `--coverage 10` simulates 10× coverage, `--read-length 100` is the read length, `--format fastq` selects FASTQ output. Default error model is wgsim (Illumina-like).

### Simulate paired-end reads
**Args:** `rnftools simulate --reference genome.fa --coverage 30 --read-length 150 --paired-end --insert-size 350 --std-dev 50 --output reads_R%.fq`
**Explanation:** `--paired-end` enables paired-end simulation; `--insert-size 350 --std-dev 50` is the typical Illumina library. The `%` in `--output` is replaced with `1` and `2` for the two mates.

### Configure mappers for benchmarking
**Args:** `cat > mappers.yaml << EOF
bwa_mem:
  executable: bwa
  args: mem -t 8
  reads_from_stdin: true
  output_to_stdout: true
minimap2:
  executable: minimap2
  args: -ax map-ont -t 8
EOF`
**Explanation:** Example YAML config for two mappers (BWA-MEM and Minimap2). `reads_from_stdin: true` and `output_to_stdout: true` are required for the RNF evaluation pipeline.

### Run a benchmark
**Args:** `rnftools mappers --mappers mappers.yaml --reads simulated.fa --reference genome.fa --output alignments/`
**Explanation:** Reads the mapper config from `mappers.yaml`, runs each mapper against the simulated reads, and writes the resulting SAMs to `alignments/`. The simulated reads and the reference must be the ones used to generate the simulation.

### Evaluate mappers against the truth
**Args:** `rnftools evaluate --truth simulated.fa --alignments alignments/ --output report/`
**Explanation:** `--truth` is the simulated reads file (with truth in headers), `--alignments` is the directory of mapper SAMs, `--output` is the evaluation report directory. Output `report/` contains a per-mapper TSV and an HTML summary.

### Convert RNF to standard FASTA
**Args:** `rnftools convert --rnf simulated.fa --output standard.fa`
**Explanation:** Strips the truth information from the FASTA headers, producing a standard FASTA suitable for tools that do not understand RNF. The truth is preserved in the original file.

### Convert SAM to BAM
**Args:** `rnftools convert --sam alignments/mapper.sam --output alignments/mapper.bam`
**Explanation:** Uses RNF's conversion wrapper around `samtools` to translate a SAM to a coordinate-sorted, indexed BAM. Useful for downstream IGV inspection.

### Benchmark with multiple simulators
**Args:** `rnftools simulate --simulator mason --reference genome.fa --coverage 10 --read-length 100 --output mason.fa && rnftools mappers --mappers mappers.yaml --reads mason.fa --reference genome.fa --output mason_alignments/`
**Explanation:** Composite: use Mason instead of wgsim for a different error model (more long-read-like, even at 100 bp). The downstream `rnftools evaluate` compares the mappers' performance on the Mason-simulated reads.
