---
name: rnaz
category: utility
description: Predict structurally conserved non-coding RNAs (ncRNAs) in multiple sequence alignments using a SVM classifier trained on thermodynamic and alignment features.
tags: ["rnaz", "structural-rna", "ncrna-prediction", "svm", "alignment", "rna-structure"]
author: oxo-call-community
source_url: "https://www.tbi.univie.ac.at/software/RNAz"
---

## Concepts

- **Tool Overview**: RNAz (v2.1.1, Vienna TBI / Hofacker / Washietl) is a tool for predicting structurally conserved non-coding RNAs (ncRNAs) in multiple sequence alignments. It uses a support-vector-machine (SVM) classifier trained on a combination of thermodynamic (z-score of MFE) and alignment-derived (sequence conservation, compensatory mutations) features.
- **Core Function**: Takes a multiple sequence alignment (in ClustalW, FASTA-aligned, or Stockholm format) and emits a per-window prediction of whether the alignment is likely a structural ncRNA, with a confidence score (P > 0.5 means "likely ncRNA"). The standard use is to scan a whole-genome alignment of two closely related species for conserved RNA structures.
- **Algorithm**: (1) The alignment is split into overlapping windows of 120 columns by default; (2) each window is folded with RNAfold (with a thermodynamic ensemble computed by the partition function); (3) the MFE z-score is computed by comparing to a set of randomized alignments; (4) the SVM combines the z-score with sequence conservation and a "structure conservation index" (SCI) computed from base-pairing probability correlations between pairs of sequences; (5) a per-window P-value is reported.
- **Input Format**: A multiple sequence alignment in ClustalW (`.aln`), FASTA-aligned, or Stockholm format. At least 2 sequences are required; 4–8 sequences of moderate diversity is the sweet spot. Very short alignments (< 50 columns) are skipped. Sequence IDs must be unique.
- **Output Format**: A plain-text report with one row per window: `start, end, length, num_sequences, mean_pairwise_identity, MFE, z-score, SCI, P, prediction`. The `prediction` is "ncRNA" for P > 0.5 and "not ncRNA" otherwise. A separate `-p` option prints a per-position bed file for visualization in IGV.
- **Use Case**: Genome-wide scans for conserved RNA structures (e.g., fly, worm, yeast comparative genomics), validating putative ncRNA families from `Infernal` cmsearch, prioritizing de novo ncRNA annotations for experimental validation, and detecting structured UTR elements from multiple alignments of orthologous 3' UTRs.

## Pitfalls

- **CRITICAL — Input MUST be a real multiple sequence alignment, not a multi-FASTA**: RNAz relies on column-wise correspondence; unaligned sequences produce random z-scores. Always run `MAFFT --auto` or `Clustal Omega` first and pass the aligned output.
- **CRITICAL — The default 120-column window is too long for some ncRNAs**: A 60-nt miRNA precursor is split across ~60 columns and may be missed. Use `-w 80` (or smaller) for short ncRNA discovery. The trade-off is that smaller windows have fewer alignment columns for the SCI calculation, so the per-window confidence drops.
- **The SVM was trained on alignments of 2–6 sequences**: Alignments with > 10 sequences saturate the conservation index and the SVM is not well-calibrated. For larger alignments, downsample to 4–6 representative sequences with `cd-hit` or `mafft --randomseed`.
- **RNAz does NOT find the ncRNA start/stop within a window**: A positive window means "this region is likely a structured ncRNA" but the exact start/stop of the RNA may be different. Refine the boundaries with `Infernal` cmsearch using a covariance model built from the predicted region.
- **The randomization in the z-score calculation is per-window**: For very large alignments (whole chromosomes), RNAz is slow because the z-score is computed by shuffling 1000× per window. Use `--shuffle-seed 1` for reproducibility.
- **No strand information is used by default**: RNAz scans both strands of the alignment. To restrict to one strand (e.g., when scanning a whole-genome alignment of transcribed strands), pre-filter with `samtools faidx -r strand_list.fa` first.

## Examples

### Basic RNAz scan
**Args:** `RNAz alignment.aln`
**Explanation:** Reads the ClustalW file `alignment.aln`, scans the alignment in 120-column windows, and prints a per-window report. Output columns include `start, end, length, num_sequences, mean_pairwise_identity, MFE, z-score, SCI, P, prediction`. The P column is the SVM posterior probability.

### Smaller windows for short ncRNAs
**Args:** `RNAz alignment.aln -w 80 -d 20`
**Explanation:** `-w 80` reduces the window size to 80 columns; `-d 20` slides the window by 20 columns (default is half the window size). Catches shorter structured ncRNAs (miRNA precursors, snoRNAs) that the default 120-column window would miss.

### Output a BED track for genome-browser visualization
**Args:** `RNAz alignment.aln -p > alignment.bed`
**Explanation:** `-p` prints a BED file (per positive window) suitable for IGV or UCSC Genome Browser upload. The score column is the SVM probability × 1000, color-coded by the prediction.

### Strand-restricted scan
**Args:** `RNAz plus_strand.aln --both-strand no`
**Explanation:** `--both-strand no` (or `--forward-only` in older versions) restricts the scan to the plus strand of the alignment. Useful for whole-genome alignments where you only care about structures on the transcribed strand.

### Filter high-confidence predictions
**Args:** `RNAz alignment.aln | awk '$NF=="ncRNA" && $(NF-1) > 0.9' > high_conf.txt`
**Explanation:** Composite: run RNAz and filter to predictions with P > 0.9 (in addition to the default prediction "ncRNA"). The last column is the prediction, the second-to-last is the P value.

### Use a custom SVM model
**Args:** `RNAz alignment.aln --model my_training.model`
**Explanation:** `--model` specifies a custom-trained SVM model (produced by the `svm_learn` step of the training set). Required when applying RNAz to non-vertebrate alignments; the default vertebrate-trained model is biased.

### Genome-wide scan with `RNAz-batch`
**Args:** `RNAz-batch aln_dir/ --out rnaz_out/ --both-strand no --slide 30`
**Explanation:** `RNAz-batch` is a wrapper that scans a directory of alignments in batch mode. `--slide 30` slides the window by 30 columns (smaller than half-window for finer resolution). Output `rnaz_out/` contains per-alignment reports and a combined summary.

### Validate a hit with Infernal
**Args:** `RNAz alignment.aln | awk '$NF=="ncRNA"' | head -1 | awk '{print $1, $2}' | tail -c +1 && cmsearch -g --tblout hits.tbl rfam.cm rnaz_hit.fa > cm.out`
**Explanation:** Composite: extract the top RNAz hit, build a small FASTA, and run `cmsearch` against an Rfam covariance model. The intersection of RNAz hits and Infernal hits is a high-confidence structured ncRNA catalog.
