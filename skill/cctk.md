---
name: cctk
category: genome-editing
description: CRISPR Comparison Toolkit for identifying and comparing CRISPR arrays
tags: [cctk, crispr, crispr-arrays, spacer-analysis, cas]
author: oxo-call-community
source_url: "https://github.com/Alan-Collins/CRISPR_comparison_toolkit"
---

## Concepts

- **Tool Overview**: CCTK identifies and compares CRISPR arrays across genomes.
- **Core Function**: Detects CRISPR arrays, extracts spacers, and compares between genomes.
- **Algorithm**: Uses pattern matching to identify CRISPR repeats and spacers.
- **Input**: FASTA genome sequences or annotated CRISPR files.
- **Output**: CRISPR array annotations and spacer comparison reports.
- **Application**: CRISPR-Cas system analysis and comparative genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda cctk`

## Pitfalls

- **Repeat Variation**: CRISPR repeats may vary between strains.
- **Array Detection**: May miss degenerate or incomplete arrays.
- **Large Genomes**: Processing large genomes may require significant time.
- **False Positives**: May detect tandem repeats as CRISPR arrays.

## Examples

### Identify CRISPR arrays
**Args:** `cctk detect -i genome.fa -o crispr_arrays.gff`
**Explanation:** Identifies CRISPR arrays in genome sequence.

### Extract spacers
**Args:** `cctk extract -i crispr_arrays.gff -g genome.fa -o spacers.fa`
**Explanation:** Extracts spacer sequences from identified arrays.

### Compare CRISPR arrays
**Args:** `cctk compare -i genome1_crispr.gff genome2_crispr.gff -o comparison.tsv`
**Explanation:** Compares CRISPR arrays between two genomes.

### Display help
**Args:** `cctk --help`
**Explanation:** Shows all available options and usage information.