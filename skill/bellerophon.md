---
name: bellerophon
category: qc
description: Filter reads that span a mapping junction, retaining the 5'-side
tags: [read-filtering, junction, mapping, soft-clipping]
author: oxo-call-community
source_url: "https://github.com/davebx/bellerophon"
---

## Concepts
- **Tool Overview**: Bellerophon filters sequencing reads that span a mapping junction (e.g., circular genome junctions, translocations), retaining the 5'-side of the read. This is useful for circular genome assembly and detecting structural variants.
- **Mapping Junction**: A position in a read where part of the read maps to one location and the rest maps to a different location (soft-clipped or split alignment).
- **Circular Genomes**: Useful for processing reads from circular genomes (viral, mitochondrial, bacterial) where reads may span the origin of replication.
- **Read Orientation**: Retains the 5'-portion of reads, which is useful for downstream assembly and analysis.

## Pitfalls
- **Alignment Requirements**: Requires proper alignment with soft-clipping information. Aligners must be configured to report soft-clipped bases.
- **Read Length**: After filtering, reads may be shorter than the original length. Downstream tools must handle variable-length reads.

## Examples
### Filter junction-spanning reads
**Args:** `bellerophon -i aligned.bam -o filtered.bam`
**Explanation:** Filters reads spanning mapping junctions, retaining 5'-ends.

### Specify minimum retained length
**Args:** `bellerophon -i input.bam -o output.bam --min-length 50`
**Explanation:** Only retains reads where the 5'-portion is at least 50bp long.
