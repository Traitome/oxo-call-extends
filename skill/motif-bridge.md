---
name: motif-bridge
category: utility
description: Bidirectional converter between MEME and HOMER motif formats
tags: [motif-bridge, utility, motif]
author: oxo-call-community
source_url: "https://github.com/zengyuanzhao/motif-bridge"
---

## Concepts

- **Tool Overview**: motif-bridge v0.1.0 converts between MEME and HOMER motif formats.
- **Core Function**: Enables seamless interoperability between motif formats.
- **MEME Format**: Supports MEME suite motif format.
- **HOMER Format**: Supports HOMER motif format.
- **Bidirectional Conversion**: Converts in both directions.
- **Input/Output**: Accepts motif files; outputs converted motif files.

## Pitfalls

- **Motif Format Specific**: Designed for MEME and HOMER formats.
- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.
- **Motif Quality**: Results depend on input motif quality.
- **Complex Motifs**: Complex motifs may require manual adjustment.
- **Memory Requirements**: Memory usage depends on motif count.

## Examples

### Convert MEME to HOMER
**Args:** `motif-bridge meme2homer -i meme_motifs.txt -o homer_motifs.txt`
**Explanation:** Converts MEME format to HOMER format.

### Convert HOMER to MEME
**Args:** `motif-bridge homer2meme -i homer_motifs.txt -o meme_motifs.txt`
**Explanation:** Converts HOMER format to MEME format.

### Batch conversion
**Args:** `motif-bridge meme2homer -i motifs/ -o converted/`
**Explanation:** Converts multiple motif files.

### With verbose output
**Args:** `motif-bridge meme2homer -i meme_motifs.txt -o homer_motifs.txt -v`
**Explanation:** Shows detailed conversion process.

### Validate motifs
**Args:** `motif-bridge validate -i motifs.txt`
**Explanation:** Validates motif file format.