---
name: spydrpick
category: comparative-genomics
description: SpydrPick - Mutual information based detection of co-evolving genomic loci
tags: [spydrpick, comparative-genomics, co-evolution, mutual-information, genomics]
author: oxo-call-community
source_url: "https://github.com/santeripuranen/SpydrPick"
---

## Concepts

- **Tool Overview**: spydrpick (v1.2.0) - A co-evolution detection tool
- **Core Function**: Detects pairs of genomic loci co-evolving under shared selective pressure
- **Input/Output**: Accepts genomic alignments; outputs co-evolution pairs
- **Algorithm**: Mutual information-based co-evolution detection
- **Installation**: `conda install -c bioconda spydrpick`
- **Key Features**: Co-evolution detection, mutual information, genomic loci

## Pitfalls

- **Input Requirements**: Requires properly formatted genomic alignments
- **Alignment Quality**: Alignment quality affects co-evolution detection
- **Mutual Information**: MI calculation depends on data characteristics
- **Memory Usage**: Large alignments require significant memory
- **Output Format**: Output format depends on configuration
- **Detection Accuracy**: Accuracy depends on alignment quality and MI threshold

## Examples

### Display help
**Args:** `spydrpick --help`
**Explanation:** Shows available options and usage information.

### Basic co-evolution detection
**Args:** `spydrpick -i alignments.fasta -o coevolution_pairs.txt`
**Explanation:** Detect co-evolving genomic loci pairs.

### With MI threshold
**Args:** `spydrpick -i alignments.fasta -o coevolution_pairs.txt --mi-threshold 0.5`
**Explanation:** Set mutual information threshold.

### With window size
**Args:** `spydrpick -i alignments.fasta -o coevolution_pairs.txt --window 100`
**Explanation:** Set window size for co-evolution analysis.

### Multiple alignments
**Args:** `spydrpick -i align1.fasta align2.fasta -o coevolution_pairs.txt`
**Explanation:** Analyze multiple alignment files.

### Output detailed results
**Args:** `spydrpick -i alignments.fasta -o coevolution_pairs.txt --detailed`
**Explanation:** Output detailed co-evolution information.

### Output MI values
**Args:** `spydrpick -i alignments.fasta -o coevolution_pairs.txt --mi-values`
**Explanation:** Output mutual information values.

### Output statistics
**Args:** `spydrpick -i alignments.fasta -o coevolution_pairs.txt --stats`
**Explanation:** Output detection statistics.

### Generate report
**Args:** `spydrpick -i alignments.fasta -o coevolution_pairs.txt --report`
**Explanation:** Generate co-evolution detection report.

### With threads
**Args:** `spydrpick -i alignments.fasta -o coevolution_pairs.txt -p 8`
**Explanation:** Use multiple threads for detection.