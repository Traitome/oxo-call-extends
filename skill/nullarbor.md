---
name: nullarbor
category: utility
description: Nullarbor is a complete reads-to-report pipeline for bacterial isolate NGS data analysis.
tags: [nullarbor, utility, bacterial-genomics, ngs-pipeline]
author: oxo-call-community
source_url: "https://github.com/tseemann/nullarbor"
---

## Concepts

- **Tool Overview**: Nullarbor automates bacterial genome analysis from raw reads to final report.
- **Core Function**: Runs complete bioinformatics pipeline for bacterial isolates.
- **Algorithm**: Integrates multiple tools for assembly, annotation, and analysis.
- **Input Format**: Accepts FASTQ sequencing reads.
- **Output**: Produces comprehensive HTML reports with analysis results.
- **Use Case**: Bacterial genomics, pathogen identification, and epidemiological analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Resource Requirements**: Pipeline requires significant computational resources.
- **Time Consuming**: Full pipeline can take hours to complete.
- **Dependency Issues**: Requires multiple dependencies to be installed.
- **Memory Usage**: Large datasets require memory.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `nullarbor --help`
**Explanation:** Shows available options and usage instructions.

### Run pipeline
**Args:** `nullarbor.pl --name my_project --input samples.txt --outdir results/`
**Explanation:** Runs complete pipeline on samples.

### Create sample file
**Args:** `nullarbor.pl --make-template > samples.txt`
**Explanation:** Creates template sample input file.

### Resume pipeline
**Args:** `nullarbor.pl --resume --outdir results/`
**Explanation:** Resumes previously interrupted pipeline.

### Force mode
**Args:** `nullarbor.pl --force --input samples.txt --outdir results/`
**Explanation:** Overwrites existing output directory.

### Threads
**Args:** `nullarbor.pl --threads 8 --input samples.txt --outdir results/`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nullarbor.pl --verbose --input samples.txt --outdir results/`
**Explanation:** Runs with verbose output.