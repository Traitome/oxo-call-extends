---
name: bismark
category: epigenomics
description: Map bisulfite-treated reads and perform methylation calls
tags: [bisulfite, methylation, epigenomics, mapping]
author: oxo-call-community
source_url: "https://github.com/FelixKrueger/Bismark/"
---

## Concepts
- **Tool Overview**: Bismark maps bisulfite-treated sequencing reads to a genome and performs methylation calls in a single step. It is the standard tool for whole-genome bisulfite sequencing (WGBS) analysis.
- **Bisulfite Mapping**: Converts reference genome to bisulfite versions (C→T and G→A), maps reads using Bowtie2/Hisat2, and reports methylation context.
- **Methylation Calling**: Identifies methylated cytosines in CpG, CHG, and CHH contexts.
- **Workflow**: Genome preparation → alignment → deduplication → methylation extraction → reporting.
- **Output**: BAM alignments, coverage reports, and methylation calls compatible with genome browsers.

## Pitfalls
- **Strand Direction**: Bisulfite libraries can be directional or non-directional; specify correctly.
- **Deduplication**: PCR duplicates must be removed for accurate methylation quantification.
- **Genome Preparation**: Must run `bismark_genome_preparation` before alignment.

## Examples
### Prepare genome
**Args:** `bismark_genome_preparation --path_to_bowtie2 /usr/bin/ reference_genome/`
**Explanation:** Prepares bisulfite-converted reference genome indices.

### Align bisulfite reads
**Args:** `bismark --genome reference_genome/ -1 reads_R1.fq -2 reads_R2.fq -o results/`
**Explanation:** Maps paired-end bisulfite reads to the reference genome.

### Deduplicate alignments
**Args:** `deduplicate_bismark --paired aligned.bam`
**Explanation:** Removes PCR duplicates from bisulfite alignment.

### Extract methylation calls
**Args:** `bismark_methylation_extractor --bedGraph --CX deduplicated.bam`
**Explanation:** Extracts methylation calls and generates bedGraph output.

### Generate methylation report
**Args:** `bismark2report --dir results/`
**Explanation:** Generates HTML summary report of methylation analysis.
