---
name: ale
category: assembly
description: Assembly Likelihood Estimator for evaluating genome assembly quality using read mapping
tags: [assembly, evaluation, likelihood, quality-assessment, reads]
author: oxo-call-community
source_url: "https://github.com/sc932/ALE"
---

## Concepts

- **Tool Overview**: ALE (Assembly Likelihood Estimator) evaluates genome assembly quality by computing a likelihood score based on read mapping evidence.
- **Core Function**: Scores assemblies by assessing how well mapped reads support the assembled sequence, identifying misassemblies and coverage inconsistencies.
- **Input/Output**: Input: BAM file of reads mapped to assembly, reference (optional). Output: Assembly likelihood score, per-position quality metrics.
- **Scoring**: Combines read depth, insert size, and mapping quality into a single likelihood score for assembly comparison.
- **Installation**: Install via bioconda: `conda install -c bioconda ale`

## Pitfalls

- **BAM Input Required**: Requires pre-mapped BAM file - use BWA or Bowtie2 to map reads to assembly first.
- **Insert Size**: Proper paired-end insert size estimation is critical for accurate scoring.
- **Reference Optional**: Can work without reference but reference improves misassembly detection.
- **Score Interpretation**: Higher scores indicate better assemblies - compare relative scores, not absolute values.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and input requirements for ALE.

### Score an assembly
**Args:** `ALE mapped_reads.bam assembly.fasta -o ale_score.txt`
**Explanation:** Computes assembly likelihood score from mapped reads.

### Score with reference comparison
**Args:** `ALE mapped_reads.bam assembly.fasta -r reference.fasta -o ale_score.txt`
**Explanation:** Includes reference-based comparison for improved misassembly detection.

### Output per-position scores
**Args:** `ALE mapped_reads.bam assembly.fasta -o score.txt --per-position positions.tsv`
**Explanation:** Outputs per-position likelihood scores for detailed analysis.

### Compare multiple assemblies
**Args:** `ALE map1.bam asm1.fasta -o score1.txt && ALE map2.bam asm2.fasta -o score2.txt`
**Explanation:** Scores two assemblies for comparison (higher score = better assembly).

### Set insert size parameters
**Args:** `ALE mapped_reads.bam assembly.fasta --insert-mean 300 --insert-sd 50 -o score.txt`
**Explanation:** Specifies insert size distribution for paired-end scoring.

### Output detailed statistics
**Args:** `ALE mapped_reads.bam assembly.fasta -o score.txt --stats stats.tsv`
**Explanation:** Outputs detailed assembly statistics alongside likelihood score.
