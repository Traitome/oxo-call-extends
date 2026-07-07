---
name: mutmap
category: variant-calling
description: "MutMap: pipeline to identify causative mutations responsible for a phenotype."
tags: [mutmap, variant-calling, mutation, phenotype, causative, bulked-segregant, snp-index]
author: oxo-call-community
source_url: "https://github.com/YuSugihara/MutMap"
---
## Concepts

- **Tool Overview**: MutMap v2.4.0 is a bioinformatics pipeline for identifying causal mutations responsible for a phenotype of interest. It uses bulked segregant analysis (BSA) combined with whole-genome resequencing to pinpoint mutations that associate with a phenotype.
- **Core Function**: Compares whole-genome sequences of pooled individuals showing a phenotype (mutants) against a reference genome. By calculating SNP index across the genome, it identifies genomic regions containing the causal mutation.
- **Algorithm**: Employs SNP index analysis - calculating the proportion of pooled reads that differ from the reference at each genomic position. Regions with unusually high or low SNP index indicate the causal locus.
- **Input Format**: Accepts paired-end FASTQ files from whole-genome sequencing of mutant bulk and, optionally, a wild-type control bulk. Requires a reference genome FASTA file.
- **Output**: Produces SNP index plots across chromosomes, candidate mutation lists in BED/VCF format, and statistical analysis of significant genomic regions.
- **Use Case**: Originally developed for plant genetics (especially rice), MutMap has been widely adopted for forward genetic screens and mapping-by-sequencing experiments.

## Pitfalls

- **Bulk Size**: The power of MutMap depends on having a sufficiently large bulk (typically 20-50 individuals). Too small bulks reduce statistical power to detect associations.
- **Reference Genome Quality**: Requires a high-quality reference genome. Poor references with gaps or misassemblies can confound SNP calling and index calculations.
- **Mutation Type**: MutMap works best for recessive mutations causing clear phenotypic differences. Dominant or partially penetrant mutations may show weaker signals.
- **Coverage Requirements**: Sufficient sequencing depth is needed across the genome. Low coverage reduces SNP calling accuracy and statistical power.
- **Multiple Mutations**: If the phenotype is caused by multiple independent mutations, the analysis becomes complicated. MutMap assumes a single major effect locus.
- **VCF Filtering**: Default variant filtering may need adjustment depending on sequencing quality and species. Be cautious about false positives and negatives.

## Examples

### Basic MutMap analysis
**Args:** `-1 mutant_R1.fastq -2 mutant_R2.fastq -r reference.fasta -o output_dir`
**Explanation:** Standard MutMap pipeline. Analyzes mutant bulk against reference genome and outputs SNP index analysis results.

### Include wild-type control
**Args:** `-1 mut_R1.fq -2 mut_R2.fq -r ref.fa -o BSA/ --ctl1 wt_R1.fq --ctl2 wt_R2.fq`
**Explanation:** Adding wild-type control bulk improves accuracy by accounting for pre-existing polymorphisms. Delta SNP index is calculated.

### Calculate Delta SNP index
**Args:** `-1 mut_bulk.fq -2 mut_bulk.fq -r ref.fa -o delta_snp/ --ctl1 wt_bulk.fq --ctl2 wt_bulk.fq --delta`
**Explanation:** The `--delta` flag explicitly calculates delta SNP index (mutant - wildtype), which better isolates the causal region.

### Filter low-confidence SNPs
**Args:** `-1 mut.fq -2 mut.fq -r ref.fa -o filtered/ -dep 10 -que 30`
**Explanation:** Sets minimum read depth (`-dep`) of 10 and minimum mapping quality (`-que`) of 30 to filter unreliable SNP calls.

### Generate Manhattan plot
**Args:** `-1 mut.fq -2 mut.fq -r ref.fa -o results/ --manhattan`
**Explanation:** The `--manhattan` flag generates a Manhattan plot visualization of SNP index across chromosomes, highlighting significant regions.
