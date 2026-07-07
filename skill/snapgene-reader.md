---
name: snapgene-reader
category: formatting
description: snapgene-reader - Convert SnapGene *.dna files to dict/json/biopython formats
tags: [snapgene-reader, formatting, snapgene, json, conversion]
author: oxo-call-community
source_url: "https://github.com/Edinburgh-Genome-Foundry/SnapGeneReader"
---

## Concepts

- **Tool Overview**: snapgene-reader (v0.1.23) - A tool for reading SnapGene DNA files
- **Core Function**: Converts SnapGene .dna files to various formats for analysis
- **Input/Output**: Accepts .dna files; outputs JSON, dict, or Biopython objects
- **Algorithm**: Parses SnapGene file format and extracts sequence and annotation data
- **Installation**: `conda install -c bioconda snapgene-reader`
- **Key Features**: Format conversion, annotation extraction, Biopython integration

## Pitfalls

- **File Format**: Only works with SnapGene .dna files
- **Version Compatibility**: May not support all SnapGene file versions
- **Annotation Loss**: Some annotations may not be preserved in conversion
- **Large Files**: Large .dna files may be slow to parse
- **Biopython Dependency**: Requires Biopython for some conversions
- **Encoding Issues**: May have encoding issues with special characters

## Examples

### Display help
**Args:** `snapgene-reader --help`
**Explanation:** Shows available options and usage information.

### Convert to JSON
**Args:** `snapgene-reader -i plasmid.dna -o output.json -f json`
**Explanation:** Convert SnapGene file to JSON format.

### Convert to dict
**Args:** `snapgene-reader -i plasmid.dna -o output.txt -f dict`
**Explanation:** Convert SnapGene file to dictionary format.

### Convert to Biopython
**Args:** `snapgene-reader -i plasmid.dna -o output.gb -f genbank`
**Explanation:** Convert SnapGene file to GenBank format for Biopython.

### Extract sequence only
**Args:** `snapgene-reader -i plasmid.dna -o sequence.fasta -f fasta`
**Explanation:** Extract only sequence in FASTA format.

### Extract annotations
**Args:** `snapgene-reader -i plasmid.dna -o annotations.json --annotations-only`
**Explanation:** Extract only annotations in JSON format.

### Batch conversion
**Args:** `snapgene-reader -i *.dna -o output_dir/ -f json`
**Explanation:** Convert multiple SnapGene files to JSON.

### With verbose output
**Args:** `snapgene-reader -i plasmid.dna -o output.json -f json -v`
**Explanation:** Run with verbose output for debugging.