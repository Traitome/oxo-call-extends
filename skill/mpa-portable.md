---
name: mpa-portable
category: utility
description: Light-weight software for identification and analysis of metaproteomics data.
tags: [mpa-portable, utility, proteomics]
author: oxo-call-community
source_url: "https://github.com/compomics/meta-proteome-analyzer"
---

## Concepts

- **Tool Overview**: MPA Portable v2.0.0 analyzes metaproteomics and proteomics data.
- **Core Function**: Identifies proteins and performs in-depth analysis.
- **Stand-alone**: Light-weight and self-contained software.
- **Metaproteomics**: Specialized for metaproteomics data analysis.
- **Proteomics Support**: Also works with standard proteomics data.
- **Input/Output**: Accepts MS data; outputs protein identifications.

## Pitfalls

- **Proteomics Specific**: Designed for mass spectrometry data.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for identification.
- **Data Quality**: Results depend on MS data quality.
- **Database Dependence**: Requires protein sequence database.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Analyze metaproteomics data
**Args:** `mpa -i ms_data.mzML -d uniprot.fasta -o results.txt`
**Explanation:** Identifies proteins from metaproteomics data.

### With decoy database
**Args:** `mpa -i ms_data.mzML -d uniprot.fasta -decoy -o results.txt`
**Explanation:** Uses decoy database for FDR estimation.

### Generate report
**Args:** `mpa -i ms_data.mzML -d uniprot.fasta -r report.html -o results.txt`
**Explanation:** Generates analysis report.

### Batch processing
**Args:** `mpa -i mzML/ -d uniprot.fasta -o results/`
**Explanation:** Processes multiple MS files.

### With custom parameters
**Args:** `mpa -i ms_data.mzML -d uniprot.fasta -p params.txt -o results.txt`
**Explanation:** Uses custom analysis parameters.