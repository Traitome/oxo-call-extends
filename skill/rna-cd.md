---
name: rna-cd
category: utility
description: detect RNA contamination in DNA-seq BAM files using a trained SVM classifier on per-chunk metrics
tags: ["rna-cd", "contamination", "qc", "svm", "bam", "mitochondria"]
author: oxo-call-community
source_url: "https://rna-cd.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: rna-cd (RNA Contamination Detector, v0.2.0) is a Python tool that classifies a BAM file as "contaminated" (significant RNA carry-over) or "clean" by extracting per-chunk coverage metrics from a chosen contig (typically the mitochondrial chromosome) and feeding them to a support-vector machine.
- **Core Function**: Two subcommands: `rna_cd-train` builds an SVM model from labeled positive (contaminated) and negative (clean) BAMs, and `rna_cd-classify` applies that model to a new BAM and reports `pos` / `neg` / `unknown` plus a class probability.
- **Algorithm**: Splits a chosen contig into fixed-size chunks (default 100 bp), collects per-chunk read-coverage and base-composition metrics, optionally projects to two principal components, and fits a C-SVC with k-fold cross-validation (default 3 folds).
- **Input/Output**: Inputs are BAM files (must be indexed: `samtools index foo.bam foo.bam.bai`) supplied either as a directory or a flat list file (one BAM path per line). Training produces a `model.json` containing the pickled SVM and the PCA transform; classification produces a three-column TSV: filename, predicted_class, class_probability.
- **Mitochondrial Contig Default**: Default contig name is `chrM` and default chunksize is 100 bp. The contig and chunksize used at training time **must** match the classification call; mismatches silently degrade accuracy.
- **Use Case**: QC step in DNA-seq (WGS, exome, ChIP-seq) pipelines to flag samples with significant RNA carry-over from the wet-lab extraction — recommended before variant calling, where RNA contamination can cause false-positive splice-aware variants.

## Pitfalls

- **CRITICAL — Contig and chunksize must match between train and classify**: The model encodes the chunksize and contig name; classifying with different values produces nonsense predictions. Always pass the same `-c` and `--chunksize` at both stages.
- **CRITICAL — BAM files must be coordinate-sorted and indexed**: rna-cd uses `pysam` and requires `*.bai` indexes; unindexed BAMs fail immediately with `ValueError: BAM not indexed`.
- **Positives/negatives can be supplied as directory or list, but not both**: `-pd` (positives-dir) is mutually exclusive with `-pl` (positives-list), and the same for negatives. Passing both raises an argparse error and aborts.
- **Default `unknown` threshold is 0.75**: Samples with the most-likely class probability below 0.75 are labeled `unknown`. Override with `-t 0.6` (must be > 0.5 and < 1.0) to be more permissive, or `-t 0.9` to be stricter.
- **Cross-validation default is 3 folds**: For small training sets (< 30 BAMs) the model may be unstable; raise `--cross-validations 5` or 10 to get a more stable score, at the cost of training time.
- **Multicore `-j` only parallelizes across BAM files**: A single BAM is processed serially regardless of `-j`. For very large BAMs, consider splitting by chromosome first with `samtools view -b` and processing each subset as a "sample".

## Examples

### Train a contamination model from directories
**Args:** `rna_cd-train -c chrM -pd positives_dir -nd negatives_dir -j 4 --chunksize 100 -o model.json`
**Explanation:** `-c chrM` selects the mitochondrial contig; `-pd`/`-nd` point at directories whose BAM files are the positive (contaminated) and negative (clean) training sets; `-j 4` processes 4 BAMs in parallel; `--chunksize 100` is the metric-extraction window; `-o model.json` writes the trained SVM.

### Train a contamination model from list files
**Args:** `rna_cd-train -c chrM -pl positives.list -nl negatives.list -j 4 --chunksize 100 -o model.json`
**Explanation:** Same as the directory form, but the inputs are text files with one BAM path per line — useful when positive and negative BAMs are scattered across multiple directories.

### Train with PCA-plot diagnostic
**Args:** `rna_cd-train -c chrM -pl positives.list -nl negatives.list -j 4 --chunksize 100 -o model.json --plot-out pca.png`
**Explanation:** `--plot-out` saves a 2-D PCA scatter of the training samples; if the two clusters overlap heavily in the plot, the contamination signal is weak in this contig and you should pick a different one (e.g., a long autosomal chromosome for some library types).

### Classify new BAMs from a directory
**Args:** `rna_cd-classify -m model.json -d bams_dir -j 4 -c chrM --chunksize 100 -o classifications.out`
**Explanation:** `-m model.json` is the SVM produced by training; `-d bams_dir` is the directory of BAMs to score; `-c chrM` and `--chunksize 100` MUST match the training values; `-o classifications.out` is a 3-column TSV (filename, predicted_class, class_probability).

### Classify new BAMs from a list
**Args:** `rna_cd-classify -m model.json -l bams.list -j 4 -c chrM --chunksize 100 -o classifications.out`
**Explanation:** Same as the directory form, but the inputs are read from a text file (one BAM path per line) via `-l`.

### Use a stricter unknown threshold
**Args:** `rna_cd-classify -m model.json -d bams_dir -j 4 -c chrM --chunksize 100 -t 0.9 -o classifications.out`
**Explanation:** `-t 0.9` raises the unknown threshold from the default 0.75 to 0.9, so only samples with ≥90% probability of the predicted class get a definite `pos`/`neg` label; everything else is `unknown`.

### Parse the classification output
**Args:** `awk '$2=="pos" {print $1}' classifications.out > contaminated_samples.txt`
**Explanation:** The output is tab-delimited with columns (filename, predicted_class, class_probability); `awk` extracts the BAM paths labeled as `pos` so they can be flagged in a downstream pipeline (e.g., excluded from variant calling).

### Use 5-fold cross-validation for a small training set
**Args:** `rna_cd-train -c chrM -pl positives.list -nl negatives.list -j 4 --chunksize 100 --cross-validations 5 -o model.json`
**Explanation:** `--cross-validations 5` runs 5-fold CV instead of the default 3; recommended when the training set has fewer than 30 BAMs, because 3-fold leaves very few samples in each test fold.
