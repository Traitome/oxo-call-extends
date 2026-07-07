---
name: flexi-formatter
category: formatting
description: "Flexi-formatter moves flexiplex barcode and UMI sequences to BAM tags for downstream analysis."
tags: [flexi-formatter, formatting, bam, barcode, umi, bioinformatics, sequencing]
author: oxo-call-community
source_url: "https://github.com/VIB-CCB-BioIT/flexiplex_tag_formatter"
---

## Concepts
- **Tool Overview**: Flexi-formatter processes BAM files to extract barcode and UMI sequences from read names and store them as BAM tags for easy access in downstream analysis.
- **Core Function**: Parses flexiplex-formatted read names and converts embedded barcode/UMI information into standardized BAM tags.
- **Input/Output**: Input: BAM file with flexiplex-formatted read names. Output: BAM file with barcode (BC) and UMI (UQ) tags.
- **Tag Standards**: Uses standard SAM/BAM tags (BC for barcode, UQ for UMI) compatible with most bioinformatics tools.
- **Flexiplex Integration**: Specifically designed to work with flexiplex demultiplexing output format.
- **Parallel Processing**: Supports multi-threaded processing for efficient handling of large BAM files.
- **Installation**: `conda install -c bioconda flexi-formatter` or clone from GitHub. Requires Python 3.x and pysam.

## Pitfalls
- **Read Name Format**: Requires flexiplex-specific read name format. Non-flexiplex reads may produce incorrect tags.
- **BAM Index**: Input BAM must be indexed for efficient processing. Generate index if missing.
- **Tag Overwriting**: Existing BC/UQ tags will be overwritten. Backup original BAM if needed.
- **Barcode Length**: Variable barcode lengths require consistent formatting. Ensure all barcodes follow same pattern.
- **Memory Usage**: Large BAM files require sufficient memory. Use chunked processing for memory efficiency.
- **Paired-End Handling**: Ensure proper pairing of reads. Unpaired reads may cause tag assignment errors.

## Examples
### Basic BAM tag formatting
**Args:** `flexi-formatter -i input.bam -o output.bam`
**Explanation:** Processes input BAM and adds BC/UMI tags from flexiplex-formatted read names.

### Multi-threaded processing
**Args:** `flexi-formatter -i input.bam -o output.bam --threads 8`
**Explanation:** Uses 8 threads for parallel processing of large BAM files.

### Custom tag names
**Args:** `flexi-formatter -i input.bam -o output.bam --barcode-tag ZB --umi-tag ZU`
**Explanation:** Uses custom tag names instead of default BC/UQ tags.

### Include unmapped reads
**Args:** `flexi-formatter -i input.bam -o output.bam --include-unmapped`
**Explanation:** Processes and tags unmapped reads in addition to mapped reads.

### Dry run mode
**Args:** `flexi-formatter -i input.bam --dry-run`
**Explanation:** Shows what tags would be added without modifying the BAM file.
