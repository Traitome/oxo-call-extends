---
name: spestimator
category: microbiology
description: Spestimator - Bacterial species prediction from 16S sequences
tags: [spestimator, microbiology, species-prediction, 16s, refseq]
author: oxo-call-community
source_url: "https://github.com/erinyoung/Spestimator"
---

## Concepts

- **Tool Overview**: spestimator (v0.3.0.234) - A bacterial species prediction tool
- **Core Function**: Predicts bacterial species from 16S sequences using RefSeq database
- **Input/Output**: Accepts 16S sequences; outputs species predictions
- **Algorithm**: Sequence alignment and database matching
- **Installation**: `conda install -c bioconda spestimator`
- **Key Features**: Species prediction, 16S analysis, RefSeq database

## Pitfalls

- **Input Requirements**: Requires properly formatted 16S sequences
- **Sequence Quality**: Sequence quality affects prediction accuracy
- **Database Coverage**: Database coverage affects prediction completeness
- **Memory Usage**: Large sequence sets require significant memory
- **Output Format**: Output format depends on configuration
- **Prediction Accuracy**: Accuracy depends on sequence quality and database

## Examples

### Display help
**Args:** `spestimator --help`
**Explanation:** Shows available options and usage information.

### Basic species prediction
**Args:** `spestimator -i 16s_sequences.fasta -o species_predictions.tsv`
**Explanation:** Predict bacterial species from 16S sequences.

### With database
**Args:** `spestimator -i 16s_sequences.fasta -d refseq_db/ -o species_predictions.tsv`
**Explanation:** Use specific RefSeq database.

### Multiple sequences
**Args:** `spestimator -i seq1.fasta seq2.fasta -o species_predictions.tsv`
**Explanation:** Predict species for multiple sequences.

### With confidence threshold
**Args:** `spestimator -i 16s_sequences.fasta -o species_predictions.tsv --confidence 0.9`
**Explanation:** Set confidence threshold for predictions.

### Output detailed results
**Args:** `spestimator -i 16s_sequences.fasta -o species_predictions.tsv --detailed`
**Explanation:** Output detailed prediction information.

### Output alignments
**Args:** `spestimator -i 16s_sequences.fasta -o species_predictions.tsv --alignments`
**Explanation:** Output sequence alignments.

### Output statistics
**Args:** `spestimator -i 16s_sequences.fasta -o species_predictions.tsv --stats`
**Explanation:** Output prediction statistics.

### Generate report
**Args:** `spestimator -i 16s_sequences.fasta -o species_predictions.tsv --report`
**Explanation:** Generate prediction report.

### With threads
**Args:** `spestimator -i 16s_sequences.fasta -o species_predictions.tsv -p 8`
**Explanation:** Use multiple threads for prediction.