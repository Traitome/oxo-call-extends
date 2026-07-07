---
name: solote
category: annotation
description: SoloTE - Conversion utility for RepeatMasker output to BED format
tags: [solote, annotation, transposable-elements, repeatmasker, bed]
author: oxo-call-community
source_url: "https://github.com/bvaldebenitom/SoloTE"
---

## Concepts

- **Tool Overview**: solote (v1.09) - A conversion utility for SoloTE
- **Core Function**: Converts RepeatMasker output to BED format
- **Input/Output**: Accepts RepeatMasker .out files; outputs BED format
- **Algorithm**: Transforms RepeatMasker annotations to BED coordinates
- **Installation**: `conda install -c bioconda solote`
- **Key Features**: Format conversion, TE annotation, BED output

## Pitfalls

- **Input Requirements**: Requires properly formatted RepeatMasker output
- **Output Format**: Output must be in BED format for SoloTE
- **Coordinate System**: Must correctly handle coordinate conversion
- **Repeat Types**: Different repeat types may require special handling
- **File Size**: Large RepeatMasker files may require significant memory
- **Validation**: Output should be validated for correctness

## Examples

### Display help
**Args:** `solote --help`
**Explanation:** Shows available options and usage information.

### Basic conversion
**Args:** `solote -i repeatmasker.out -o output.bed`
**Explanation:** Convert RepeatMasker output to BED.

### With filtering
**Args:** `solote -i repeatmasker.out -o output.bed --filter "SINE"`
**Explanation:** Filter specific repeat type.

### With coordinates
**Args:** `solote -i repeatmasker.out -o output.bed --coords`
**Explanation:** Include coordinate information.

### Output statistics
**Args:** `solote -i repeatmasker.out -o output.bed --stats`
**Explanation:** Output conversion statistics.

### With validation
**Args:** `solote -i repeatmasker.out -o output.bed --validate`
**Explanation:** Validate converted output.

### Generate report
**Args:** `solote -i repeatmasker.out -o output.bed --report`
**Explanation:** Generate conversion report.

### Multiple files
**Args:** `solote -i rm1.out rm2.out -o output.bed`
**Explanation:** Convert multiple RepeatMasker files.