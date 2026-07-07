---
name: cutesv
category: variant-calling
description: cuteSV is a sensitive, fast long-read structural variation detector using clustering and refinement algorithms
tags: [cutesv, structural-variation, long-read, pacbio, nanopore, SV, DEL, INS, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/tjiangHIT/cuteSV"
---

## Concepts

- **Tool Overview**: cuteSV (v2.1.3+) is a sensitive, fast, scalable long-read-based structural variation detection tool.
- **Core Function**: Discovers SVs (insertions, deletions, duplications, inversions, translocations) from PacBio and Oxford Nanopore sequencing data using signature clustering and refinement.
- **Algorithm**: (1) Collects SV signatures from split alignments and discordant read pairs. (2) Clusters signatures by type and proximity. (3) Refines breakpoints through local alignment. (4) Reports high-confidence SV calls in VCF format.
- **Input/Output**: Input: sorted BAM, reference FASTA. Output: VCF file with SV calls
- **Installation**: `pip install cuteSV` or `conda install -c bioconda cutesv`

## Pitfalls

- **Sorted BAM Required**: Input BAM must be coordinate-sorted with proper index (.bai file)
- **Parameter Tuning**: Different data types require different parameters (see below for PacBio CLR, CCS, ONT recommendations)
- **Min Support**: Use `--min_support` to filter spurious SVs; higher values increase specificity
- **Genotyping**: Use `--genotype` flag to enable actual genotyping rather than just detection

## Examples

### Basic SV detection
**Args:** `cuteSV sorted_reads.bam reference.fa output.vcf work_dir/`
**Explanation:** Standard workflow: provide sorted BAM, reference, output VCF path, and working directory.

### Multi-threaded detection
**Args:** `cuteSV sorted_reads.bam ref.fa output.vcf work_dir/ --threads 16`
**Explanation:** Use multiple threads to accelerate processing; recommended for large datasets.

### PacBio CLR data
**Args:** `cuteSV reads.bam ref.fa output.vcf work_dir/ --max_cluster_bias_INS 100 --diff_ratio_merging_INS 0.3 --max_cluster_bias_DEL 200 --diff_ratio_merging_DEL 0.5`
**Explanation:** Parameters optimized for PacBio CLR data with higher error rate.

### PacBio CCS/HIFI data
**Args:** `cuteSV reads.bam ref.fa output.vcf work_dir/ --max_cluster_bias_INS 1000 --diff_ratio_merging_INS 0.9 --max_cluster_bias_DEL 1000 --diff_ratio_merging_DEL 0.5 --min_support 5`
**Explanation:** HiFi data has lower error rate, allowing more lenient clustering and higher sensitivity.

### Oxford Nanopore data
**Args:** `cuteSV reads.bam ref.fa output.vcf work_dir/ --max_cluster_bias_INS 100 --diff_ratio_merging_INS 0.3 --max_cluster_bias_DEL 100 --diff_ratio_merging_DEL 0.3`
**Explanation:** ONT-optimized settings with moderate clustering bias for both insertions and deletions.

### Genotyping SVs
**Args:** `cuteSV reads.bam ref.fa output.vcf work_dir/ --genotype --min_support 3`
**Explanation:** Enable genotyping mode to estimate allele frequencies and improve accuracy of SV calls.

### Report read IDs supporting each SV
**Args:** `cuteSV reads.bam ref.fa output.vcf work_dir/ --report_readid`
**Explanation:** Add read names to VCF INFO field for downstream validation or manual inspection.
