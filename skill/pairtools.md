---
name: pairtools
category: alignment
description: pairtools provides CLI tools to process mapped Hi-C data.
tags: [pairtools, alignment, hic, chromatin-interaction]
author: oxo-call-community
source_url: "https://github.com/open2c/pairtools"
---

## Concepts

- **Tool Overview**: pairtools processes and analyzes Hi-C sequencing data.
- **Core Function**: Manipulates paired-end alignment data from Hi-C experiments.
- **Algorithm**: Uses efficient parsing and filtering of paired reads.
- **Input Format**: Accepts SAM/BAM files and pairs format.
- **Output**: Produces processed pairs and statistics.
- **Use Case**: Hi-C analysis, 3D genomics, and chromatin interaction studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Input Format**: Requires specific input format.
- **Sorting**: May require sorted input.
- **Duplicates**: May need duplicate removal.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pairtools --help`
**Explanation:** Shows available options and usage instructions.

### Parse SAM
**Args:** `pairtools parse -o pairs.txt alignments.sam`
**Explanation:** Converts SAM to pairs format.

### Sort pairs
**Args:** `pairtools sort -o sorted.pairs pairs.txt`
**Explanation:** Sorts pairs by genomic coordinates.

### Dedup
**Args:** `pairtools dedup -o deduplicated.pairs sorted.pairs`
**Explanation:** Removes duplicate reads.

### Statistics
**Args:** `pairtools stats pairs.txt`
**Explanation:** Computes Hi-C statistics.

### Verbose mode
**Args:** `pairtools parse -v -o pairs.txt alignments.sam`
**Explanation:** Runs with verbose output.

### Compression
**Args:** `pairtools parse -o pairs.txt.gz alignments.sam`
**Explanation:** Outputs compressed pairs.