---
name: chain2paf
category: formatting
description: Convert CHAIN alignment format to PAF (Pairwise mApping Format)
tags: [chain2paf, chain, paf, format-conversion, alignment]
author: oxo-call-community
source_url: "https://github.com/AndreaGuarracino/chain2paf"
---

## Concepts

- **Tool Overview**: chain2paf converts CHAIN format alignments to PAF (Pairwise mApping Format) for compatibility with sequence alignment tools.
- **Core Function**: Transforms alignment data from CHAIN format to PAF format while preserving alignment information.
- **Algorithm**: Parses CHAIN format and converts each alignment block to PAF format.
- **Input**: CHAIN format alignment file.
- **Output**: PAF format alignment file.
- **Application**: Alignment format conversion for downstream analysis tools.
- **Installation**: Install via bioconda: `conda install -c bioconda chain2paf`

## Pitfalls

- **Format Compatibility**: Input must be valid CHAIN format.
- **Coordinate System**: Ensure correct handling of coordinate systems.
- **Large Files**: Large alignment files may require significant memory.
- **PAF Version**: Different PAF versions may have different fields.

## Examples

### Convert CHAIN to PAF
**Args:** `chain2paf -i input.chain -o output.paf`
**Explanation:** Converts CHAIN file to PAF format.

### Compressed input
**Args:** `chain2paf -i input.chain.gz -o output.paf`
**Explanation:** Handles gzipped CHAIN input files.

### Add sequence names
**Args:** `chain2paf -i input.chain -o output.paf --add-names`
**Explanation:** Includes sequence names in output.

### Display help
**Args:** `chain2paf --help`
**Explanation:** Shows all available options and usage information.