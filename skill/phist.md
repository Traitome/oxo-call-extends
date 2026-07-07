---
name: phist
category: metagenomics
description: phist searches phage-host interactions.
tags: [phist, metagenomics, phage, host-interaction]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/PHIST"
---

## Concepts

- **Tool Overview**: phist searches phage-host interactions.
- **Core Function**: Phage-host interaction analysis.
- **Algorithm**: Uses interaction detection methods.
- **Input Format**: Accepts phage and host genomes.
- **Output**: Produces interaction analysis results.
- **Use Case**: Phage-host analysis, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Interaction Detection**: May miss weak interactions.
- **Genome Quality**: Results depend on genome quality.
- **Runtime**: Search may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phist --help`
**Explanation:** Shows available options and usage instructions.

### Search interactions
**Args:** `phist -i phage.fasta -h host.fasta -o interactions.txt`
**Explanation:** Searches phage-host interactions.

### With parameters
**Args:** `phist -i phage.fasta -h host.fasta -p params.yaml -o interactions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phist -v -i phage.fasta -h host.fasta -o interactions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phist -t 4 -i phage.fasta -h host.fasta -o interactions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phist -i phage.fasta -h host.fasta -o interactions.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phist -i phage.fasta -h host.fasta -o interactions.txt --report report.html`
**Explanation:** Generates HTML report.