---
name: kled
category: variant-calling
description: An ultra-fast and sensitive structural variant detection tool for long-read sequencing data.
tags: [kled, variant-calling, structural-variants, long-reads, nanopore]
author: oxo-call-community
source_url: "https://github.com/CoREse/kled"
---

## Concepts

- **Structural Variant Detection**: Calls structural variants (deletions, insertions, inversions, duplications) from long-read data
- **Long-read Sequencing**: Optimized for Oxford Nanopore and PacBio sequencing data
- **Ultra-fast Analysis**: Processes BAM files rapidly with multi-threading support
- **Precise Breakpoints**: Provides precise breakpoint estimation for SVs
- **VCF Output**: Outputs results in standard VCF format for downstream analysis
- **BAM Input**: Works directly with coordinate-sorted BAM files

## Pitfalls

- **Read Mapping Quality**: Low mapping quality reads affect detection accuracy
- **Coverage Requirements**: Sufficient coverage needed for reliable SV detection
- **Read Length**: Longer reads improve SV detection, especially for large events
- **Reference Genome**: Results depend on reference genome quality
- **Parameter Tuning**: Default parameters may need adjustment for different data types
- **False Positives**: May detect false positives in repetitive regions

## Examples

### Detect structural variants
**Args:** `kled -i input.bam -o output.vcf`
**Explanation:** Detects structural variants from a sorted BAM file.

### Specify minimum read length
**Args:** `kled -i input.bam -o output.vcf -l 1000`
**Explanation:** Only uses reads longer than 1000bp for SV detection.

### Multi-threaded processing
**Args:** `kled -i input.bam -o output.vcf -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Filter by SV size
**Args:** `kled -i input.bam -o output.vcf -s 50`
**Explanation:** Reports only SVs larger than 50bp.

### Set minimum allele frequency
**Args:** `kled -i input.bam -o output.vcf -f 0.1`
**Explanation:** Reports SVs with minimum allele frequency of 10%.

### Verbose logging
**Args:** `kled -i input.bam -o output.vcf -v`
**Explanation:** Enables verbose logging for debugging.