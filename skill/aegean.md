---
name: aegean
category: annotation
description: Toolkit for evaluating gene structure annotations and genome organization using GFF3 format
tags: [annotation, gff3, gene-structure, parseval, evaluation]
author: oxo-call-community
source_url: "https://github.com/BrendelGroup/AEGeAn"
---

## Concepts

- **Tool Overview**: AEGeAn provides software tools for evaluating gene structure annotations and genome organization, implemented in C and Python.
- **Core Function**: Compares and evaluates gene annotations in GFF3 format, computing similarity statistics and identifying structural differences.
- **Main Tools**: ParsEval (annotation comparison), CanonGFF3 (GFF3 canonicalization), LocusPocus (locus extraction), GAEVAL (gene annotation evaluation).
- **Input/Output**: Input: GFF3 annotation files. Output: Comparison statistics, reports, and validated GFF3 files.
- **Installation**: Install via bioconda: `conda install -c bioconda aegean`

## Pitfalls

- **Strict GFF3 Parsing**: Uses GenomeTools GFF3 parser that strictly enforces GFF3 specification - malformed files will cause errors.
- **Protein-Coding Focus**: ParsEval only processes features related to protein-coding genes - non-coding RNA annotations are ignored.
- **Same Sequence Required**: Annotation files being compared must be for the same genomic sequence/region.
- **Feature Hierarchy**: GFF3 features must have proper parent-child relationships defined for correct parsing.

## Examples

### Display help for ParsEval
**Args:** `parseval --help`
**Explanation:** Shows options for comparing two sets of gene structure annotations.

### Compare two annotation files
**Args:** `parseval annotation1.gff3 annotation2.gff3 -o comparison_report`
**Explanation:** Compares two GFF3 annotation files and generates similarity statistics.

### Canonicalize GFF3 file
**Args:** `canongff3 input.gff3 > canonical.gff3`
**Explanation:** Converts GFF3 file to canonical format with consistent feature ordering.

### Extract loci from annotation
**Args:** `locuspocus annotation.gff3 genome.fasta -o loci.gff3`
**Explanation:** Extracts gene loci from annotation file with genomic sequence context.

### Compare with detailed output
**Args:** `parseval -d annotation1.gff3 annotation2.gff3 -o detailed_report`
**Explanation:** Generates detailed comparison report including per-locus statistics.

### Evaluate annotation quality
**Args:** `gaeval annotation.gff3 genome.fasta -o evaluation_report`
**Explanation:** Evaluates gene annotation quality against the genome sequence.

### Filter GFF3 by feature type
**Args:** `canongff3 -t gene,exon,CDS input.gff3 > filtered.gff3`
**Explanation:** Retains only specified feature types in the output GFF3 file.
