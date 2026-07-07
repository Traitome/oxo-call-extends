---
name: flagx
category: utility
description: "FLAG-X is an automated gating toolbox for flow cytometry data analysis, providing machine learning-based cell population identification."
tags: [flagx, utility, flow-cytometry, gating, automated, bioinformatics, cell-analysis]
author: oxo-call-community
source_url: "https://github.com/bionetslab/FLAG-X"
---

## Concepts
- **Tool Overview**: FLAG-X (FLow cytometry Automated Gating toolboX) is a machine learning-based automated gating tool for flow cytometry data analysis. It uses supervised learning to identify cell populations without manual gating.
- **Core Function**: Automated identification and quantification of cell populations in flow cytometry data using machine learning models.
- **Input/Output**: Input: FCS 2.0/3.0 flow cytometry files. Output: Gating results, population statistics, visualization plots.
- **ML Models**: Supports multiple machine learning algorithms including Random Forest, XGBoost, and neural networks for population classification.
- **Training Mode**: Can train custom models on manually gated datasets for improved performance on specific experimental setups.
- **Batch Processing**: Supports batch processing of multiple FCS files with parallel computation for large experiments.
- **Installation**: `conda install -c bioconda flagx` or `pip install flagx`. Requires Python 3.7+, scikit-learn, flowio, numpy.

## Pitfalls
- **Training Data Quality**: Model performance depends heavily on quality of training data. Poorly gated training sets produce inaccurate results.
- **Marker Panel Compatibility**: Models trained on one marker panel may not generalize to different staining panels.
- **FCS File Format**: Older FCS 2.0 files may have compatibility issues. Convert to FCS 3.0 format if encountering errors.
- **Normalization Requirements**: Data should be normalized before analysis. Non-normalized data may produce incorrect population boundaries.
- **Cell Viability Gates**: FLAG-X does not automatically apply viability gates. Pre-process data to remove dead cells.
- **Class Imbalance**: Uneven population sizes in training data can bias model towards majority populations.

## Examples
### Basic automated gating
**Args:** `flagx --input sample.fcs --output results/ --model default`
**Explanation:** Runs FLAG-X with default pre-trained model on a single FCS file, producing automated gating results.

### Batch processing multiple files
**Args:** `flagx --input-dir fcs_files/ --output results/ --model default`
**Explanation:** Processes all FCS files in input directory using parallel computation for efficiency.

### Train custom model
**Args:** `flagx --train --input training_data/ --output-model custom_model.pkl`
**Explanation:** Trains a custom Random Forest model on manually gated training data for improved performance on specific datasets.

### Use custom model for gating
**Args:** `flagx --input sample.fcs --output results/ --model custom_model.pkl`
**Explanation:** Uses a previously trained custom model for automated gating instead of the default model.

### Generate visualization
**Args:** `flagx --input sample.fcs --output results/ --visualize --dimensions FSC-A,SSC-A,CD45,CD3`
**Explanation:** Generates scatter plots and density plots for specified marker dimensions to visualize gating results.
