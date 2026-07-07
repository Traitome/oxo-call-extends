---
name: hmftools-pave
category: variant-calling
description: PAVE annotates SNV/MNV/INDEL calls with consequence on corresponding genes, transcripts, and proteins.
tags: [hmftools-pave, variant-calling, SNV, MNV, INDEL, annotation, VCF, genes]
author: oxo-call-community
source_url: "https://github.com/hartwigmedical/hmftools/tree/master/pave"
---

## Concepts

- **Tool Overview**: PAVE (v1.8.2) is a Java-based variant annotation tool from Hartwig Medical Foundation that annotates SNVs, MNVs, and small indels with their functional consequences on genes, transcripts, and proteins.

- **Transcript Consequence Prediction**: Predicts variant effects including missense, nonsense, frameshift, in-frame indels, splice site disruptions, and upstream/downstream annotations using Ensembl gene annotations.

- **Canonical Transcript Selection**: Automatically selects canonical transcripts based on CCDS and Ensembl annotations. Reports consequences on both canonical and all affected transcripts.

- **VCF Standard Compliance**: Input and output in standard VCF 4.x format with INFO field annotations. Compatible with downstream GATK, ANNOVAR, and VEP workflows.

- **Multi-sample Processing**: Can annotate multiple samples in a single VCF file with separate output per sample. Efficient for cohort studies and matched tumor-normal analysis.

- **Annotation Sources**: Uses Ensembl gene annotations (via gene-utils resources) for GRCh37 and GRCh38. Requires pre-generated annotation databases for both genome builds.

## Pitfalls

- **Ensembl Annotation Dependency**: Requires gene-utils to generate Ensembl annotation files beforehand. Without annotations, PAVE cannot determine transcript consequences.

- **Reference Genome Match**: Input VCF must be aligned to the same reference genome as the annotation files. GRCh37 annotations cannot be used with GRCh38 VCFs.

- **Multi-allelic Variant Handling**: Multi-allelic variants in VCF require special handling. PAVE may split multi-allelics into separate annotations but some downstream tools prefer decomposed VCFs.

- **Splice Region Definitions**: Splice site annotations depend on definitions in the gene-utils resource files. Different annotation versions may use different splice region boundaries.

- **Insufficient Memory for Large Files**: WGS VCFs with millions of variants need 4GB+ heap memory. Use `-Xmx8G` for whole genome samples.

- **Non-standard Chromosome Names**: Input VCFs must use chromosome names matching the annotation (chr1 vs 1). Mismatches cause zero annotations.

## Examples

### Annotate somatic variants
**Args:** `pave -sample tumor1 -input somatic_variants.vcf -ref_genome GRCh37_hmf -output_dir ./pave/`
**Explanation:** Annotates somatic VCF from SAGE or similar variant caller. Adds gene, transcript, and protein consequence annotations to INFO field.

### Tumor-normal paired annotation
**Args:** `pave -sample tumor1 -input variants.vcf -ref_genome GRCh37_hmf -output_dir ./pave/ -tumor_id tumor1 -normal_id normal1`
**Explanation:** Specifies tumor and normal sample IDs for proper sample-specific annotation in multi-sample VCF.

### Use custom gene annotation file
**Args:** `pave -sample tumor1 -input variants.vcf -ref_genome GRCh37_hmf -annotation_file custom_annotations.tsv -output_dir ./pave/`
**Explanation:** Uses custom annotation file instead of default Ensembl annotations. Useful for custom gene sets or novel transcripts.

### Annotate and preserve existing annotations
**Args:** `pave -sample tumor1 -input variants_with_gnomad.vcf -ref_genome GRCh37_hmf -output_dir ./pave/ -preserve_info`
**Explanation:** Preserves existing INFO field annotations from input VCF. New PAVE annotations are added alongside existing ones.

### Specify output VCF filename
**Args:** `pave -sample tumor1 -input variants.vcf -ref_genome GRCh37_hmf -output_file annotated_variants.vcf -output_dir ./pave/`
**Explanation:** Sets explicit output filename. Default uses sample ID as filename prefix.

### High-memory mode for WGS
**Args:** `pave -sample tumor1 -input wgs_variants.vcf -ref_genome GRCh37_hmf -output_dir ./pave/ -Xmx16G`
**Explanation:** Allocates 16GB heap memory for WGS samples with millions of variants. Prevents out-of-memory errors for large-scale studies.

### Run on GRCh38 reference
**Args:** `pave -sample tumor1 -input variants.vcf -ref_genome GRCh38_hmf -output_dir ./pave/`
**Explanation:** Uses GRCh38 Ensembl annotations. All input must be GRCh38-aligned. Separate annotation files are required for GRCh38.
