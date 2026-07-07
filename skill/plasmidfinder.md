---
name: plasmidfinder
category: annotation
description: plasmidfinder identifies plasmids in bacterial sequences.
tags: [plasmidfinder, annotation, plasmid, bacteria]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/plasmidfinder"
---

## Concepts

- **Tool Overview**: plasmidfinder identifies bacterial plasmids.
- **Core Function**: Plasmid identification.
- **Algorithm**: Uses sequence comparison methods.
- **Input Format**: Accepts bacterial sequence files.
- **Output**: Produces plasmid identification results.
- **Use Case**: Bacterial genomics, plasmid detection.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Detection Accuracy**: May have detection errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plasmidfinder --help`
**Explanation:** Shows available options and usage instructions.

### Identify plasmids
**Args:** `plasmidfinder -i bacteria.fasta -o plasmids.txt`
**Explanation:** Identifies plasmids in bacterial sequences.

### With parameters
**Args:** `plasmidfinder -i bacteria.fasta -p params.yaml -o plasmids.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plasmidfinder -v -i bacteria.fasta -o plasmids.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plasmidfinder -t 4 -i bacteria.fasta -o plasmids.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plasmidfinder -i bacteria.fasta -o plasmids.tab --tab`
**Explanation:** Outputs in tab-delimited format.

### Generate report
**Args:** `plasmidfinder -i bacteria.fasta -o plasmids.txt --report report.html`
**Explanation:** Generates HTML report.