---
name: insilicosv
category: variant-calling
description: Simulator for complex structural variants that generates realistic SV events including deletions, duplications, inversions, translocations, and complex rearrangements.
tags: [insilicosv, variant-calling, structural-variation, simulator]
author: oxo-call-community
source_url: "https://github.com/PopicLab/insilicoSV"
---

## Concepts

- **Structural Variant Simulation**: InSilicoSV generates synthetic structural variants (SVs) including deletions, duplications, inversions, translocations, and complex rearrangements.
- **SV Complexity**: Supports nested SVs, overlapping events, and realistic breakpoints to mimic true biological variation.
- **Reference-based Simulation**: Works on reference genomes to introduce SVs while maintaining sequence context and integrity.
- **Output Formats**: Generates modified FASTA sequences with SVs and corresponding VCF files for downstream variant calling benchmarking.
- **SV Size Distributions**: Models realistic SV size distributions observed in real sequencing data.

## Pitfalls

- **Reference Dependencies**: Simulation accuracy depends on reference genome quality and completeness.
- **Breakpoint Complexity**: Complex SVs with multiple breakpoints may require careful parameter tuning.
- **Overlap Handling**: Overlapping SV events can complicate interpretation; verify output with visualization tools.
- **VCF Format**: Generated VCF files may require normalization for compatibility with downstream tools.
- **Performance**: Simulating large genomes with many SVs can be computationally intensive.

## Examples

### Basic SV simulation
**Args:** `insilicosv simulate --reference hg38.fasta --output_prefix sv_sim --n_sv 100`
**Explanation:** Simulates 100 structural variants in the hg38 reference genome.

### Specify SV types
**Args:** `insilicosv simulate --reference genome.fasta --output_prefix sv_types --sv_types DEL DUP INV --n_sv_per_type 50`
**Explanation:** Generates 50 deletions, 50 duplications, and 50 inversions.

### Complex SV simulation
**Args:** `insilicosv simulate --reference genome.fasta --output_prefix complex_sv --allow_nested --allow_overlapping --n_sv 200`
**Explanation:** Simulates 200 complex SVs including nested and overlapping events.

### Generate reads with SVs
**Args:** `insilicosv simulate --reference genome.fasta --output_prefix sv_reads --generate_reads --read_depth 30`
**Explanation:** Simulates SVs and generates paired-end reads at 30x coverage.

### Custom SV size range
**Args:** `insilicosv simulate --reference genome.fasta --output_prefix custom_sv --min_size 100 --max_size 100000 --n_sv 150`
**Explanation:** Generates 150 SVs with sizes ranging from 100bp to 100kb.

### Output to VCF only
**Args:** `insilicosv simulate --reference genome.fasta --output_prefix sv_vcf --vcf_only`
**Explanation:** Generates only VCF output without modifying the reference FASTA.