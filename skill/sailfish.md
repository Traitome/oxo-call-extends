---
name: sailfish
category: transcriptomics
description: Rapid mapping-based isoform quantification from RNA-Seq reads
tags: ["sailfish", "RNA-seq", "quantification", "isoform", "transcriptomics"]
author: oxo-call-community
source_url: "http://www.cs.cmu.edu/~ckingsf/software/sailfish/"
---

## Concepts

- **Tool Overview**: Sailfish (v0.10.1) is a rapid transcript quantification tool that estimates isoform abundances directly from RNA-seq reads without full alignment.
- **Core Function**: Uses lightweight mapping to assign reads to transcripts and compute expression levels using an expectation-maximization algorithm.
- **Algorithm**: Implements quasi-mapping for fast read assignment, followed by EM-based quantification to resolve multi-mapping reads.
- **Input Format**: RNA-seq reads (FASTQ), transcriptome index, optional gene annotation (GTF).
- **Output Format**: Transcript-level expression estimates (TPM, FPKM), gene-level summaries, abundance files.
- **Use Case**: RNA-seq expression analysis, differential expression studies, transcriptome profiling, isoform quantification.

## Pitfalls

- **Index building**: Requires building a transcriptome index before quantification.
- **Reference bias**: Quantification depends on transcriptome completeness.
- **Multi-mapping reads**: May underestimate expression for highly similar isoforms.
- **Strand specificity**: Requires proper handling for strand-specific libraries.
- **Memory requirements**: Large transcriptomes require significant memory.
- **Paired-end handling**: Requires proper specification of paired-end data.

## Examples

### Build transcriptome index
**Args:** `sailfish index -t transcripts.fasta -o index`
**Explanation:** `-t` transcript sequences; `-o` output index directory.

### Quantify expression
**Args:** `sailfish quant -i index -l IU -1 reads_1.fastq -2 reads_2.fastq -o quant_output`
**Explanation:** `-i` index directory; `-l` library type; `-1/-2` paired reads; `-o` output directory.

### Single-end quantification
**Args:** `sailfish quant -i index -l SR -r reads.fastq -o quant_output`
**Explanation:** `-l SR` single-end library type; `-r` single-end reads.

### Strand-specific library
**Args:** `sailfish quant -i index -l ISR -1 reads_1.fastq -2 reads_2.fastq -o quant_output`
**Explanation:** `-l ISR` specifies strand-specific library orientation.

### Bias correction
**Args:** `sailfish quant -i index -l IU -1 reads_1.fastq -2 reads_2.fastq -o quant_output --biasCorrect`
**Explanation:** `--biasCorrect` enables sequence-specific bias correction.

### Output TPM only
**Args:** `sailfish quant -i index -l IU -1 reads_1.fastq -2 reads_2.fastq -o quant_output --useVBOpt`
**Explanation:** `--useVBOpt` uses variational Bayesian optimization for improved quantification.

### Quantify with gene annotation
**Args:** `sailfish quant -i index -l IU -1 reads_1.fastq -2 reads_2.fastq -o quant_output -g genes.gtf`
**Explanation:** `-g` gene annotation for gene-level summarization.