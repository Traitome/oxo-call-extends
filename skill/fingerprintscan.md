---
name: fingerprintscan
category: annotation
description: "FingerPRINTScan scans protein sequences against the PRINTS database of diagnostic protein fingerprints for family and domain identification."
tags: [fingerprintscan, annotation, PRINTS, protein-fingerprint, protein-family, domain-annotation, bioinformatics, motif-analysis]
author: oxo-call-community
source_url: "https://github.com/ebi-pf-team/interproscan"
---

## Concepts

- **Tool Overview**: FingerPRINTScan is a tool for scanning protein sequences against the PRINTS database of diagnostic protein fingerprints. PRINTS is a compendium of protein motif "fingerprints" where each fingerprint is a group of conserved motifs that together form a diagnostic signature for identifying protein families.
- **Core Function**: Identifies protein family membership by matching query sequences against the PRINTS fingerprint database, detecting conserved motifs and their sequential relationships.
- **Input/Output**: Input: Protein sequence(s) in FASTA format. Output: Match results indicating which fingerprints the sequence matches, including partial and full matches.
- **Algorithm**: Uses position-specific scoring matrices (PSSM) derived from multiple sequence alignments of each fingerprint. Matches are scored based on motif occurrence, order, and spacing, with statistical E-values computed for significance assessment.
- **Key Features**: Hierarchical protein family classification, detects distant evolutionary relationships, considers motif context and order, provides statistical significance estimates, integrates with InterProScan.
- **Installation**: Part of the InterProScan package: `conda install -c bioconda interproscan` or download from https://github.com/ebi-pf-team/interproscan

## Pitfalls

- **Database Availability**: The standalone FingerPRINTScan tool is deprecated; PRINTS is now primarily accessed through InterProScan. Ensure you have access to current database files.
- **Threshold Selection**: Default E-value thresholds may be too stringent for remote homolog detection or too lenient for specific subfamily discrimination.
- **Motif Order Sensitivity**: Some proteins may have motifs in different orders due to domain shuffling. Configure sensitivity settings appropriately.
- **Partial Matches**: Sequences matching only some motifs may represent degenerate families or truncation artifacts. Review partial match reports carefully.
- **Database Curation**: PRINTS is no longer actively maintained (ceased ~2012). For current analysis, consider using InterPro which incorporates PRINTS data.

## Examples

### Scan a protein sequence with InterProScan
**Args:** `interproscan -i protein.fasta -f TSV -o results.tsv`
**Explanation:** Scans protein sequences using InterProScan which includes PRINTS fingerprint matching. Outputs results in TSV format with protein family assignments.

### Run PRINTS analysis with EMBOSS pscan
**Args:** `pscan -sequence protein.fasta -outfile results.pscan`
**Explanation:** EMBOSS pscan provides direct access to PRINTS databases. Specify minimum/maximum number of fingerprint elements to match.

### Search with specific motif count
**Args:** `pscan -sequence protein.fasta -emin 3 -emax 10 -outfile results.pscan`
**Explanation:** Requires at least 3 and at most 10 fingerprint elements to match. Increasing emin reduces false positives, decreasing it captures more remote homologs.

### Batch process multiple sequences
**Args:** `interproscan -i sequences.fasta -b batch_results -f XML -dp`
**Explanation:** Processes all sequences in batch mode with disabled pre-calculated lookups. The -dp flag enables parallel processing for faster results.

### Extract specific annotation fields
**Args:** `interproscan -i protein.fasta -f TSV -o results.tsv -t p`
**Explanation:** Only runs the PRINTS (p) analysis type. Useful when you specifically need fingerprint-based annotation.

### Parse results for specific families
**Args:** `grep "PR00191" results.tsv`
**Explanation:** After scanning, filter results by signature accession (e.g., PRINTS patterns starting with "PR00191" for kinases) to identify specific protein families.

### Evaluate match quality
**Args:** `awk '$5<1e-5 && $6>=3' results.tsv`
**Explanation:** Check the number of motifs matched, E-value, and whether the match is full or partial. Full matches (all motifs in correct order) indicate confident family assignments.

### Integrate with protein function prediction
**Args:** `interproscan -i protein.fasta -f TSV -o results.tsv && grep "PR00191" results.tsv`
**Explanation:** Use PRINTS matches to infer protein function. Fingerprints often correspond to functional sites like enzyme active domains or binding pockets.

### Compare multiple isoforms
**Args:** `interproscan -i isoforms.fasta -f TSV -o isoform_comparison.tsv`
**Explanation:** Compare fingerprint profiles across protein isoforms to identify conserved and divergent domains, useful for studying protein evolution.

### Export to bioinformatics formats
**Args:** `interproscan -i protein.fasta -f GFF3 -o annotations.gff3`
**Explanation:** Exports results in GFF3 format for direct integration with genome browsers and other bioinformatics pipelines.
