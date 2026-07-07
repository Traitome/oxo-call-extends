---
name: pyliftover
category: programming
description: pyliftover is a pure-Python implementation of UCSC liftOver for genome coordinate conversion.
tags: [pyliftover, programming, liftOver, coordinates]
author: oxo-call-community
source_url: "https://github.com/konstantint/pyliftover"
---

## Concepts

- **Tool Overview**: pyliftover converts genome coordinates.
- **Core Function**: Coordinate liftover.
- **Algorithm**: Uses chain files.
- **Input Format**: Accepts BED/coordinates.
- **Output**: Produces converted coordinates.
- **Use Case**: Genome assembly conversion.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Chain File**: Requires chain file.
- **Coordinate Format**: Must be correct.
- **Assembly Compatibility**: Must match chain file.
- **Runtime**: Conversion may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyliftover --help`
**Explanation:** Shows available options and usage instructions.

### Lift over coordinates
**Args:** `pyliftover hg19ToHg38.over.chain.gz input.bed -o output.bed`
**Explanation:** Converts coordinates between assemblies.

### With parameters
**Args:** `pyliftover chain.chain -i input.bed -p params.yaml -o output.bed`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyliftover -v chain.chain -i input.bed -o output.bed`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyliftover -t 4 chain.chain -i input.bed -o output.bed`
**Explanation:** Uses 4 threads for parallel processing.

### List available chains
**Args:** `pyliftover --list-chains`
**Explanation:** Lists available chain files.

### Generate report
**Args:** `pyliftover chain.chain -i input.bed -o output.bed --report report.html`
**Explanation:** Generates HTML report.