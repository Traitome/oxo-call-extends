---
name: obitools4
category: utility
description: OBITools4 is a software package for DNA metabarcoding and biodiversity analysis.
tags: [obitools4, utility, metabarcoding, biodiversity]
author: oxo-call-community
source_url: "https://obitools4.metabarcoding.org"
---

## Concepts

- **Tool Overview**: OBITools4 provides tools for DNA metabarcoding data analysis.
- **Core Function**: Processes and analyzes metabarcoding sequencing data.
- **Algorithm**: Uses sequence processing and taxonomic classification methods.
- **Input Format**: Accepts FASTQ/FASTA sequencing reads and taxonomic databases.
- **Output**: Produces taxonomic assignments and biodiversity metrics.
- **Use Case**: Metabarcoding analysis, biodiversity assessment, and environmental DNA.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Database Requirements**: Requires reference taxonomic databases.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Taxonomic Resolution**: Depends on database completeness.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `obitools4 --help`
**Explanation:** Shows available options and usage instructions.

### Import reads
**Args:** `obi import -i reads.fastq -o reads.obitab`
**Explanation:** Imports FASTQ reads into OBITools4 format.

### Quality filtering
**Args:** `obi filter -i reads.obitab -o filtered.obitab --quality-min 30`
**Explanation:** Filters reads by quality score.

### Dereplicate
**Args:** `obi unique -i reads.obitab -o unique.obitab`
**Explanation:** Removes duplicate sequences.

### Assign taxonomy
**Args:** `obi classify -i unique.obitab -d database -o classified.obitab`
**Explanation:** Assigns taxonomic classifications.

### Generate report
**Args:** `obi stats -i classified.obitab -o report.txt`
**Explanation:** Generates biodiversity statistics report.

### Export to CSV
**Args:** `obi export -i classified.obitab -o results.csv --csv`
**Explanation:** Exports results to CSV format.