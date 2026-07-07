---
name: mlst
category: assembly
description: Scan contig files against PubMLST typing schemes
tags: [mlst, assembly, mlst]
author: oxo-call-community
source_url: "https://github.com/tseemann/mlst"
---

## Concepts

- **Tool Overview**: mlst v2.33.1 scans contigs against PubMLST typing schemes.
- **Core Function**: Identifies sequence types from assembled contigs.
- **PubMLST Integration**: Uses PubMLST typing schemes.
- **Contig Analysis**: Works directly with assembled contigs.
- **Input/Output**: Accepts contig files; outputs MLST types.
- **Strain Identification**: Supports bacterial strain typing.

## Pitfalls

- **Assembly Required**: Requires assembled contigs as input.
- **Computational Resources**: Processing may require significant resources.
- **Memory Requirements**: Memory usage depends on assembly size.
- **Parameter Tuning**: May require parameter adjustment for optimal typing.
- **Data Quality**: Results depend on assembly quality.
- **Scheme Updates**: May require scheme database updates.

## Examples

### Scan contigs
**Args:** `mlst contigs.fasta`
**Explanation:** Scans contigs against PubMLST schemes.

### With output file
**Args:** `mlst contigs.fasta > result.txt`
**Explanation:** Saves results to file.

### Specify scheme
**Args:** `mlst --scheme ecoli contigs.fasta`
**Explanation:** Uses specific MLST scheme.

### Batch processing
**Args:** `mlst *.fasta > results.txt`
**Explanation:** Processes multiple FASTA files.

### Detailed output
**Args:** `mlst --verbose contigs.fasta`
**Explanation:** Shows detailed typing information.