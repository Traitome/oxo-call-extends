---
name: svim-asm
category: variant-calling
description: SVIM-asm is a fork of SVIM for structural variant detection from genome-genome alignments.
tags: [svim-asm, structural-variants, genome-alignment, sv-detection]
author: oxo-call-community
source_url: "https://github.com/eldariont/svim-asm"
---

## Concepts

- **Tool Overview**: svim-asm (v1.0.3) detects structural variants from genome-genome alignments.
- **Core Function**: Identifies SVs by comparing assembled genomes.
- **Algorithm**: Uses alignment-based approach for SV detection between genomes.
- **Input/Output**: Input: Genome assemblies (FASTA); Output: VCF with SV calls.
- **Applications**: Comparative genomics, genome assembly comparison, SV discovery.
- **Installation**: `conda install -c bioconda svim-asm` or download from GitHub.

## Pitfalls

- **Assembly Quality**: Poor quality assemblies affect detection.
- **Memory Requirements**: Large genomes require significant memory.
- **Computational Time**: Alignment of large genomes can be slow.
- **Parameter Tuning**: Incorrect parameters affect sensitivity.
- **Assembly Completeness**: Incomplete assemblies miss SVs.
- **Alignment Quality**: Poor alignments affect SV detection.

## Examples

### Display help
**Args:** `svim-asm --help`
**Explanation:** Shows available options and usage information.

### Basic SV detection
**Args:** `svim-asm genome1.fasta genome2.fasta output.vcf`
**Explanation:** Detect SVs between two genome assemblies.

### With reference
**Args:** `svim-asm -r reference.fasta genome.fasta output.vcf`
**Explanation:** Compare genome against reference.

### Verbose mode
**Args:** `svim-asm genome1.fasta genome2.fasta output.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svim-asm genome1.fasta genome2.fasta output.vcf --stats`
**Explanation:** Generate statistics about SV detection.

### Batch processing
**Args:** `svim-asm -r reference.fasta genomes/ -o results/`
**Explanation:** Compare multiple genomes against reference.

### Filter by size
**Args:** `svim-asm genome1.fasta genome2.fasta output.vcf -m 100`
**Explanation:** Minimum SV size of 100bp.

### Include all SV types
**Args:** `svim-asm genome1.fasta genome2.fasta output.vcf --all-types`
**Explanation:** Detect all types of structural variants.

### Generate report
**Args:** `svim-asm genome1.fasta genome2.fasta output.vcf --report`
**Explanation:** Generate comprehensive HTML report.
