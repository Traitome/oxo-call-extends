---
name: rnasamba
category: expression
description: Deep-learning classifier (k-mer CNN) for predicting the coding potential of RNA transcript sequences; a fast, alignment-free alternative to CPC2/CPAT.
tags: ["rnasamba", "coding-potential", "deep-learning", "cnn", "k-mer", "lncrna", "alignment-free"]
author: oxo-call-community
source_url: "http://apcamargo.github.io/RNAsamba/"
---

## Concepts

- **Tool Overview**: RNAsamba (v0.2.5, apcamargo) is a deep-learning classifier for predicting the coding potential of RNA sequences. It uses a 1D convolutional neural network over k-mer embeddings (k=3, default) and is one of the fastest coding-potential tools — a 100,000-transcript FASTA is scored in seconds.
- **Core Function**: Reads a multi-FASTA of nucleotide sequences and emits a per-sequence coding probability (0–1). The default pre-trained model is fit on human RefSeq mRNAs vs lncRNAs; users can retrain on species-specific data via the `rnasamba train` subcommand.
- **Algorithm**: A 1D CNN with three convolutional layers + global max pooling + a dense layer + sigmoid output. Input is a 3-mer one-hot encoding of the sequence. The CNN learns positional motifs associated with coding potential (e.g., reading-frame periodicity of substitutions, ORF coverage). Training uses cross-entropy with class weighting.
- **Input Format**: A multi-FASTA file of nucleotide sequences. Each sequence should be the full-length transcript; truncated sequences bias the model. The Bioconda recipe installs a `rnasamba` CLI; the package also exposes a Python API (`from rnasamba import RNAsamba`).
- **Output Format**: A TSV with one row per sequence: `name, length, coding_probability, coding_label`. `coding_label` is "coding" if `coding_probability ≥ 0.5` (default threshold). Output to stdout by default; redirect to a file with `-o`.
- **Use Case**: Filtering lncRNA candidates from a de novo transcriptome assembly (Trinity, StringTie) without depending on ORF content, distinguishing ORFs from spurious open reading frames in viral genomes, and adding coding-potential annotations to GTF features via `gffread` + `rnasamba`.

## Pitfalls

- **CRITICAL — Default model is trained on human data**: The bundled model is fit on human RefSeq mRNAs vs GENCODE lncRNAs; applying it to plants, fungi, or prokaryotes produces skewed probabilities. For non-human data, retrain via `rnasamba train` using a species-specific set of known coding and non-coding transcripts.
- **CRITICAL — Sequences must be at least 100 nt long**: The CNN was trained on transcripts ≥ 200 nt; sequences shorter than 100 nt produce unreliable scores (the global max pool over too few positions). Pre-filter with `seqkit seq -m 100 transcripts.fa > transcripts.filtered.fa`.
- **Ambiguous bases (N) reduce confidence**: The CNN treats N as a separate k-mer; sequences with >5% Ns produce probabilities near 0.5 (the model's uncertainty floor). Pre-clean with `seqkit seq -g -G`.
- **`-t 0.5` is the default threshold; the optimal threshold depends on the species**: For human data, 0.5 is well-calibrated. For species with shorter ORFs (Drosophila, C. elegans), 0.4 may give better recall. Validate on a small known-good set and re-tune.
- **No ORF finding step is performed**: Unlike CPAT or CPC2, RNAsamba does NOT compute ORF length/coverage. It is a pure sequence-based classifier; if you need ORF statistics for follow-up, run `pyrodigal-gv` or `TransDecoder` separately.
- **The model file is bundled in the pip package**: It is a small `.h5` file inside the package directory; deleting or moving the package's `data/` directory breaks prediction. The `conda install -c bioconda rnasamba` recipe handles this correctly; a manual pip install + delete may not.

## Examples

### Basic coding-potential prediction
**Args:** `rnasamba classify -i transcripts.fa -o predictions.tsv`
**Explanation:** `-i` is the input multi-FASTA, `-o` is the output TSV with one row per sequence (`name, length, coding_probability, coding_label`). Default model is the human-trained CNN. Output is a single line per sequence — easy to merge with a GTF.

### Predict with a custom threshold
**Args:** `rnasamba classify -i transcripts.fa -o predictions.tsv -t 0.6`
**Explanation:** `-t 0.6` raises the coding-label threshold to 0.6, increasing precision at the cost of recall. Use 0.6–0.7 when the downstream step (e.g., structural analysis) is expensive and you want few false positives.

### Retrain on a species-specific set
**Args:** `rnasamba train -c coding.fa -n noncoding.fa -o zebrafish_model/`
**Explanation:** `-c` is the coding training set (FASTA), `-n` is the non-coding training set (FASTA), `-o` is the output directory for the new model. The training set should be balanced (same number of coding and non-coding transcripts) and species-matched to the prediction set.

### Apply a custom model
**Args:** `rnasamba classify -i transcripts.fa -m zebrafish_model/model.h5 -o predictions.tsv`
**Explanation:** `-m` specifies a custom model file produced by `rnasamba train`. Required for non-human data; using the human default for plants or fungi is the most common RNAsamba failure.

### Pre-filter short sequences
**Args:** `seqkit seq -m 100 transcripts.fa | rnasamba classify -i - -o predictions.tsv`
**Explanation:** Pipes a length-filtered FASTA into RNAsamba via stdin. Recommended for transcriptome assemblies that include many short contamination fragments (e.g., rRNA fragments, tRNA halves).

### Use the Python API
**Args:** `python -c "from rnasamba import RNAsamba; r = RNAsamba(); r.classify('transcripts.fa', 'predictions.tsv')"`
**Explanation:** The Python API for embedding RNAsamba in a larger pipeline (e.g., a Snakemake rule that runs the classifier in-process). The `RNAsamba` class accepts the same arguments as the CLI; see the package's API doc for `classify_batch` on a list of sequences.

### Filter coding transcripts from a FASTA
**Args:** `rnasamba classify -i transcripts.fa -o predictions.tsv && awk -F'\t' '$4=="coding" {print $1}' predictions.tsv > coding_ids.txt && seqkit grep -f coding_ids.txt transcripts.fa > coding_only.fa`
**Explanation:** Composite example: predict, extract coding IDs, subset the FASTA with `seqkit grep`. Useful for separating mRNA from lncRNA catalogs in a de novo assembly.
