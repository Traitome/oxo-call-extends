---
name: 3d-dna
category: assembly
description: 3D de novo assembly (3D-DNA) pipeline for Hi-C based genome scaffolding.
tags: [3d-dna, assembly, hic, scaffolding, genome, 3d-structure]
author: oxo-call-community
source_url: "https://github.com/aidenlab/3d-dna/tree/201008"
---

## Concepts

- **Tool Overview**: 3D de novo assembly pipeline that uses Hi-C data to scaffold draft assemblies into chromosome-scale genomes. Version 201008.
- **Core Function**: Iteratively corrects misjoins in input scaffolds and orders/orients them into chromosome-level assemblies using Hi-C contact maps.
- **Input/Output**: Input requires a draft assembly FASTA and Hi-C contact map (from Juicer). Output is a corrected, scaffolded assembly FASTA.
- **Installation**: Install via bioconda: `conda install -c bioconda 3d-dna`
- **Platform Support**: Platform-independent (noarch)
- **Pipeline Workflow**: Draft assembly + Hi-C data → Juicer analysis → 3D-DNA scaffolding → Juicebox manual review → Final assembly
- **Key Scripts**: `run-asm-pipeline.sh` (main pipeline), `run-asm-pipeline-post-review.sh` (post-review processing)
- **Iterative Correction**: Pipeline runs multiple rounds to detect and break misjoins, then re-scaffold based on Hi-C signal.

## Pitfalls

- **Version Differences**: The version number is a date stamp (201008 = October 8, 2020). Different dates may have significant changes.
- **Prerequisite Pipeline**: 3D-DNA requires Hi-C data processed by Juicer first. Running without proper Hi-C input produces errors.
- **Diploid Assemblies**: For diploid species, 3D-DNA is considered one of the best scaffolding tools, but requires careful parameter tuning.
- **Manual Review Required**: Automated results should be reviewed in Juicebox for misjoins. The pipeline includes a post-review step.
- **Memory Usage**: Large genomes require substantial RAM. Ensure sufficient memory for the assembly size.

## Examples

### Display help and version information
**Args:** `run-asm-pipeline.sh --help`
**Explanation:** Shows usage information for the main 3D-DNA pipeline script.

### Run the full 3D-DNA pipeline
**Args:** `run-asm-pipeline.sh -i input_draft.asm.fasta -j juicer_output/ -o output_dir/`
**Explanation:** Runs the complete 3D-DNA pipeline on a draft assembly using Hi-C data processed by Juicer. The -i flag specifies the draft assembly, -j points to Juicer output directory.

### Run pipeline with custom parameters
**Args:** `run-asm-pipeline.sh -i draft.fa -j juicer_out/ -o results/ -m diploid -s 500`
**Explanation:** Runs the pipeline in diploid mode (-m diploid) with a minimum scaffold size of 500bp. Diploid mode is recommended for heterozygous genomes.

### Run post-review processing after Juicebox curation
**Args:** `run-asm-pipeline-post-review.sh -i reviewed.assembly -j juicer_output/ -o final_assembly/`
**Explanation:** Processes the manually reviewed assembly from Juicebox to produce the final chromosome-level assembly. This step applies the changes made during manual curation.

### Run with specific round parameters
**Args:** `run-asm-pipeline.sh -i draft.fa -j juicer_out/ -o results/ -r 1 2 3`
**Explanation:** Runs only the specified correction rounds (1, 2, 3). Useful for resuming interrupted runs or testing specific iterations.
