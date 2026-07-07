---
name: progressivemauve
category: alignment
description: progressivemauve performs multiple genome alignment with gene gain, loss and rearrangement.
tags: [progressivemauve, alignment, genome-alignment, comparative-genomics]
author: oxo-call-community
source_url: "http://darlinglab.org/mauve/user-guide/progressivemauve.html"
---

## Concepts

- **Tool Overview**: progressivemauve aligns multiple genomes.
- **Core Function**: Whole-genome multiple alignment.
- **Algorithm**: Uses progressive alignment methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces alignment files.
- **Use Case**: Comparative genomics, evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on input quality.
- **Genome Complexity**: May affect alignment.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `progressiveMauve --help`
**Explanation:** Shows available options and usage instructions.

### Align genomes
**Args:** `progressiveMauve genome1.fasta genome2.fasta --output alignment.xmfa`
**Explanation:** Aligns multiple genomes.

### With parameters
**Args:** `progressiveMauve --parameters params.txt genome1.fasta genome2.fasta --output alignment.xmfa`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `progressiveMauve -v genome1.fasta genome2.fasta --output alignment.xmfa`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `progressiveMauve -t 4 genome1.fasta genome2.fasta --output alignment.xmfa`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `progressiveMauve genome1.fasta genome2.fasta --output alignment.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Generate report
**Args:** `progressiveMauve genome1.fasta genome2.fasta --output alignment.xmfa --report report.html`
**Explanation:** Generates HTML report.