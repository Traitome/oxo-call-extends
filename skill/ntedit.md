---
name: ntedit
category: assembly
description: ntEdit is an ultrafast, lightweight genome assembly polishing and SNV detection tool.
tags: [ntedit, assembly, polishing, snv-detection]
author: oxo-call-community
source_url: "https://github.com/BirolLab/ntEdit"
---

## Concepts

- **Tool Overview**: ntEdit performs genome assembly polishing and variant detection efficiently.
- **Core Function**: Polishes assemblies and detects/annotates single nucleotide variants.
- **Algorithm**: Uses k-mer based approach for assembly refinement.
- **Input Format**: Accepts FASTA assemblies and sequencing reads.
- **Output**: Produces polished assemblies and variant annotations.
- **Use Case**: Genome assembly improvement, variant calling, and quality enhancement.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **k-mer Size**: Requires appropriate k-mer size selection.
- **Computational Cost**: Processing can be computationally intensive.
- **Input Quality**: Results depend on input data quality.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `ntedit --help`
**Explanation:** Shows available options and usage instructions.

### Polish assembly
**Args:** `ntedit -k 21 -i reads.fastq -a assembly.fasta -o polished.fasta`
**Explanation:** Polishes assembly using k-mers from reads.

### Detect variants
**Args:** `ntedit -k 21 -i reads.fastq -a assembly.fasta -v variants.vcf`
**Explanation:** Detects and outputs variants in VCF format.

### Multiple k-mer sizes
**Args:** `ntedit -k 21,31,51 -i reads.fastq -a assembly.fasta -o polished.fasta`
**Explanation:** Uses multiple k-mer sizes for polishing.

### Threads
**Args:** `ntedit -k 21 -i reads.fastq -a assembly.fasta -t 8 -o polished.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `ntedit -k 21 -i reads.fastq -a assembly.fasta -v -o polished.fasta`
**Explanation:** Runs with verbose output.

### Quality filtering
**Args:** `ntedit -k 21 -i reads.fastq -a assembly.fasta -q 30 -o polished.fasta`
**Explanation:** Filters by minimum quality score.