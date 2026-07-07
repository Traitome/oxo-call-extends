---
name: damageprofiler
category: utility
description: Java-based tool to determine damage patterns on ancient DNA
tags: [damageprofiler, utility, ancient-DNA, damage-patterns, mapDamage]
author: oxo-call-community
source_url: "https://github.com/Integrative-Transcriptomics/DamageProfiler"
---

## Concepts

- **Tool Overview**: damageprofiler (v1.1+) is a Java-based tool for determining damage patterns in ancient DNA, serving as an alternative to mapDamage.
- **Core Function**: Analyzes nucleotide misincorporation patterns to characterize ancient DNA damage.
- **Input/Output**: Input: BAM alignments, reference genome. Output: Damage profiles, quality metrics.
- **Algorithm**: Calculates nucleotide frequency at read ends and generates damage profiles.
- **Key Features**: Fast processing, visual reports, multiple output formats.
- **Installation**: `conda install -c bioconda damageprofiler`

## Pitfalls

- **Java Requirement**: Requires Java runtime environment.
- **BAM Index**: BAM files must be indexed for efficient processing.
- **Reference Genome**: Must match the alignment reference.
- **Damage Interpretation**: Requires understanding of aDNA damage patterns.
- **Library Type**: Results may vary with different library preparation methods.

## Examples

### Analyze damage patterns
**Args:** `damageprofiler -i aligned.bam -r reference.fasta -o damage_results/`
**Explanation:** Analyze ancient DNA damage patterns from aligned reads.

### Generate PDF report
**Args:** `damageprofiler -i aligned.bam -r reference.fasta -o results/ --pdf`
**Explanation:** Generate PDF damage profile report.

### Specify read length distribution
**Args:** `damageprofiler -i aligned.bam -r reference.fasta -o results/ --length 30`
**Explanation:** Analyze damage for reads with minimum length of 30bp.
