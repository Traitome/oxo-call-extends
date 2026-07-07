---
name: soapec
category: qc
description: SOAPec - Error correction tool for SOAPdenovo assembly
tags: [soapec, qc, error-correction, assembly, soapdenovo]
author: oxo-call-community
source_url: "http://soap.genomics.org.cn/soapdenovo.html"
---

## Concepts

- **Tool Overview**: soapec (v2.03) - An error correction tool for SOAPdenovo
- **Core Function**: Corrects sequencing errors in reads before assembly
- **Input/Output**: Accepts FASTQ reads; outputs corrected reads
- **Algorithm**: Uses k-mer frequency analysis for error detection
- **Installation**: `conda install -c bioconda soapec`
- **Key Features**: Error correction, k-mer analysis, assembly preparation

## Pitfalls

- **Input Requirements**: Requires properly formatted FASTQ files
- **K-mer Size**: K-mer size affects correction accuracy
- **Memory Usage**: Large datasets require significant memory
- **Coverage**: Low coverage reduces correction effectiveness
- **Over-correction**: May over-correct in high-coverage regions
- **Output Quality**: Quality of corrected reads affects assembly

## Examples

### Display help
**Args:** `SOAPec --help`
**Explanation:** Shows available options and usage information.

### Basic error correction
**Args:** `SOAPec -i reads.fastq -o corrected.fastq`
**Explanation:** Correct errors in reads.

### With k-mer size
**Args:** `SOAPec -i reads.fastq -o corrected.fastq -k 31`
**Explanation:** Set k-mer size for correction.

### Paired-end correction
**Args:** `SOAPec -i reads_1.fastq -2 reads_2.fastq -o corrected_1.fastq -o2 corrected_2.fastq`
**Explanation:** Correct paired-end reads.

### With frequency threshold
**Args:** `SOAPec -i reads.fastq -o corrected.fastq -f 5`
**Explanation:** Set minimum k-mer frequency threshold.

### With threads
**Args:** `SOAPec -i reads.fastq -o corrected.fastq -p 8`
**Explanation:** Use multiple threads for correction.

### Output statistics
**Args:** `SOAPec -i reads.fastq -o corrected.fastq --stats`
**Explanation:** Output correction statistics.

### Generate report
**Args:** `SOAPec -i reads.fastq -o corrected.fastq --report`
**Explanation:** Generate correction report.