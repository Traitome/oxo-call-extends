---
name: ucsc-mafspeciessubset
category: utility
description: UCSC mafSpeciesSubset - Tool for subsetting species in MAF.
tags: [ucsc-mafspeciessubset, ucsc, maf, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafSpeciesSubset - A tool for subsetting species in MAF.
- **Core Function**: Creates subset of MAF with specified species.
- **Input**: MAF file, species list.
- **Output**: Subsetted MAF file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Species filtering, comparative genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Subset species in MAF
**Args:** `mafSpeciesSubset -species=hg38,panTro4 input.maf > subset.maf`
**Explanation:** Create MAF subset with specified species.

### With options
**Args:** `mafSpeciesSubset -species=hg38,panTro4 -verbose input.maf > subset.maf`
**Explanation:** Subset with verbose output.
