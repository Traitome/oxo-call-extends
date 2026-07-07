---
name: spectra-cluster-cli
category: metabolomics
description: Spectra Cluster CLI - PRIDE Cluster algorithm for mass spectrometry data
tags: [spectra-cluster-cli, metabolomics, mass-spectrometry, clustering, pride]
author: oxo-call-community
source_url: "https://github.com/spectra-cluster/spectra-cluster-cli"
---

## Concepts

- **Tool Overview**: spectra-cluster-cli (v1.1.2) - A mass spectrometry clustering tool
- **Core Function**: Implements PRIDE Cluster algorithm for MS spectra clustering
- **Input/Output**: Accepts MS spectra; outputs clustered spectra
- **Algorithm**: PRIDE Cluster algorithm for similarity-based clustering
- **Installation**: `conda install -c bioconda spectra-cluster-cli`
- **Key Features**: MS clustering, PRIDE algorithm, similarity-based

## Pitfalls

- **Input Requirements**: Requires properly formatted MS spectra
- **Spectra Quality**: Spectra quality affects clustering accuracy
- **Similarity Threshold**: Threshold affects cluster formation
- **Memory Usage**: Large spectral datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Cluster Quality**: Cluster quality depends on similarity measure

## Examples

### Display help
**Args:** `spectra-cluster-cli --help`
**Explanation:** Shows available options and usage information.

### Basic clustering
**Args:** `spectra-cluster-cli -i spectra.mgf -o clusters.mgf`
**Explanation:** Cluster MS spectra using PRIDE algorithm.

### With similarity threshold
**Args:** `spectra-cluster-cli -i spectra.mgf -o clusters.mgf --threshold 0.7`
**Explanation:** Set similarity threshold for clustering.

### With clustering method
**Args:** `spectra-cluster-cli -i spectra.mgf -o clusters.mgf --method average`
**Explanation:** Use specific clustering method.

### Output detailed results
**Args:** `spectra-cluster-cli -i spectra.mgf -o clusters.mgf --detailed`
**Explanation:** Output detailed cluster information.

### Output cluster representatives
**Args:** `spectra-cluster-cli -i spectra.mgf -o clusters.mgf --representatives`
**Explanation:** Output cluster representatives.

### Output statistics
**Args:** `spectra-cluster-cli -i spectra.mgf -o clusters.mgf --stats`
**Explanation:** Output clustering statistics.

### Generate report
**Args:** `spectra-cluster-cli -i spectra.mgf -o clusters.mgf --report`
**Explanation:** Generate clustering report.

### With threads
**Args:** `spectra-cluster-cli -i spectra.mgf -o clusters.mgf -p 8`
**Explanation:** Use multiple threads for clustering.