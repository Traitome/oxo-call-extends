---
name: biscot
category: assembly
description: Bionano Scaffolding Correction Tool for genome assembly improvement
tags: [bionano, scaffolding, assembly, genome]
author: oxo-call-community
source_url: "https://github.com/institut-de-genomique/biscot"
---

## Concepts

- **Tool Overview**: Biscot (Bionano Scaffolding Correction Tool) is designed to correct errors and improve genome assemblies using Bionano optical mapping data.
- **Bionano Integration**: Uses Bionano optical maps to identify and correct misassemblies in sequence assemblies.
- **Scaffold Correction**: Detects chimeric scaffolds, incorrect joins, and other assembly errors.
- **Applications**: Genome assembly improvement, structural variation detection, assembly validation.

## Pitfalls

- **Bionano Data Required**: Requires Bionano optical map data as input.
- **Reference Assembly**: Works best with existing sequence assemblies for comparison.

## Examples

### Correct assembly with Bionano
**Args:** `biscot.py -i assembly.fasta -b bionano.cmap -o corrected_assembly/`
**Explanation:** Corrects assembly using Bionano optical map data.

### Run with specific parameters
**Args:** `biscot.py -i assembly.fasta -b bionano.cmap -o output/ --min-length 1000`
**Explanation:** Corrects assembly with minimum scaffold length filter.

### Generate report
**Args:** `biscot.py -i assembly.fasta -b bionano.cmap -o output/ --report`
**Explanation:** Generates detailed correction report.