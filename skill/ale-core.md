---
name: ale-core
category: assembly
description: Assembly Likelihood Estimator - reference-independent framework for evaluating genome and metagenome assembly accuracy
tags: [ale-core, assembly-evaluation, likelihood, assembly-quality, metagenome]
author: oxo-call-community
source_url: "https://github.com/sc932/ALE"
---

## Concepts

- **Tool Overview**: ALE (Assembly Likelihood Estimator) is a generic framework for evaluating the accuracy of genome and metagenome assemblies in a reference-independent manner using rigorous statistical methods.
- **Core Function**: Computes a likelihood score for assemblies by integrating read quality, mate pair orientation, insert length, sequencing coverage, read alignment, and k-mer frequency.
- **Statistical Framework**: Uses comprehensive statistical methods to evaluate assembly quality without requiring a reference genome.
- **Error Detection**: Identifies synthetic errors including single-base errors, insertions/deletions, genome rearrangements, and chimeric assemblies in metagenomes.
- **Input/Output**: Input: Assembly FASTA file and BAM file with read mappings. Output: ALE score and detailed assembly quality metrics.
- **Installation**: Install via bioconda: `conda install -c bioconda ale-core`
- **Citation**: Clark, S.C., Egan, R., Frazier, P.I., & Wang, Z. (2013). ALE: a generic assembly likelihood evaluation framework for assessing the accuracy of genome and metagenome assemblies. Bioinformatics, 29(8), 1008-1015.

## Pitfalls

- **Read Mapping**: Requires properly sorted BAM file with reads mapped to the assembly.
- **Assembly Format**: Input assembly must be in FASTA format with valid sequence headers.
- **Computational Resources**: Likelihood calculation can be computationally intensive for large assemblies.
- **Score Interpretation**: ALE scores are relative - use for comparing assemblies rather than absolute quality assessment.
- **Core Version**: ale-core contains only C scoring programs without supplementary Python plotting scripts.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options and input format requirements.

### Evaluate assembly with reads
**Args:** `ale assembly.fasta reads.bam -o assembly_ale.txt`
**Explanation:** Evaluates assembly quality using mapped reads and outputs ALE score.

### Specify insert size parameters
**Args:** `ale assembly.fasta reads.bam --mean-insert 500 --std-insert 50 -o results.txt`
**Explanation:** Uses custom insert size parameters for paired-end read evaluation.

### Set read length
**Args:** `ale assembly.fasta reads.bam --read-length 150 -o results.txt`
**Explanation:** Specifies read length for likelihood calculation.

### Enable verbose output
**Args:** `ale assembly.fasta reads.bam -v -o results.txt`
**Explanation:** Enables verbose mode for detailed progress information.

### Output detailed metrics
**Args:** `ale assembly.fasta reads.bam --detailed -o detailed_results.txt`
**Explanation:** Outputs detailed metrics including local and global scores.

### Evaluate metagenome assembly
**Args:** `ale metagenome_assembly.fasta metagenome_reads.bam -o metagenome_ale.txt`
**Explanation:** Evaluates metagenome assembly quality using the same statistical framework.

### Set minimum coverage
**Args:** `ale assembly.fasta reads.bam --min-coverage 5 -o results.txt`
**Explanation:** Sets minimum coverage threshold for evaluation.

### Compare two assemblies
**Args:** `ale assembly1.fasta reads.bam -o assembly1_ale.txt && ale assembly2.fasta reads.bam -o assembly2_ale.txt`
**Explanation:** Evaluates multiple assemblies with the same reads for comparison.

### Use custom k-mer size
**Args:** `ale assembly.fasta reads.bam --kmer-size 31 -o results.txt`
**Explanation:** Uses k-mer size of 31 for k-mer frequency analysis.
