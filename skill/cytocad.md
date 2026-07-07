---
name: cytocad
category: qc
description: Large copy-number variation detector with low-depth whole-genome sequencing data
tags: [cytocad, qc, CNV, copy-number, low-depth-sequencing]
author: oxo-call-community
source_url: "https://github.com/cytham/cytocad"
---

## Concepts

- **Tool Overview**: cytocad (v1.0.3+) is a tool for detecting large copy-number variations (CNVs) from low-depth whole-genome sequencing data.
- **Core Function**: Identifies large-scale genomic copy-number changes using read depth analysis.
- **Input/Output**: Input: BAM alignments or read count files. Output: CNV calls, segmentation profiles.
- **Algorithm**: Uses Hidden Markov Models (HMM) or segmentation algorithms for CNV detection.
- **Key Features**: Works with low-depth data, detects large CNVs, provides visualization.
- **Installation**: `conda install -c bioconda cytocad`

## Pitfalls

- **Low-Depth Data**: Optimized for low-depth sequencing; may miss small CNVs.
- **Reference Bias**: Requires matched normal or reference panel for normalization.
- **Segmentation**: May merge adjacent CNVs or miss complex events.
- **GC Content**: GC bias may affect read depth calculations.
- **Validation**: CNV calls should be validated with orthogonal methods.

## Examples

### Detect CNVs from BAM
**Args:** `cytocad -i tumor.bam -o cnv_calls.txt`
**Explanation:** Detect copy-number variations from low-depth sequencing data.

### Use matched normal
**Args:** `cytocad -i tumor.bam -n normal.bam -o cnv_calls.txt`
**Explanation:** Use matched normal sample for improved CNV calling.

### Generate visualization
**Args:** `cytocad -i tumor.bam -o cnv_calls.txt --plot cnv_profile.png`
**Explanation:** Generate visualization of CNV profile.
