---
name: anchorwave
category: alignment
description: Sensitive whole-genome alignment for genomes with high sequence diversity, structural polymorphism, and whole-genome duplication
tags: [genome-alignment, structural-variant, whole-genome-duplication, collinearity, maf]
author: oxo-call-community
source_url: "https://github.com/baoxingsong/AnchorWave"
---

## Concepts

- **Tool Overview**: AnchorWave (Anchored Wavefront Alignment) performs sensitive whole-genome alignment by identifying collinear regions via conserved anchors (CDS/exons) and aligning anchor/inter-anchor intervals separately. Version 1.2.6.
- **Anchor-Based Strategy**: Uses full-length CDS or exon sequences as anchors to identify collinear regions, then performs sensitive 2-piece affine gap cost alignment on each interval.
- **WGD Support**: Implements genome duplication-informed longest path algorithm to handle whole-genome duplication events. Set -R and -Q parameters based on ploidy.
- **Two Alignment Modes**: `genoAli` for collinear genomes (no rearrangements), `proali` for genomes with rearrangements, chromosome fusions, or WGD.
- **Output Format**: MAF (Multiple Alignment Format) output, convertible to other formats using maf-convert or bioconvert.
- **Four-Step Workflow**: Extract CDS → Map CDS to reference → Map CDS to query → Run genome alignment.
- **Memory Requirements**: ~20GB for single thread, ~10GB additional per thread. Requires substantial memory for large genomes.

## Pitfalls

- **Memory Usage**: Large plant genomes require 50GB+ RAM. Monitor memory usage and adjust thread count accordingly.
- **R/Q Parameters**: Must set -R (reference coverage) and -Q (query coverage) correctly based on genome ploidy/WGD history. Incorrect values produce wrong alignments.
- **Chromosome Naming**: For `genoAli`, reference and query must use same chromosome naming convention.
- **minimap2 Dependency**: Requires minimap2 or GMAP for CDS mapping step. Must be installed and in PATH.
- **GFF Quality**: Poorly formatted GFF files cause gff2seq failures. Ensure GFF has proper CDS/exon features with Parent attributes.
- **Runtime**: Large genomes (e.g., maize, wheat) may take days. Consider running on HPC clusters.

## Examples

### Extract CDS sequences from GFF
**Args:** `anchorwave gff2seq -i annotation.gff3 -r genome.fa -o cds.fa`
**Explanation:** First step: extracts longest CDS per gene from GFF annotation and genome FASTA. Output used as anchor sequences for subsequent steps.

### Extract exon sequences instead of CDS
**Args:** `anchorwave gff2seq -i annotation.gff3 -r genome.fa -o exons.fa -x -m 50`
**Explanation:** Uses exon records instead of CDS (-x flag). Minimum exon length 50bp. Useful when CDS annotations are incomplete but exon annotations are available.

### Map CDS to reference genome
**Args:** `minimap2 -x splice -t 8 -a -p 0.9999 genome.fa cds.fa > ref.sam`
**Explanation:** Maps CDS anchor sequences to reference genome using minimap2 splice mode. High -p value (0.9999) ensures only best matches are reported.

### Map CDS to query genome
**Args:** `minimap2 -x splice -t 8 -a -p 0.9999 query.fa cds.fa > query.sam`
**Explanation:** Maps same CDS anchors to query genome. Both ref.sam and query.sam are needed for genome alignment step.

### Collinear genome alignment (genoAli)
**Args:** `anchorwave genoAli -i annotation.gff3 -as cds.fa -r ref.fa -a query.sam -ar ref.sam -s query.fa -n anchors.txt -o alignment.maf -f fragments.maf -t 8`
**Explanation:** Aligns collinear genomes without rearrangements. 8 threads. Outputs MAF alignment and anchor file. Use for closely related genomes.

### Genome alignment with rearrangements (proali)
**Args:** `anchorwave proali -i annotation.gff3 -as cds.fa -r ref.fa -a query.sam -ar ref.sam -s query.fa -n anchors.txt -R 1 -Q 2 -o alignment.maf -f fragments.maf -t 4`
**Explanation:** Aligns genomes with rearrangements or WGD. -R 1 (reference diploid), -Q 2 (query tetraploid/WGD). Essential for polyploid or WGD genomes.

### Detect inversions
**Args:** `anchorwave genoAli -i annotation.gff3 -as cds.fa -r ref.fa -a query.sam -ar ref.sam -s query.fa -n anchors.txt -o alignment.maf -IV -t 8`
**Explanation:** Enables inversion detection (-IV flag). Useful for genomes with known chromosomal inversions. Adds inversion-aware alignment logic.

### Adjust alignment sensitivity
**Args:** `anchorwave proali -i annotation.gff3 -as cds.fa -r ref.fa -a query.sam -ar ref.sam -s query.fa -n anchors.txt -R 1 -Q 1 -mi 0.9 -mi2 0.3 -o alignment.maf -t 4`
**Explanation:** Sets minimum anchor similarity to 0.9 and minimum new anchor similarity to 0.3. Higher -mi values increase stringency for anchor selection.