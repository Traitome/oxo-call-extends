---
name: taxator-tk
category: taxonomy
description: Sequence taxonomic annotation tool.
tags: [taxator-tk, taxonomy, annotation, metagenomics]
author: oxo-call-community
source_url: "https://github.com/fungs/taxator-tk"
---

## Concepts

- **Tool Overview**: taxator-tk (v1.3.3e) annotates sequences with taxonomy.
- **Core Function**: Assigns taxonomic labels to sequences.
- **Algorithm**: Uses k-mer and alignment-based classification.
- **Input/Output**: Input: FASTA/FASTQ; Output: Annotated sequences.
- **Applications**: Metagenomics, taxonomic profiling, sequence annotation.
- **Installation**: `conda install -c bioconda taxator-tk` or download from GitHub.

## Pitfalls

- **Database Quality**: Classification depends on reference database.
- **Sequence Length**: Short sequences may be misclassified.
- **Computational Time**: Large datasets process slowly.
- **Memory Usage**: Large databases require memory.
- **Ambiguous Classification**: May assign incorrect taxonomy.
- **Database Updates**: Requires updated reference databases.

## Examples

### Display help
**Args:** `taxator-tk --help`
**Explanation:** Shows available options and usage information.

### Basic annotation
**Args:** `taxator-tk -i sequences.fasta -d database/ -o annotated.fasta`
**Explanation:** Annotate sequences with taxonomy.

### With confidence
**Args:** `taxator-tk -i sequences.fasta -d database/ -o annotated.fasta -c 0.8`
**Explanation:** Minimum confidence threshold.

### Verbose mode
**Args:** `taxator-tk -i sequences.fasta -d database/ -o annotated.fasta -v`
**Explanation:** Run with detailed logging.

### Output statistics
**Args:** `taxator-tk -i sequences.fasta -d database/ -o annotated.fasta --stats`
**Explanation:** Generate statistics.

### Batch processing
**Args:** `for f in fasta/*.fasta; do taxator-tk -i $f -d database/ -o out/${f%.fasta}_ann.fasta; done`
**Explanation:** Process multiple files.

### Generate report
**Args:** `taxator-tk -i sequences.fasta -d database/ -o annotated.fasta --report`
**Explanation:** Generate comprehensive report.

### Export to CSV
**Args:** `taxator-tk -i sequences.fasta -d database/ -o annotations.csv -f csv`
**Explanation:** Export annotations to CSV.

### Include lineage
**Args:** `taxator-tk -i sequences.fasta -d database/ -o annotated.fasta --lineage`
**Explanation:** Include full taxonomic lineage.
