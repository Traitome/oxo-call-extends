---
name: mvp
category: annotation
description: MVP - Detect creation/destruction of sequence motifs as a result of mutations
tags: [mvp, annotation, motif, mutation, variant, vcf, sequence]
author: oxo-call-community
source_url: "https://gitlab.com/LPCDRP/motif-variants"
---

## Concepts

- **Tool Overview**: mvp (motif-variant probe) v0.4.3 detects sequence motifs that are created or destroyed by genetic variants. It identifies which mutations in a VCF file are responsible for changing the number of occurrences of specified motifs in nucleotide or amino acid sequences.
- **Core Function**: Takes a VCF file containing variants, a reference sequence, and a set of motif definitions, then outputs a table indicating which variants create, destroy, or modify motif occurrences.
- **Algorithm**: Uses pattern matching to scan reference sequences for motif sites, then compares motif occurrences before and after each variant to identify changes in motif count.
- **Input Format**: Requires a VCF file (variants), a reference genome/sequence (FASTA), and a motif definition file (text format with one motif per line). Supports both DNA and protein sequences.
- **Output**: Produces a tab-delimited table showing for each variant: the motif affected, change in motif count (gained/lost), and genomic position. Summary statistics on motif gain/loss events.
- **Use Case**: Functional annotation of variants, understanding how mutations affect transcription factor binding sites, restriction enzyme sites, or other sequence motifs important for biological function.

## Pitfalls

- **Motif Format**: Motif definitions must be in a specific format. Incorrect motif notation will produce no results or errors. Check the documentation for supported motif syntax.
- **VCF Compression**: mvp requires uncompressed or bgzip-compressed VCF files. Tabix-indexed VCFs (.vcf.gz) must be tabix-enabled for random access.
- **Reference Matching**: Variants must be annotated against the correct reference genome. Using a mismatched reference will produce incorrect motif change predictions.
- **Protein vs DNA Modes**: The tool must be told whether analyzing nucleotide or amino acid sequences. Using the wrong mode will give nonsensical results.
- **Multi-allelic Sites**: Handling of multi-allelic variants may require splitting into separate records before running mvp.
- **Memory Usage**: Large VCF files with many variants may require substantial memory. Process in batches for genome-scale datasets.

## Examples

### Basic motif variant detection
**Args:** `-v variants.vcf -r reference.fasta -m motifs.txt -o results.tsv`
**Explanation:** Standard mvp workflow. Analyzes variants against reference and outputs motif changes.

### Specify DNA sequence mode
**Args:** `-v snps.vcf -r genome.fa -m tf_motifs.txt -o dna_results.tsv --type DNA`
**Explanation:** Explicitly sets DNA mode for nucleotide sequence analysis.

### Protein sequence analysis
**Args:** `-v protein_variants.vcf -r protein.fasta -m protein_motifs.txt -o aa_results.tsv --type AA`
**Explanation:** Analyzes amino acid sequences to find variants affecting protein motifs.

### Limit analysis to specific chromosomes
**Args:** `-v variants.vcf -r ref.fasta -m motifs.txt -o results.tsv -c chr1 -c chr2`
**Explanation:** Restricts analysis to specified chromosomes for faster processing of targeted studies.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options including input formats and output specifications.
