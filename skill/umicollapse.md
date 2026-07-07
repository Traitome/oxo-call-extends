---
name: umicollapse
category: bioinformatics
description: UMIcollapse - Tool for collapsing UMI sequences.
tags: [umicollapse, umi, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/umicollapse/"
---

## Concepts

- **Tool Overview**: UMIcollapse - A tool for collapsing unique molecular identifiers.
- **Core Function**: Groups reads by UMI and generates consensus sequences.
- **Input**: BAM/SAM file with UMIs.
- **Output**: Collapsed consensus sequences.
- **Installation**: Install via conda or source
- **Use Case**: UMI analysis, variant calling, bioinformatics.

## Pitfalls

- **UMI Design**: Requires proper UMI design.
- **Memory**: May require significant memory for large datasets.

## Examples

### Collapse UMIs
**Args:** `umicollapse -i input.bam -o output.bam`
**Explanation:** Collapse reads by UMI.

### With quality filtering
**Args:** `umicollapse -i input.bam -o output.bam -q 20`
**Explanation:** Collapse with quality filtering.
