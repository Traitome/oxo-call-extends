---
name: plasmar
category: annotation
description: plasmar identifies antibiotic resistance plasmids.
tags: [plasmar, annotation, antibiotic-resistance, plasmid]
author: oxo-call-community
source_url: "https://github.com/rastanton/PLASMAR"
---

## Concepts

- **Tool Overview**: plasmar identifies resistance plasmids.
- **Core Function**: Antibiotic resistance plasmid detection.
- **Algorithm**: Uses sequence matching methods.
- **Input Format**: Accepts assembly sequence files.
- **Output**: Produces resistance plasmid results.
- **Use Case**: Antibiotic resistance research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Detection Accuracy**: May have detection errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plasmar --help`
**Explanation:** Shows available options and usage instructions.

### Identify resistance plasmids
**Args:** `plasmar -i assembly.fasta -o resistance_plasmids.txt`
**Explanation:** Identifies antibiotic resistance plasmids.

### With parameters
**Args:** `plasmar -i assembly.fasta -p params.yaml -o resistance_plasmids.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plasmar -v -i assembly.fasta -o resistance_plasmids.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plasmar -t 4 -i assembly.fasta -o resistance_plasmids.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plasmar -i assembly.fasta -o resistance_plasmids.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `plasmar -i assembly.fasta -o resistance_plasmids.txt --report report.html`
**Explanation:** Generates HTML report.