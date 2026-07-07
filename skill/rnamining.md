---
name: rnamining
category: utility
description: Machine-learning pipeline for predicting the coding potential of RNA sequences from FASTA input, with a built-in feature extractor and pre-trained models.
tags: ["rnamining", "coding-potential", "machine-learning", "fasta", "lncrna", "orf"]
author: oxo-call-community
source_url: "https://github.com/lfreitasl/RNAmining/tree/pypackage"
---

## Concepts

- **Tool Overview**: RNAmining (v1.0.4, lfreitasl) is a Python package for predicting the coding potential of RNA sequences provided in FASTA format. It is designed primarily for distinguishing long non-coding RNAs (lncRNAs) from mRNAs in de novo transcriptome assemblies, and exposes both a CLI (`rnamining`) and a Python API.
- **Core Function**: Computes sequence-based features (ORF length, ORF coverage, k-mer frequencies, GC content, Fickett score, hexamer score, etc.), feeds them into a pre-trained classifier (default: a gradient-boosted ensemble), and emits a per-sequence coding-potential label and score. The classifier is bundled with the package; custom models can be retrained.
- **Algorithm**: Feature extraction (ORF finding via `pyrodigal`/`transDecoder`, k-mer counting via `scikit-learn`'s CountVectorizer, sequence-statistics via custom code) followed by a fixed classifier (default `sklearn.ensemble.GradientBoostingClassifier`). The exact feature set is configurable; the default set follows the CPAT/CPC2 convention.
- **Input Format**: A multi-FASTA file (nucleotide sequences). Sequences should be the mature transcript (no poly-A tails, no introns). The CLI also accepts a directory of FASTA files via `--input-dir`.
- **Output Format**: A TSV with one row per input sequence: `id, length, orf_length, orf_coverage, fickett_score, hexamer_score, coding_probability, label`. Output to stdout by default; redirect to a file with `-o`.
- **Use Case**: Filtering lncRNA candidates from de novo transcriptome assemblies (Trinity, StringTie), validating the coding status of putative ORFs in viral genomes, and adding coding-potential annotations to GTF/GFF files via `gffread` + `rnamining` + `bedtools intersect`.

## Pitfalls

- **CRITICAL — Default classifier is trained on human data**: The bundled model is fit on human RefSeq mRNAs vs lncRNAs; applying it to plants, fungi, or prokaryotes will produce skewed probabilities. For non-human data, retrain with `rnamining-train` (a subcommand in newer versions) using a species-specific training set.
- **CRITICAL — Input sequences must not contain ambiguous bases or poly-A tails**: Sequences with >5% Ns or a long (>50 nt) poly-A tail will bias the ORF finder. Pre-clean with `seqkit seq -g -G -r` (drop reads with Ns) and `seqkit cut -t poly` (trim poly-A).
- **Feature order matters for custom models**: When retraining with `rnamining-train`, the test set must have the same feature order; the package re-creates the order from the training config but a mis-aligned CSV can produce a model that scores 0.5 for everything.
- **The default model is biased toward longer ORFs**: For transcriptomes with many short regulatory ncRNAs (miRNAs, snoRNAs, snRNAs) the model will tend to label them as non-coding — usually correct, but be aware that genuine small mRNAs (< 100 aa) will also be mislabelled.
- **`pyrodigal` must be installed for ORF-based features**: Older versions used `transDecoder`; new versions use `pyrodigal-gv` for prokaryotic ORFs. The `conda install -c bioconda rnamining` recipe pulls both, but a manual pip install does not.
- **Output `coding_probability` is not a calibrated p-value**: It is the classifier's `predict_proba` output, not a calibrated probability. Comparing 0.7 vs 0.8 across different classifiers (or different species) is not meaningful without calibration via `sklearn.calibration.CalibratedClassifierCV`.

## Examples

### Basic coding-potential prediction
**Args:** `rnamining -i transcripts.fa -o predictions.tsv`
**Explanation:** `-i` is the input multi-FASTA, `-o` is the output TSV. The output has one row per sequence with `id, length, orf_length, orf_coverage, fickett_score, hexamer_score, coding_probability, label`. Default classifier is the human-trained gradient boosting model.

### Predict for a directory of FASTA files
**Args:** `rnamining --input-dir fa_dir/ --output-dir out_dir/`
**Explanation:** `--input-dir` reads every `*.fa`, `*.fasta`, or `*.fna` file in the directory and writes a per-file TSV with the same name in `--output-dir`. Convenient for batch processing of per-sample assemblies.

### Use a custom-trained model
**Args:** `rnamining -i transcripts.fa -m my_species_model.pkl -o predictions.tsv`
**Explanation:** `-m` specifies a pre-trained model pickle (produced by `rnamining-train`); required when applying RNAmining to non-human data. The model pickle contains both the classifier and the feature-order metadata, so the same input feature pipeline is preserved.

### Pre-clean input FASTAs before prediction
**Args:** `seqkit seq -g -G transcripts.fa | rnamining -i - -o predictions.tsv`
**Explanation:** `seqkit seq -g -G` removes FASTA records with >10% Ns or with sequences shorter than a threshold; the pipe feeds the cleaned FASTA to RNAmining. Highly recommended for low-quality de novo assemblies (Trinity components with degenerate ends).

### Filter coding sequences from a transcriptome
**Args:** `rnamining -i transcripts.fa -o predictions.tsv && awk -F'\t' '$NF=="coding" || $NF=="mRNA" {print $1}' predictions.tsv > coding_ids.txt && seqkit grep -f coding_ids.txt transcripts.fa > coding_only.fa`
**Explanation:** Three-step composite: (1) predict, (2) extract IDs of coding sequences, (3) use `seqkit grep` to subset the FASTA. The `awk` filter accepts both "coding" and "mRNA" labels depending on the version's label vocabulary.

### Run as a Python module
**Args:** `python -c "from rnamining import RNAmining; r = RNAmining(); r.predict('transcripts.fa', out='predictions.tsv')"`
**Explanation:** Python API for embedding RNAmining in a larger pipeline (e.g., a Snakemake rule that runs the prediction in-process). The `RNAmining` class accepts the same arguments as the CLI; see the package's API doc for `predict_batch` on a list of sequences.
