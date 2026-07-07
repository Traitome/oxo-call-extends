---
name: encyclopedia
category: formatting
description: "EncyclopeDIA is library search engine comprised of several algorithms for DIA data analysis"
tags: [encyclopedia, formatting, proteomics, DIA, mass-spectrometry]
author: oxo-call-community
source_url: "https://bitbucket.org/searleb/encyclopedia/wiki/Home"
---

## Concepts

- **Tool Overview**: EncyclopeDIA is a comprehensive library search engine for Data-Independent Acquisition (DIA) mass spectrometry data analysis, enabling peptide identification and quantification.
- **Core Function**: Performs peptide identification and quantification using spectrum libraries or chromatogram libraries generated from DIA data.
- **Input/Output**: Input: DIA mass spectrometry data (mzML, mzXML), spectrum/chromatogram libraries, FASTA databases. Output: Identified peptides, quantification results, statistical reports.
- **Algorithm**: Implements multiple scoring algorithms including Walnut (PECAN-based) for chromatogram library generation and peptide identification.
- **Key Features**: DIA data analysis, spectrum library search, chromatogram library generation, FDR control, quantification, batch processing, visualization.
- **Installation**: `conda install -c bioconda encyclopedia`

## Pitfalls

- **Data Format**: Requires specific mass spectrometry data formats.
- **Library Quality**: Search performance depends on library quality and completeness.
- **Computation Time**: Large datasets may require significant computation time.
- **Memory Usage**: May require substantial memory for large libraries.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic DIA search
**Args:** `encyclopedia search -i dia_data.mzML -l library.splib -o results.txt`
**Explanation:** Searches DIA data against spectrum library.

### Generate chromatogram library
**Args:** `encyclopedia generate -i dia_data.mzML -f proteins.fasta -o chrom_library.clib`
**Explanation:** Generates chromatogram library from DIA data and FASTA.

### Quantification
**Args:** `encyclopedia quantify -i dia_data.mzML -l library.splib -o quant_results.txt`
**Explanation:** Performs peptide quantification from DIA data.

### FDR filtering
**Args:** `encyclopedia search -i dia_data.mzML -l library.splib -o results.txt -f 0.01`
**Explanation:** Filters results at 1% FDR threshold.

### Batch processing
**Args:** `encyclopedia batch -i samples/ -l library.splib -o results/`
**Explanation:** Processes multiple DIA files in batch mode.