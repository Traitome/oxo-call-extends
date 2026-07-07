---
name: nucamino
category: alignment
description: Nucamino performs nucleotide to amino acid alignment optimized for virus gene sequences.
tags: [nucamino, alignment, virus, translation]
author: oxo-call-community
source_url: "https://github.com/hivdb/nucamino"
---

## Concepts

- **Tool Overview**: Nucamino aligns nucleotide sequences to amino acid references, optimized for viral genes.
- **Core Function**: Translates and aligns nucleotide sequences to protein references.
- **Algorithm**: Uses specialized alignment algorithms for viral sequence analysis.
- **Input Format**: Accepts FASTA nucleotide sequences.
- **Output**: Produces aligned sequences with translation information.
- **Use Case**: Viral sequence analysis, HIV/HBV genotyping, and vaccine research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Virus Specific**: Optimized for specific viruses, may not work well for others.
- **Frame Shifts**: Requires correct reading frame.
- **Indels**: May not handle complex indels well.
- **Reference Quality**: Results depend on reference sequence quality.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `nucamino --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `nucamino align -i sequences.fasta -r reference.fasta -o aligned.fasta`
**Explanation:** Aligns nucleotide sequences to reference.

### HIV typing
**Args:** `nucamino hiv -i hiv_sequences.fasta -o hiv_report.txt`
**Explanation:** Performs HIV subtype classification.

### Output VCF
**Args:** `nucamino align -i sequences.fasta -r reference.fasta -o variants.vcf --vcf`
**Explanation:** Outputs variants in VCF format.

### Threads
**Args:** `nucamino align -i sequences.fasta -r reference.fasta -t 8 -o aligned.fasta`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `nucamino align -i sequences.fasta -r reference.fasta -v -o aligned.fasta`
**Explanation:** Runs with verbose output.

### Quality filtering
**Args:** `nucamino align -i sequences.fasta -r reference.fasta -q 30 -o aligned.fasta`
**Explanation:** Filters by minimum quality score.