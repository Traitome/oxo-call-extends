---
name: cellsnp-lite
category: variant-calling
description: Efficient genotyping bi-allelic SNPs on single cells
tags: [cellsnp-lite, single-cell, snp, genotyping, variant-calling, scrna-seq]
author: oxo-call-community
source_url: "https://github.com/single-cell-genetics/cellsnp-lite"
---

## Concepts

- **Tool Overview**: cellsnp-lite is a fast and memory-efficient tool for genotyping bi-allelic SNPs in single-cell RNA-seq data. Supports both UMI-based and read-based counting.
- **Core Function**: Counts alleles and genotypes SNPs from single-cell BAM/CRAM files with cell barcode information.
- **Input/Output**: Input: Indexed BAM/CRAM files with cell barcodes (CB tag), optional VCF with candidate SNPs. Output: VCF file and sparse matrices of allele counts.
- **Two Modes**: Mode 1 uses candidate SNPs from input VCF. Mode 2 performs de novo SNP calling (requires reference genome).
- **UMI Handling**: Automatically handles UMI deduplication when UB tag is present. Use `--UMItag None` for read-based counting.
- **Cell Barcodes**: Uses CB tag by default. Provide barcode list with `-b/--barcodeFile` for specific cells.
- **Threading**: Supports multi-threading with `-p/--nproc` for parallel processing of multiple positions.

## Pitfalls

- **Indexed BAM Required**: Input BAM/CRAM files must be indexed (.bai/.crai files present).
- **Reference for Mode 2**: De novo SNP calling requires faidx-indexed reference genome (`-f/--refseq`).
- **Memory Usage**: Use `--maxDEPTH` to limit reads per position and avoid excessive memory usage.
- **Chromosome Names**: Default chromosomes are 1-22. Use `--chrom` for other chromosomes or chr-prefix format.
- **UMI vs Read Counting**: UMI mode filters duplicates by default. For read-based counting, set `--UMItag None`.
- **Missing REF**: If input VCF has missing REF alleles, provide reference genome to extract them.

## Examples

### Genotype SNPs from single-cell BAM with UMI
**Args:** `-s sample.bam -b barcodes.tsv -R snps.vcf -O output_dir --genotype -p 4`
**Explanation:** Genotypes SNPs from the VCF file in the single-cell BAM using UMI deduplication, outputs VCF and count matrices with 4 threads.

### Count alleles without genotyping
**Args:** `-s sample.bam -b barcodes.tsv -R snps.vcf -O output_dir -p 8`
**Explanation:** Only counts alleles without performing genotyping, faster for large-scale counting tasks.

### De novo SNP calling with reference genome
**Args:** `-s sample.bam -b barcodes.tsv -f reference.fa --chrom 1,2,3 -O output_dir --genotype`
**Explanation:** Performs de novo SNP calling on chromosomes 1-3 using the reference genome for REF alleles.

### Process multiple samples
**Args:** `-s sample1.bam,sample2.bam,sample3.bam -I sample1,sample2,sample3 -R snps.vcf -O output_dir`
**Explanation:** Processes multiple BAM files with corresponding sample IDs, outputs combined results.

### Use targets instead of regions for streaming
**Args:** `-s sample.bam -T snps.vcf -O output_dir`
**Explanation:** Uses streaming mode (-T) instead of random access (-R), faster for processing many SNPs sequentially.

### Genotype with custom barcode tag
**Args:** `-s sample.bam --cellTAG XC -b barcodes.tsv -R snps.vcf -O output_dir`
**Explanation:** Uses custom tag XC for cell barcodes instead of default CB tag.

### Read-based counting without UMI
**Args:** `-s sample.bam -b barcodes.tsv -R snps.vcf -O output_dir --UMItag None`
**Explanation:** Counts reads instead of UMIs, useful when UMI information is not available or not needed.

### Apply quality filters
**Args:** `-s sample.bam -b barcodes.tsv -R snps.vcf -O output_dir --minMAPQ 30 --minLEN 50`
**Explanation:** Filters reads with MAPQ < 30 and alignment length < 50bp for higher confidence calls.

### Output compressed files
**Args:** `-s sample.bam -b barcodes.tsv -R snps.vcf -O output_dir --gzip`
**Explanation:** Compresses output files using BGZF format for storage efficiency.

### Set minimum UMI count and MAF
**Args:** `-s sample.bam -b barcodes.tsv -R snps.vcf -O output_dir --minCOUNT 10 --minMAF 0.05`
**Explanation:** Requires minimum 10 UMIs and 5% minor allele frequency for SNP inclusion in output.
