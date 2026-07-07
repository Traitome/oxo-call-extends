---
name: phaser
category: variant-calling
description: phaser performs haplotype phasing and measures haplotypic expression.
tags: [phaser, variant-calling, phasing, haplotype]
author: oxo-call-community
source_url: "https://github.com/secastel/phaser"
---

## Concepts

- **Tool Overview**: phaser phases haplotypes.
- **Core Function**: Measures haplotypic expression.
- **Algorithm**: Uses RNA-based phasing methods.
- **Input Format**: Accepts RNA sequencing data.
- **Output**: Produces phased haplotype results.
- **Use Case**: Haplotype phasing, expression analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Results depend on read quality.
- **Phasing Accuracy**: May have phasing errors.
- **Runtime**: Phasing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phaser --help`
**Explanation:** Shows available options and usage instructions.

### Phase haplotypes
**Args:** `phaser -i rna_data.bam -o phased_haplotypes.txt`
**Explanation:** Phases haplotypes from RNA data.

### With reference
**Args:** `phaser -i rna_data.bam -r ref.fasta -o phased_haplotypes.txt`
**Explanation:** Uses specific reference genome.

### Verbose mode
**Args:** `phaser -v -i rna_data.bam -o phased_haplotypes.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phaser -t 4 -i rna_data.bam -o phased_haplotypes.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phaser -i rna_data.bam -o phased_haplotypes.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phaser -i rna_data.bam -o phased_haplotypes.txt --report report.html`
**Explanation:** Generates HTML report.