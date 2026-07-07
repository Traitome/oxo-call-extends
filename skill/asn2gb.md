---
name: asn2gb
category: formatting
description: asn2gb - Convert ASN1 format sequence records to GenBank format
tags: [asn2gb, formatting, sequence-format, conversion, ncbi]
author: oxo-call-community
source_url: "https://www.ncbi.nlm.nih.gov/IEB/ToolBox/C_DOC/lxr/source/doc/asn2gb.txt"
---

## Concepts

- **Tool Overview**: asn2gb is a NCBI tool for converting sequence records from ASN.1 format to GenBank flat file format. Version 18.2.
- **Core Function**: Converts ASN.1 (Abstract Syntax Notation One) formatted sequence records to GenBank format for easier analysis and sharing.
- **ASN.1 Format**: ASN.1 is a standardized notation for describing data structures. Used by NCBI for sequence data storage and exchange.
- **GenBank Format**: Flat file format containing sequence data with annotations (features, references, etc.). Widely used in bioinformatics.
- **NCBI Integration**: Part of NCBI ToolBox, designed to work with NCBI sequence databases.
- **Input/Output**: Accepts ASN.1 binary or text format, outputs GenBank flat file format.
- **Installation**: `conda install -c bioconda asn2gb` or download from NCBI.

## Pitfalls

- **ASN.1 Format**: Requires properly formatted ASN.1 input. Invalid ASN.1 causes conversion errors.
- **Binary vs Text**: ASN.1 can be binary or text format. May need to specify format type.
- **Large Files**: Very large sequence files may require significant memory. Monitor resource usage.
- **Feature Preservation**: Not all ASN.1 features may be preserved in GenBank format. Check output carefully.
- **Version Compatibility**: Different NCBI tool versions may produce slightly different output.
- **Compressed Input**: Does not handle compressed ASN.1 files directly. Uncompress first.

## Examples

### Display help
**Args:** `asn2gb -h`
**Explanation:** Shows all available command-line options and usage information.

### Basic conversion
**Args:** `asn2gb -i input.asn -o output.gb`
**Explanation:** Converts ASN.1 input file to GenBank format. Output written to specified file.

### Convert binary ASN.1
**Args:** `asn2gb -i input.asnb -o output.gb -b`
**Explanation:** Converts binary ASN.1 file to GenBank format. -b flag indicates binary input.

### Convert multiple sequences
**Args:** `asn2gb -i sequences.asn -o output.gb -m`
**Explanation:** Processes multiple sequence records in single ASN.1 file. -m flag enables multi-record mode.

### Add locus prefix
**Args:** `asn2gb -i input.asn -o output.gb -p LOCUS_`
**Explanation:** Adds prefix "LOCUS_" to all sequence locus names in output.

### Set division code
**Args:** `asn2gb -i input.asn -o output.gb -d PRI`
**Explanation:** Sets division code to PRI (primate). Other codes include ROD (rodent), MAM (mammal), etc.

### Include features
**Args:** `asn2gb -i input.asn -o output.gb -f`
**Explanation:** Includes feature annotations in output. Ensures CDS, gene, and other features are preserved.

### Convert from stdin
**Args:** `cat input.asn | asn2gb -o output.gb`
**Explanation:** Reads ASN.1 input from standard input and writes GenBank output to file.

### Generate FASTA from ASN.1
**Args:** `asn2gb -i input.asn -o output.gb && seqret output.gb output.fasta`
**Explanation:** Converts ASN.1 to GenBank, then converts GenBank to FASTA using EMBOSS seqret.