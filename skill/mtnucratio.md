---
name: mtnucratio
category: utility
description: A small tool to determine MT to Nuclear ratios for NGS data.
tags: [mtnucratio, utility, mitochondrial, copy-number, NGS]
author: oxo-call-community
source_url: "https://github.com/apeltzer/MTNucRatioCalculator"
---

## Concepts

- **Tool Overview**: MTNucRatio v0.7.1 calculates mitochondrial to nuclear DNA copy number ratio from BAM files.
- **Core Function**: Computes depth ratio between mitochondrial and nuclear genomes.
- **Input**: Accepts coordinate-sorted, indexed BAM files.
- **Output**: Generates text and JSON format results with ratio values.
- **Methodology**: Uses coverage comparison between mtDNA and nuclear DNA for copy number estimation.
- **Applications**: Mitochondrial DNA copy number analysis in cancer studies, aging research, and eDNA surveys.

## Pitfalls

- **BAM Quality**: Requires high-quality alignments; poorly mapped reads affect accuracy.
- **Chromosome Naming**: Mitochondrial chromosome must be named consistently (MT, chrM, or actual name).
- **Coverage Requirements**: Sufficient sequencing depth needed for both mitochondrial and nuclear genomes.
- **Ploidy Assumption**: Default calculation assumes diploid nuclear genome.
- **Assembly Effects**: Different reference assemblies may affect nuclear genome size calculations.
- **CNV Interference**: Copy number variants in nuclear genome may skew ratio estimates.

## Examples

### Basic ratio calculation
**Args:** `mtnucratio input.bam MT > ratio.txt`
**Explanation:** Calculates mitochondrial to nuclear ratio assuming MT chromosome name.

### Specify chromosome name
**Args:** `mtnucratio alignments.bam chrM -o result.json`
**Explanation:** Uses chrM as mitochondrial chromosome identifier.

### Multiple sample processing
**Args:** `for bam in *.bam; do mtnucratio $bam MT > ${bam}.ratio; done`
**Explanation:** Batch processes multiple BAM files in a loop.

### JSON output for downstream analysis
**Args:** `mtnucratio sample.bam MT --json sample.json`
**Explanation:** Outputs results in JSON format for programmatic processing.

### MultiQC integration
**Args:** `mtnucratio sample.bam MT && mv sample.mtnuc.json mqc/`
**Explanation:** Generates output compatible with MultiQC mtnucratio module.
