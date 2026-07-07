---
name: spliced_bam2gff
category: alignment
description: Spliced BAM to GFF - Convert spliced BAM alignments to GFF2 format
tags: [spliced_bam2gff, alignment, bam, gff, format-conversion]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/spliced_bam2gff"
---

## Concepts

- **Tool Overview**: spliced_bam2gff (v1.3) - A format conversion tool
- **Core Function**: Converts spliced BAM alignments to GFF2 format
- **Input/Output**: Accepts spliced BAM files; outputs GFF2 format
- **Algorithm**: BAM parsing and GFF2 format conversion
- **Installation**: `conda install -c bioconda spliced_bam2gff`
- **Key Features**: Format conversion, spliced alignments, GFF2 output

## Pitfalls

- **Input Requirements**: Requires properly formatted spliced BAM files
- **Spliced Information**: BAM must contain spliced alignment information
- **GFF2 Format**: Output format follows GFF2 specifications
- **Memory Usage**: Large BAM files require significant memory
- **Output Format**: Output format depends on configuration
- **Conversion Accuracy**: Accuracy depends on BAM file quality

## Examples

### Display help
**Args:** `spliced_bam2gff --help`
**Explanation:** Shows available options and usage information.

### Basic conversion
**Args:** `spliced_bam2gff -i aligned.bam -o output.gff`
**Explanation:** Convert spliced BAM to GFF2 format.

### With reference genome
**Args:** `spliced_bam2gff -i aligned.bam -r reference.fasta -o output.gff`
**Explanation:** Use reference genome for conversion.

### With gene annotation
**Args:** `spliced_bam2gff -i aligned.bam -a annotation.gtf -o output.gff`
**Explanation:** Use gene annotation for conversion.

### Output detailed results
**Args:** `spliced_bam2gff -i aligned.bam -o output.gff --detailed`
**Explanation:** Output detailed conversion information.

### Output splice junctions
**Args:** `spliced_bam2gff -i aligned.bam -o output.gff --junctions`
**Explanation:** Output splice junction information.

### Output statistics
**Args:** `spliced_bam2gff -i aligned.bam -o output.gff --stats`
**Explanation:** Output conversion statistics.

### Generate report
**Args:** `spliced_bam2gff -i aligned.bam -o output.gff --report`
**Explanation:** Generate conversion report.

### With threads
**Args:** `spliced_bam2gff -i aligned.bam -o output.gff -p 8`
**Explanation:** Use multiple threads for conversion.