---
name: extract_genome_region
category: formatting
description: "Given a CSV file of variable information defining the regions of interest, return a file that contains a fasta-formatted representation of these regions."
tags: [extract_genome_region, formatting, genome-extraction, FASTA, sequence-analysis]
author: oxo-call-community
source_url: "https://github.com/xguse/extract-genome-region"
---

## Concepts

- **Tool Overview**: extract_genome_region is a tool for extracting specific genomic regions from a reference genome based on coordinate information.
- **Core Function**: Extracts DNA sequences from specified genomic regions defined in a CSV file.
- **Input/Output**: Input: Reference genome (FASTA), region coordinates (CSV). Output: Extracted sequences (FASTA).
- **Algorithm**: Parses coordinate file and extracts corresponding sequences from reference genome.
- **Key Features**: Region extraction, coordinate parsing, FASTA output, batch processing, strand-specific extraction.
- **Installation**: `conda install -c bioconda extract_genome_region`

## Pitfalls

- **Coordinate Format**: Requires properly formatted coordinate file.
- **Genome Index**: May require indexed genome for efficient extraction.
- **Strand Awareness**: Requires careful handling of strand-specific extraction.
- **Coordinate Validation**: Invalid coordinates may cause errors.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic region extraction
**Args:** `extract_genome_region -g genome.fasta -c regions.csv -o extracted.fasta`
**Explanation:** Extracts genomic regions defined in CSV file.

### Strand-specific extraction
**Args:** `extract_genome_region -g genome.fasta -c regions.csv -o extracted.fasta --strand`
**Explanation:** Extracts sequences with strand awareness.

### With bed file
**Args:** `extract_genome_region -g genome.fasta -b regions.bed -o extracted.fasta --bed`
**Explanation:** Uses BED format for region definitions.

### Batch processing
**Args:** `extract_genome_region -g genome.fasta -c regions/ -o extracted/ --batch`
**Explanation:** Processes multiple region files in batch mode.

### Flanking regions
**Args:** `extract_genome_region -g genome.fasta -c regions.csv -o extracted.fasta --flank 100`
**Explanation:** Extracts regions with 100bp flanking sequence.