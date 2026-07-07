---
name: hafez
category: bioinformatics
description: hafez identifies active prophage elements in bacterial genomes through read mapping analysis.
tags: [hafez, prophage, bacteriophage, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Chrisjrt/hafeZ"
---

## Concepts

- **Prophage Identification**: hafez detects active prophage elements in bacterial genomes.

- **Read Mapping**: Maps sequencing reads to identify prophage regions.

- **Bacteriophage Analysis**: Analyzes bacteriophage integration sites.

- **Active Prophages**: Identifies prophages that are actively expressed.

- **Genomic Islands**: Detects horizontally transferred genomic regions.

- **Sequence Analysis**: Analyzes prophage sequences and integration sites.

## Pitfalls

- **Reference Genome**: Requires good quality reference genome.

- **Read Quality**: Low-quality reads may affect detection.

- **False Positives**: May identify false positive prophage regions.

- **Integration Sites**: Integration site prediction may be inaccurate.

- **Database Dependencies**: Results depend on prophage database quality.

## Examples

### Identify prophages
**Args:** `hafez -r reference.fasta -1 reads_1.fastq -2 reads_2.fastq -o prophages.txt`
**Explanation:** Identifies prophage elements in genome.

### Single-end reads
**Args:** `hafez -r reference.fasta -s reads.fastq -o prophages.txt`
**Explanation:** Processes single-end sequencing data.

### With prophage database
**Args:** `hafez -r reference.fasta -1 reads_1.fastq -2 reads_2.fastq -d prophage_db.fasta -o prophages.txt`
**Explanation:** Uses custom prophage database.

### Generate visualization
**Args:** `hafez -r reference.fasta -1 reads_1.fastq -2 reads_2.fastq -v -o visualization.pdf`
**Explanation:** Generates visualization of prophage regions.

### Quality filtering
**Args:** `hafez -r reference.fasta -1 reads_1.fastq -2 reads_2.fastq -q 20 -o prophages.txt`
**Explanation:** Filters reads by quality score.

### Batch processing
**Args:** `for ref in *.fasta; do hafez -r $ref -1 reads_1.fastq -2 reads_2.fastq -o ${ref%.fasta}_prophages.txt; done`
**Explanation:** Processes multiple reference genomes.

### Help command
**Args:** `hafez --help`
**Explanation:** Shows available options and usage information.