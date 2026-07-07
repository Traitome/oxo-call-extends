---
name: kaptive
category: formatting
description: Reports information about surface polysaccharide loci for Klebsiella pneumoniae and Acinetobacter baumannii.
tags: [kaptive, formatting, Klebsiella, Acinetobacter, polysaccharide, MLST]
author: oxo-call-community
source_url: "https://kaptive.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: kaptive (v3.2.1) - Analyzes surface polysaccharide loci in bacterial genomes.
- **Klebsiella Analysis**: Specialized for Klebsiella pneumoniae species complex.
- **Acinetobacter Analysis**: Supports Acinetobacter baumannii analysis.
- **Locus Identification**: Identifies capsule and O-antigen loci.
- **MLST Integration**: Integrates with multi-locus sequence typing.
- **Report Generation**: Generates comprehensive reports of findings.

## Pitfalls

- **Species Specificity**: Only works for specific bacterial species.
- **Assembly Quality**: Requires high-quality genome assemblies.
- **Database Updates**: Needs regular database updates.
- **Partial Assemblies**: May fail on incomplete assemblies.
- **Sequence Similarity**: Highly similar loci can cause misidentification.
- **Version Compatibility**: Database format may change between versions.

## Examples

### Analyze Klebsiella genome
**Args:** `kaptive.py -a genome.fasta -k klebsiella -o output/`
**Explanation:** Analyzes Klebsiella genome for capsule loci.

### Analyze Acinetobacter genome
**Args:** `kaptive.py -a genome.fasta -k acinetobacter -o output/`
**Explanation:** Analyzes Acinetobacter genome for surface polysaccharide loci.

### Update database
**Args:** `kaptive.py --update`
**Explanation:** Updates Kaptive reference databases.

### Verbose output
**Args:** `kaptive.py -a genome.fasta -k klebsiella -o output/ -v`
**Explanation:** Shows verbose output during analysis.

### Generate summary report
**Args:** `kaptive.py -a genome.fasta -k klebsiella -o output/ --summary`
**Explanation:** Generates summary report in text format.

### Batch processing
**Args:** `kaptive.py -b batch_list.txt -k klebsiella -o output/`
**Explanation:** Processes multiple genomes in batch mode.