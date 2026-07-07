---
name: rpbp
category: utility
description: Ribosome Profiling with Bayesian Predictions (Rp-Bp) — detects translational ORFs and quantifies ribosome occupancy from ribosome profiling (Ribo-Seq) data using a Bayesian framework that models read-length distributions.
tags: ["rpbp", "ribosome-profiling", "ribo-seq", "orf-detection", "bayesian", "translation"]
author: oxo-call-community
source_url: "https://rp-bp.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: Rp-Bp (v4.0.1, Michel / Snijder / Barna lab) is a tool for detecting and quantifying translational ORFs from ribosome profiling (Ribo-Seq) data. It uses a Bayesian framework that models the periodic read-length distribution characteristic of genuine translating ribosomes, and provides per-ORF posterior probabilities of translation.
- **Core Function**: Takes Ribo-Seq reads (BAM, with the matching transcriptome FASTA and GTF) and reports candidate ORFs with per-ORF translation probabilities, P-site offsets, and ribosome density. The output is a TSV with one row per ORF: `orf_id, transcript_id, start, stop, length, p_translation, mean_p_site_offset, ribosome_density`.
- **Algorithm**: (1) For each read length, compute the P-site offset from the ribosome's A-site position; (2) Aggregate reads at the codon level; (3) Compute a periodic score based on the in-frame read density; (4) Apply a Bayesian model that incorporates a prior on read-length distribution to compute the per-ORF posterior probability of translation. The model is read-length-aware, so it correctly handles the multi-length read distribution typical of Ribo-Seq libraries.
- **Input Format**: A BAM file of Ribo-Seq reads (coordinate-sorted, indexed), a transcriptome FASTA, and a GTF annotation. Optional: a list of read lengths to use (auto-detected from the BAM), and a minimum read count per ORF (default 10).
- **Output Format**: A TSV with one row per ORF (annotated + novel) and a BED file with the ORF coordinates. The TSV columns are: `orf_id, transcript_id, start, stop, strand, length, num_reads, p_translation, p_site_offset, frame, ribosome_density`. The BED is suitable for IGV visualization.
- **Use Case**: The standard ORF-detection step in a Ribo-Seq analysis (canonical use case), identifying translated uORFs (upstream ORFs) in 5' UTRs, finding non-canonical ORFs (e.g., in lncRNAs or circRNAs), and quantifying translational efficiency (Ribo-Seq / RNA-Seq) for differential translation analysis.

## Pitfalls

- **CRITICAL — The transcriptome FASTA must match the GTF**: A GTF with GRCh38 coordinates and a FASTA with GRCh37 sequences produces a silent "no ORFs found" error. Verify with `samtools faidx transcriptome.fa | head` and `head -1 annotation.gtf`.
- **CRITICAL — Read length must be specified OR auto-detected correctly**: For libraries with a tight read-length distribution (e.g., monosome-protected fragments of 28–30 nt), the auto-detection works. For libraries with a wide distribution (e.g., polysome profiling), explicitly pass `--read-lengths 26,27,28,29,30`.
- **The Bayesian prior is calibrated on mammalian (mouse/human) libraries**: For distant species (e.g., bacteria, plants, parasites), the prior may not match the actual read-length distribution. Re-calibrate via `rpbp-calibrate` (if available) on a known translated ORF.
- **P-site offsets are computed per read length, not globally**: A library with multiple read lengths will have multiple P-site offsets. The output reports the offset used per ORF; verify with a metagene analysis.
- **No built-in differential translation analysis**: Rp-Bp detects and quantifies ORFs but does not compare conditions. Use `anota2seq` or `riborex` for differential translation, with the Rp-Bp counts as input.
- **uORF detection requires the 5' UTR annotation**: For organisms with poorly annotated 5' UTRs (e.g., from RefSeq), the uORF detection is incomplete. Use a comprehensive 5' UTR annotation (e.g., from CAGE or 5' RACE data) for the best uORF results.

## Examples

### Basic ORF detection
**Args:** `rpbp prepare-orfs --gtf annotation.gtf --fasta transcriptome.fa --out orfs.tsv && rpbp --bam ribo.bam --orfs orfs.tsv --out rpbp_out/`
**Explanation:** Two-step: first, `prepare-orfs` extracts the annotated ORFs from the GTF; second, `rpbp` runs the Bayesian model on each ORF. Output `rpbp_out/` contains the per-ORF TSV and BED.

### Specify read lengths
**Args:** `rpbp --bam ribo.bam --orfs orfs.tsv --read-lengths 28,29,30 --out rpbp_out/`
**Explanation:** `--read-lengths 28,29,30` restricts the analysis to reads of length 28–30 nt. Useful for libraries with a tight length distribution (e.g., monosome-protected fragments). Default is auto-detection.

### Run on a specific chromosome
**Args:** `samtools view -b ribo.bam chr1 > ribo_chr1.bam && rpbp --bam ribo_chr1.bam --orfs orfs_chr1.tsv --out rpbp_chr1/`
**Explanation:** Composite: pre-filter the BAM to a specific chromosome, then run Rp-Bp. Useful for chromosome-level analyses or for running Rp-Bp in parallel per chromosome.

### Detect uORFs
**Args:** `rpbp prepare-orfs --gtf annotation.gtf --fasta transcriptome.fa --include-5utr --out orfs_5utr.tsv && rpbp --bam ribo.bam --orfs orfs_5utr.tsv --out rpbp_5utr/`
**Explanation:** `--include-5utr` includes the 5' UTR in the ORF search space. Required for uORF detection. The output reports per-uORF translation probabilities.

### Detect novel ORFs in lncRNAs
**Args:** `rpbp prepare-orfs --gtf annotation.gtf --fasta transcriptome.fa --include-ncrna --out orfs_ncrna.tsv && rpbp --bam ribo.bam --orfs orfs_ncrna.tsv --out rpbp_ncrna/`
**Explanation:** `--include-ncrna` includes the non-coding RNA loci in the ORF search space. Useful for finding translated ORFs in lncRNAs (a known phenomenon in some cancers).

### Calibrate the Bayesian prior
**Args:** `rpbp calibrate --bam ribo.bam --gtf annotation.gtf --fasta transcriptome.fa --out calibration/`
**Explanation:** `calibrate` (if available) re-calibrates the Bayesian prior using a set of known translated ORFs (e.g., canonical CDS). Required for species with atypical read-length distributions.

### Quantify translation efficiency
**Args:** `rpbp --bam ribo.bam --orfs orfs.tsv --out rpbp_out/ && featureCounts -a annotation.gtf -o counts.txt ribo.bam rna.bam && anota2seq --countmat counts.txt --conditions treat,ctrl --out anota2seq_out/`
**Explanation:** Composite: get the Ribo-Seq counts from Rp-Bp, the RNA-Seq counts from `featureCounts`, then run `anota2seq` for differential translation analysis. The output reports genes with significant changes in translation efficiency.
