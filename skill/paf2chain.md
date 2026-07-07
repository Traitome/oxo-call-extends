---
name: paf2chain
category: formatting
description: paf2chain converts PAF format alignments to CHAIN format.
tags: [paf2chain, formatting, paf, chain]
author: oxo-call-community
source_url: "https://github.com/AndreaGuarracino/paf2chain"
---

## Concepts

- **Tool Overview**: paf2chain converts alignment formats between PAF and CHAIN.
- **Core Function**: Translates PAF alignments to CHAIN format.
- **Algorithm**: Uses coordinate mapping for format conversion.
- **Input Format**: Accepts PAF alignment files.
- **Output**: Produces CHAIN format alignments.
- **Use Case**: Comparative genomics, genome alignment, and format conversion.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Format Compatibility**: May not support all PAF features.
- **Coordinate Issues**: May have coordinate conversion issues.
- **Performance**: May be slow for very large files.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `paf2chain --help`
**Explanation:** Shows available options and usage instructions.

### Convert PAF to CHAIN
**Args:** `paf2chain -i alignments.paf -o alignments.chain`
**Explanation:** Converts PAF to CHAIN format.

### With compression
**Args:** `paf2chain -i alignments.paf.gz -o alignments.chain`
**Explanation:** Reads gzipped PAF file.

### Output options
**Args:** `paf2chain -i alignments.paf -o alignments.chain --sort`
**Explanation:** Sorts output by position.

### Verbose mode
**Args:** `paf2chain -i alignments.paf -v -o alignments.chain`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `paf2chain batch -d paf_files/ -o chain_files/`
**Explanation:** Processes multiple PAF files.

### Filtering
**Args:** `paf2chain -i alignments.paf -m 1000 -o alignments.chain`
**Explanation:** Filters by minimum alignment length.