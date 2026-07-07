---
name: svclone
category: cancer
description: Computational method for inferring cancer cell fraction of tumour SVs from WGS.
tags: [svclone, cancer-genomics, sv-analysis, copy-number]
author: oxo-call-community
source_url: "https://github.com/mcmero/SVclone"
---

## Concepts

- **Tool Overview**: svclone (v1.1.4) infers cancer cell fraction from structural variants.
- **Core Function**: Determines cancer cell fraction (CCF) of somatic SVs in tumors.
- **Algorithm**: Uses statistical modeling to estimate cellular prevalence of SVs.
- **Input/Output**: Input: SV VCF, copy number data; Output: CCF estimates.
- **Applications**: Cancer genomics, tumor heterogeneity, clonal evolution.
- **Installation**: `conda install -c bioconda svclone` or download from GitHub.

## Pitfalls

- **Input Requirements**: Requires both SV calls and copy number data.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Analysis of large datasets can be slow.
- **Parameter Tuning**: Incorrect parameters affect CCF estimation.
- **Tumor Purity**: Requires accurate tumor purity estimates.
- **Copy Number Quality**: Poor copy number data affects results.

## Examples

### Display help
**Args:** `svclone --help`
**Explanation:** Shows available options and usage information.

### Basic CCF estimation
**Args:** `svclone infer -i sv.vcf -c copy_number.txt -o ccf_results.txt`
**Explanation:** Infer cancer cell fraction from SVs.

### With purity estimate
**Args:** `svclone infer -i sv.vcf -c copy_number.txt -o ccf_results.txt -p 0.8`
**Explanation:** Use known tumor purity of 80%.

### Verbose mode
**Args:** `svclone infer -i sv.vcf -c copy_number.txt -o ccf_results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svclone infer -i sv.vcf -c copy_number.txt -o ccf_results.txt --stats`
**Explanation:** Generate statistics about CCF estimation.

### Batch processing
**Args:** `svclone infer -i vcfs/ -c copy_numbers/ -o results/`
**Explanation:** Process multiple samples together.

### Filter by quality
**Args:** `svclone infer -i sv.vcf -c copy_number.txt -o ccf_results.txt -q 0.9`
**Explanation:** Filter by confidence score.

### Include clonal clusters
**Args:** `svclone infer -i sv.vcf -c copy_number.txt -o ccf_results.txt --clusters`
**Explanation:** Identify clonal clusters.

### Generate report
**Args:** `svclone infer -i sv.vcf -c copy_number.txt -o ccf_results.txt --report`
**Explanation:** Generate comprehensive HTML report.
