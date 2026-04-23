---
name: bed2gtf
category: formatting
description: A high-performance BED-to-GTF converter written in Rust
tags: [bed, gtf, format-conversion, rust]
author: oxo-call-community
source_url: "https://github.com/alejandrogzi/bed2gtf"
---

## Concepts
- **Tool Overview**: bed2gtf is a high-performance command-line tool written in Rust for converting BED format files to GTF format. It leverages Rust's performance characteristics to provide fast conversion of large genomic interval files.
- **BED Format**: BED (Browser Extensible Data) is a tab-separated format describing genomic intervals with at least 3 columns: chrom, chromStart, chromEnd. Optional columns include name, score, strand, etc.
- **GTF Format**: GTF (Gene Transfer Format) is a tab-separated format with 9 columns: seqname, source, feature, start, end, score, strand, frame, attribute. GTF uses 1-based coordinates while BED uses 0-based.
- **Coordinate Conversion**: bed2gtf handles the coordinate system conversion from BED's 0-based half-open to GTF's 1-based closed interval.

## Pitfalls
- **Coordinate System**: BED uses 0-based half-open coordinates while GTF uses 1-based closed coordinates. bed2gtf handles this conversion automatically.
- **Feature Type**: BED files lack explicit feature type information. The default feature type in the output GTF may need manual adjustment depending on the biological context.
- **Attribute Field**: GTF requires an attribute field (column 9). If the BED file lacks a name column, bed2gtf generates placeholder attributes.

## Examples
### Basic BED to GTF conversion
**Args:** `bed2gtf -i input.bed -o output.gtf`
**Explanation:** Converts input.bed to GTF format, writing results to output.gtf.

### Convert with strand information
**Args:** `bed2gtf -i peaks.bed -o peaks.gtf`
**Explanation:** Converts a BED file containing peak regions to GTF format, preserving strand information if present in the BED file.

### Convert and pipe to downstream tool
**Args:** `bed2gtf -i regions.bed -o - | head -20`
**Explanation:** Converts BED to GTF and outputs to stdout for piping to other tools.
