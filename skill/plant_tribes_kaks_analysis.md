---
name: plant_tribes_kaks_analysis
category: hpc
description: plant_tribes_kaks_analysis performs Ka/Ks ratio analysis.
tags: [plant_tribes_kaks_analysis, hpc, kaks, evolutionary-analysis]
author: oxo-call-community
source_url: "https://github.com/dePamphilis/PlantTribes"
---

## Concepts

- **Tool Overview**: plant_tribes_kaks_analysis analyzes Ka/Ks ratios.
- **Core Function**: Ka/Ks ratio calculation.
- **Algorithm**: Uses codon substitution methods.
- **Input Format**: Accepts coding sequence files.
- **Output**: Produces Ka/Ks results.
- **Use Case**: Molecular evolution, selection analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Calculation Accuracy**: May have estimation errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plant_tribes_kaks_analysis --help`
**Explanation:** Shows available options and usage instructions.

### Perform Ka/Ks analysis
**Args:** `plant_tribes_kaks_analysis -i cds.fasta -o kaks_results.txt`
**Explanation:** Calculates Ka/Ks ratios for plant genes.

### With parameters
**Args:** `plant_tribes_kaks_analysis -i cds.fasta -p params.yaml -o kaks_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plant_tribes_kaks_analysis -v -i cds.fasta -o kaks_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plant_tribes_kaks_analysis -t 4 -i cds.fasta -o kaks_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plant_tribes_kaks_analysis -i cds.fasta -o kaks_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `plant_tribes_kaks_analysis -i cds.fasta -o kaks_results.txt --report report.html`
**Explanation:** Generates HTML report.