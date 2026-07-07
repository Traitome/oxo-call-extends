---
name: pgap2
category: hpc
description: PGAP2 performs pan-genome analysis for prokaryotic genomes.
tags: [pgap2, hpc, pan-genome, prokaryotic]
author: oxo-call-community
source_url: "https://github.com/bucongfan/PGAP2"
---

## Concepts

- **Tool Overview**: PGAP2 analyzes pan-genomes.
- **Core Function**: Performs comprehensive pan-genome analysis.
- **Algorithm**: Uses pan-genome analysis pipeline.
- **Input Format**: Accepts prokaryotic genome files.
- **Output**: Produces pan-genome analysis results.
- **Use Case**: Pan-genome analysis, comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genome sets require memory.
- **Genome Quality**: Results depend on genome quality.
- **Pipeline Configuration**: Requires proper config setup.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pgap2 --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pgap2 -i genomes/ -o pan_genome_results/`
**Explanation:** Runs pan-genome analysis pipeline.

### With config
**Args:** `pgap2 -i genomes/ -c config.yaml -o pan_genome_results/`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `pgap2 -v -i genomes/ -o pan_genome_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pgap2 -t 8 -i genomes/ -o pan_genome_results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pgap2 -i genomes/ -o pan_genome_results/ --format json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pgap2 -i genomes/ -o pan_genome_results/ --report report.html`
**Explanation:** Generates HTML report.