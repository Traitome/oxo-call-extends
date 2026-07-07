---
name: pasa
category: expression
description: PASA annotates eukaryotic genes using spliced transcript alignments.
tags: [pasa, expression, gene-annotation, splicing]
author: oxo-call-community
source_url: "https://github.com/PASApipeline/PASApipeline"
---

## Concepts

- **Tool Overview**: PASA models eukaryotic gene structures from transcripts.
- **Core Function**: Assembles spliced alignments for gene annotation.
- **Algorithm**: Uses transcript alignments to model gene structures.
- **Input Format**: Accepts transcript sequences and genome assemblies.
- **Output**: Produces gene structure annotations.
- **Use Case**: Eukaryotic genome annotation, alternative splicing analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Dependency Management**: Requires multiple dependencies.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pasa --help`
**Explanation:** Shows available options and usage instructions.

### Run annotation
**Args:** `pasa -c pasa.conf -o results/`
**Explanation:** Runs gene annotation pipeline.

### Align transcripts
**Args:** `pasa_align_assembly -c pasa.conf`
**Explanation:** Aligns transcripts to genome.

### Verbose mode
**Args:** `pasa -v -c pasa.conf -o results/`
**Explanation:** Runs with verbose output.

### Load annotations
**Args:** `pasa_load_annotations -c pasa.conf -g genes.gff`
**Explanation:** Loads existing annotations.

### Update annotations
**Args:** `pasa_update_annotations -c pasa.conf`
**Explanation:** Updates annotations with new data.

### Generate report
**Args:** `pasa_report -c pasa.conf -o report.txt`
**Explanation:** Generates annotation report.