---
name: ccat
category: epigenomics
description: ChIP-seq peak caller with negative control for identifying enriched regions
tags: [ccat, chip-seq, peak-calling, epigenomics]
author: oxo-call-community
source_url: "http://cmb.gis.a-star.edu.sg/ChIPSeq/paperCCAT.htm"
---

## Concepts

- **Tool Overview**: CCAT is a ChIP-seq peak caller that uses negative control for improved specificity.
- **Core Function**: Identifies enriched regions in ChIP-seq data with control sample normalization.
- **Algorithm**: Uses signal-to-noise ratio and local background estimation.
- **Input**: Aligned BAM files for ChIP and control samples.
- **Output**: Peak calls with significance scores.
- **Application**: Transcription factor binding and histone modification studies.
- **Installation**: Install via bioconda: `conda install -c bioconda ccat`

## Pitfalls

- **Control Required**: Requires input/control sample for accurate peak calling.
- **BAM Format**: Requires sorted and indexed BAM files.
- **Fragment Size**: Must specify or estimate fragment length.
- **FDR Control**: Adjust FDR threshold based on desired stringency.

## Examples

### Call ChIP-seq peaks
**Args:** `CCAT -c chip.bam -i input.bam -f 200 -o peaks.tsv`
**Explanation:** Calls peaks from ChIP sample with input control, using 200bp fragment size.

### Set FDR threshold
**Args:** `CCAT -c chip.bam -i input.bam -f 200 -q 0.01 -o peaks.tsv`
**Explanation:** Uses 1% FDR threshold for peak calling.

### Display help
**Args:** `CCAT --help`
**Explanation:** Shows all available options and usage information.
