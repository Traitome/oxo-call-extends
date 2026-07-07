---
name: primerprospector
category: genome-editing
description: primerprospector designs and analyzes PCR primers.
tags: [primerprospector, genome-editing, primers, pcr]
author: oxo-call-community
source_url: "http://pprospector.sourceforge.net/"
---

## Concepts

- **Tool Overview**: primerprospector designs PCR primers.
- **Core Function**: Primer design and analysis.
- **Algorithm**: Uses bioinformatics methods.
- **Input Format**: Accepts sequence files.
- **Output**: Produces primer sets.
- **Use Case**: PCR assay design, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Primer Specificity**: May have mispriming.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `primer_prospector.py --help`
**Explanation:** Shows available options and usage instructions.

### Design primers
**Args:** `primer_prospector.py -i sequences.fasta -o primers.txt`
**Explanation:** Designs PCR primers from sequences.

### With parameters
**Args:** `primer_prospector.py -i sequences.fasta -p params.txt -o primers.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `primer_prospector.py -v -i sequences.fasta -o primers.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `primer_prospector.py -t 4 -i sequences.fasta -o primers.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `primer_prospector.py -i sequences.fasta -o primers.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `primer_prospector.py -i sequences.fasta -o primers.txt --report report.html`
**Explanation:** Generates HTML report.