---
name: hilinetojuicer
category: bioinformatics
description: HiLineToJuicer converts HiLine SAM alignments to Juicer format for Hi-C data analysis.
tags: [hilinetojuicer, Hi-C, format-conversion, bioinformatics]
author: oxo-call-community
source_url: "https://pypi.org/project/HiLineToJuicer/0.0.2/"
---

## Concepts

- **Format Conversion**: HiLineToJuicer converts alignment formats.

- **Hi-C Data**: Handles Hi-C sequencing data.

- **SAM Format**: Reads SAM alignment files.

- **Juicer Format**: Produces Juicer-compatible output.

- **Data Integration**: Facilitates data integration between tools.

- **Contact Maps**: Supports contact map generation.

## Pitfalls

- **File Compatibility**: Ensure compatibility between versions.

- **Data Integrity**: Verify data integrity after conversion.

- **Memory Usage**: Large files may require significant memory.

- **Format Validation**: Validate input format before conversion.

- **Output Quality**: Verify output quality after conversion.

## Examples

### Convert SAM to Juicer format
**Args:** `hilinetojuicer --input alignments.sam --output juicer.txt`
**Explanation:** Converts HiLine SAM alignments to Juicer format.

### Batch processing
**Args:** `for f in *.sam; do hilinetojuicer --input $f --output ${f%.sam}_juicer.txt; done`
**Explanation:** Processes multiple SAM files.

### With quality filtering
**Args:** `hilinetojuicer --input alignments.sam --output juicer.txt --quality 20`
**Explanation:** Filters alignments by quality score.

### Generate statistics
**Args:** `hilinetojuicer --input alignments.sam --output juicer.txt --stats`
**Explanation:** Generates conversion statistics.

### Help command
**Args:** `hilinetojuicer --help`
**Explanation:** Shows available options and usage information.