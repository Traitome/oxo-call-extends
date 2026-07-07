---
name: pod5
category: qc
description: pod5 provides tools for Oxford Nanopore Pod5 file format.
tags: [pod5, qc, nanopore, file-format]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/pod5-file-format"
---

## Concepts

- **Tool Overview**: pod5 handles nanopore sequencing data.
- **Core Function**: Pod5 file format manipulation.
- **Algorithm**: Uses Apache Arrow for data storage.
- **Input Format**: Accepts Pod5 format files.
- **Output**: Produces processed sequencing data.
- **Use Case**: Nanopore data processing, sequencing analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Format Compatibility**: May have version issues.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pod5 --help`
**Explanation:** Shows available options and usage instructions.

### Convert to Pod5
**Args:** `pod5 convert fast5 -i data/ -o output.pod5`
**Explanation:** Converts FAST5 files to Pod5 format.

### With parameters
**Args:** `pod5 view -i data.pod5 -p params.yaml -o output.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pod5 -v convert fast5 -i data/ -o output.pod5`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pod5 -t 4 convert fast5 -i data/ -o output.pod5`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pod5 export -i data.pod5 -o output.fastq --fastq`
**Explanation:** Exports to FASTQ format.

### Generate report
**Args:** `pod5 inspect -i data.pod5 --report report.html`
**Explanation:** Generates HTML report.