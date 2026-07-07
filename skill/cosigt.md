---
name: cosigt
category: variant-calling
description: Cosine Similarity-based GenoTyper for variant calling
tags: [cosigt, variant-calling, genotyping, cosine-similarity, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/davidebolo1993/cosigt"
---

## Concepts

- **Tool Overview**: Cosigt (COsine SImilarity-based GenoTyper) is a variant calling tool that uses cosine similarity for accurate genotype calling from sequencing data.
- **Core Function**: Calls genotypes from aligned sequencing reads using cosine similarity metrics.
- **Algorithm**: Uses cosine similarity between read vectors and reference/alternative alleles to determine genotypes.
- **Input**: Aligned reads (BAM), reference genome (FASTA).
- **Output**: Variant calls in VCF format, genotype probabilities.
- **Application**: Variant calling, genotype imputation, genetic analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda cosigt`

## Pitfalls

- **Read Coverage**: Requires sufficient coverage for accurate genotyping.
- **Mapping Quality**: Low-quality mappings can affect calling accuracy.
- **Variant Density**: High variant density may reduce performance.
- **Memory Usage**: Large datasets may require significant memory.
- **Reference Bias**: May have bias toward reference alleles.

## Examples

### Call variants
**Args:** `cosigt -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Calls variants from aligned reads using cosine similarity.

### With quality filtering
**Args:** `cosigt -i aligned.bam -r reference.fasta -q 30 -o variants.vcf`
**Explanation:** Applies quality threshold of 30 for variant calls.

### Output genotype probabilities
**Args:** `cosigt -i aligned.bam -r reference.fasta --probs -o variants.vcf`
**Explanation:** Outputs genotype probabilities along with calls.

### Call specific regions
**Args:** `cosigt -i aligned.bam -r reference.fasta -t targets.bed -o variants.vcf`
**Explanation:** Calls variants only in specified target regions.

### Display help
**Args:** `cosigt --help`
**Explanation:** Shows all available options and usage information.