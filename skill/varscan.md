---
name: varscan
category: variant-calling
description: variant detection in massively parallel sequencing data
tags: [varscan, variant-calling, snp, indel, tumor-normal]
author: oxo-call-community
source_url: "http://dkoboldt.github.io/varscan/"
---

## Concepts

- **Tool Overview**: VarScan (v2.4.6+) is a variant detection tool for massively parallel sequencing data that identifies SNPs and indels from aligned reads. It supports both germline and somatic variant calling.
- **Core Function**: Calls variants by comparing read alignments against a reference genome, using statistical thresholds to distinguish true variants from sequencing errors.
- **Input/Output**: Input: BAM file with aligned reads, reference FASTA. Output: VCF file with called variants.
- **Algorithm**: Uses a statistical approach to detect variants based on allele frequency, coverage, and quality scores. Supports somatic calling with matched tumor-normal pairs.
- **Key Features**: Supports germline, somatic, and copy number variation calling; works with both single and paired-end data; outputs VCF format for downstream analysis.
- **Installation**: `conda install -c bioconda varscan`

## Pitfalls

- **Input Requirements**: Requires sorted and indexed BAM files. Use `samtools sort` and `samtools index` before running.
- **Reference Index**: Reference FASTA must be indexed with `samtools faidx`.
- **Tumor-Normal Pairing**: For somatic calling, ensure tumor and normal BAMs are from the same individual and aligned to the same reference.
- **Filtering**: VarScan outputs unfiltered variants. Apply filters based on quality, depth, and allele frequency for reliable results.
- **Memory Usage**: For large datasets, consider processing in chunks or increasing Java heap size.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Call variants from mpileup
**Args:** `mpileup2snp mpileup.txt --output-vcf > snps.vcf`
**Explanation:** Calls SNPs from a samtools mpileup file and outputs VCF format.

### Call indels from mpileup
**Args:** `mpileup2indel mpileup.txt --output-vcf > indels.vcf`
**Explanation:** Calls indels from a samtools mpileup file and outputs VCF format.

### Call somatic variants (tumor-normal)
**Args:** `somatic mpileup_normal.txt mpileup_tumor.txt --output-vcf --min-coverage 8`
**Explanation:** Calls somatic variants by comparing normal and tumor mpileup files, requiring minimum coverage of 8.

### Call germline variants
**Args:** `mpileup2cns mpileup.txt --output-vcf > cns.vcf`
**Explanation:** Calls germline variants and outputs copy number status.

### Filter variants by quality
**Args:** `filter snps.vcf --min-avg-qual 20 --min-reads2 3 > filtered.vcf`
**Explanation:** Filters SNPs with minimum average quality of 20 and at least 3 reads supporting the variant.

### Generate mpileup for VarScan
**Args:** `samtools mpileup -f reference.fa aligned.bam > mpileup.txt`
**Explanation:** Generates mpileup file from aligned BAM for VarScan variant calling.

### Call with minimum allele frequency
**Args:** `mpileup2snp mpileup.txt --output-vcf --min-var-freq 0.05 > snps.vcf`
**Explanation:** Calls SNPs with minimum allele frequency of 5%.

### Batch mode for multiple samples
**Args:** `processSomatic somatic.vcf`
**Explanation:** Processes somatic VCF to separate germline, somatic, and LOH calls.