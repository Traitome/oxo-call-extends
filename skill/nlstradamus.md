---
name: nlstradamus
category: prediction
description: NLStradamus predicts nuclear localization signals using Hidden Markov Models.
tags: [nlstradamus, prediction, nuclear-localization, hmm]
author: oxo-call-community
source_url: "http://www.moseslab.csb.utoronto.ca/NLStradamus/"
---

## Concepts

- **Tool Overview**: NLStradamus predicts nuclear localization signals in protein sequences.
- **Core Function**: Identifies NLS motifs for protein subcellular localization prediction.
- **Algorithm**: Uses Hidden Markov Model for pattern recognition.
- **Input Format**: Accepts FASTA protein sequences.
- **Output**: Produces NLS predictions with confidence scores.
- **Use Case**: Proteomics analysis, protein localization prediction, and bioinformatics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Sequence Quality**: Results depend on input sequence quality.
- **False Positives**: May predict false positives.
- **Specificity**: Optimized for specific NLS types.
- **Parameter Tuning**: Requires careful threshold setting.
- **Validation**: Results should be experimentally validated.

## Examples

### Display help
**Args:** `nlstradamus --help`
**Explanation:** Shows available options and usage instructions.

### Predict NLS
**Args:** `nlstradamus -i proteins.fasta -o predictions.txt`
**Explanation:** Predicts NLS in protein sequences.

### Output detailed
**Args:** `nlstradamus -i proteins.fasta -o predictions.txt -d`
**Explanation:** Outputs detailed prediction information.

### Threshold setting
**Args:** `nlstradamus -i proteins.fasta -o predictions.txt -t 0.8`
**Explanation:** Sets prediction threshold to 0.8.

### Batch processing
**Args:** `nlstradamus -d fasta_files/ -o predictions/`
**Explanation:** Processes multiple FASTA files.

### Output XML
**Args:** `nlstradamus -i proteins.fasta -o predictions.xml --xml`
**Explanation:** Outputs results in XML format.

### Verbose mode
**Args:** `nlstradamus -i proteins.fasta -o predictions.txt -v`
**Explanation:** Runs with verbose output.