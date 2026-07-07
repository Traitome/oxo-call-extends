---
name: extract-codon-alignment
category: alignment
description: "To extract some codon positions (1st, 2nd, 3rd) from a CDS alignment."
tags: [extract-codon-alignment, alignment, codon-analysis, sequence-manipulation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/linzhi2013/extract_codon_alignment"
---

## Concepts

- **Tool Overview**: extract-codon-alignment is a tool for extracting specific codon positions from coding sequence (CDS) alignments.
- **Core Function**: Extracts first, second, or third codon positions from aligned CDS sequences for evolutionary analysis.
- **Input/Output**: Input: CDS alignment (FASTA). Output: Extracted codon positions (FASTA), concatenated alignments.
- **Algorithm**: Parses aligned sequences and extracts specified codon positions while maintaining reading frame.
- **Key Features**: Codon position extraction, frame preservation, concatenation support, multi-format input, batch processing.
- **Installation**: `conda install -c bioconda extract-codon-alignment`

## Pitfalls

- **Frame Integrity**: Requires properly aligned sequences in correct reading frame.
- **Sequence Length**: Sequences must be multiple of 3 for proper codon extraction.
- **Alignment Quality**: Results depend on high-quality alignments.
- **Format Compatibility**: Requires specific input formats.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Extract first codon positions
**Args:** `extract_codon_alignment.py -i alignment.fasta -o first_positions.fasta --position 1`
**Explanation:** Extracts first codon positions from alignment.

### Extract second codon positions
**Args:** `extract_codon_alignment.py -i alignment.fasta -o second_positions.fasta --position 2`
**Explanation:** Extracts second codon positions from alignment.

### Extract third codon positions
**Args:** `extract_codon_alignment.py -i alignment.fasta -o third_positions.fasta --position 3`
**Explanation:** Extracts third codon positions from alignment.

### Concatenate all positions
**Args:** `extract_codon_alignment.py -i alignment.fasta -o concatenated.fasta --concatenate`
**Explanation:** Concatenates all codon positions into single alignment.

### Batch processing
**Args:** `extract_codon_alignment.py -i alignments/ -o results/ --batch`
**Explanation:** Processes multiple alignment files in batch mode.