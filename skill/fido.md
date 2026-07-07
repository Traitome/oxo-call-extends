---
name: fido
category: proteomics
description: "A Bayesian protein identification engine for MS/MS proteomics that uses a probabilistic model to rank protein matches by posterior probability."
tags: [fido, proteomics, protein-identification, MS/MS, Bayesian-inference, mass-spectrometry, bioinformatics]
author: oxo-call-community
source_url: "https://noble.gs.washington.edu/proj/fido"
---

## Concepts

- **Tool Overview**: Fido is a Bayesian protein identification engine for MS/MS proteomics. It takes scored peptide-spectrum matches (PSMs) and returns proteins ranked by posterior probability using probabilistic inference.
- **Core Function**: Implements a Bayesian probabilistic model to perform protein group inference from peptide-spectrum matches, accounting for peptide uniqueness and shared peptides.
- **Input/Output**: Input: PSM graph file (format: `e peptide_string r protein1 r protein2 ... p probability`), optional target/decoy file. Output: Proteins ranked by posterior probability.
- **Algorithm**: Uses graphical model inference to compute marginal posterior probabilities for proteins. The model considers peptide emission probabilities, protein prior probabilities, and spurious identification rates.
- **Key Features**: Bayesian inference, protein group inference, handles shared peptides, supports target-decoy estimation, parameter auto-tuning via FidoChooseParameters.
- **Installation**: `conda install -c bioconda fido` or `pixi global install fido`
- **Note**: This standalone version is no longer maintained. Fido has been integrated into [Percolator](http://per-colator.com/) and the [Crux toolkit](http://cruxtoolkit.sourceforge.net/).

## Pitfalls

- **Deprecated Tool**: The standalone Fido version is no longer maintained. For new projects, use Percolator or Crux which include updated Fido functionality.
- **Input Format Complexity**: Requires specific PSM graph format from PeptideProphet or similar tools. Direct use of other search engine outputs requires format conversion.
- **Parameter Sensitivity**: Results are sensitive to gamma (protein prior), alpha (peptide emission), and beta (spurious identification) parameters. Use FidoChooseParameters for calibration.
- **Computational Intensity**: Large protein groups with many shared peptides can make exact inference intractable; the log2_maximum_number_of_states parameter trades speed for accuracy.
- **PepXML Namespace Issues**: When reformatting PepXML using XSLT, namespace-related problems may occur that require manual intervention.

## Examples

### Automatic parameter selection
**Args:** `FidoChooseParameters -g psm_graph_file targetDecoy.txt`
**Explanation:** Automatically selects optimal gamma, alpha, and beta parameters using the PSM graph file and target/decoy accessions. The -g flag enables protein group-level inference.

### Basic protein inference
**Args:** `Fido psm_graph_file 0.5 0.1 0.01`
**Explanation:** Runs protein inference with gamma=0.5 (protein prior), alpha=0.1 (peptide emission), beta=0.01 (spurious identification). These are reasonable defaults but should be tuned for specific datasets.

### High-accuracy inference
**Args:** `Fido psm_graph_file 0.5 0.1 0.01 10`
**Explanation:** Runs inference with log2_maximum_number_of_states=10, ensuring every connected subgraph takes up to 1024 steps for marginalization. Slower but more accurate.

### Fast inference with approximation
**Args:** `FidoChooseParameters -g -c 3 psm_graph_file targetDecoy.txt`
**Explanation:** Uses accuracy level 3 (sloppy/fastest) for parameter selection. Use when processing large datasets where speed matters more than precision.

### Using all PSM matches
**Args:** `Fido -a psm_graph_file 0.5 0.1 0.01`
**Explanation:** Uses all PSM matches instead of just the best one per spectrum (enabled by -a flag). More computationally intensive but can improve recall.
