---
name: ngsindex
category: utility
description: NGSindex provides utilities for working with NGS index formats.
tags: [ngsindex, utility, indexing, bam, vcf]
author: oxo-call-community
source_url: "https://github.com/jdidion/ngsindex"
---

## Concepts

- **Tool Overview**: NGSindex offers tools for manipulating NGS index files.
- **Core Function**: Creates, modifies, and queries various index formats.
- **Algorithm**: Handles BAM index (BAI), VCF index (TBI), and other formats.
- **Input Format**: Accepts indexed files and index files.
- **Output**: Produces index files and index information.
- **Use Case**: Index management, file validation, and data access optimization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **File Compatibility**: Requires matching index versions.
- **Memory Usage**: Large indexes may require memory.
- **Index Corruption**: Corrupted indexes need rebuilding.
- **Format Support**: Limited to specific index formats.
- **Validation**: Requires proper file validation.

## Examples

### Display help
**Args:** `ngsindex --help`
**Explanation:** Shows available options and usage instructions.

### Create BAM index
**Args:** `ngsindex create -i alignment.bam -o alignment.bai`
**Explanation:** Creates BAM index file.

### Check index
**Args:** `ngsindex check -i alignment.bai`
**Explanation:** Validates index file integrity.

### Extract index info
**Args:** `ngsindex info -i alignment.bai`
**Explanation:** Shows index metadata.

### Convert index
**Args:** `ngsindex convert -i alignment.bai -o alignment.csi`
**Explanation:** Converts BAI to CSI format.

### Query index
**Args:** `ngsindex query -i alignment.bai -r chr1:1-10000`
**Explanation:** Queries index for specific region.

### Validate BAM-index pair
**Args:** `ngsindex validate -b alignment.bam -i alignment.bai`
**Explanation:** Validates BAM and index match.