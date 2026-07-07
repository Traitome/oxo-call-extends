---
name: haploconduct
category: bioinformatics
description: HaploConduct reconstructs individual haplotypes from NGS data using SAVAGE and POLYTE methods for Illumina sequencing.
tags: [haploconduct, haplotype-reconstruction, NGS, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/HaploConduct/HaploConduct"
---

## Concepts

- **Haplotype Reconstruction**: HaploConduct reconstructs individual haplotypes.

- **SAVAGE Method**: Uses SAVAGE algorithm for haplotype assembly.

- **POLYTE Method**: Uses POLYTE algorithm for phasing.

- **Illumina Data**: Optimized for Illumina sequencing data.

- **Diploid Genomes**: Handles diploid genome phasing.

- **Variant Integration**: Integrates variant information for phasing.

## Pitfalls

- **Read Quality**: Low-quality reads may affect phasing.

- **Coverage Depth**: Requires sufficient sequencing coverage.

- **Complex Regions**: Complex genomic regions may be challenging.

- **Memory Usage**: Large datasets may require significant memory.

- **Parameter Selection**: Choose appropriate method for data.

## Examples

### Run SAVAGE
**Args:** `haploconduct savage -i input.bam -v variants.vcf -o haplotypes.txt`
**Explanation:** Uses SAVAGE method for haplotype reconstruction.

### Run POLYTE
**Args:** `haploconduct polyte -i input.bam -v variants.vcf -o haplotypes.txt`
**Explanation:** Uses POLYTE method for haplotype phasing.

### With reference genome
**Args:** `haploconduct savage -i input.bam -v variants.vcf -r reference.fasta -o haplotypes.txt`
**Explanation:** Uses reference genome for improved phasing.

### Batch processing
**Args:** `for f in *.bam; do haploconduct savage -i $f -v variants.vcf -o ${f%.bam}_haplotypes.txt; done`
**Explanation:** Processes multiple BAM files.

### Generate phased VCF
**Args:** `haploconduct savage -i input.bam -v variants.vcf -o phased.vcf -f vcf`
**Explanation:** Outputs phased variants in VCF format.

### Compare methods
**Args:** `haploconduct compare -i input.bam -v variants.vcf -o comparison.txt`
**Explanation:** Compares SAVAGE and POLYTE results.

### Help command
**Args:** `haploconduct --help`
**Explanation:** Shows available options and usage information.