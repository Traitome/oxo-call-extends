---
name: platon
category: annotation
description: platon classifies and characterizes plasmid contigs.
tags: [platon, annotation, plasmid, contig]
author: oxo-call-community
source_url: "https://github.com/oschwengers/platon"
---

## Concepts

- **Tool Overview**: platon classifies plasmid contigs.
- **Core Function**: Plasmid contig classification.
- **Algorithm**: Uses sequence analysis methods.
- **Input Format**: Accepts draft assembly files.
- **Output**: Produces plasmid characterization results.
- **Use Case**: Bacterial genomics, plasmid analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Data Quality**: Results depend on assembly quality.
- **Classification Accuracy**: May have classification errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `platon --help`
**Explanation:** Shows available options and usage instructions.

### Classify plasmids
**Args:** `platon -i assembly.fasta -o plasmids.txt`
**Explanation:** Classifies plasmid contigs from assembly.

### With parameters
**Args:** `platon -i assembly.fasta -p params.yaml -o plasmids.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `platon -v -i assembly.fasta -o plasmids.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `platon -t 4 -i assembly.fasta -o plasmids.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `platon -i assembly.fasta -o plasmids.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `platon -i assembly.fasta -o plasmids.txt --report report.html`
**Explanation:** Generates HTML report.