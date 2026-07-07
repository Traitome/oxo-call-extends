---
name: pandora
category: utility
description: Pandora performs pan-genome inference and genotyping with long or short reads.
tags: [pandora, utility, pangenome, genotyping]
author: oxo-call-community
source_url: "https://github.com/rmcolq/pandora"
---

## Concepts

- **Tool Overview**: Pandora analyzes pangenomes using both long and short sequencing reads.
- **Core Function**: Performs pangenome indexing and variant genotyping.
- **Algorithm**: Uses graph-based approach for pangenome representation.
- **Input Format**: Accepts FASTA pangenome and FASTQ reads.
- **Output**: Produces genotyping results and variant calls.
- **Use Case**: Pangenome analysis, population genetics, and variant detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large pangenomes require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Read Quality**: Results depend on input read quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pandora --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `pandora index -p pangenome.fasta -o index/`
**Explanation:** Creates pangenome index.

### Genotype
**Args:** `pandora map -x index/ -i reads.fastq -o variants.vcf`
**Explanation:** Genotypes variants from reads.

### With long reads
**Args:** `pandora map -x index/ -i long_reads.fastq --long-reads -o variants.vcf`
**Explanation:** Optimized for long-read data.

### Verbose mode
**Args:** `pandora map -v -x index/ -i reads.fastq -o variants.vcf`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pandora map -t 16 -x index/ -i reads.fastq -o variants.vcf`
**Explanation:** Uses 16 threads for parallel processing.

### Output format
**Args:** `pandora map -x index/ -i reads.fastq -o output/ --output-all`
**Explanation:** Outputs all intermediate files.