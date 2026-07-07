---
name: methyldackel
category: epigenomics
description: A (mostly) universal methylation extractor for BS-seq experiments. Formerly named PileOMeth.
tags: [methyldackel, epigenomics, methylation]
author: oxo-call-community
source_url: "https://github.com/dpryan79/MethylDackel"
---

## Concepts

- **Tool Overview**: MethylDackel v0.6.1 is a universal methylation extractor for bisulfite sequencing experiments, formerly known as PileOMeth.
- **Core Function**: Extracts methylation information from aligned bisulfite sequencing reads.
- **Universal Compatibility**: Works with various bisulfite sequencing protocols.
- **Methylation Calling**: Identifies and quantifies DNA methylation at single-base resolution.
- **Input/Output**: Accepts aligned BAM files; outputs methylation calls in various formats.
- **Multiple Output Formats**: Supports BED, CpG, and custom output formats.

## Pitfalls

- **Alignment Requirements**: Requires properly aligned sequencing data.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Methylation calling accuracy depends on input data quality.
- **Reference Genome**: Requires reference genome for coordinate-based output.

## Examples

### Extract methylation
**Args:** `MethylDackel extract -i reads.bam -o methylation.txt`
**Explanation:** Extracts methylation calls from aligned bisulfite reads.

### With reference genome
**Args:** `MethylDackel extract -i reads.bam -r reference.fasta -o methylation.txt`
**Explanation:** Uses reference genome for coordinate-based methylation calling.

### Output in BED format
**Args:** `MethylDackel extract -i reads.bam -o methylation.bed -f bed`
**Explanation:** Outputs methylation calls in BED format.

### Filter by quality
**Args:** `MethylDackel extract -i reads.bam -o methylation.txt -q 30`
**Explanation:** Filters methylation calls by minimum quality score.

### Batch processing
**Args:** `MethylDackel extract -i bam/ -o methylation/`
**Explanation:** Processes multiple BAM files in batch mode.