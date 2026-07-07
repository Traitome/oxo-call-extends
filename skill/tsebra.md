---
name: tsebra
category: assembly
description: TSEBRA - Tool for merging gene annotations from multiple sources.
tags: [tsebra, gene-annotation, annotation-merging, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/Gaius-Augustus/TSEBRA"
---

## Concepts

- **Tool Overview**: TSEBRA - A tool for merging gene annotations from multiple prediction tools.
- **Core Function**: Combines annotations from multiple sources into a consensus annotation set.
- **Input**: Multiple GFF/GTF annotation files.
- **Output**: Merged annotation file, consensus gene models.
- **Installation**: `pip install tsebra`
- **Use Case**: Genome annotation, gene prediction integration, annotation improvement.

## Pitfalls

- **Format Compatibility**: Requires consistent GFF/GTF formatting.
- **Conflicts**: May have conflicts between annotation sources.

## Examples

### Merge annotations
**Args:** `tsebra -g annotations.gff -m evidence.txt -o merged.gff`
**Explanation:** Merge gene annotations from multiple sources.

### With hints
**Args:** `tsebra -g gffs/ -m hints.txt -o consensus.gff`
**Explanation:** Merge annotations using evidence hints.
