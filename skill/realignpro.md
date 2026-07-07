---
name: realignpro
category: alignment
description: ReAlignPro provides FASTA-to-MAF, MAF-to-BED, and TSV-to-figures utilities for comparative genomics.
tags: [realignpro, alignment, comparative-genomics, maf]
author: oxo-call-community
source_url: "https://github.com/chulbioinfo/ReAlignPro"
---

## Concepts

- **Tool Overview**: realignpro converts alignments.
- **Core Function**: Alignment conversion.
- **Algorithm**: Uses parsing methods.
- **Input Format**: Accepts alignment files.
- **Output**: Produces converted files.
- **Use Case**: Comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Alignment Format**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Conversion may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `realignpro --help`
**Explanation:** Shows available options and usage instructions.

### Convert FASTA to MAF
**Args:** `realignpro fasta2maf -i alignment.fasta -o alignment.maf`
**Explanation:** Converts FASTA to MAF format.

### With parameters
**Args:** `realignpro fasta2maf -i alignment.fasta -p params.yaml -o alignment.maf`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `realignpro -v fasta2maf -i alignment.fasta -o alignment.maf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `realignpro -t 4 fasta2maf -i alignment.fasta -o alignment.maf`
**Explanation:** Uses 4 threads for parallel processing.

### Convert MAF to BED
**Args:** `realignpro maf2bed -i alignment.maf -o regions.bed`
**Explanation:** Converts MAF to BED format.

### Generate report
**Args:** `realignpro fasta2maf -i alignment.fasta -o alignment.maf --report report.html`
**Explanation:** Generates HTML report.