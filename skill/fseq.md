---
name: fseq
category: utility
description: "F-Seq: A feature density estimator for high-throughput sequence tags."
tags: [fseq, ChIP-seq, peak calling, feature detection]
author: oxo-call-community
source_url: "http://fureylab.web.unc.edu/software/fseq/"
---
## Concepts
- **Peak Calling**: Identifies peaks in high-throughput sequencing data.
- **Feature Density**: Estimates density of sequence tags across the genome.
- **ChIP-seq Analysis**: Designed for ChIP-seq peak detection.
- **Statistical Modeling**: Uses kernel density estimation for peak identification.
- **False Discovery Rate**: Controls false positive rate in peak calling.

## Pitfalls
- **Data Quality**: Requires high-quality sequencing data.
- **Input Format**: Limited input format support.
- **Parameter Tuning**: Requires careful parameter adjustment.
- **Genome Size**: Performance depends on genome size.
- **Memory Usage**: Large datasets require significant memory.

## Examples
### Call peaks from BED file
**Args:** `fseq -i peaks.bed -o peaks_out/`
**Explanation:** Calls peaks from input BED file.

### With control data
**Args:** `fseq -i treatment.bed -c control.bed -o peaks_out/`
**Explanation:** Uses control data for background subtraction.

### Specify fragment size
**Args:** `fseq -i peaks.bed -f 200 -o peaks_out/`
**Explanation:** Sets fragment size to 200bp.

### Adjust bandwidth
**Args:** `fseq -i peaks.bed -b 100 -o peaks_out/`
**Explanation:** Sets kernel bandwidth to 100bp.

### Output BED format
**Args:** `fseq -i peaks.bed -f 200 -o peaks.bed -F bed`
**Explanation:** Outputs peaks in BED format.