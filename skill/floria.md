---
name: floria
category: metagenomics
description: "Floria recovers strain-level haplotypes and clusters reads from metagenomic short or long-read sequencing data by haplotype phasing."
tags: [floria, metagenomics, haplotype, strain-level, bioinformatics, microbiome]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/floria"
---

## Concepts
- **Tool Overview**: Floria is a computational method for recovering strain-level haplotypes from metagenomic sequencing data through haplotype phasing.
- **Core Function**: Identifies and clusters reads belonging to different strains by phasing genetic variants present in the metagenome.
- **Input/Output**: Input: Metagenomic reads (FASTQ), reference genome or assembly. Output: Strain-level haplotypes, read clusters.
- **Haplotype Phasing**: Phases variants across the metagenome to distinguish between different strains of the same species.
- **Strain Identification**: Groups reads into strain-specific clusters based on their haplotype profiles.
- **Short/Long Read Support**: Works with both short-read (Illumina) and long-read (ONT/PacBio) sequencing data.
- **Installation**: `conda install -c bioconda floria` or clone from GitHub. Requires Python 3.x and numpy.

## Pitfalls
- **Strain Similarity**: Closely related strains may be merged. Requires sufficient genetic variation for differentiation.
- **Coverage Depth**: Low coverage strains may not be recovered. Deep sequencing improves detection.
- **Reference Bias**: Reference genome choice affects strain detection. Use species-specific references when possible.
- **Computational Complexity**: Large metagenomic datasets require significant computational resources.
- **Contamination**: Host or contaminant reads can interfere with strain calling. Filter before analysis.
- **Multi-species Samples**: Complex communities with many species increase computational demands.

## Examples
### Basic strain recovery
**Args:** `floria --reads metagenome.fastq --ref reference.fasta --output strains/`
**Explanation:** Recovers strain-level haplotypes from metagenomic reads using reference genome.

### Long-read mode
**Args:** `floria --reads long_reads.fastq --ref reference.fasta --long-reads --output strains/`
**Explanation:** Optimizes for long-read sequencing data for better haplotype resolution.

### Specify strain count
**Args:** `floria --reads metagenome.fastq --ref reference.fasta --strains 5 --output strains/`
**Explanation:** Specifies expected number of strains for clustering.

### Read clustering only
**Args:** `floria --reads metagenome.fastq --ref reference.fasta --cluster-only --output clusters.txt`
**Explanation:** Only performs read clustering without full haplotype reconstruction.

### Generate visualization
**Args:** `floria --reads metagenome.fastq --ref reference.fasta --visualize --output plot.png`
**Explanation:** Creates visualization of strain relationships and haplotype diversity.
