---
name: tophat-recondition
category: utility
description: TopHat-Recondition - Tool for reconditioning and improving TopHat alignments.
tags: [tophat-recondition, alignment-improvement, rna-seq, splice-junction]
author: oxo-call-community
source_url: "https://github.com/compbio/tophat-recondition"
---

## Concepts

- **Tool Overview**: TopHat-Recondition - A tool for improving and reconditioning TopHat alignments for better accuracy.
- **Core Function**: Refines splice junction calls and improves alignment quality for RNA-seq data.
- **Input**: TopHat alignment (BAM), reference genome (FASTA).
- **Output**: Improved alignment (BAM), updated junction calls.
- **Installation**: `conda install -c bioconda tophat-recondition`
- **Use Case**: RNA-seq alignment improvement, splice junction refinement.

## Pitfalls

- **TopHat Dependency**: Requires existing TopHat alignments.
- **Compatibility**: May not work with other aligners' outputs.

## Examples

### Recondition alignments
**Args:** `tophat-recondition -i tophat_out/accepted_hits.bam -o reconditioned/`
**Explanation:** Improve TopHat alignment quality.

### With genome
**Args:** `tophat-recondition -i alignments.bam -g genome.fasta -o improved/`
**Explanation:** Recondition alignments with reference genome.
