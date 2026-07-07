---
name: hic2cool
category: bioinformatics
description: hic2cool converts .hic files (from Juicer) to .cool files (for cooler) for Hi-C data analysis.
tags: [hic2cool, Hi-C, data-format, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/4dn-dcic/hic2cool"
---

## Concepts

- **Hi-C Data Conversion**: hic2cool converts Hi-C data formats.

- **.hic Format**: Handles Juicer's .hic format.

- **.cool Format**: Produces cooler's .cool format.

- **Multi-resolution**: Supports multi-resolution data.

- **Contact Maps**: Processes Hi-C contact maps.

- **Genomic Interactions**: Analyzes genomic interactions.

## Pitfalls

- **File Compatibility**: Ensure compatibility between versions.

- **Memory Usage**: Large Hi-C files may require significant memory.

- **Resolution**: Choose appropriate resolution.

- **File Size**: Hi-C files can be very large.

- **Data Integrity**: Verify data integrity after conversion.

## Examples

### Convert .hic to .cool
**Args:** `hic2cool convert input.hic output.cool`
**Explanation:** Converts Hi-C data from .hic to .cool format.

### Multi-resolution
**Args:** `hic2cool convert input.hic output.cool --resolutions 10000,25000,50000`
**Explanation:** Converts with specific resolutions.

### Batch processing
**Args:** `for f in *.hic; do hic2cool convert $f ${f%.hic}.cool; done`
**Explanation:** Converts multiple .hic files.

### Include all resolutions
**Args:** `hic2cool convert input.hic output.cool --all-resolutions`
**Explanation:** Extracts all available resolutions.

### Help command
**Args:** `hic2cool --help`
**Explanation:** Shows available options and usage information.