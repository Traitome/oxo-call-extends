---
name: cthreepo
category: annotation
description: A python script to interconvert seq-ids in gff3, gtf, bed and other files.
tags: [cthreepo, annotation, GFF, GTF, BED, seq-id, conversion]
author: oxo-call-community
source_url: "https://github.com/vkkodali/cthreepo"
---

## Concepts

- **Tool Overview**: cthreepo (v0.1.3+) is a Python script for interconverting sequence identifiers across genomic annotation formats.
- **Core Function**: Converts sequence IDs (chromosome names) between different naming conventions in GFF3, GTF, BED, and related files.
- **Input/Output**: Input: GFF3, GTF, BED, or FASTA files. Output: Same format with converted sequence IDs.
- **Supported Conversions**: UCSC to Ensembl, Ensembl to NCBI, custom ID mappings, and more.
- **Key Features**: Batch processing, support for multiple file formats, custom mapping files.
- **Installation**: `conda install -c bioconda cthreepo`

## Pitfalls

- **Mapping File**: Requires a mapping file for custom ID conversions; use `--map-file` option.
- **Format Detection**: Automatically detects input format; ensure files have correct extensions.
- **Header Lines**: Some formats have special header lines that need preservation.
- **Compressed Files**: Supports gzipped input but may require explicit decompression for some operations.
- **Output Overwriting**: By default overwrites output files; use `--no-overwrite` to prevent.

## Examples

### Convert UCSC to Ensembl chromosome names
**Args:** `cthreepo -i input.gff3 -o output.gff3 --from ucsc --to ensembl`
**Explanation:** Convert chromosome names from UCSC format (chr1) to Ensembl format (1).

### Use custom mapping file
**Args:** `cthreepo -i input.bed -o output.bed --map-file custom_mapping.txt`
**Explanation:** Convert sequence IDs using a custom mapping file.

### Process multiple files
**Args:** `cthreepo -i file1.gtf file2.gtf -o output/ --from ncbi --to ucsc`
**Explanation:** Convert multiple GTF files from NCBI to UCSC format.
