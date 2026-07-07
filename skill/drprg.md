---
name: drprg
category: annotation
description: "Drug resistance prediction with reference graphs"
tags: [drprg, annotation, drug-resistance, antimicrobial, variant-graph]
author: oxo-call-community
source_url: "https://github.com/mbhall88/drprg"
---

## Concepts

- **Tool Overview**: DRPRG is a tool for predicting drug resistance using reference graphs, enabling accurate variant calling in repetitive regions.
- **Core Function**: Uses pangenome reference graphs to improve variant detection and drug resistance prediction.
- **Input/Output**: Input: Sequencing reads (FASTQ), reference graph. Output: Drug resistance predictions, variant calls.
- **Algorithm**: Leverages graph-based genome representation to resolve complex genomic regions.
- **Key Features**: Graph-based variant calling, drug resistance database integration, support for multiple pathogens.
- **Installation**: `conda install -c bioconda drprg`

## Pitfalls

- **Graph Quality**: Reference graph quality affects variant calling accuracy.
- **Sequencing Depth**: Low coverage may reduce sensitivity for rare variants.
- **Database Updates**: Drug resistance databases require regular updates.
- **Complex Variants**: Structural variants may be challenging to detect.
- **False Positives**: Highly polymorphic regions can produce false positive calls.

## Examples

### Basic resistance prediction
**Args:** `--reads sample.fastq --graph ref.gfa --output results/`
**Explanation:** Predicts drug resistance from sequencing reads using reference graph.

### With custom database
**Args:** `--reads sample.fastq --graph ref.gfa --db resistance_db.tsv --output results/`
**Explanation:** Uses custom drug resistance database for prediction.

### Specific drugs
**Args:** `--reads sample.fastq --graph ref.gfa --drugs isoniazid rifampicin --output results/`
**Explanation:** Predicts resistance for specific drugs only.

### Generate report
**Args:** `--reads sample.fastq --graph ref.gfa --output results/ --report report.html`
**Explanation:** Generates HTML report with resistance predictions.

### Batch processing
**Args:** `--reads-dir samples/ --graph ref.gfa --output results/ --batch`
**Explanation:** Processes multiple samples in batch mode.