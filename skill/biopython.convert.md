---
name: biopython.convert
category: formatting
description: Interconvert various bioinformatics file formats using BioPython
tags: [biopython, format-conversion, sequence-formats]
author: oxo-call-community
source_url: "https://github.com/brinkmanlab/BioPython-Convert"
---

## Concepts

- **Tool Overview**: biopython.convert is a command-line tool for converting between various bioinformatics file formats using BioPython's SeqIO and AlignIO modules.
- **Format Support**: Supports sequence formats (FASTA, FASTQ, GenBank, EMBL), alignment formats (Clustal, Stockholm, Phylip), and other bioinformatics formats.
- **BioPython Integration**: Leverages BioPython's robust format parsers and writers.
- **Batch Processing**: Can process multiple files in a single command.
- **Applications**: Sequence format conversion, alignment format conversion, batch processing.

## Pitfalls

- **Format Limitations**: Some formats have specific constraints (e.g., FASTQ quality encoding).
- **Large Files**: Converting very large files may require significant memory.
- **Format Detection**: Auto-detection may fail for ambiguous formats.

## Examples

### Convert FASTA to GenBank
**Args:** `biopython.convert -i input.fasta -o output.gb`
**Explanation:** Converts FASTA file to GenBank format.

### Convert FASTQ to FASTA
**Args:** `biopython.convert -i reads.fastq -o reads.fasta`
**Explanation:** Converts FASTQ file to FASTA format (discards quality scores).

### Convert alignment formats
**Args:** `biopython.convert -i alignment.clustal -o alignment.phylip`
**Explanation:** Converts Clustal alignment to Phylip format.

### Batch conversion
**Args:** `biopython.convert -i *.fasta -o output_dir/ --format genbank`
**Explanation:** Batch converts all FASTA files to GenBank format.