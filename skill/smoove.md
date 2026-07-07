---
name: smoove
category: structural-variation
description: smoove - structural variant calling and genotyping pipeline using existing tools in a smooth workflow
tags: [smoove, structural-variation, variant-calling, sv, lumpy]
author: oxo-call-community
source_url: "https://github.com/brentp/smoove"
---

## Concepts

- **Tool Overview**: smoove (v0.2.8) - A pipeline for structural variant calling and genotyping
- **Core Function**: Detects and genotypes structural variants using LUMPY and other tools
- **Input/Output**: Accepts BAM files; outputs VCF with structural variant calls
- **Algorithm**: Combines multiple SV callers with genotype refinement
- **Installation**: `conda install -c bioconda smoove`
- **Key Features**: Integrated pipeline, multi-sample calling, genotype refinement

## Pitfalls

- **BAM Requirements**: Requires properly aligned and indexed BAM files
- **Reference Genome**: Must use correct reference genome
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory for large BAM files
- **SV Complexity**: May miss complex structural variants
- **Output Interpretation**: SV calls require manual verification

## Examples

### Display help
**Args:** `smoove --help`
**Explanation:** Shows available options and usage information.

### Call SVs from single sample
**Args:** `smoove call -x -p 8 --outdir results/ --name sample1 -f reference.fasta input.bam`
**Explanation:** Call structural variants from single BAM file.

### Call SVs from multiple samples
**Args:** `smoove call -x -p 8 --outdir results/ --name cohort -f reference.fasta sample1.bam sample2.bam sample3.bam`
**Explanation:** Call SVs from multiple samples together.

### Genotype SVs
**Args:** `smoove genotype -x -p 8 --outdir results/ -f reference.fasta --vcf cohort.svs.vcf.gz sample.bam`
**Explanation:** Genotype SVs in additional samples.

### Merge SV calls
**Args:** `smoove merge --outdir results/ --name merged -f reference.fasta cohort1.svs.vcf.gz cohort2.svs.vcf.gz`
**Explanation:** Merge SV calls from multiple cohorts.

### Clean SV calls
**Args:** `smoove clean -i raw.vcf -o cleaned.vcf`
**Explanation:** Clean and filter raw SV calls.

### Generate report
**Args:** `smoove stats -i cohort.svs.vcf.gz -o stats.txt`
**Explanation:** Generate SV calling statistics.

### With custom parameters
**Args:** `smoove call -x -p 8 --outdir results/ --name sample -f reference.fasta --extra lumpy --extra-svtyper input.bam`
**Explanation:** Pass extra parameters to LUMPY and SVtyper.