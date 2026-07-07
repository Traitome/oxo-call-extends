---
name: rnaprot
category: utility
description: Train and apply deep-learning models of RNA-binding protein (RBP) sequence preferences to predict RBP binding sites in transcripts.
tags: ["rnaprot", "rbp", "binding-sites", "deep-learning", "rna-protein", "clip"]
author: oxo-call-community
source_url: "https://github.com/BackofenLab/RNAProt"
---

## Concepts

- **Tool Overview**: RNAProt (v0.5, Backofen Lab) is a Python framework for training and applying deep-learning models that predict RNA-binding protein (RBP) binding sites from sequence. It supports a CNN/Transformer model family and is designed for the analysis of CLIP-seq (PAR-CLIP, HITS-CLIP, iCLIP) and RNACompete data.
- **Core Function**: Two main modes: (1) `rnaprot-train` fits a model on a BED-like file of bound positions and a transcript FASTA, learning an RBP's sequence preference; (2) `rnaprot-predict` applies a trained model to score every position of a new transcript set. The package is GPU-aware (PyTorch backend) and supports multi-task training across multiple RBPs simultaneously.
- **Algorithm**: The core model is a 1D CNN with optional dilated convolutions and a Transformer encoder; the input is a one-hot RNA sequence window (default 100 nt, configurable). The model outputs a per-position binding probability. Training uses cross-entropy loss with negative sampling from non-bound regions.
- **Input Format**: For training, a BED-like TSV with columns `chrom, start, end, name, score, strand, rbp_label` plus a transcript FASTA. For prediction, just a transcript FASTA plus a trained model checkpoint (`.pt` PyTorch file). The BED file is typically derived from `PureCLIP` or `Piranha` peak calling on CLIP-seq data.
- **Output Format**: For training, a model checkpoint (`*.pt`) and a JSON with training history (loss, AUPRC per epoch). For prediction, a BED-like TSV of per-transcript windows with binding probability, plus a BEDGRAPH wiggle file for genome-browser visualization.
- **Use Case**: Predicting RBP binding from CLIP-seq peaks (post-PureCLIP), comparing RBP binding preferences across species (a model trained on human can be applied to mouse orthologs), and designing RNA sequences that bind or evade a given RBP (synthetic biology / RNA therapeutics).

## Pitfalls

- **CRITICAL — PyTorch must be installed and CUDA-aware if you have a GPU**: The Bioconda recipe (`conda install -c bioconda rnaprot`) installs a CPU-only PyTorch; GPU usage requires `conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia`. Without it, `rnaprot-predict` will run on CPU and take 10–50× longer.
- **CRITICAL — Training data must be balanced across positive/negative sets**: If the BED file has 10,000 positive windows and only 100 negative, the model will predict "bound" for every position. RNAProt has a `--balance` flag that auto-subsamples the larger class; use it for the first training run.
- **Window size must match the biological RBP footprint**: Default is 100 nt, suitable for most RBPs (≈ 30–60 nt of contact). A large RBP (e.g., a multi-RBP complex) may need 200–500 nt; a small RBP (e.g., a single zinc finger) may be better at 40 nt. Tune via `--window-size` and re-validate with held-out CLIP data.
- **Negative regions must be sequence-matched, not random**: Random negatives are too easy and produce a model that does not generalize. RNAProt can sample negatives from gene bodies of equal expression (using `--expression-table`) or from shuffled peaks; both options are in the manual.
- **`--genome` is required if the BED uses chromosome names**: The BED file is read directly; if the chromosomes are named with `chr1` (UCSC) but the FASTA is named with `1` (Ensembl), no matches will be found. Pre-normalize with `sed 's/^chr//' peaks.bed > peaks_clean.bed`.
- **Model checkpoints are NOT cross-version compatible**: A model trained with RNAProt 0.4 will not load in 0.5 due to a model-architecture change. Re-train or downgrade the package if you must use an old model.

## Examples

### Train a model from a CLIP-seq peak set
**Args:** `rnaprot-train --bed clip_peaks.bed --fasta transcripts.fa --window-size 100 --balance --output-dir model_run/`
**Explanation:** `--bed` is the BED-like peak file from PureCLIP/Piranha, `--fasta` is the transcriptome, `--window-size 100` sets the per-peak window, `--balance` auto-balances positive/negative examples. Output directory `model_run/` contains the model checkpoint and training log.

### Predict binding sites with a trained model
**Args:** `rnaprot-predict --fasta new_transcripts.fa --model model_run/checkpoint.pt --output predictions.bed`
**Explanation:** `--model` is the trained checkpoint from `rnaprot-train`, `--fasta` is the new transcriptome, `--output` is a BED file with per-window binding probability. Combine with `bedtools sort` and `bgzip`/`tabix` for genome-browser display.

### Force CPU-only inference
**Args:** `rnaprot-predict --fasta transcripts.fa --model model.pt --cpu --output predictions.bed`
**Explanation:** `--cpu` disables CUDA even if a GPU is available; useful for reproducibility on heterogeneous hardware or in containers without GPU support. Slower, but deterministic across machines.

### Train on multi-RBP data (multi-task)
**Args:** `rnaprot-train --bed multi_rbp_peaks.bed --fasta transcripts.fa --rbp-col 7 --window-size 100 --output-dir multi_model/`
**Explanation:** `--rbp-col 7` is the column index in the BED file (1-based) that contains the RBP label. Multi-task training allows the model to share sequence features across RBPs, improving performance on data-scarce RBPs. The output checkpoint can be used for all RBPs in the training set.

### Convert predictions to a BEDGRAPH wiggle track
**Args:** `rnaprot-predict --fasta transcripts.fa --model model.pt --output predictions.bed --wiggle predictions.bg`
**Explanation:** `--wiggle` writes a BEDGRAPH file in addition to the BED file; the wiggle is suitable for direct upload as a custom track in the UCSC Genome Browser or for IGV visualization.

### Apply a human-trained model to mouse orthologs
**Args:** `rnaprot-predict --fasta mouse_transcripts.fa --model human_model.pt --output mouse_predictions.bed`
**Explanation:** Cross-species application works only for highly conserved RBPs (e.g., PTBP1, HNRNPA1); the binding motif must be conserved. For divergent RBPs, retrain with mouse-specific CLIP data.

### Predict with a probability threshold
**Args:** `rnaprot-predict --fasta transcripts.fa --model model.pt --threshold 0.7 --output high_conf.bed`
**Explanation:** `--threshold 0.7` writes only positions with binding probability ≥ 0.7 to the output, reducing the false-positive rate. Tune the threshold to balance precision and recall against held-out CLIP data.
