---
name: srf-n-trf
category: repeat-analysis
description: SRF-N-TRF - Extract monomers, motifs, and regions from SRF and TRF output
tags: [srf-n-trf, repeat-analysis, monomers, motifs, telomeres]
author: oxo-call-community
source_url: "https://github.com/koisland/srf-n-trf"
---

## Concepts

- **Tool Overview**: srf-n-trf (v0.1.2) - A repeat analysis extraction tool
- **Core Function**: Extracts specific monomers, motifs, and regions from SRF and TRF output
- **Input/Output**: Accepts SRF/TRF output; outputs extracted features
- **Algorithm**: Feature extraction from repeat analysis results
- **Installation**: `conda install -c bioconda srf-n-trf`
- **Key Features**: Repeat extraction, monomer analysis, motif detection

## Pitfalls

- **Input Requirements**: Requires properly formatted SRF/TRF output
- **Output Format**: SRF/TRF format affects extraction accuracy
- **Feature Selection**: Feature selection affects extraction results
- **Memory Usage**: Large files require significant memory
- **Output Format**: Output format depends on configuration
- **Extraction Accuracy**: Accuracy depends on input format and parameters

## Examples

### Display help
**Args:** `srf-n-trf --help`
**Explanation:** Shows available options and usage information.

### Basic feature extraction
**Args:** `srf-n-trf -i srf_output.txt -o extracted_features.txt`
**Explanation:** Extract features from SRF output.

### With monomer extraction
**Args:** `srf-n-trf -i srf_output.txt -o extracted_features.txt --monomers`
**Explanation:** Extract monomers from SRF output.

### With motif extraction
**Args:** `srf-n-trf -i srf_output.txt -o extracted_features.txt --motifs`
**Explanation:** Extract motifs from SRF output.

### Multiple files
**Args:** `srf-n-trf -i srf1.txt srf2.txt -o extracted_features.txt`
**Explanation:** Extract features from multiple files.

### Output detailed results
**Args:** `srf-n-trf -i srf_output.txt -o extracted_features.txt --detailed`
**Explanation:** Output detailed extraction information.

### Output statistics
**Args:** `srf-n-trf -i srf_output.txt -o extracted_features.txt --stats`
**Explanation:** Output extraction statistics.

### Generate report
**Args:** `srf-n-trf -i srf_output.txt -o extracted_features.txt --report`
**Explanation:** Generate extraction report.

### With region specification
**Args:** `srf-n-trf -i srf_output.txt -o extracted_features.txt --region chr1:1000-2000`
**Explanation:** Extract features from specific region.