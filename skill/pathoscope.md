---
name: pathoscope
category: assembly
description: PathoScope performs species identification and strain attribution from sequencing data.
tags: [pathoscope, assembly, species-identification, strain-typing]
author: oxo-call-community
source_url: "https://github.com/PathoScope/PathoScope"
---

## Concepts

- **Tool Overview**: PathoScope identifies species and strains from sequencing data.
- **Core Function**: Performs taxonomic classification and strain attribution.
- **Algorithm**: Uses alignment and database matching.
- **Input Format**: Accepts unassembled sequencing reads.
- **Output**: Produces species and strain assignments.
- **Use Case**: Metagenomics, clinical microbiology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Database Updates**: Requires updated reference databases.
- **Sensitivity**: Depends on sequencing depth.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pathoscope --help`
**Explanation:** Shows available options and usage instructions.

### Identify species
**Args:** `pathoscope -i reads.fastq -o results/`
**Explanation:** Identifies species from sequencing reads.

### With reference
**Args:** `pathoscope -i reads.fastq -r reference/ -o results/`
**Explanation:** Uses custom reference database.

### Verbose mode
**Args:** `pathoscope -v -i reads.fastq -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pathoscope -t 8 -i reads.fastq -o results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pathoscope -i reads.fastq -o results.csv --csv`
**Explanation:** Outputs in CSV format.

### Strain attribution
**Args:** `pathoscope -i reads.fastq -s -o results/`
**Explanation:** Performs strain-level attribution.