---
name: aakomp
category: qc
description: AAComp assesses genome assembly completeness using amino acid k-mer analysis with a multi-index Bloom filter approach.
tags: [aakomp, qc, genome, completeness, k-mer, assembly, amino-acid]
author: oxo-call-community
source_url: "https://github.com/bcgsc/aakomp"
---

## Concepts

- **Tool Overview**: aaKomp (v1.0.0) assesses draft genome completeness using a fast, alignment-free, k-mer hash-based approach. It uses amino acid k-mers and a multi-index Bloom filter (miBf) to estimate assembly completeness.
- **Core Function**: Evaluates genome completeness by comparing amino acid k-mer profiles against reference databases or BUSCO lineages.
- **Input/Output**: Input is a genome assembly (FASTA); output includes completeness assessment report and visualization.
- **Installation**: Install via bioconda: `conda install -c bioconda aakomp`
- **Platform Support**: Linux (x86_64)
- **K-mer Based**: Uses amino acid k-mers (default k=9) rather than nucleotide k-mers, which is more robust to sequencing errors and assembly fragmentation.
- **Driver Script**: The `run-aakomp` script automates downloading BUSCO lineages, building miBf, running aaKomp, and generating visualizations.

## Pitfalls

- **CRITICAL: Command Name**: The main command is `run-aakomp`, not `aakomp`. The `aakomp` binary is used internally by the driver script.
- **Reference Database**: Requires either a reference FASTA file or a BUSCO lineage name for comparison.
- **Dependencies**: Requires HMMER for downloading BUSCO lineages and R with ggplot2 for visualization.
- **miBf Reuse**: If the miBf already exists in --db-dir, it will be reused. Delete it to rebuild with updated parameters.
- **Memory Usage**: May require significant memory for large reference databases.

## Examples

### Display help information
**Args:** `run-aakomp --help`
**Explanation:** Shows all available command-line options for the driver script.

### Assess genome completeness with reference file
**Args:** `run-aakomp --db-dir ./ --reference reference.faa --input genome.fasta -t 4 -o output_ref`
**Explanation:** Runs aaKomp using a provided amino acid reference file. Uses 4 threads and stores outputs in output_ref prefix.

### Assess genome completeness using BUSCO lineage
**Args:** `run-aakomp --db-dir ./ --lineage eukaryota --input genome.fasta -t 4 -o output_eukaryota`
**Explanation:** Downloads the eukaryota BUSCO lineage HMMs, extracts consensus sequences to generate a reference, and runs aaKomp.

### Run with custom k-mer size
**Args:** `run-aakomp --db-dir ./ --lineage bacteria --input genome.fasta -k 7 -o output_k7`
**Explanation:** Uses k-mer size of 7 instead of the default 9. Smaller k-mers may be more sensitive to partial gene matches.

### List available BUSCO lineages
**Args:** `run-aakomp --list-lineages`
**Explanation:** Lists all available BUSCO lineages that can be used with the --lineage option.

### Run with verbose output
**Args:** `run-aakomp --db-dir ./ --lineage fungi --input genome.fasta -v -o output_verbose`
**Explanation:** Enables verbose output to see detailed progress information during each step.

### Dry run mode
**Args:** `run-aakomp --db-dir ./ --lineage metazoa --input genome.fasta --dry-run`
**Explanation:** Prints the commands that would be executed without actually running them. Useful for debugging.

### Track runtime statistics
**Args:** `run-aakomp --db-dir ./ --lineage plantae --input genome.fasta --track-time -o output_timed`
**Explanation:** Records and reports runtime statistics for each major step of the pipeline.