---
name: padloc
category: utility
description: Padloc locates antiviral defence systems in prokaryotic genomes.
tags: [padloc, utility, antiviral-defence, prokaryotes]
author: oxo-call-community
source_url: "https://github.com/padlocbio/padloc"
---

## Concepts

- **Tool Overview**: Padloc identifies antiviral defense systems in bacteria and archaea.
- **Core Function**: Detects CRISPR-Cas, restriction-modification, and other defense systems.
- **Algorithm**: Uses profile HMMs and signature-based detection.
- **Input Format**: Accepts FASTA genome sequences.
- **Output**: Produces annotations of defense systems.
- **Use Case**: Prokaryotic genomics, phage defense research, and microbial ecology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Database Updates**: Requires regular database updates.
- **False Positives**: May report false positive predictions.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `padloc --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `padloc -i genome.fasta -o results.txt`
**Explanation:** Identifies defense systems in genome.

### With database
**Args:** `padloc -i genome.fasta -d database/ -o results.txt`
**Explanation:** Uses custom database.

### Output format
**Args:** `padloc -i genome.fasta -o results.gff --gff`
**Explanation:** Outputs in GFF format.

### Verbose mode
**Args:** `padloc -i genome.fasta -v -o results.txt`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `padloc batch -d genomes/ -o results/`
**Explanation:** Processes multiple genome files.

### Update database
**Args:** `padloc update`
**Explanation:** Updates reference database.