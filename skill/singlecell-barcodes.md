---
name: singlecell-barcodes
category: single-cell
description: singlecell-barcodes - Whitelisted barcodes for single-cell protocols
tags: ["singlecell-barcodes", "single-cell", "barcodes", "protocols"]
author: oxo-call-community
source_url: "https://github.com/roryk/singlecell-barcodes"
---

## Concepts

- **Tool Overview**: singlecell-barcodes (v0.2) provides whitelisted barcodes for various single-cell protocols.
- **Core Function**: Manages cellular and molecular barcodes for single-cell sequencing.
- **Algorithm**: Stores and retrieves barcode whitelists for different sequencing protocols.
- **Input/Output**: Accepts protocol name and produces barcode sequences.
- **Barcode Management**: Specialized for handling single-cell barcode libraries.
- **Applications**: Single-cell sequencing, scRNA-seq, scATAC-seq.

## Pitfalls

- **Protocol Compatibility**: Barcodes are protocol-specific.
- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format before running.
- **Barcode Quality**: Results depend on barcode whitelist quality.
- **Documentation**: Limited documentation available.
- **Update Frequency**: Whitelists may not include latest protocols.

## Examples

### List available protocols
**Args:** `singlecell-barcodes list`
**Explanation:** Shows available single-cell protocols.

### Get barcodes for protocol
**Args:** `singlecell-barcodes get -p 10x_v2 -o barcodes.txt`
**Explanation:** `-p` protocol name; `-o` output file.

### Validate barcodes
**Args:** `singlecell-barcodes validate -i barcodes.txt -p 10x_v3`
**Explanation:** Validates barcodes against protocol whitelist.

### Help command
**Args:** `singlecell-barcodes --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `singlecell-barcodes --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `singlecell-barcodes -v get -p 10x_v2 -o barcodes.txt`
**Explanation:** `-v` verbose output.

### Convert format
**Args:** `singlecell-barcodes convert -i barcodes.txt -f csv -o barcodes.csv`
**Explanation:** `-f csv` output format.
