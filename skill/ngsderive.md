---
name: ngsderive
category: utility
description: NGSderive derives attributes and metadata from NGS sequencing data.
tags: [ngsderive, utility, metadata, sequencing]
author: oxo-call-community
source_url: "https://github.com/stjudecloud/ngsderive"
---

## Concepts

- **Tool Overview**: NGSderive infers sequencing attributes from raw data.
- **Core Function**: Derives metadata like library type, strandedness, and insert size.
- **Algorithm**: Analyzes read patterns and quality metrics.
- **Input Format**: Accepts FASTQ and BAM files.
- **Output**: Produces derived attributes and reports.
- **Use Case**: Data QC, pipeline validation, and metadata generation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Data Quality**: Results depend on input data quality.
- **Memory Usage**: Large datasets require memory.
- **Accuracy**: Derived attributes may have uncertainty.
- **Read Depth**: Requires sufficient read depth.
- **Library Type**: May not work for all library types.

## Examples

### Display help
**Args:** `ngsderive --help`
**Explanation:** Shows available options and usage instructions.

### Derive all attributes
**Args:** `ngsderive all -i reads.fastq -o attributes.json`
**Explanation:** Derives all available attributes.

### Library type
**Args:** `ngsderive library-type -i reads.fastq`
**Explanation:** Determines library type.

### Strandedness
**Args:** `ngsderive strandedness -i alignment.bam`
**Explanation:** Infers strand specificity.

### Insert size
**Args:** `ngsderive insert-size -i alignment.bam`
**Explanation:** Estimates insert size distribution.

### GC content
**Args:** `ngsderive gc-content -i reads.fastq`
**Explanation:** Calculates GC content.

### Multiple files
**Args:** `ngsderive all -i sample1.fastq sample2.fastq -o results/`
**Explanation:** Processes multiple files.

### Output YAML
**Args:** `ngsderive all -i reads.fastq -o attributes.yaml --format yaml`
**Explanation:** Outputs in YAML format.