---
name: spectacle
category: epigenomics
description: Spectacle - Fast chromatin state annotation using spectral learning
tags: [spectacle, epigenomics, chromatin-state, hidden-markov-model, spectral-learning]
author: oxo-call-community
source_url: "https://github.com/jiminsong/Spectacle"
---

## Concepts

- **Tool Overview**: spectacle (v1.4) - A chromatin state annotation tool
- **Core Function**: Implements spectral learning for hidden Markov models on epigenomic data
- **Input/Output**: Accepts epigenomic data; outputs chromatin state annotations
- **Algorithm**: Spectral learning algorithm for HMMs
- **Installation**: `conda install -c bioconda spectacle`
- **Key Features**: Chromatin annotation, spectral learning, HMM modeling

## Pitfalls

- **Input Requirements**: Requires properly formatted epigenomic data
- **Model Parameters**: HMM parameters affect annotation quality
- **Spectral Learning**: Learning parameters affect model convergence
- **Memory Usage**: Large epigenomic datasets require significant memory
- **Output Format**: Output format depends on configuration
- **State Accuracy**: Annotation accuracy depends on data quality

## Examples

### Display help
**Args:** `spectacle --help`
**Explanation:** Shows available options and usage information.

### Basic chromatin annotation
**Args:** `spectacle -i epigenomic_data.bed -o chromatin_states.bed`
**Explanation:** Annotate chromatin states from epigenomic data.

### With model parameters
**Args:** `spectacle -i epigenomic_data.bed -o chromatin_states.bed --states 15`
**Explanation:** Set number of chromatin states.

### With spectral parameters
**Args:** `spectacle -i epigenomic_data.bed -o chromatin_states.bed --spectral-params params.txt`
**Explanation:** Use specific spectral learning parameters.

### With multiple marks
**Args:** `spectacle -i mark1.bed mark2.bed mark3.bed -o chromatin_states.bed`
**Explanation:** Use multiple epigenomic marks.

### Output detailed results
**Args:** `spectacle -i epigenomic_data.bed -o chromatin_states.bed --detailed`
**Explanation:** Output detailed state information.

### Output probabilities
**Args:** `spectacle -i epigenomic_data.bed -o chromatin_states.bed --probabilities`
**Explanation:** Output state probabilities.

### Output statistics
**Args:** `spectacle -i epigenomic_data.bed -o chromatin_states.bed --stats`
**Explanation:** Output annotation statistics.

### Generate report
**Args:** `spectacle -i epigenomic_data.bed -o chromatin_states.bed --report`
**Explanation:** Generate annotation report.