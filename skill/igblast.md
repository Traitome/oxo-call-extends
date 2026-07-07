---
name: igblast
category: sequence-analysis
description: IgBLAST is a specialized BLAST tool for analyzing immunoglobulin (Ig) and T cell receptor (TR) variable domain sequences, identifying V(D)J gene segments and CDR regions.
tags: [igblast, sequence-analysis, immunoglobulin, TCR, VDJ, antibody]
author: oxo-call-community
source_url: "http://www.ncbi.nlm.nih.gov/projects/igblast/"
---

## Concepts

- **V(D)J Gene Identification**: Identifies Variable (V), Diversity (D), and Joining (J) gene segments in rearranged immunoglobulin and T cell receptor sequences.
- **CDR Annotation**: Delineates Complementarity Determining Regions (CDR1, CDR2, CDR3) and Framework Regions (FR1-FR4).
- **Germline Database**: Uses specialized germline gene databases (IMGT, NCBI) for accurate gene segment matching.
- **Junction Analysis**: Analyzes V(D)J junction details including N nucleotide insertions and P nucleotide additions.
- **Frame Detection**: Determines whether the rearrangement is in-frame or out-of-frame.

## Pitfalls

- **Database Selection**: Requires appropriate germline database selection for the target organism and receptor type.
- **Sequence Quality**: Poor quality sequences may lead to incorrect gene assignments.
- **Somatic Mutations**: High somatic mutation rates can complicate germline gene identification.
- **Receptor Type**: Must specify correct receptor type (Ig or TCR) for accurate analysis.
- **Organism Specificity**: Germline databases are organism-specific; using the wrong database produces incorrect results.

## Examples

### Basic IgBLAST analysis
**Args:** `igblastn -query antibody.fasta -db germline_db -out results.txt`
**Explanation:** Runs IgBLAST on an antibody sequence against a germline database.

### With human Ig germline database
**Args:** `igblastn -query seq.fasta -db human_ig_v -out results.txt -organism human`
**Explanation:** Analyzes human immunoglobulin sequences with appropriate germline database.

### T cell receptor analysis
**Args:** `igblastn -query tcr.fasta -db tcr_db -out results.txt -receptor_type TCR`
**Explanation:** Analyzes T cell receptor sequences instead of immunoglobulins.

### Detailed output with annotations
**Args:** `igblastn -query seq.fasta -db germline_db -out results.txt -show_translation -outfmt 7`
**Explanation:** Generates detailed output including translation and tabular format.

### Web-based analysis
**Args:** `# Access NCBI IgBLAST web server at https://www.ncbi.nlm.nih.gov/igblast/`
**Explanation:** Alternative web interface for interactive sequence analysis.