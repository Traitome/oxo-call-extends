---
name: metabat2
category: metagenomics
description: Metagenome binning tool for reconstructing microbial genomes from metagenomic data.
tags: [metabat2, metagenomics, binning]
author: oxo-call-community
source_url: "https://bitbucket.org/berkeleylab/metabat"
---

## Concepts

- **Tool Overview**: MetaBAT2 bins metagenomic contigs into MAGs.
- **Core Function**: Metagenomic binning using composition and coverage.
- **Coverage-based**: Uses depth information for binning.
- **Composition-based**: Uses tetranucleotide frequency.
- **MAG Generation**: Creates metagenome-assembled genomes.
- **Installation**: `conda install -c bioconda metabat2`

## Pitfalls

- **Coverage Data**: Requires depth information.
- **Assembly Quality**: Depends on good assembly.
- **Memory Requirements**: High memory for large datasets.
- **Computation Time**: Slow for complex metagenomes.
- **Parameter Tuning**: Requires careful threshold adjustment.
- **Contamination**: May produce contaminated bins.

## Examples

### Bin contigs
**Args:** `metabat2 -i assembly.fa -a depth.txt -o bins/bin`
**Explanation:** Bins metagenomic contigs into MAGs.

### With multiple samples
**Args:** `metabat2 -i assembly.fa -a sample1.depth,sample2.depth -o bins/bin`
**Explanation:** Uses multiple depth files.

### High sensitivity
**Args:** `metabat2 -i assembly.fa -a depth.txt --sensitive -o bins/bin`
**Explanation:** Runs in sensitive mode.

### Max bin size
**Args:** `metabat2 -i assembly.fa -a depth.txt --maxBinSize 2000000 -o bins/bin`
**Explanation:** Sets maximum bin size.

### Help documentation
**Args:** `metabat2 --help`
**Explanation:** Displays available options.
