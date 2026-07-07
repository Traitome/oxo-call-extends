---
name: mlst-cge
category: assembly
description: Multi Locus Sequence Typing (MLST) determine the ST from an assembled genome or from a set of reads.
tags: [mlst-cge, assembly, mlst]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/mlst"
---

## Concepts

- **Tool Overview**: MLST-CGE v2.0.9 performs Multi Locus Sequence Typing from genomes or reads.
- **Core Function**: Determines sequence type (ST) from assembled genomes or sequencing reads.
- **MLST Analysis**: Identifies sequence types based on housekeeping gene alleles.
- **CGE Implementation**: Developed by the Center for Genomic Epidemiology.
- **Input/Output**: Accepts genomes or reads; outputs MLST types.
- **Bacterial Typing**: Supports bacterial strain identification.

## Pitfalls

- **Bacterial Specific**: Designed for bacterial MLST analysis.
- **Computational Resources**: Processing may require significant resources.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for optimal typing.
- **Data Quality**: Results depend on input sequence quality.
- **Scheme Availability**: Requires appropriate MLST scheme.

## Examples

### Determine ST from genome
**Args:** `mlst-cge genome.fasta -o result.txt`
**Explanation:** Determines sequence type from assembled genome.

### From reads
**Args:** `mlst-cge --reads reads.fastq -o result.txt`
**Explanation:** Determines sequence type directly from reads.

### Verbose output
**Args:** `mlst-cge genome.fasta -o result.txt -v`
**Explanation:** Shows detailed typing results.

### Custom scheme
**Args:** `mlst-cge genome.fasta -s scheme.def -o result.txt`
**Explanation:** Uses custom MLST scheme.

### Batch processing
**Args:** `mlst-cge --input fasta/ --output results/`
**Explanation:** Processes multiple genome files.