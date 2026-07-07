---
name: pling
category: annotation
description: pling computes rearrangement distance between plasmids.
tags: [pling, annotation, plasmid, rearrangement]
author: oxo-call-community
source_url: "https://github.com/iqbal-lab-org/pling"
---

## Concepts

- **Tool Overview**: pling analyzes plasmid rearrangements.
- **Core Function**: Rearrangement distance computation.
- **Algorithm**: Uses genomic rearrangement methods.
- **Input Format**: Accepts plasmid sequence files.
- **Output**: Produces distance matrix results.
- **Use Case**: Plasmid evolution, comparative genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Distance Accuracy**: May have calculation errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pling --help`
**Explanation:** Shows available options and usage instructions.

### Compute rearrangement distance
**Args:** `pling -i plasmids.fasta -o distances.txt`
**Explanation:** Computes rearrangement distance between plasmids.

### With parameters
**Args:** `pling -i plasmids.fasta -p params.yaml -o distances.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pling -v -i plasmids.fasta -o distances.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pling -t 4 -i plasmids.fasta -o distances.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pling -i plasmids.fasta -o distances.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `pling -i plasmids.fasta -o distances.txt --report report.html`
**Explanation:** Generates HTML report.