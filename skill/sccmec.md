---
name: sccmec
category: typing
description: SCCmec - Typing SCCmec cassettes in bacterial assemblies
tags: ["sccmec", "typing", "MRSA", "bacterial-genomics"]
author: oxo-call-community
source_url: "https://github.com/rpetit3/sccmec"
---

## Concepts

- **Tool Overview**: SCCmec (v1.2.0) is a tool for typing SCCmec cassettes in bacterial genome assemblies.
- **Core Function**: Identifies and types SCCmec elements responsible for methicillin resistance.
- **Algorithm**: Uses BLAST-based approach to identify SCCmec cassette components.
- **Input/Output**: Accepts genome assemblies and produces SCCmec type classification.
- **MRSA Focus**: Specifically designed for methicillin-resistant Staphylococcus aureus (MRSA).
- **Applications**: Clinical microbiology, antibiotic resistance surveillance, and bacterial genomics.

## Pitfalls

- **Assembly Quality**: Results depend on input assembly quality.
- **Reference Databases**: Requires up-to-date SCCmec reference sequences.
- **Partial Cassettes**: May not correctly type partial SCCmec elements.
- **Sequence Similarity**: Highly similar cassettes may cause misclassification.
- **Computational Resources**: May require significant compute resources.
- **False Negatives**: May miss novel SCCmec types.

## Examples

### Basic SCCmec typing
**Args:** `sccmec -i assembly.fasta -o result.txt`
**Explanation:** `-i` input genome assembly; `-o` typing results.

### Multiple assemblies
**Args:** `sccmec -i assembly1.fasta assembly2.fasta -o results/`
**Explanation:** Processes multiple genome assemblies.

### Verbose output
**Args:** `sccmec -i assembly.fasta -v -o result.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Custom database
**Args:** `sccmec -i assembly.fasta -d custom_db/ -o result.txt`
**Explanation:** `-d` specifies custom SCCmec database.

### Output JSON
**Args:** `sccmec -i assembly.fasta -f json -o result.json`
**Explanation:** `-f json` outputs results in JSON format.

### Quality filtering
**Args:** `sccmec -i assembly.fasta -q 90 -o result.txt`
**Explanation:** `-q 90` requires 90% identity threshold.

### Batch processing
**Args:** `sccmec -i assemblies/*.fasta -o results/`
**Explanation:** Processes all assemblies in a directory.