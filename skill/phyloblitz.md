---
name: phyloblitz
category: qc
description: phyloblitz screens SSU rRNA marker genes in metagenomes.
tags: [phyloblitz, qc, ssu-rrna, metagenomics]
author: oxo-call-community
source_url: "https://github.com/kbseah/phyloblitz"
---

## Concepts

- **Tool Overview**: phyloblitz screens marker genes.
- **Core Function**: SSU rRNA marker screening.
- **Algorithm**: Uses long-read screening methods.
- **Input Format**: Accepts metagenome read files.
- **Output**: Produces marker gene screening results.
- **Use Case**: Metagenomics, marker gene screening.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on read quality.
- **Marker Detection**: May miss rare markers.
- **Runtime**: Screening may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phyloblitz --help`
**Explanation:** Shows available options and usage instructions.

### Screen marker genes
**Args:** `phyloblitz -i metagenome_reads.fastq -o marker_genes.txt`
**Explanation:** Screens SSU rRNA marker genes.

### With parameters
**Args:** `phyloblitz -i metagenome_reads.fastq -p params.yaml -o marker_genes.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phyloblitz -v -i metagenome_reads.fastq -o marker_genes.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phyloblitz -t 4 -i metagenome_reads.fastq -o marker_genes.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phyloblitz -i metagenome_reads.fastq -o marker_genes.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `phyloblitz -i metagenome_reads.fastq -o marker_genes.txt --report report.html`
**Explanation:** Generates HTML report.