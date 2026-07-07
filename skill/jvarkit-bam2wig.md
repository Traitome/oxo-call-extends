---
name: jvarkit-bam2wig
category: formatting
description: Converts BAM files to fixedStep Wiggle or BED GRAPH format.
tags: [jvarkit-bam2wig, formatting, BAM, WIG, BED]
author: oxo-call-community
source_url: "http://lindenb.github.io/jvarkit/Bam2Wig.html"
---

## Concepts

- **Tool Overview**: jvarkit-bam2wig (v201904251722) - Converts BAM alignments to Wiggle or BED GRAPH format.
- **Format Conversion**: Converts BAM to Wiggle or BED GRAPH formats.
- **Coverage Tracks**: Generates coverage tracks from alignment data.
- **FixedStep Wiggle**: Outputs in fixedStep wiggle format.
- **BED GRAPH**: Outputs in BED GRAPH format.
- **Strand Specific**: Supports strand-specific coverage calculations.

## Pitfalls

- **BAM Index**: Requires indexed BAM file.
- **Memory Usage**: Large genomes require significant memory.
- **Output Size**: Coverage tracks can be very large.
- **Resolution**: Higher resolution increases file size.
- **Strand Handling**: Requires proper strand information.
- **Java Version**: Requires specific Java version.

## Examples

### BAM to Wiggle
**Args:** `java -jar jvarkit-bam2wig.jar -i alignments.bam -o coverage.wig`
**Explanation:** Converts BAM to fixedStep Wiggle format.

### BAM to BED GRAPH
**Args:** `java -jar jvarkit-bam2wig.jar -i alignments.bam -o coverage.bedgraph -bed`
**Explanation:** Outputs in BED GRAPH format.

### Strand-specific coverage
**Args:** `java -jar jvarkit-bam2wig.jar -i alignments.bam -o coverage.wig -strand +`
**Explanation:** Outputs coverage for positive strand only.

### Specific region
**Args:** `java -jar jvarkit-bam2wig.jar -i alignments.bam -R chr1:1-100000 -o region.wig`
**Explanation:** Generates coverage for specific region.

### Skip duplicates
**Args:** `java -jar jvarkit-bam2wig.jar -i alignments.bam -o coverage.wig -nodup`
**Explanation:** Excludes PCR duplicates from coverage calculation.

### Minimum mapping quality
**Args:** `java -jar jvarkit-bam2wig.jar -i alignments.bam -o coverage.wig -mapq 20`
**Explanation:** Only includes reads with mapping quality >= 20.