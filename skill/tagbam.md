---
name: tagbam
category: sequencing
description: Tool for tagging BAM files with custom tags.
tags: [tagbam, bam, tags, sequencing]
author: oxo-call-community
source_url: "https://github.com/fellen31/tagbam"
---

## Concepts

- **Tool Overview**: tagbam (v0.1.0) adds custom tags to BAM files.
- **Core Function**: Tags BAM alignments with user-defined information.
- **Algorithm**: Parses BAM and adds custom SAM tags.
- **Input/Output**: Input: BAM file; Output: Tagged BAM file.
- **Applications**: BAM annotation, sample tracking, data provenance.
- **Installation**: `conda install -c bioconda tagbam` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large BAM files require significant memory.
- **Tag Format**: Must follow SAM tag conventions.
- **BAM Index**: Requires indexed BAM files.
- **Tag Overwriting**: May overwrite existing tags.
- **Validation**: Tags must be valid SAM format.
- **Performance**: Processing large BAM files can be slow.

## Examples

### Display help
**Args:** `tagbam --help`
**Explanation:** Shows available options and usage information.

### Add custom tag
**Args:** `tagbam -i input.bam -o tagged.bam -t "XX:Z:my_tag"`
**Explanation:** Add custom tag to BAM file.

### Multiple tags
**Args:** `tagbam -i input.bam -o tagged.bam -t "XX:Z:tag1" -t "YY:i:42"`
**Explanation:** Add multiple tags to BAM file.

### Verbose mode
**Args:** `tagbam -i input.bam -o tagged.bam -t "XX:Z:tag" -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `tagbam -i input.bam -o tagged.bam -t "XX:Z:tag" --stats`
**Explanation:** Generate statistics about tagging.

### Batch processing
**Args:** `for f in bams/*.bam; do tagbam -i $f -o tagged/${f%.bam}.bam -t "XX:Z:processed"; done`
**Explanation:** Tag multiple BAM files.

### Filter by region
**Args:** `tagbam -i input.bam -o tagged.bam -t "XX:Z:region" -r chr1:1-1000000`
**Explanation:** Tag only specific genomic region.

### Include read groups
**Args:** `tagbam -i input.bam -o tagged.bam -t "XX:Z:sample1" --read-group RG001`
**Explanation:** Tag specific read groups.

### Generate report
**Args:** `tagbam -i input.bam -o tagged.bam -t "XX:Z:tag" --report`
**Explanation:** Generate comprehensive tagging report.
