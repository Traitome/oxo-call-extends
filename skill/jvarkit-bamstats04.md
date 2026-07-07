---
name: jvarkit-bamstats04
category: formatting
description: Calculates coverage statistics for regions defined in a BED file.
tags: [jvarkit-bamstats04, formatting, BED, coverage, statistics]
author: oxo-call-community
source_url: "https://lindenb.github.io/jvarkit/BamStats04.html"
---

## Concepts

- **Tool Overview**: jvarkit-bamstats04 (v2025.07.28) - Calculates coverage statistics for BED-defined genomic regions.
- **Coverage Statistics**: Computes coverage metrics across BED regions.
- **BED Input**: Takes BED file defining regions of interest.
- **BAM Integration**: Uses BAM file for coverage calculation.
- **Statistical Output**: Generates comprehensive statistics.
- **Quality Metrics**: Reports coverage quality metrics.

## Pitfalls

- **BAM Index**: Requires indexed BAM file.
- **BED Format**: Requires properly formatted BED file.
- **Memory Usage**: Large BED files require significant memory.
- **Region Limits**: Very large BED regions may cause issues.
- **Java Version**: Requires specific Java version.
- **Output Interpretation**: Requires understanding of statistics.

## Examples

### Calculate coverage statistics
**Args:** `java -jar jvarkit-bamstats04.jar -i alignments.bam -B regions.bed -o stats.txt`
**Explanation:** Calculates coverage stats for BED regions.

### Include zero coverage
**Args:** `java -jar jvarkit-bamstats04.jar -i alignments.bam -B regions.bed -o stats.txt -zero`
**Explanation:** Includes regions with zero coverage.

### Detailed output
**Args:** `java -jar jvarkit-bamstats04.jar -i alignments.bam -B regions.bed -o stats.txt -detail`
**Explanation:** Generates detailed statistics report.

### Filter by mapping quality
**Args:** `java -jar jvarkit-bamstats04.jar -i alignments.bam -B regions.bed -o stats.txt -mapq 30`
**Explanation:** Only uses reads with mapping quality >= 30.

### Exclude duplicates
**Args:** `java -jar jvarkit-bamstats04.jar -i alignments.bam -B regions.bed -o stats.txt -nodup`
**Explanation:** Excludes PCR duplicates from calculation.

### Output JSON
**Args:** `java -jar jvarkit-bamstats04.jar -i alignments.bam -B regions.bed -o stats.json -json`
**Explanation:** Outputs statistics in JSON format.