---
name: annotwg
category: annotation
description: Efficiently annotate Whole Genome (WG) variants in VCF files with multiple annotation sources
tags: [annotwg, annotation, VCF, CADD, GERP, GnomAD, RefSeq]
author: oxo-call-community
source_url: "https://gitlab.com/cnrgh/annotwg"
---

## Concepts

- **Tool Overview**: annotwg (v1.0) is a high-performance tool for annotating large whole-genome VCF files with annotations from multiple sources including CADD scores, GERP scores, RefSeq, GnomAD frequencies, and more.
- **Core Function**: Efficiently annotates bgzipped and tabix-indexed VCF files using BCF-formatted annotation databases. Built on bcftools for robust performance.
- **Input Requirements**: Input VCF must be bgzipped and indexed with tabix. Annotation files must be in CSI-indexed BCF format.
- **Annotation Sources**: Supports CADD scores, GERP++ conservation scores, RefSeq gene annotations, GnomAD population frequencies, and custom annotation databases.
- **Multi-threading**: Supports parallel processing with configurable thread count for faster annotation of large datasets.
- **Output Options**: Can output as compressed VCF (default) or BCF format. Supports both CSI and TBI indexing.
- **Installation**: Available via Bioconda (`conda install -c bioconda annotwg`) or source installation with bcftools dependency.

## Pitfalls

- **VCF Format**: Input VCF must be bgzipped and indexed with tabix. Use `bgzip` and `tabix` if needed.
- **Annotation Database**: Annotation files must be in BCF format with CSI index. TBI index not supported for annotation files.
- **Reference Genome**: Must provide indexed reference FASTA file (.fai or .dict format).
- **Allele Splitting**: Some variants may be skipped due to allele splitting; use `-m` flag to join alleles.
- **Memory Usage**: Large VCF files with many annotations require sufficient memory. Consider using temporary directory with enough space.
- **Compression Level**: Adjust compression level (-l) based on speed vs file size requirements.

## Examples

### Basic VCF annotation
**Args:** `annotwg -v file.vcf.gz -r ref.fasta -a annot.bcf -o annotated.vcf.gz`
**Explanation:** Annotates VCF file with annotations from BCF file. Requires bgzipped/indexed VCF and CSI-indexed BCF annotation file.

### Multi-threaded annotation
**Args:** `annotwg -v file.vcf.gz -r ref.fasta -a annot.bcf -t 8 -o annotated.vcf.gz`
**Explanation:** Uses 8 threads for parallel processing. Significantly speeds up annotation of large whole-genome VCF files.

### Annotate with specific INFO fields
**Args:** `annotwg -v file.vcf.gz -r ref.fasta -a annot.bcf -s CADD,GERP,GnomAD_AF -o annotated.vcf.gz`
**Explanation:** Only annotates with specified INFO fields (CADD score, GERP score, GnomAD allele frequency). Reduces output size by excluding unnecessary annotations.

### Add prefix to annotations
**Args:** `annotwg -v file.vcf.gz -r ref.fasta -a annot.bcf -p annotwg_ -o annotated.vcf.gz`
**Explanation:** Adds "annotwg_" prefix to all annotation field names. Useful when combining annotations from multiple sources to avoid name conflicts.

### Output as BCF format
**Args:** `annotwg -v file.vcf.gz -r ref.fasta -a annot.bcf -O b -o annotated.bcf`
**Explanation:** Outputs compressed BCF format instead of VCF. Smaller file size, faster I/O for downstream tools.

### Generate TBI index
**Args:** `annotwg -v file.vcf.gz -r ref.fasta -a annot.bcf -T -o annotated.vcf.gz`
**Explanation:** Generates TBI index instead of CSI index for compatibility with tools that require TBI format.

### Join alleles for complete annotation
**Args:** `annotwg -v file.vcf.gz -r ref.fasta -a annot.bcf -m -o annotated.vcf.gz`
**Explanation:** Uses `bcftools norm -m +` to join split alleles, preventing annotation skips for complex variants.

### Custom temporary directory
**Args:** `annotwg -v file.vcf.gz -r ref.fasta -a annot.bcf -d /tmp/annotwg_temp -o annotated.vcf.gz`
**Explanation:** Specifies custom temporary directory for intermediate files. Useful when default /tmp has limited space.

### Display help
**Args:** `annotwg -h`
**Explanation:** Shows available options and usage information.