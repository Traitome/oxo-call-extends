---
name: obitools
category: formatting
description: OBITools is a suite of tools for analyzing NGS data in DNA metabarcoding context with taxonomic information.
tags: [obitools, formatting, metabarcoding, taxonomy]
author: oxo-call-community
source_url: "http://metabarcoding.org/obitools"
---

## Concepts

- **Tool Overview**: OBITools processes NGS data for DNA metabarcoding analysis.
- **Core Function**: Analyzes sequencing data with taxonomic classification.
- **Algorithm**: Uses sequence comparison and taxonomic databases.
- **Input Format**: Accepts FASTQ/FASTA reads and taxonomic references.
- **Output**: Produces taxonomic assignments and sequence data.
- **Use Case**: Metabarcoding, biodiversity studies, and environmental sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Legacy Version**: Consider using OBITools4 instead.
- **Database Updates**: Requires regular database updates.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `obitools --help`
**Explanation:** Shows available options and usage instructions.

### Create sequence file
**Args:** `obi_fastq2fasta -i reads.fastq -o reads.fasta`
**Explanation:** Converts FASTQ to FASTA format.

### Filter by length
**Args:** `obi_seqfilter -i reads.fasta -o filtered.fasta --minlen 100`
**Explanation:** Filters sequences by minimum length.

### Dereplicate sequences
**Args:** `obi_uniq -i reads.fasta -o unique.fasta`
**Explanation:** Removes duplicate sequences.

### Assign taxonomy
**Args:** `obi_taxonomy -i unique.fasta -d reference.fasta -o classified.txt`
**Explanation:** Assigns taxonomic classification.

### Generate OTU table
**Args:** `obi_otu -i classified.txt -o otu_table.txt`
**Explanation:** Creates OTU table from classified sequences.

### Statistics
**Args:** `obi_stat -i reads.fasta -o stats.txt`
**Explanation:** Generates sequence statistics.