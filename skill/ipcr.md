---
name: ipcr
category: pcr
description: Fast, streaming, IUPAC-aware in-silico PCR toolkit supporting probe, nested, multiplex, and thermo calculations.
tags: [ipcr, PCR, in-silico, primer-design, IUPAC]
author: oxo-call-community
source_url: "https://github.com/KPU-AGC/ipcr/blob/v4.1.1/README.md"
---

## Concepts

- **Tool Overview**: ipcr (v4.1.1) - A fast, streaming in-silico PCR toolkit with comprehensive primer design capabilities.
- **Core Function**: Performs in-silico PCR simulations to validate primer specificity and predict amplicon sizes.
- **IUPAC Support**: Full support for IUPAC degeneracy codes for flexible primer design.
- **Multiplex PCR**: Capable of designing and validating multiplex PCR assays.
- **Thermodynamic Calculations**: Includes Tm calculation and primer-dimer prediction.
- **Streaming Processing**: Processes large genomes efficiently through streaming algorithms.

## Pitfalls

- **Primer Length Constraints**: Very short or very long primers may produce unexpected results.
- **Template Quality**: Requires high-quality reference sequences for accurate predictions.
- **Mismatch Tolerance**: Default mismatch settings may need adjustment for specific applications.
- **Amplicon Size Limits**: Very large amplicons may not be accurately predicted.
- **GC Content**: Extreme GC content can affect primer specificity predictions.
- **Circular Templates**: Special handling required for plasmid or circular DNA templates.

## Examples

### Basic in-silico PCR
**Args:** `ipcr amplify -f genome.fa -p primers.fasta -o amplicons.fasta`
**Explanation:** Performs in-silico PCR amplification using specified primers against a reference genome.

### Multiplex PCR design
**Args:** `ipcr multiplex -f genome.fa -p primer_set.tsv -o multiplex_results/ --max-amplicons 10`
**Explanation:** Designs and validates multiplex PCR assays with up to 10 primer pairs.

### Primer specificity check
**Args:** `ipcr specificity -f genome.fa -p forward.fasta -r reverse.fasta --max-mismatches 2`
**Explanation:** Checks primer specificity allowing up to 2 mismatches in primer binding sites.

### Tm calculation
**Args:** `ipcr tm -p primers.fasta --salt-concentration 50 --oligo-concentration 200`
**Explanation:** Calculates melting temperatures for primers under specified reaction conditions.

### Probe design
**Args:** `ipcr probe -f genome.fa -t target_region.bed -o probes.fasta --tm-range 58-62`
**Explanation:** Designs TaqMan probes for specified target regions with Tm between 58-62°C.

### Batch processing
**Args:** `ipcr batch -i input_list.txt -f genome.fa -o batch_results/ --threads 4`
**Explanation:** Processes multiple primer sets in parallel batch mode.