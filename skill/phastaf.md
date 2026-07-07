---
name: phastaf
category: metagenomics
description: phastaf identifies phage regions in bacterial genomes for masking.
tags: [phastaf, metagenomics, phage, masking]
author: oxo-call-community
source_url: "https://github.com/tseemann/phastaf"
---

## Concepts

- **Tool Overview**: phastaf identifies phage regions.
- **Core Function**: Masks phage regions in genomes.
- **Algorithm**: Uses phage detection methods.
- **Input Format**: Accepts bacterial genome files.
- **Output**: Produces phage region annotations.
- **Use Case**: Phage detection, genome masking.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Phage Detection**: May miss novel phages.
- **Genome Quality**: Results depend on genome quality.
- **Runtime**: Detection may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phastaf --help`
**Explanation:** Shows available options and usage instructions.

### Identify phages
**Args:** `phastaf -i bacteria.fasta -o phage_regions.txt`
**Explanation:** Identifies phage regions.

### With database
**Args:** `phastaf -i bacteria.fasta -d phage_db.fasta -o phage_regions.txt`
**Explanation:** Uses specific phage database.

### Verbose mode
**Args:** `phastaf -v -i bacteria.fasta -o phage_regions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phastaf -t 4 -i bacteria.fasta -o phage_regions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phastaf -i bacteria.fasta -o phage_regions.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phastaf -i bacteria.fasta -o phage_regions.txt --report report.html`
**Explanation:** Generates HTML report.