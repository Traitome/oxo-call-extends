---
name: spectrseqtools
category: metabolomics
description: SpectrSeqTools - Analysis platform for small RNA with PTMs via LC-MS/MS
tags: [spectrseqtools, metabolomics, small-rna, ptms, lc-msms]
author: oxo-call-community
source_url: "https://github.com/spectrseq/spectrseqtools"
---

## Concepts

- **Tool Overview**: spectrseqtools (v0.1.3) - A small RNA analysis platform
- **Core Function**: Analyzes small RNA molecules with PTMs using LC-MS/MS data
- **Input/Output**: Accepts LC-MS/MS data; outputs RNA analysis results
- **Algorithm**: Automatic analysis pipeline for small RNA modifications
- **Installation**: `conda install -c bioconda spectrseqtools`
- **Key Features**: Small RNA analysis, PTM detection, LC-MS/MS processing

## Pitfalls

- **Input Requirements**: Requires properly formatted LC-MS/MS data
- **Data Quality**: Data quality affects analysis accuracy
- **PTM Detection**: PTM detection parameters affect results
- **Memory Usage**: Large MS datasets require significant memory
- **Output Format**: Output format depends on configuration
- **Analysis Accuracy**: Accuracy depends on data quality and parameters

## Examples

### Display help
**Args:** `spectrseqtools --help`
**Explanation:** Shows available options and usage information.

### Basic RNA analysis
**Args:** `spectrseqtools -i ms_data.mgf -o rna_analysis.tsv`
**Explanation:** Analyze small RNA from MS data.

### With PTM detection
**Args:** `spectrseqtools -i ms_data.mgf -o rna_analysis.tsv --detect-ptm`
**Explanation:** Enable PTM detection.

### With RNA database
**Args:** `spectrseqtools -i ms_data.mgf -d rna_db.fasta -o rna_analysis.tsv`
**Explanation:** Use specific RNA database.

### With modification types
**Args:** `spectrseqtools -i ms_data.mgf -o rna_analysis.tsv --modifications m6A m5C`
**Explanation:** Specify modification types.

### Output detailed results
**Args:** `spectrseqtools -i ms_data.mgf -o rna_analysis.tsv --detailed`
**Explanation:** Output detailed analysis information.

### Output PTM sites
**Args:** `spectrseqtools -i ms_data.mgf -o rna_analysis.tsv --ptm-sites`
**Explanation:** Output PTM site information.

### Output statistics
**Args:** `spectrseqtools -i ms_data.mgf -o rna_analysis.tsv --stats`
**Explanation:** Output analysis statistics.

### Generate report
**Args:** `spectrseqtools -i ms_data.mgf -o rna_analysis.tsv --report`
**Explanation:** Generate analysis report.