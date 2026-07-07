---
name: rrmscorer
category: utility
description: RRMScorer — a sequence-based RRM-RNA binding predictor that scores how likely a single RNA Recognition Motif (RRM) is to bind single-stranded RNA, with residue-level interaction propensities.
tags: ["rrmscorer", "rrm", "rna-binding", "rbp", "bio2byte", "rnact", "predictor"]
author: oxo-call-community
source_url: "https://bio2byte.be/rrmscorer/"
---

## Concepts

- **Tool Overview**: RRMScorer (v1.0.11, Bio2Byte / VUB, Roca-Martínez, Díaz, Vranken 2023) is a sequence-based predictor of RNA-binding preferences for proteins containing RNA Recognition Motifs (RRMs), the most prevalent RNA-binding domain in eukaryotes. Given a protein sequence and an optional RNA sequence, it returns residue-level binding scores and an overall RNA-binding likelihood.
- **Core Function**: Takes a single RRM protein sequence (or a UniProt ID) and an optional RNA sequence; predicts per-residue binding scores and an overall binding likelihood. The scores are derived from a probabilistic model trained on 187 RRM–RNA structural complexes (Roca-Martínez et al., PLOS Comput Biol 2023). The web server (https://bio2byte.be/rrmscorer) provides precomputed predictions for >1400 human RRM-containing proteins.
- **Algorithm**: (1) Detect RRM domains in the input sequence (HMMER-based); (2) for each RRM, extract per-residue features (physicochemical properties, secondary-structure propensity, conservation); (3) score the RRM-RNA interaction using a probabilistic model derived from amino acid–nucleotide interaction propensities; (4) output per-residue scores and an overall binding score.
- **Input Format**: (1) A protein sequence in FASTA (or a UniProt ID); (2) optional: an RNA sequence in FASTA (the prediction is more accurate when an RNA is supplied); (3) optional: a list of RRM domain coordinates (if known). The CLI accepts FASTA files; the web server also accepts UniProt IDs.
- **Output Format**: A JSON/CSV with per-residue binding scores, an overall binding likelihood (0–1), a sequence logo of preferred RNA bases per RRM position, and bar plots (PNG/SVG) of per-residue scores. Pre-computed predictions are returned instantly for UniProt IDs.
- **Use Case**: Predicting the RNA-binding preferences of an RRM-containing protein (canonical use case), studying the impact of single-point mutations on RNA binding, comparing binding preferences across multiple RRM domains, and prioritizing candidate RBPs in a proteome.

## Pitfalls

- **CRITICAL — The protein sequence MUST contain an RRM domain**: Non-RRM proteins return a low/zero score and a "no RRM detected" warning. RRMScorer is not a generic RBP predictor; for that, use iDeepE, RBPCNN, or PrismNet.
- **CRITICAL — RRMScorer is a SEQUENCE-based predictor, not a structure-based one**: It does not require a 3D structure, but it also does not use one. For structure-aware predictions, use AlphaFold3 or RoseTTAFoldNA (which can predict the complex directly).
- **The HMMER database is required for RRM detection**: The first run downloads the RRM HMM profile from Pfam. Without internet access, supply the RRM coordinates explicitly with `--rrm-coords`.
- **The RNA sequence (if supplied) should be single-stranded**: The model is trained on ssRNA binding. dsRNA or structured RNA sequences produce unreliable scores; truncate the structured regions to single-stranded stretches before scoring.
- **Pre-computed predictions are only available for human and a few model organisms**: The web server has pre-computed predictions for >1400 human RRM proteins; non-human or non-model-organism proteins require a fresh prediction.
- **The overall score is a relative rank, not an absolute probability**: A score of 0.8 means the RRM is in the top 20% of RNA-binding RRMs; it does NOT mean a 0.8 probability of binding. Calibrate with the supplied benchmark data.

## Examples

### Score a single RRM sequence
**Args:** `rrmscorer predict --protein seq.fasta --out results.json`
**Explanation:** `predict` is the main subcommand; `--protein` is the input FASTA, `--out` is the output JSON. The output includes per-residue scores and an overall binding likelihood.

### Score with an explicit RNA
**Args:** `rrmscorer predict --protein seq.fasta --rna target_rna.fasta --out results.json`
**Explanation:** `--rna` supplies a specific RNA sequence. The prediction becomes RNA-specific (preferred bases per RRM position). More accurate than the RRM-only mode.

### Query a UniProt ID
**Args:** `rrmscorer uniprot --id P19339 --out results.json`
**Explanation:** `uniprot` uses the precomputed predictions for the given UniProt ID. Available for ~1400 human RBPs; returns the prediction immediately.

### Score a list of RRM sequences
**Args:** `rrmscorer batch --fasta rrms.fasta --out batch_results/`
**Explanation:** `batch` processes a multi-FASTA file of RRM sequences; output is one JSON per sequence in the `--out` directory. Multiprocessing is automatic.

### Generate a sequence logo
**Args:** `rrmscorer predict --protein seq.fasta --rna target_rna.fasta --logo logo.png --out results.json`
**Explanation:** `--logo` writes a sequence logo of preferred RNA bases per RRM position. Useful for visualizing the binding preferences.

### Compare two RRM domains
**Args:** `rrmscorer compare --rrm1 seq1.fasta --rrm2 seq2.fasta --out comparison.json`
**Explanation:** `compare` computes a similarity score between two RRM domains based on their binding preferences. Useful for clustering RRM domains in a proteome.

### Output a CSV
**Args:** `rrmscorer predict --protein seq.fasta --format csv --out results.csv`
**Explanation:** `--format csv` writes a CSV with one row per residue: `position, residue, score, preferred_base`. Easier to parse downstream with pandas.
