---
name: bayesase
category: variant-calling
description: BayesASE - Bayesian analysis of allele-specific expression
tags: [bayesase, variant-calling, allele-specific-expression, RNA-seq]
author: oxo-call-community
source_url: "https://github.com/McIntyre-Lab/BayesASE"
---

## Concepts

- **Tool Overview**: BayesASE (v21.1.13.1) performs Bayesian analysis of allele-specific expression (ASE), detecting cis-regulatory variation through allelic imbalance in RNA-seq data.
- **Core Function**: Identifies allele-specific expression patterns using Bayesian statistical methods.
- **Allelic Imbalance**: Detects differences in expression between alleles at heterozygous loci.
- **Bayesian Inference**: Uses Bayesian methods to quantify evidence for allele-specific expression.
- **cis-Regulatory Variation**: Identifies regulatory differences in cis-acting elements.
- **Input/Output**: Accepts BAM files and VCF genotypes; outputs ASE statistics.
- **Installation**: `conda install -c bioconda bayesase`.

## Pitfalls

- **Heterozygous Sites**: Requires heterozygous SNP calls for ASE analysis.
- **Read Coverage**: Requires sufficient coverage at heterozygous sites.
- **Mapping Bias**: May be affected by mapping bias between alleles.
- **Phasing**: Requires phased genotypes for accurate haplotype-specific expression.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic ASE analysis
**Args:** `bayesase -b alignments.bam -v genotypes.vcf -o ase_results.txt`
**Explanation:** Performs Bayesian ASE analysis on RNA-seq data.

### Specify reference allele
**Args:** `bayesase -b alignments.bam -v genotypes.vcf -r reference.fasta -o ase_results.txt`
**Explanation:** Uses reference genome to determine reference alleles.

### Output posterior probabilities
**Args:** `bayesase -b alignments.bam -v genotypes.vcf -o ase_results.txt --posterior`
**Explanation:** Outputs posterior probabilities for ASE.

### Filter by coverage
**Args:** `bayesase -b alignments.bam -v genotypes.vcf -o ase_results.txt --min-coverage 10`
**Explanation:** Only analyzes sites with minimum 10x coverage.

### Multiple samples
**Args:** `bayesase -b sample1.bam sample2.bam -v genotypes.vcf -o ase_results.txt`
**Explanation:** Analyzes multiple samples together.

### Generate visualization
**Args:** `bayesase -b alignments.bam -v genotypes.vcf -o ase_results.txt --plot ase_plot.png`
**Explanation:** Generates visualization of ASE results.

### Display help
**Args:** `bayesase --help`
**Explanation:** Shows all available command-line options and usage information.