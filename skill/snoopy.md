---
name: snoopy
category: variant-analysis
description: Snoopy - Metagenomic SNP caller for strain-level variant detection in long reads
tags: [snoopy, variant-analysis, metagenomics, snps, long-reads]
author: oxo-call-community
source_url: "https://github.com/RolandFaure/snoopy"
---

## Concepts

- **Tool Overview**: snoopy (v0.4.3) - A SNP caller for metagenomic long-read data
- **Core Function**: Detects strain-level SNPs in metagenomic long-read sequences
- **Input/Output**: Accepts BAM alignments; outputs VCF with SNP calls
- **Algorithm**: Analyzes long-read alignments for strain-specific variants
- **Installation**: `conda install -c bioconda snoopy`
- **Key Features**: Strain-level detection, long-read support, metagenomics

## Pitfalls

- **Input Requirements**: Requires properly aligned long-read BAM files
- **Read Depth**: Requires sufficient read depth for strain detection
- **Reference Quality**: Quality of reference affects SNP calling
- **Strain Complexity**: Complex communities may be difficult to resolve
- **Memory Usage**: Large datasets require significant memory
- **False Positives**: May produce false positives in low-coverage regions

## Examples

### Display help
**Args:** `snoopy --help`
**Explanation:** Shows available options and usage information.

### Basic SNP calling
**Args:** `snoopy -i aligned.bam -r reference.fasta -o snps.vcf`
**Explanation:** Call SNPs from metagenomic BAM file.

### With minimum depth
**Args:** `snoopy -i aligned.bam -r reference.fasta -o snps.vcf --min-depth 10`
**Explanation:** Set minimum read depth for SNP calling.

### With strain detection
**Args:** `snoopy -i aligned.bam -r reference.fasta -o snps.vcf --detect-strains`
**Explanation:** Enable strain-level detection.

### Filter by quality
**Args:** `snoopy -i aligned.bam -r reference.fasta -o snps.vcf --min-quality 20`
**Explanation:** Filter SNPs by minimum quality score.

### With frequency threshold
**Args:** `snoopy -i aligned.bam -r reference.fasta -o snps.vcf --min-freq 0.05`
**Explanation:** Set minimum allele frequency threshold.

### Output strain info
**Args:** `snoopy -i aligned.bam -r reference.fasta -o snps.vcf --strain-info strains.txt`
**Explanation:** Output strain information to file.

### Generate report
**Args:** `snoopy -i aligned.bam -r reference.fasta -o snps.vcf --report report.html`
**Explanation:** Generate analysis report.