---
name: ucsc-axttopsl
category: utility
description: UCSC axtToPsl - Tool for converting axt alignments to PSL format.
tags: [ucsc-axttopsl, ucsc, format-conversion, axt, psl, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC axtToPsl - A tool for converting axt format alignments to PSL format.
- **Core Function**: Converts axt alignments to PSL (Percent Sequence Identity) format.
- **Input**: Axt format alignment file.
- **Output**: PSL format alignment file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Format conversion, alignment visualization, genome browser.

## Pitfalls

- **Format Requirements**: Requires proper axt format.
- **Sequence Names**: Requires matching sequence names.

## Examples

### Convert to PSL
**Args:** `axtToPsl input.axt output.psl`
**Explanation:** Convert axt alignment to PSL format.

### With quality
**Args:** `axtToPsl -q input.axt output.psl`
**Explanation:** Convert with quality scores.
