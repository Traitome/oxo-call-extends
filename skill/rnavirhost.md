---
name: rnavirhost
category: utility
description: Machine-learning predictor of the likely host of an RNA virus from its genome sequence, using k-mer features and a gradient-boosted ensemble.
tags: ["rnavirhost", "rna-virus", "host-prediction", "machine-learning", "viral-genome", "metagenomics"]
author: oxo-call-community
source_url: "https://github.com/GreyGuoweiChen/VirHost.git"
---

## Concepts

- **Tool Overview**: RNAVirHost (v1.0.5, GreyGuoweiChen / VirHost) is a machine-learning tool for predicting the host of an RNA virus directly from its genome sequence. It is designed for the rapid triage of novel viral contigs (e.g., from metagenomic assemblies) and uses a gradient-boosted ensemble trained on k-mer features from known virus-host pairs.
- **Core Function**: Takes one or more viral nucleotide sequences (FASTA, typically full or near-full genomes) and outputs a per-sequence host prediction with a confidence score. The host label is at the genus or family level (e.g., "Homo sapiens", "Sus scrofa", "Gallus gallus") depending on the training data version.
- **Algorithm**: A fixed k-mer (k = 6, default) frequency vector per sequence, fed into a scikit-learn GradientBoostingClassifier trained on RefSeq viral genomes with curated host labels. The classifier is bundled with the package; users can retrain with `rnavirhost-train` (in newer versions). The output is the class with the highest probability plus a calibrated confidence score.
- **Input Format**: A multi-FASTA file with one viral sequence per record. Sequences should be at least 1000 nt (shorter sequences lose the k-mer signal). Ambiguous bases (Ns) and very low-complexity regions (e.g., poly-A tails) should be cleaned before prediction. The CLI also accepts a directory of FASTA files.
- **Output Format**: A TSV with one row per sequence: `id, length, predicted_host, host_probability, top3_hosts`. The `top3_hosts` column lists the three most likely hosts with their probabilities, useful for ambiguous cases. Output to stdout by default; redirect to a file with `-o`.
- **Use Case**: Prioritizing novel viral contigs from a wastewater metagenomic assembly (which viruses should we screen for human tropism?), flagging zoonotic potential of wildlife-sampled viral genomes, and adding host predictions to a viral database (e.g., for a custom BLAST screen).

## Pitfalls

- **CRITICAL — Predictions are at the host-family or host-genus level**: The default model collapses many host species into higher taxa (e.g., "Birds" or "Mammalia"). For strain-level host prediction, the model must be retrained with a strain-level training set (not provided in the Bioconda recipe).
- **CRITICAL — Sequences shorter than 1000 nt produce unreliable predictions**: The k-mer frequency vector is too sparse; the model predicts the most common host class. Pre-filter with `seqkit seq -m 1000 viral_contigs.fa > filtered.fa`.
- **The default model is trained on RefSeq vertebrate viruses**: For bacteriophages, plant viruses, or insect-specific viruses, the model performs poorly (most phage contigs are predicted as "unknown"). Retrain with a phage/plant/insect training set, or pre-filter by viral family via `DIAMOND blastp` against the NCBI viral proteins database.
- **No segment-level information is used**: For segmented viruses (e.g., Influenza, Rotavirus), each segment is predicted independently. A multi-segment virus will have per-segment host predictions that may disagree. The "vote" across segments is the correct approach but is not built in.
- **Ambiguous bases (N) reduce confidence**: A viral contig with >5% Ns produces a low `host_probability`. Pre-clean with `seqkit seq -g -G -m 1000` and gap-fill via `medaka` or `Pilon` if possible.
- **Calibration assumes a balanced host distribution**: The host probabilities are not well-calibrated for rare hosts (e.g., "Tursiops truncatus" appears in < 0.1% of the training set). The model is biased toward common hosts (humans, mice, chickens).

## Examples

### Basic host prediction
**Args:** `rnavirhost -i viral_contigs.fa -o host_predictions.tsv`
**Explanation:** `-i` is the input multi-FASTA, `-o` is the output TSV with one row per sequence (`id, length, predicted_host, host_probability, top3_hosts`). Default model is the vertebrate-virus-trained gradient boosting model.

### Predict for a directory of FASTA files
**Args:** `rnavirhost --input-dir viral_dir/ --output-dir host_out/`
**Explanation:** `--input-dir` reads every `*.fa` or `*.fasta` file in the directory and writes a per-file TSV with the same name in `--output-dir`. Convenient for batch processing of per-sample metagenomic assemblies.

### Restrict to high-confidence predictions
**Args:** `rnavirhost -i contigs.fa -o predictions.tsv && awk -F'\t' '$4 > 0.9' predictions.tsv > high_conf.tsv`
**Explanation:** Composite example: predict, then filter to predictions with `host_probability > 0.9`. Useful for building a high-confidence subset for downstream experimental validation (e.g., cell-culture host range testing).

### Pre-filter short contigs
**Args:** `seqkit seq -m 1000 viral_contigs.fa | rnavirhost -i - -o predictions.tsv`
**Explanation:** Pipes a length-filtered FASTA (≥ 1000 nt) into RNAVirHost via stdin. Recommended for metagenomic assemblies that include many short viral fragments (e.g., 200–500 nt contigs from short-read assemblers).

### Apply a custom-trained model
**Args:** `rnavirhost -i contigs.fa -m my_phage_model.pkl -o phage_predictions.tsv`
**Explanation:** `-m` specifies a pre-trained model pickle (produced by `rnavirhost-train` in newer versions). Required when applying RNAVirHost to non-vertebrate viruses; the default vertebrate model is the most common RNAVirHost failure mode.

### Use the Python API
**Args:** `python -c "from rnavirhost import RNAVirHost; r = RNAVirHost(); r.predict('viral_contigs.fa', out='predictions.tsv')"`
**Explanation:** The Python API for embedding RNAVirHost in a larger pipeline (e.g., a Snakemake rule that runs the classifier in-process). The `RNAVirHost` class accepts the same arguments as the CLI; see the package's API doc for `predict_batch` on a list of sequences.

### Convert per-segment predictions to a single virus-level call
**Args:** `rnavirhost -i segments/*.fa -o seg_preds.tsv && awk -F'\t' '{votes[$3]++} END {for (v in votes) print v, votes[v]}' seg_preds.tsv | sort -k2,2nr | head -1`
**Explanation:** Composite example: predict per segment, then "vote" across segments to get a single virus-level host. For Influenza, the HA segment is the most informative, but the simple majority-vote works for most well-characterized multi-segment viruses.
