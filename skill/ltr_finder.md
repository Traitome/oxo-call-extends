---
name: ltr_finder
category: utility
description: LTR_Finder is an efficient program for finding full-length LTR retrotransposons in genome sequences.
tags: [ltr_finder, utility, LTR, retrotransposons]
author: oxo-call-community
source_url: "https://github.com/NBISweden/LTR_Finder"
---

## Concepts

- **Tool Overview**: ltr_finder v1.07 is an efficient program for identifying full-length LTR retrotransposons in genome sequences.
- **Core Function**: Detects LTR retrotransposons by identifying long terminal repeats and characteristic structural features.
- **LTR Structure**: Identifies features like LTR boundaries, target site duplications (TSDs), and primer binding sites (PBS).
- **Input/Output**: Input: FASTA genome sequence; Output: GFF file with LTR retrotransposon annotations.
- **Installation**: `conda install -c bioconda ltr_finder`
- **Key Features**: High sensitivity and specificity, supports multiple organisms, outputs standard GFF format.

## Pitfalls

- **False Positives**: May identify non-LTR sequences as LTRs, requiring manual curation.
- **Genome Complexity**: Performance may vary with highly repetitive genomes.
- **Memory Usage**: Processing large genomes may require significant memory.
- **Computation Time**: Can be slow for very large genome sequences.
- **Parameter Tuning**: May require adjustment of sensitivity thresholds for different organisms.
- **Assembly Quality**: Depends on genome assembly quality; fragmented assemblies may miss complete LTRs.

## Examples

### Find LTRs in genome
**Args:** `ltr_finder genome.fasta -o ltr_results.gff`
**Explanation:** Identifies LTR retrotransposons in genome sequence.

### With TSD detection
**Args:** `ltr_finder -D genome.fasta -o ltr_results.gff`
**Explanation:** Enables target site duplication (TSD) detection.

### Minimum LTR length
**Args:** `ltr_finder -L 100 genome.fasta -o ltr_results.gff`
**Explanation:** Sets minimum LTR length to 100bp.

### Threads
**Args:** `ltr_finder -t 4 genome.fasta -o ltr_results.gff`
**Explanation:** Uses 4 threads for parallel processing.

### Verbose output
**Args:** `ltr_finder -v genome.fasta -o ltr_results.gff`
**Explanation:** Outputs detailed information during processing.

### Help documentation
**Args:** `ltr_finder --help`
**Explanation:** Displays all available options and parameters.