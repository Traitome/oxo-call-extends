---
name: spacerextractor
category: metagenomics
description: SpacerExtractor - Extract CRISPR spacers from metagenome reads
tags: [spacerextractor, metagenomics, crispr, spacer, extraction]
author: oxo-call-community
source_url: "https://code.jgi.doe.gov/SRoux/spacerextractor"
---

## Concepts

- **Tool Overview**: spacerextractor (v0.9.8) - A CRISPR spacer extraction tool
- **Core Function**: Extracts CRISPR spacers from metagenome short reads
- **Input/Output**: Accepts metagenome reads; outputs CRISPR spacer sequences
- **Algorithm**: Identifies and extracts CRISPR spacer sequences
- **Installation**: `conda install -c bioconda spacerextractor`
- **Key Features**: Spacer extraction, CRISPR detection, metagenomics analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted metagenome reads
- **Read Quality**: Read quality affects spacer extraction
- **CRISPR Detection**: CRISPR array detection affects extraction
- **Memory Usage**: Large metagenomes require significant memory
- **Output Format**: Output format depends on configuration
- **Validation**: Extracted spacers should be validated

## Examples

### Display help
**Args:** `spacerextractor --help`
**Explanation:** Shows available options and usage information.

### Basic spacer extraction
**Args:** `spacerextractor -i metagenome.fastq -o spacers.fasta`
**Explanation:** Extract CRISPR spacers from metagenome.

### With paired-end reads
**Args:** `spacerextractor -i reads_1.fastq reads_2.fastq -o spacers.fasta`
**Explanation:** Extract spacers from paired-end reads.

### With quality filter
**Args:** `spacerextractor -i metagenome.fastq -o spacers.fasta --min-quality 20`
**Explanation:** Filter reads by quality before extraction.

### With length filter
**Args:** `spacerextractor -i metagenome.fastq -o spacers.fasta --min-length 30`
**Explanation:** Filter spacers by minimum length.

### Output detailed results
**Args:** `spacerextractor -i metagenome.fastq -o spacers.fasta --detailed`
**Explanation:** Output detailed extraction results.

### Output statistics
**Args:** `spacerextractor -i metagenome.fastq -o spacers.fasta --stats`
**Explanation:** Output extraction statistics.

### Generate report
**Args:** `spacerextractor -i metagenome.fastq -o spacers.fasta --report`
**Explanation:** Generate extraction report.