---
name: fastindep
category: utility
description: "A fast random heuristic algorithm for identifying large sets of unrelated individuals and unrelated markers"
tags: [fastindep, utility, population-genetics, relatedness, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/endrebak/fastindep"
---

## Concepts

- **Tool Overview**: fastindep is a tool for identifying large sets of unrelated individuals and unrelated markers using a fast random heuristic algorithm.
- **Core Function**: Identifies independent individuals and markers in population genetics data.
- **Input/Output**: Input: Genotype data (PLINK, VCF). Output: Lists of independent individuals/markers.
- **Algorithm**: Uses random heuristic algorithm for efficient identification of independent samples.
- **Key Features**: Fast computation, handles large datasets, population genetics analysis, marker selection, batch processing.
- **Installation**: `conda install -c bioconda fastindep`

## Pitfalls

- **Data Quality**: Requires high-quality genotype data.
- **Memory Usage**: Large datasets may require significant memory.
- **Algorithm Randomness**: Results may vary between runs.
- **Parameter Tuning**: Requires careful parameter selection.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Identify independent individuals
**Args:** `fastindep -i genotypes.vcf -o independent_individuals.txt`
**Explanation:** Identifies unrelated individuals.

### Identify independent markers
**Args:** `fastindep -i genotypes.vcf -o independent_markers.txt --markers`
**Explanation:** Identifies independent markers.

### With PLINK format
**Args:** `fastindep -i genotypes.bed -b -o independent_individuals.txt`
**Explanation:** Processes PLINK formatted data.

### Set relatedness threshold
**Args:** `fastindep -i genotypes.vcf -o independent.txt -t 0.1`
**Explanation:** Sets relatedness threshold.

### Batch processing
**Args:** `fastindep -i vcf_files/ -o results/ --batch`
**Explanation:** Processes multiple files in batch mode.