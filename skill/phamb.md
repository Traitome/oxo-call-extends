---
name: phamb
category: metagenomics
description: phamb isolates metagenome-derived viromes and viral genomes.
tags: [phamb, metagenomics, virome, viral]
author: oxo-call-community
source_url: "https://github.com/RasmussenLab/phamb"
---

## Concepts

- **Tool Overview**: phamb isolates viral genomes.
- **Core Function**: Discovers metagenome-derived viromes.
- **Algorithm**: Uses viral genome discovery methods.
- **Input Format**: Accepts metagenomic data files.
- **Output**: Produces high-quality viral genomes.
- **Use Case**: Virome analysis, viral discovery.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Metagenome Quality**: Results depend on data quality.
- **Viral Detection**: May miss novel viruses.
- **Runtime**: Discovery may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phamb --help`
**Explanation:** Shows available options and usage instructions.

### Isolate viromes
**Args:** `phamb -i metagenome.fasta -o viral_genomes.fasta`
**Explanation:** Isolates viral genomes from metagenome.

### With parameters
**Args:** `phamb -i metagenome.fasta -p params.yaml -o viral_genomes.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phamb -v -i metagenome.fasta -o viral_genomes.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phamb -t 4 -i metagenome.fasta -o viral_genomes.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phamb -i metagenome.fasta -o viral_genomes.gfa --gfa`
**Explanation:** Outputs in GFA format.

### Generate report
**Args:** `phamb -i metagenome.fasta -o viral_genomes.fasta --report report.html`
**Explanation:** Generates HTML report.