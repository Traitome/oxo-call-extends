---
name: rs3
category: utility
description: Rule Set 3 (RS3) — Python package for predicting the on-target activity of CRISPR sgRNA sequences using sequence-only and target-site features, with LightGBM models.
tags: ["rs3", "rule-set-3", "crispr", "sgrna", "on-target", "activity-prediction", "lightgbm", "genome-editing"]
author: oxo-call-community
source_url: "https://github.com/gpp-rnd/rs3"
---

## Concepts

- **Tool Overview**: RS3 (Rule Set 3, v0.0.18, gpp-rnd / DeWeirdt et al. 2022) is a Python package for predicting the on-target activity of CRISPR sgRNA sequences. It provides two models: a sequence-only model (trained on the 30mer context sequence + tracrRNA) and a target-site model (which adds features from the endogenous target site: amino acid sequence, conservation, protein domains).
- **Core Function**: Takes a list of sgRNA 30mer context sequences (or a design table with target site annotations) and predicts the on-target activity score. The sequence-only model returns a per-sgRNA score in arbitrary units (typically -1 to +2). The target-site model uses additional features (amino acid composition around the cut site, protein domain features, conservation scores) to refine the prediction.
- **Algorithm**: (1) Compute sequence-based features (GC content, position-specific nucleotides, dinucleotides) from the 30mer context + tracrRNA; (2) for the target-site model, compute target features (amino acid subsequence, conservation, protein domain annotation); (3) feed the features into a LightGBM model trained on large-scale sgRNA activity screens (e.g., Brunello, GeckoV2); (4) return the predicted activity score.
- **Input Format**: (1) A list of 30mer context sequences (Python list of strings, or a TSV column), or (2) a design DataFrame with the columns `sgRNA Context Sequence, Target Cut Length, Target Transcript, Orientation, Target Cut %`. The target features require a transcript amino-acid sequence (downloaded from Ensembl via `build_transcript_aa_seq_df`).
- **Output Format**: A numpy array of per-sgRNA activity scores. For the target-site model, a DataFrame with one row per sgRNA and columns `sequence, predicted_activity`. The scores are typically in the range -1 to +2 (higher = more active).
- **Use Case**: Ranking sgRNAs in a CRISPRko library by predicted activity (canonical use case), prioritizing sgRNAs for arrayed validation, comparing the predicted activity of sgRNAs targeting different exons/domains of a gene, and selecting sgRNAs for in vivo CRISPR screens.

## Pitfalls

- **CRITICAL — The 30mer context must be in the 5'→3' direction of the PROTOSPACER, not the PAM-proximal end**: The convention is: 4 nt 5' flank + 20 nt protospacer + 3 nt PAM + 3 nt 3' flank. Reverse-complementing the entire 30mer produces a different (worse) prediction.
- **CRITICAL — Two tracrRNA conventions are supported (Hsu2013, Chen2013)**: The Hsu2013 tracrRNA has a T in the 5th position; the Chen2013 does not. RS3 recommends Chen2013 for tracrRNAs without a 5th-position T. Mixing tracrRNAs within a library is a common error.
- **The LightGBM model requires OpenMP**: On macOS, install libomp (`brew install libomp`) or install LightGBM without OpenMP (`pip install lightgbm --install-option=--nomp`). Without this, the model crashes on import.
- **The target-site model requires precomputed transcript data**: The amino-acid sequences, conservation scores, and protein domains must be downloaded from Ensembl/UniProt/COSMIC before scoring. This is a one-time setup per organism; see `write_transcript_data` in the docs.
- **The sequence-only model is fast (~1 ms per sgRNA); the target-site model is slow (minutes per 1000 sgRNAs)**: Plan accordingly. For libraries >10k sgRNAs, use the sequence-only model for an initial rank and refine with the target-site model for the top candidates.
- **The scores are NOT probabilities**: A score of 2.0 does not mean a 2x probability of activity. The scores are in arbitrary units, calibrated to a Brunello-screen-like training set. Compare within a screen; do not compare across screens.
- **The default Python is 3.7+; the package is in alpha (v0.0.18)**: API may change. Pin the version in production: `pip install rs3==0.0.18`.

## Examples

### Sequence-only prediction
**Args:** `python -c "from rs3.seq import predict_seq; print(predict_seq(['GACGAAAGCGACAACGCGTTCATCCGGGCA','AGAAAACACTAGCATCCCCACCCGCGGACT'], sequence_tracr='Hsu2013'))"`
**Explanation:** `predict_seq` is the sequence-only entry point. The list contains two 30mer context sequences; `sequence_tracr='Hsu2013'` selects the tracrRNA model. Returns a numpy array of predicted activity scores.

### Target-site prediction
**Args:** `python -c "import pandas as pd; from rs3.predicttarg import predict_target; df=pd.read_table('sgrna-designs.txt'); print(predict_target(df))"`
**Explanation:** `predict_target` is the target-site entry point. The DataFrame must contain the columns `sgRNA Context Sequence, Target Cut Length, Target Transcript, Orientation`. Returns a DataFrame with per-sgRNA target scores.

### Specify the Chen2013 tracrRNA
**Args:** `python -c "from rs3.seq import predict_seq; predict_seq(['GACGAAAGCGACAACGCGTTCATCCGGGCA'], sequence_tracr='Chen2013')"`
**Explanation:** `sequence_tracr='Chen2013'` switches the tracrRNA. Use this for tracrRNAs that do not have a T in the 5th position.

### Compute target features
**Args:** `python -c "import pandas as pd; from rs3.targetfeat import add_target_columns; df=pd.read_table('sgrna-designs.txt'); print(add_target_columns(df).head())"`
**Explanation:** `add_target_columns` adds the `AA Index` and `Transcript Base` columns to the design DataFrame, which are required for the target-site model. The transcript base is the Ensembl ID without the version.

### Build the transcript amino-acid sequence
**Args:** `python -c "from rs3.targetdata import build_transcript_aa_seq_df; df=build_transcript_aa_seq_df(transcript_ids=['ENST00000259457']); print(df.head())"`
**Explanation:** `build_transcript_aa_seq_df` downloads the amino-acid sequence from Ensembl. Required for the target-site model. Slow (one-time setup per organism).

### Install on macOS with OpenMP
**Args:** `brew install libomp && pip install rs3`
**Explanation:** LightGBM (a dependency of RS3) requires OpenMP on macOS. Without libomp, the import fails.

### Install LightGBM without OpenMP (alternative on macOS)
**Args:** `pip install lightgbm --install-option=--nomp && pip install rs3`
**Explanation:** Alternative to installing libomp. Slower than the OpenMP version but works without homebrew.
