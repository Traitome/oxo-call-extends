---
name: bamtocov
category: utility
description: bamtocov - Extract coverage information from BAM/CRAM files
tags: [coverage, bedgraph, wig, bam-processing]
author: oxo-call-community
source_url: "https://github.com/telatin/bamtocov"
---

## Concepts

- **Tool Overview**: bamtocov extracts coverage information from BAM/CRAM files, supporting stranded and physical coverage, outputting in bedGraph or WIG format.

- **Coverage Types**: Supports standard coverage, stranded coverage, and physical (insert) coverage.

- **Target Regions**: Can extract coverage for specific target regions (BED, GFF).

- **Output Formats**: Outputs in bedGraph (BED) or WIG format for genome browser visualization.

## Pitfalls

- **Index Required**: BAM/CRAM files must be indexed before processing.

- **Memory Usage**: Large genomes require substantial memory for genome-wide coverage.

- **Strand Convention**: Verify strand convention matches expectations for stranded libraries.

## Examples

### Basic coverage extraction
**Args:** `bamtocov -i alignments.bam -o coverage.bedgraph`
**Explanation:** Extracts coverage in bedGraph format from BAM file.

### Stranded coverage
**Args:** `bamtocov -i alignments.bam -s -o stranded_coverage.bedgraph`
**Explanation:** Generates separate coverage tracks for forward and reverse strands.

### Target regions only
**Args:** `bamtocov -i alignments.bam -t targets.bed -o target_coverage.bedgraph`
**Explanation:** Extracts coverage only for specified target regions.

### WIG format output
**Args:** `bamtocov -i alignments.bam -f wig -o coverage.wig`
**Explanation:** Outputs coverage in WIG format instead of bedGraph.

### Physical coverage
**Args:** `bamtocov -i alignments.bam --physical -o insert_coverage.bedgraph`
**Explanation:** Calculates physical (insert) coverage instead of read coverage.
