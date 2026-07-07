---
name: ctat-mutations
category: variant-calling
description: Mutation detection in RNA-Seq using GATK-v4.0 with CRAVAT filtering
tags: [ctat-mutations, variant-calling, RNA-seq, GATK, CRAVAT, mutations]
author: oxo-call-community
source_url: "https://github.com/NCIP/ctat-mutations"
---

## Concepts

- **Tool Overview**: ctat-mutations (v2.1.0+) is a pipeline for detecting mutations from RNA-Seq data using GATK v4.0 with CRAVAT-based filtering.
- **Core Function**: Identifies somatic mutations in RNA-Seq data, performs variant calling, annotation, and filtering.
- **Input/Output**: Input: BAM alignments, reference genome, VCF files. Output: Filtered variant calls, annotation reports.
- **Algorithm**: Uses GATK HaplotypeCaller for variant calling, CRAVAT for functional annotation and filtering.
- **Key Features**: RNA-Seq specific variant calling, comprehensive annotation sources, automated filtering based on biological impact.
- **Installation**: `conda install -c bioconda ctat-mutations`

## Pitfalls

- **RNA-Seq Specific**: Optimized for RNA-Seq data; not suitable for DNA sequencing data.
- **Strand Bias**: RNA editing events may be misidentified as mutations; use strand-specific filtering.
- **Splice Junctions**: Variants near splice junctions require special handling; ensure proper annotation.
- **Annotation Databases**: Requires up-to-date annotation databases for accurate variant classification.
- **Memory Usage**: Large BAM files may require significant memory for variant calling.

## Examples

### Call variants from RNA-Seq BAM
**Args:** `ctat-mutations -i aligned.bam -r reference.fasta -o variants.vcf`
**Explanation:** Perform variant calling on RNA-Seq alignments using GATK.

### Annotate and filter variants
**Args:** `ctat-mutations -i variants.vcf -o annotated.vcf --annotate --filter`
**Explanation:** Annotate variants with CRAVAT and apply filtering based on functional impact.

### Run complete pipeline
**Args:** `ctat-mutations pipeline -1 reads_R1.fastq -2 reads_R2.fastq -r reference.fasta -o results/`
**Explanation:** Run the complete mutation detection pipeline from raw reads to filtered variants.
