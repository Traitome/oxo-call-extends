---
name: maxentscan
category: expression
description: Maximum Entropy model for predicting RNA splicing sites and sequence motifs.
tags: [maxentscan, splicing, motif-analysis]
author: oxo-call-community
source_url: "http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html"
---

## Concepts

- **Tool Overview**: MaxEntScan predicts RNA splicing sites using maximum entropy models.
- **Core Function**: Scores splice acceptor and donor sites.
- **Maximum Entropy**: Uses MaxEnt principle for motif modeling.
- **Position Dependencies**: Accounts for non-adjacent position dependencies.
- **Input/Output**: Accepts FASTA sequences, produces splice site scores.
- **Installation**: `conda install -c bioconda maxentscan`

## Pitfalls

- **Sequence Context**: Requires proper sequence context around splice sites.
- **Model Limitations**: Trained on specific organisms/data types.
- **Score Interpretation**: Scores require careful interpretation.
- **Alternative Splicing**: May not capture all alternative splicing events.
- **Memory Requirements**: Processing large sequences may require memory.
- **Output Format**: May need parsing for downstream analysis.

## Examples

### Score splice donor sites
**Args:** `score5.pl sequences.fasta`
**Explanation:** Scores potential 5' splice donor sites.

### Score splice acceptor sites
**Args:** `score3.pl sequences.fasta`
**Explanation:** Scores potential 3' splice acceptor sites.

### Output detailed results
**Args:** `score5.pl -d sequences.fasta`
**Explanation:** Shows detailed scoring information.

### Batch processing
**Args:** `score5.pl *.fasta`
**Explanation:** Processes multiple FASTA files.

### Custom model
**Args:** `score5.pl -m custom_model.mod sequences.fasta`
**Explanation:** Uses custom scoring model.

### Help documentation
**Args:** `score5.pl -h`
**Explanation:** Displays available options.
