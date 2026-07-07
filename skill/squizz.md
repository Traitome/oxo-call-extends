---
name: squizz
category: qc
description: Squizz - Sequence/alignment format checker and converter
tags: [squizz, qc, format-checker, sequence-format, conversion]
author: oxo-call-community
source_url: "http://ftp.pasteur.fr/pub/gensoft/projects/squizz/"
---

## Concepts

- **Tool Overview**: squizz (v0.99d) - A format checking tool
- **Core Function**: Checks sequence/alignment formats and provides conversion capabilities
- **Input/Output**: Accepts sequence files; outputs format validation and conversions
- **Algorithm**: Format validation and conversion algorithms
- **Installation**: `conda install -c bioconda squizz`
- **Key Features**: Format checking, conversion, quality control

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence files
- **Format Compatibility**: Not all formats are compatible
- **Conversion Accuracy**: Conversion may lose information
- **Memory Usage**: Large files require significant memory
- **Output Format**: Output format depends on configuration
- **Validation Accuracy**: Accuracy depends on format specifications

## Examples

### Display help
**Args:** `squizz --help`
**Explanation:** Shows available options and usage information.

### Basic format checking
**Args:** `squizz -i sequences.fasta`
**Explanation:** Check sequence file format.

### With format conversion
**Args:** `squizz -i sequences.fasta -o sequences.phylip --format phylip`
**Explanation:** Convert sequence format.

### With detailed validation
**Args:** `squizz -i sequences.fasta --detailed`
**Explanation:** Output detailed validation information.

### Multiple files
**Args:** `squizz -i seq1.fasta seq2.fasta`
**Explanation:** Check multiple sequence files.

### Output statistics
**Args:** `squizz -i sequences.fasta --stats`
**Explanation:** Output format statistics.

### Generate report
**Args:** `squizz -i sequences.fasta --report`
**Explanation:** Generate format validation report.

### With alignment checking
**Args:** `squizz -i alignment.aln --alignment`
**Explanation:** Check alignment format.

### With reference comparison
**Args:** `squizz -i sequences.fasta -r reference.fasta`
**Explanation:** Compare with reference format.