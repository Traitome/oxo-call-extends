---
name: rodeo
category: annotation
description: Rapid ORF Description and Evaluation Online (RODEO) for the discovery and characterization of RiPP (ribosomally synthesized and post-translationally modified peptide) biosynthetic gene clusters and precursor peptides.
tags: ["rodeo", "ripps", "precursor-peptide", "biosynthetic-cluster", "annotation", "svm"]
author: oxo-call-community
source_url: "http://ripp.rodeo/index.html"
---

## Concepts

- **Tool Overview**: RODEO (v2.3.3, Hetrick / Kelleher / van der Donk) is a tool for the discovery and characterization of RiPP (ribosomally synthesized and post-translationally modified peptide) biosynthetic gene clusters and their precursor peptides. It evaluates a gene neighborhood against a library of pHMMs (profile hidden Markov models) for RiPP-modifying enzymes, and uses an SVM classifier and motif analysis to scan unannotated intergenic regions for RiPP precursors.
- **Core Function**: Takes a GenBank file or a genome FASTA + GFF3, and reports candidate RiPP precursor peptides and their surrounding biosynthetic gene clusters. The output is a TSV/HTML report with per-gene annotations, pHMM hits, and a confidence score for the RiPP call.
- **Algorithm**: (1) HMMER scan of all proteins in the input against a custom library of RiPP-modifying-enzyme pHMMs; (2) SVM classifier trained on known RiPP precursor features (length, charge, sequence motifs) to score candidate precursor ORFs; (3) neighborhood analysis to identify the core peptide + modification enzymes within a configurable window (default 20 kb).
- **Input Format**: A GenBank file (`*.gbk`) or a directory of GenBank files (one per genome). Smaller inputs (single contigs) are accepted; very large genomes (whole chromosomes) may take minutes per cluster. The HMMER database and SVM model are bundled with the package.
- **Output Format**: An HTML report and a TSV summary with one row per candidate cluster: `cluster_id, scaffold, start, end, product, pHMM_hits, precursor_score, modification_enzymes`. The HTML report is per-cluster with annotated sequences and a clickable gene map.
- **Use Case**: Discovering new RiPP clusters in a bacterial genome assembly, prioritizing candidate lanthipeptide / lasso peptide / thiopeptide clusters for experimental validation, scanning a metagenomic assembly for novel RiPPs, and curating the MIBiG / BiG-FAM database of secondary metabolites.

## Pitfalls

- **CRITICAL — Input must be a GenBank file with annotations, not a plain FASTA**: RODEO uses the annotated CDS features to scan for precursors. A plain FASTA produces no hits. Convert with `prokka --outdir annotated/ --prefix sample sample.fa` first.
- **CRITICAL — The pHMM database is bundled but is not exhaustive**: The default library covers the major RiPP classes (lanthipeptide, lasso, thiopeptide, sactipeptide, etc.) but may miss recently described classes. Update the library via `rodeo-update-hmms` (if available) or download from MIBiG.
- **The SVM threshold is a soft cut-off**: The SVM score is calibrated on known RiPPs from a specific training set; a "high-confidence" hit in a divergent clade may be filtered. Adjust the threshold with `--score-cutoff 0.5` (default 0.7) to recall more candidates.
- **Small ORFs are not annotated by PROKKA by default**: RODEO's strength is its ability to scan unannotated intergenic regions for small ORFs. PROKKA's `--metagenome` mode annotates small ORFs; without it, RODEO may miss them.
- **The neighborhood window (20 kb) is small for some RiPP classes**: A 20 kb window misses the lanthipeptide modification enzymes that are often 30+ kb away. Increase via `--window 50000` for lanthipeptide discovery.
- **No automatic taxonomic filtering**: RODEO reports all candidates regardless of taxonomy. A cluster from a fungal genome is reported as a RiPP candidate, even though RiPPs are predominantly bacterial. Filter the output by taxonomy post hoc.

## Examples

### Basic RODEO run on a GenBank file
**Args:** `rodeo --genbank sample.gbk --output rodeo_out/`
**Explanation:** `--genbank` is the input GenBank file, `--output` is the output directory. Produces `rodeo_out/report.html` and `rodeo_out/clusters.tsv`. Default neighborhood window is 20 kb.

### Run on a directory of GenBank files
**Args:** `rodeo --genbank-dir genbank_dir/ --output rodeo_out/`
**Explanation:** `--genbank-dir` scans a directory of GenBank files (one per genome) in batch. Useful for screening a multi-genome dataset (e.g., a genus-level pangenome).

### Scan unannotated intergenic regions for precursor ORFs
**Args:** `rodeo --genbank sample.gbk --scan-intergenic --output rodeo_out/`
**Explanation:** `--scan-intergenic` enables the manual-ORF scan: small ORFs in unannotated regions are translated and scored by the SVM. Catches precursors that PROKKA's `CDS` filter missed. Slower than the default annotation-based scan.

### Increase the neighborhood window
**Args:** `rodeo --genbank sample.gbk --window 50000 --output rodeo_out/`
**Explanation:** `--window 50000` increases the cluster neighborhood window to 50 kb. Use for lanthipeptide clusters, where the modification enzymes are often 30+ kb from the precursor. The output reports larger clusters.

### Lower the SVM score cutoff for higher recall
**Args:** `rodeo --genbank sample.gbk --score-cutoff 0.5 --output rodeo_out/`
**Explanation:** `--score-cutoff 0.5` (default 0.7) recalls more candidate precursors at the cost of more false positives. Use for initial exploration; raise the cutoff in a follow-up run for the high-confidence set.

### Use a custom pHMM database
**Args:** `rodeo --genbank sample.gbk --hmm-db custom_ripps.hmm --output rodeo_out/`
**Explanation:** `--hmm-db` specifies a custom HMMER database. Use to add newly characterized RiPP classes not in the bundled library. The database must be in HMMER3 format (`hmmpress` first).

### Output a GenBank file with the cluster annotations
**Args:** `rodeo --genbank sample.gbk --output-gbk annotated.gbk --output rodeo_out/`
**Explanation:** `--output-gbk` writes the input GenBank with RODEO's cluster annotations appended as new features. Useful for downstream submission to MIBiG or BiG-FAM.
