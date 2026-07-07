---
name: simplesam
category: formatting
description: simplesam - Simple Python SAM parser
tags: ["simplesam", "formatting", "sam", "python"]
author: oxo-call-community
source_url: "http://simplesam.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: simplesam (v0.1.4.2) is a simple Python SAM/BAM parser.
- **Core Function**: Reads and writes SAM/BAM alignment files.
- **Algorithm**: Parses SAM format with lightweight Python objects.
- **Input/Output**: Accepts SAM/BAM files and produces alignment objects.
- **Alignment Handling**: Specialized for SAM/BAM processing.
- **Applications**: Alignment processing, bioinformatics pipelines.

## Pitfalls

- **Memory Usage**: High memory for large alignment files.
- **Dependency Issues**: Requires Python environment.
- **BAM Support**: Limited BAM handling capabilities.
- **Version Compatibility**: Different versions may have breaking changes.
- **Performance**: May be slower for very large files.
- **Documentation**: Limited documentation available.

## Examples

### Read SAM file
**Args:** `python -c "import simplesam; for read in simplesam.reader(open('alignments.sam')): print(read.qname)"`
**Explanation:** Iterates over SAM records.

### Write SAM file
**Args:** `python -c "import simplesam; writer = simplesam.writer(open('out.sam', 'w')); writer.write(read)"`
**Explanation:** Writes SAM records to file.

### Filter reads
**Args:** `python -c "import simplesam; [r for r in simplesam.reader(open('alignments.sam')) if r.mapping_quality >= 30]"`
**Explanation:** Filters reads by mapping quality.

### Help command
**Args:** `python -c "import simplesam; help(simplesam)"`
**Explanation:** Shows available classes and methods.

### Version check
**Args:** `python -c "import simplesam; print(simplesam.__version__)"`
**Explanation:** Shows current version.

### Parse BAM
**Args:** `python -c "import simplesam; for read in simplesam.reader(open('alignments.bam', 'rb')): print(read)"`
**Explanation:** Reads BAM file in binary mode.

### Get read info
**Args:** `python -c "import simplesam; read = next(simplesam.reader(open('alignments.sam'))); print(read.pos, read.cigar)"`
**Explanation:** Accesses read position and CIGAR string.
