---
name: 3d-dna
category: assembly
description: 3D de novo assembly (3D-DNA) pipeline for Hi-C based genome scaffolding.
tags: [3d-dna, assembly, hic, scaffolding, genome, 3d-structure, juicer, aiden-lab]
author: oxo-call-community
source_url: "https://github.com/aidenlab/3d-dna"
---

## Concepts

- **Tool Overview**: 3D de novo assembly pipeline that uses Hi-C data to scaffold draft assemblies into chromosome-scale genomes. Latest version is 180922 (201008 is also commonly used).
- **Core Function**: Iteratively corrects misjoins in input scaffolds and orders/orients them into chromosome-level assemblies using Hi-C contact maps.
- **Input/Output**: Input requires a draft assembly FASTA and Hi-C contact map (merged_nodups.txt from Juicer). Output is a corrected, scaffolded assembly FASTA and .hic file for visualization.
- **Installation**: 
  - Install via bioconda: `conda install -c bioconda 3d-dna`
  - Or clone from GitHub: `git clone https://github.com/aidenlab/3d-dna.git`
- **Platform Support**: Platform-independent (noarch), but requires Linux/Unix environment
- **Pipeline Workflow**: Draft assembly + Hi-C data → Juicer analysis → 3D-DNA scaffolding → Juicebox manual review → Final assembly
- **Key Scripts**: 
  - `run-asm-pipeline.sh` (main pipeline)
  - `run-asm-pipeline-post-review.sh` (post-review processing)
- **Iterative Correction**: Pipeline runs multiple rounds to detect and break misjoins, then re-scaffold based on Hi-C signal.
- **Prerequisites**: Java >=1.7, Bash >=4, GNU Awk >=4.0.2, GNU coreutils sort >=8.11, Python >=2.7, LastZ (for diploid mode)

## Pitfalls

- **CRITICAL: Juicer Prerequisite**: 3D-DNA requires Hi-C data processed by Juicer first to generate merged_nodups.txt. Running without proper Juicer input produces errors.
- **Version Differences**: Version numbers are date stamps (e.g., 201008 = October 8, 2020, 180922 = September 22, 2018). Different dates may have significant changes.
- **Diploid Assemblies**: For diploid species, 3D-DNA is considered one of the best scaffolding tools, but requires careful parameter tuning and LastZ for diploid mode.
- **Manual Review Required**: Automated results should be reviewed in Juicebox for misjoins. The pipeline includes a post-review step (`run-asm-pipeline-post-review.sh`).
- **Memory Usage**: Large genomes require substantial RAM. Ensure sufficient memory for the assembly size (e.g., 160Mb genome with 1B Hi-C reads needs ~128GB RAM).
- **No Installation Required**: The pipeline consists of bash scripts that can be run directly after cloning. No compilation needed.
- **Correct Usage**: Usage is `./run-asm-pipeline.sh [options] <input_fasta> <merged_nodups.txt>` - note the positional arguments, not flags.

## Examples

### Display help information
**Args:** `./run-asm-pipeline.sh --help`
**Explanation:** Shows usage information and available options for the main 3D-DNA pipeline script.

### Run the full 3D-DNA pipeline
**Args:** `./run-asm-pipeline.sh draft_assembly.fa merged_nodups.txt`
**Explanation:** Runs the complete 3D-DNA pipeline on a draft assembly using Hi-C data processed by Juicer. The draft assembly FASTA and Juicer's merged_nodups.txt are required positional arguments.

### Run pipeline in diploid mode
**Args:** `./run-asm-pipeline.sh -m diploid draft_assembly.fa merged_nodups.txt`
**Explanation:** Runs the pipeline in diploid mode. Required for heterozygous genomes. Uses LastZ to handle haplotype information.

### Run with specific iteration rounds
**Args:** `./run-asm-pipeline.sh -r 3 draft_assembly.fa merged_nodups.txt`
**Explanation:** Specifies 3 rounds of misjoin correction (default is 2). More rounds may improve accuracy but increase runtime.

### Run with minimum contig size filter
**Args:** `./run-asm-pipeline.sh -i 50000 draft_assembly.fa merged_nodups.txt`
**Explanation:** Sets minimum contig/scaffold size to 50000bp. Contigs smaller than this threshold are ignored during scaffolding.

### Run post-review processing after Juicebox curation
**Args:** `./run-asm-pipeline-post-review.sh reviewed.assembly merged_nodups.txt`
**Explanation:** Processes the manually reviewed assembly from Juicebox to produce the final chromosome-level assembly. This applies the changes made during manual curation in Juicebox.

### Run specific pipeline stages
**Args:** `./run-asm-pipeline.sh --stage seal draft_assembly.fa merged_nodups.txt`
**Explanation:** Runs only the seal stage of the pipeline. Available stages: polish, split, seal, merge, finalize. Useful for resuming interrupted runs.
