---
name: garnett-cli
category: expression
description: Command-line wrapper scripts for Garnett scRNA-seq cell type classification tool.
tags: [garnett-cli, scrna-seq, cell-type-classification, single-cell, bioconductor]
author: oxo-call-community
source_url: "https://github.com/ebi-gene-expression-group/garnett-cli"
---

## Concepts

- **Tool Overview**: Garnett-cli provides command-line wrapper scripts for the Garnett R package, enabling automated cell type classification from single-cell RNA-seq (scRNA-seq) data.
- **Core Function**: Uses marker gene files to train regression-based classifiers and classify cells into cell types automatically.
- **Classification Algorithm**: Elastic-net regression classifier trained on cell-type-specific marker genes. The classifier learns which genes define each cell type.
- **Input Data**: Single-cell expression matrices (10X Cell Ranger, Drop-seq, etc.) in Monocle3 CDS format, plus a marker file defining cell types.
- **Output**: Cell type classifications for each cell, with classification scores and optionally a trained classifier object.
- **Installation**: `conda install -c bioconda garnett-cli`
- **Dependencies**: r-garnett, monocle3-cli, bioconductor-org.hs.eg.db or org.mm.eg.db, r-glmnet
- **Wrapper Scripts**: Provides CLI access to garnett training and classification functions that are otherwise only available in R.
- **Species Support**: Human (org.Hs.eg.db), mouse (org.Mm.eg.db), and other organisms with Bioconductor annotation databases.

## Pitfalls

- **Marker File Format**: Must follow Garnett's specific hierarchical markup format. Incorrect format causes classifier training failures.
- **Species Database**: Requires matching organism annotation database (org.Hs.eg.db for human, org.Mm.eg.db for mouse). Missing database prevents initialization.
- **Monocle3 Object**: Input expression data must be properly formatted as a Monocle3 CellDataSet object. Improper formatting causes errors.
- **Classifier Version**: Pre-trained classifiers are version-specific. Using an outdated classifier may not match current Garnett version.
- **Memory Requirements**: Large single-cell datasets ( >100K cells) require significant RAM for classification. Consider subsampling for initial tests.
- **Training Data Quality**: Classifier accuracy depends on quality of marker genes. Poor markers lead to misclassification.
- **Windows Compatibility**: As an R/Bioconductor wrapper, requires Linux/macOS or Windows Subsystem for Linux (WSL).

## Examples

### Check garnett-cli help
**Args:** `garnett-cli --help`
**Explanation:** Displays available commands and usage information for the garnett-cli wrapper scripts.

### Train a classifier
**Args:** `train_garnett_classifier.R --cds input_cds.rds --marker markers.txt --output classifier.RDS`
**Explanation:** Trains a Garnett classifier using expression data and marker gene file, saves trained model.

### Classify cells
**Args:** `classify_cells.R --cds new_data.rds --classifier classifier.RDS --output classified.RDS`
**Explanation:** Applies a trained classifier to new single-cell data to assign cell types.

### Validate marker genes
**Args:** `check_markers.R --cds data.rds --markers markers.txt --organism hs`
**Explanation:** Validates that marker genes are appropriately expressed in the dataset before training.

### Install with conda
**Args:** `conda install -c bioconda garnett-cli`
**Explanation:** Installs garnett-cli and all dependencies via Bioconda package manager.

### Process 10X data
**Args:** `monocle3-cli import 10x --matrix matrix.mtx --genes genes.tsv --barcodes barcodes.tsv --output cds.rds`
**Explanation:** Converts 10X Cell Ranger output into Monocle3 CDS format for use with garnett-cli.
