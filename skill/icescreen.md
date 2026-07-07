---
name: icescreen
category: annotation
description: ICEscreen detects and annotates ICEs (Integrative and Conjugative Elements) and IMEs (Integrative and Mobilizable Elements) in Bacillota genomes.
tags: [icescreen, annotation, ICE, IME, mobile-genetic-elements, Bacillota]
author: oxo-call-community
source_url: "https://icescreen.migale.inrae.fr"
---

## Concepts

- **Tool Overview**: ICEscreen (v1.3.3) is a bioinformatics tool for detecting and annotating Integrative and Conjugative Elements (ICEs) and Integrative and Mobilizable Elements (IMEs) in Bacillota (formerly Firmicutes) genomes.
- **Signature Protein Detection**: Identifies four key signature proteins: integrase (excision/integration), relaxase (DNA transfer), coupling protein (transfer machinery), and VirB4 (conjugation pore).
- **Dual Search Strategy**: Uses BlastP for close homolog detection and HMMscan for distant homolog identification.
- **Composite Element Detection**: Capable of identifying nested or accreted ICE/IME structures.
- **False Positive Filtering**: Implements multiple filtration steps to remove false positives like ABC transporter proteins.
- **Installation**: `conda install -c bioconda icescreen`

## Pitfalls

- **Genome Specificity**: Optimized for Bacillota; may have reduced accuracy on other bacterial phyla.
- **Genome Completeness**: Requires complete or high-quality draft genomes for accurate boundary detection.
- **Annotation Dependency**: Relies on gene predictions; poor annotations affect detection accuracy.
- **Computational Requirements**: Memory-intensive for large genomes or metagenomic datasets.
- **Boundary Delimitation**: Only provides coordinates of signature proteins; actual element boundaries may extend beyond these coordinates.
- **Database Updates**: Performance depends on the currency of reference signature protein databases.

## Examples

### Detect ICEs/IMEs in a genome
**Args:** `icescreen --genome genome.fasta --out ice_results`
**Explanation:** Identifies and classifies ICEs and IMEs in the input genome sequence.

### With custom annotation file
**Args:** `icescreen --genome genome.fasta --gff genome.gff --out ice_results`
**Explanation:** Uses provided GFF annotation to improve signature protein identification.

### Enable verbose output
**Args:** `icescreen --genome genome.fasta --verbose --out ice_results`
**Explanation:** Produces detailed output including intermediate detection steps.

### Set E-value threshold
**Args:** `icescreen --genome genome.fasta --evalue 1e-5 --out ice_results`
**Explanation:** Sets custom E-value threshold for BlastP searches.

### Export detected elements
**Args:** `icescreen --genome genome.fasta --extract --out ice_sequences/`
**Explanation:** Extracts complete ICE/IME sequences and saves them as separate FASTA files.