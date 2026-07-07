---
name: bax2bam
category: formatting
description: bax2bam - Convert PacBio legacy bax.h5 format to BAM format
tags: [bax2bam, formatting, BAM, HDF5, PacBio]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/bax2bam"
---

## Concepts

- **Tool Overview**: bax2bam (v0.0.11) converts PacBio's legacy basecall format (bax.h5) into the modern BAM format, enabling compatibility with standard bioinformatics tools.
- **Core Function**: Converts legacy PacBio bax.h5 files to BAM format for downstream analysis.
- **Format Conversion**: Transforms HDF5-based bax.h5 files to BAM alignment format.
- **PacBio Specific**: Designed specifically for PacBio sequencing data conversion.
- **Lossless Conversion**: Maintains all basecall information during conversion.
- **Input/Output**: Accepts bax.h5 files; outputs BAM files.
- **Installation**: `conda install -c bioconda bax2bam`.

## Pitfalls

- **Legacy Format**: Only works with older PacBio bax.h5 format, not newer BAM-based outputs.
- **File Compatibility**: Requires matching bas.h5 and metadata files for complete conversion.
- **HDF5 Dependencies**: Requires HDF5 libraries for reading bax.h5 files.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Basic conversion
**Args:** `bax2bam -i input.bax.h5 -o output.bam`
**Explanation:** Converts bax.h5 file to BAM format.

### Multiple input files
**Args:** `bax2bam -i movie1.bax.h5 -i movie2.bax.h5 -o output.bam`
**Explanation:** Combines multiple bax.h5 files into single BAM.

### Specify bas.h5 file
**Args:** `bax2bam -i input.bax.h5 -b input.bas.h5 -o output.bam`
**Explanation:** Uses specified bas.h5 file for metadata.

### Output SAM format
**Args:** `bax2bam -i input.bax.h5 -o output.sam --sam`
**Explanation:** Outputs in SAM format instead of BAM.

### Include metadata
**Args:** `bax2bam -i input.bax.h5 -o output.bam --metadata`
**Explanation:** Includes additional metadata in output.

### Verbose mode
**Args:** `bax2bam -i input.bax.h5 -o output.bam -v`
**Explanation:** Provides detailed conversion progress information.

### Display help
**Args:** `bax2bam --help`
**Explanation:** Shows all available command-line options and usage information.