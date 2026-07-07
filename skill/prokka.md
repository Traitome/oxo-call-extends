---
name: prokka
category: annotation
description: prokka provides rapid annotation of prokaryotic genomes.
tags: [prokka, annotation, genome-annotation, prokaryotes]
author: oxo-call-community
source_url: "https://github.com/tseemann/prokka"
---

## Concepts

- **Tool Overview**: prokka annotates prokaryotic genomes.
- **Core Function**: Rapid genome annotation.
- **Algorithm**: Uses sequence similarity methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces annotation files.
- **Use Case**: Prokaryotic genome analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on input quality.
- **Annotation Accuracy**: May have false positives.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prokka --help`
**Explanation:** Shows available options and usage instructions.

### Annotate genome
**Args:** `prokka genome.fasta --outdir annotation`
**Explanation:** Annotates prokaryotic genome.

### With parameters
**Args:** `prokka genome.fasta --outdir annotation --params params.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prokka --verbose genome.fasta --outdir annotation`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prokka --threads 4 genome.fasta --outdir annotation`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prokka genome.fasta --outdir annotation --gff3`
**Explanation:** Outputs in GFF3 format.

### Generate report
**Args:** `prokka genome.fasta --outdir annotation --report report.html`
**Explanation:** Generates HTML report.