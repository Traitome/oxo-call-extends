---
name: repeatmodeler
category: containerization
description: RepeatModeler identifies and models de-novo repeat families for genome analysis.
tags: [repeatmodeler, containerization, repeat-identification, genome-analysis]
author: oxo-call-community
source_url: "https://www.repeatmasker.org/RepeatModeler"
---

## Concepts

- **Tool Overview**: repeatmodeler identifies repeats.
- **Core Function**: De novo repeat family identification.
- **Algorithm**: Uses computational methods.
- **Input Format**: Accepts genome sequences.
- **Output**: Produces repeat libraries.
- **Use Case**: Repeat analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Genome Complexity**: Affects identification.
- **Parameters**: Must be configured.
- **Runtime**: Identification may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `RepeatModeler -h`
**Explanation:** Shows available options and usage instructions.

### Build repeat library
**Args:** `RepeatModeler -database genome_db -pa 4`
**Explanation:** Builds de novo repeat library.

### With configuration
**Args:** `RepeatModeler -database genome_db -config config.ini`
**Explanation:** Uses configuration file.

### Verbose mode
**Args:** `RepeatModeler -v -database genome_db`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `RepeatModeler -pa 4 -database genome_db`
**Explanation:** Uses 4 threads for parallel processing.

### With species
**Args:** `RepeatModeler -species human -database genome_db`
**Explanation:** Uses species-specific settings.

### Generate report
**Args:** `RepeatModeler -database genome_db && cat RM_*/consensi.fa.classified`
**Explanation:** Generates classified repeat sequences.