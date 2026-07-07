---
name: ucsc-mafspecieslist
category: utility
description: UCSC mafSpeciesList - Tool for species list from MAF.
tags: [ucsc-mafspecieslist, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafSpeciesList - A tool for extracting species list from MAF.
- **Core Function**: Extracts list of species present in MAF alignments.
- **Input**: MAF file.
- **Output**: Species list.
- **Installation**: Part of UCSC utilities
- **Use Case**: Species analysis, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Extract species list
**Args:** `mafSpeciesList input.maf > species.txt`
**Explanation:** Extract species list from MAF.

### With options
**Args:** `mafSpeciesList -count input.maf > species.txt`
**Explanation:** Include count with species list.
