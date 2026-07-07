---
name: taxmyphage
category: virology
description: Assigns taxonomy to bacteriophages at genus and species level.
tags: [taxmyphage, bacteriophage, taxonomy, virus]
author: oxo-call-community
source_url: "https://github.com/amillard/tax_myPHAGE"
---

## Concepts

- **Tool Overview**: taxmyphage (v0.3.7) classifies bacteriophage sequences.
- **Core Function**: Assigns taxonomy to phage sequences.
- **Algorithm**: Uses sequence similarity and database matching.
- **Input/Output**: Input: Phage sequences; Output: Taxonomic assignments.
- **Applications**: Bacteriophage annotation, phage research.
- **Installation**: `conda install -c bioconda taxmyphage` or download from GitHub.

## Pitfalls

- **Phage Specificity**: Only works for bacteriophages.
- **Database Coverage**: Limited by phage database.
- **Sequence Quality**: Poor sequences may be misclassified.
- **Novel Phages**: Novel phages may not be classified.
- **Computational Time**: Large datasets process slowly.
- **Memory Usage**: Database requires memory.

## Examples

### Display help
**Args:** `taxmyphage --help`
**Explanation:** Shows available options and usage information.

### Basic classification
**Args:** `taxmyphage -i phage_sequences.fasta -o classification.txt`
**Explanation:** Classify phage sequences.

### With database
**Args:** `taxmyphage -i phage_sequences.fasta -d phage_db/ -o classification.txt`
**Explanation:** Use custom phage database.

### Verbose mode
**Args:** `taxmyphage -i phage_sequences.fasta -o classification.txt -v`
**Explanation:** Run with detailed logging.

### Output statistics
**Args:** `taxmyphage -i phage_sequences.fasta -o classification.txt --stats`
**Explanation:** Generate classification statistics.

### Batch processing
**Args:** `for f in phages/*.fasta; do taxmyphage -i $f -o results/${f%.fasta}_class.txt; done`
**Explanation:** Process multiple phage files.

### Confidence threshold
**Args:** `taxmyphage -i phage_sequences.fasta -o classification.txt -c 0.9`
**Explanation:** Minimum confidence of 0.9.

### Generate report
**Args:** `taxmyphage -i phage_sequences.fasta -o classification.txt --report`
**Explanation:** Generate comprehensive report.

### Export to CSV
**Args:** `taxmyphage -i phage_sequences.fasta -o classification.csv -f csv`
**Explanation:** Export to CSV format.
