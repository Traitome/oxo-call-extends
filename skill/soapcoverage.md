---
name: soapcoverage
category: analysis
description: SOAPcoverage - Calculate sequencing coverage and duplication rates
tags: [soapcoverage, analysis, coverage, duplication, alignment]
author: oxo-call-community
source_url: "http://soap.genomics.org.cn/soapaligner.html"
---

## Concepts

- **Tool Overview**: soapcoverage (v2.7.7) - A tool for coverage analysis
- **Core Function**: Calculates sequencing coverage, physical coverage, and duplication rates
- **Input/Output**: Accepts alignment files; outputs coverage statistics
- **Algorithm**: Analyzes alignment results for coverage metrics
- **Installation**: `conda install -c bioconda soapcoverage`
- **Key Features**: Coverage calculation, duplication analysis, multi-thread support

## Pitfalls

- **Input Requirements**: Requires properly formatted alignment files
- **Alignment Format**: Supports SOAP, BLAT, BLAST, MAQ formats
- **Reference Genome**: Must use compatible reference genome
- **Memory Usage**: Large alignments require significant memory
- **Output Format**: Multiple output formats available
- **Coverage Threshold**: Requires proper threshold settings

## Examples

### Display help
**Args:** `soapcoverage --help`
**Explanation:** Shows available options and usage information.

### Basic coverage analysis
**Args:** `soapcoverage -i aligned.soap -o coverage.txt`
**Explanation:** Calculate coverage from SOAP alignment.

### With reference
**Args:** `soapcoverage -i aligned.soap -r reference.fasta -o coverage.txt`
**Explanation:** Use reference for coverage calculation.

### Calculate duplication
**Args:** `soapcoverage -i aligned.soap -o coverage.txt --duplication`
**Explanation:** Calculate duplication rate.

### Physical coverage
**Args:** `soapcoverage -i aligned.soap -o coverage.txt --physical`
**Explanation:** Calculate physical coverage.

### With threads
**Args:** `soapcoverage -i aligned.soap -o coverage.txt -p 8`
**Explanation:** Use multiple threads for analysis.

### Segment analysis
**Args:** `soapcoverage -i aligned.soap -o coverage.txt --segments segments.bed`
**Explanation:** Analyze coverage for specific segments.

### Generate report
**Args:** `soapcoverage -i aligned.soap -o coverage.txt --report`
**Explanation:** Generate coverage report.