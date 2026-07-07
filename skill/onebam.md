---
name: onebam
category: alignment
description: onebam converts SAM/BAM/CRAM files to compact ONEcode format for eDNA mapping and taxonomic analysis.
tags: [onebam, alignment, edna, taxonomy]
author: oxo-call-community
source_url: "https://github.com/richarddurbin/onebam"
---

## Concepts

- **Tool Overview**: onebam provides efficient storage and processing of sequencing data.
- **Core Function**: Converts alignment files to compact ONEcode format.
- **Algorithm**: Uses efficient compression and indexing for large-scale data.
- **Input Format**: Accepts SAM/BAM/CRAM alignment files.
- **Output**: Produces .1read format with taxonomy information.
- **Use Case**: eDNA analysis, large-scale mapping, and taxonomic classification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Database**: Requires large reference databases.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Processing can be computationally intensive.
- **Format Conversion**: Requires proper format conversion.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `onebam --help`
**Explanation:** Shows available options and usage instructions.

### Convert BAM
**Args:** `onebam convert -i alignments.bam -o output.1read`
**Explanation:** Converts BAM to ONEcode format.

### Merge files
**Args:** `onebam merge -i sample1.1read sample2.1read -o merged.1read`
**Explanation:** Merges multiple ONEcode files.

### LCA assignment
**Args:** `onebam lca -i alignments.1read -o lca_results.txt`
**Explanation:** Assigns lowest common ancestor taxonomy.

### Taxonomic report
**Args:** `onebam report -i alignments.1read -o taxonomy.txt`
**Explanation:** Generates taxonomic report.

### Extract reads
**Args:** `onebam extract -i alignments.1read -o extracted.fastq`
**Explanation:** Extracts reads from ONEcode file.

### Verbose mode
**Args:** `onebam convert -i alignments.bam -o output.1read -v`
**Explanation:** Runs with verbose output.