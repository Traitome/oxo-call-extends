---
name: smncopynumbercaller
category: variant-calling
description: SMNCopyNumberCaller - Call copy number of SMN1, SMN2, and SMN2Δ7-8 from BAM files for SMA carrier screening
tags: [smncopynumbercaller, variant-calling, smn1, smn2, copy-number, sma]
author: oxo-call-community
source_url: "https://github.com/Illumina/SMNCopyNumberCaller"
---

## Concepts

- **Tool Overview**: smncopynumbercaller (v1.1.2) - A tool for calling SMN1/SMN2 copy number from sequencing data
- **Core Function**: Determines copy number of SMN1, SMN2, and SMN2Δ7-8 genes from BAM files
- **Input/Output**: Accepts BAM files; outputs VCF with copy number calls
- **Algorithm**: Uses read depth analysis to estimate gene copy number
- **Installation**: `conda install -c bioconda smncopynumbercaller`
- **Key Features**: SMA carrier screening, handles SMN1/SMN2 differentiation

## Pitfalls

- **BAM Requirements**: Requires properly aligned and indexed BAM file
- **Reference Genome**: Must use compatible reference genome (GRCh37/GRCh38)
- **Coverage Depth**: Requires sufficient coverage in SMN region
- **PCR Duplicates**: Should be marked or removed before analysis
- **Sample Quality**: Poor quality data affects copy number accuracy
- **Output Interpretation**: Copy number calls require careful interpretation

## Examples

### Display help
**Args:** `smncopynumbercaller --help`
**Explanation:** Shows available options and usage information.

### Basic copy number calling
**Args:** `smncopynumbercaller -i input.bam -r reference.fasta -o output.vcf`
**Explanation:** Call SMN1/SMN2 copy number from BAM file.

### With bed regions
**Args:** `smncopynumbercaller -i input.bam -r reference.fasta -b regions.bed -o output.vcf`
**Explanation:** Use custom BED file for target regions.

### Generate report
**Args:** `smncopynumbercaller -i input.bam -r reference.fasta -o output.vcf -s report.txt`
**Explanation:** Generate summary report with copy number statistics.

### Multi-sample analysis
**Args:** `smncopynumbercaller -b sample_list.txt -r reference.fasta -o results_dir/`
**Explanation:** Process multiple samples in batch.

### Force GRCh37 reference
**Args:** `smncopynumbercaller -i input.bam -r reference.fasta -o output.vcf --grch37`
**Explanation:** Force GRCh37 reference genome mode.

### Force GRCh38 reference
**Args:** `smncopynumbercaller -i input.bam -r reference.fasta -o output.vcf --grch38`
**Explanation:** Force GRCh38 reference genome mode.

### Output JSON format
**Args:** `smncopynumbercaller -i input.bam -r reference.fasta -o output.json -f json`
**Explanation:** Output results in JSON format.