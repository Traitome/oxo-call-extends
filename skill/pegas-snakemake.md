---
name: pegas-snakemake
category: hpc
description: PeGAS-snakemake provides Snakemake genome analysis pipeline.
tags: [pegas-snakemake, hpc, pipeline, snakemake]
author: oxo-call-community
source_url: "https://github.com/liviurotiul/PeGAS"
---

## Concepts

- **Tool Overview**: PeGAS-snakemake runs genome analysis.
- **Core Function**: Provides Snakemake workflow execution.
- **Algorithm**: Uses Snakemake workflow engine.
- **Input Format**: Accepts genome data files.
- **Output**: Produces analysis results.
- **Use Case**: Genome analysis, pipeline execution.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Pipeline Configuration**: Requires proper config setup.
- **Dependency Management**: Requires proper dependencies.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pegas-snakemake --help`
**Explanation:** Shows available options and usage instructions.

### Run pipeline
**Args:** `pegas-snakemake run -i genome.fasta -o results/`
**Explanation:** Runs genome analysis pipeline.

### With config
**Args:** `pegas-snakemake run -i genome.fasta -c config.yaml -o results/`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `pegas-snakemake -v run -i genome.fasta -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pegas-snakemake run -t 8 -i genome.fasta -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pegas-snakemake run -i genome.fasta -o results/ --format json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pegas-snakemake run -i genome.fasta -o results/ --report report.html`
**Explanation:** Generates HTML report.