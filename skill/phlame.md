---
name: phlame
category: metagenomics
description: phlame performs intraspecies profiling of metagenome samples.
tags: [phlame, metagenomics, profiling, intraspecies]
author: oxo-call-community
source_url: "https://github.com/quevan/phlame"
---

## Concepts

- **Tool Overview**: phlame profiles metagenome samples.
- **Core Function**: Intraspecies profiling analysis.
- **Algorithm**: Uses novelty-aware profiling methods.
- **Input Format**: Accepts metagenome BAM/SAM files.
- **Output**: Produces profiling analysis results.
- **Use Case**: Metagenomics, species profiling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Profiling Method**: Requires proper method selection.
- **Runtime**: Profiling may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phlame --help`
**Explanation:** Shows available options and usage instructions.

### Profile metagenome
**Args:** `phlame -i metagenome.bam -o profiling_results.txt`
**Explanation:** Profiles metagenome samples.

### With parameters
**Args:** `phlame -i metagenome.bam -p params.yaml -o profiling_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phlame -v -i metagenome.bam -o profiling_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phlame -t 4 -i metagenome.bam -o profiling_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phlame -i metagenome.bam -o profiling_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phlame -i metagenome.bam -o profiling_results.txt --report report.html`
**Explanation:** Generates HTML report.