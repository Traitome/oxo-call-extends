---
name: ncbi-amrfinderplus
category: annotation
description: AMRFinderPlus finds antimicrobial resistance and other genes in protein or nucleotide sequences.
tags: [ncbi-amrfinderplus, annotation, antimicrobial-resistance, amr, virulence]
author: oxo-call-community
source_url: "https://github.com/ncbi/amr"
---

## Concepts

- **Tool Overview**: AMRFinderPlus v4.2.7 - finds AMR, virulence, and other genes in sequences.
- **Core Function**: Identifies acquired AMR genes, point mutations, virulence factors, and stress resistance genes in bacterial sequences.
- **Input/Output**: Takes protein/nucleotide FASTA or GFF/BAM; outputs AMR and other gene matches.
- **Installation**: `conda install -c bioconda ncbi-amrfinderplus`

## Pitfalls

- **Version Differences**: Options and database versions may vary.
- **Database Update**: Requires up-to-date AMRFinderPlus database.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Nucleotide search
**Args:** `-n assembly.fasta -g annotations.gff -o amr_results.tsv`
**Explanation:** Finds AMR genes in nucleotide sequences with GFF annotations.

### Protein search
**Args:** `-p proteins.faa -o amr_results.tsv`
**Explanation:** Finds AMR genes in protein sequences.

### Update database
**Args:** `amrfinder_update`
**Explanation:** Updates the AMRFinderPlus database to latest version.
