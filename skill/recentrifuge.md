---
name: recentrifuge
category: metagenomics
description: Recentrifuge provides robust comparative analysis and contamination removal for metagenomics data.
tags: [recentrifuge, metagenomics, contamination-removal, comparative-analysis]
author: oxo-call-community
source_url: "https://github.com/khyox/recentrifuge/wiki"
---

## Concepts

- **Tool Overview**: recentrifuge analyzes metagenomes.
- **Core Function**: Metagenomic analysis.
- **Algorithm**: Uses comparative methods.
- **Input Format**: Accepts metagenomic reads.
- **Output**: Produces analysis results.
- **Use Case**: Metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Database Quality**: Affects analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recentrifuge --help`
**Explanation:** Shows available options and usage instructions.

### Analyze metagenome
**Args:** `recentrifuge analyze -i metagenome.fastq -o analysis.txt`
**Explanation:** Analyzes metagenomic data.

### With parameters
**Args:** `recentrifuge analyze -i metagenome.fastq -p params.yaml -o analysis.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recentrifuge -v analyze -i metagenome.fastq -o analysis.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recentrifuge -t 4 analyze -i metagenome.fastq -o analysis.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Remove contamination
**Args:** `recentrifuge remove -i metagenome.fastq -c contamination_db.fasta -o clean_metagenome.fastq`
**Explanation:** Removes contamination.

### Generate report
**Args:** `recentrifuge analyze -i metagenome.fastq -o analysis.txt --report report.html`
**Explanation:** Generates HTML report.