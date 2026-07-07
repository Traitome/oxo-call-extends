---
name: slimm
category: metagenomics
description: SLIMM - Species Level Identification of Microorganisms from Metagenomes using coverage information for improved taxonomic profiling
tags: [slimm, metagenomics, species-identification, taxonomic-profiling]
author: oxo-call-community
source_url: "https://github.com/seqan/slimm"
---

## Concepts

- **Tool Overview**: slimm (v0.3.4) - A metagenomic classifier for species-level identification of microorganisms
- **Core Function**: Uses coverage information to remove unlikely genomes and improve species-level assignments
- **Input/Output**: Accepts aligned reads (BAM); outputs species-level abundance profiles and coverage maps
- **Algorithm**: Combines read mapping with coverage-based filtering for improved taxonomic resolution
- **Installation**: `conda install -c bioconda slimm`
- **Key Features**: Outperforms state-of-the-art tools in runtime and memory usage; provides species-level resolution

## Pitfalls

- **Reference Database**: Requires SLIMM-formatted reference database
- **Alignment Dependency**: Requires pre-aligned reads in BAM format
- **Memory Management**: Large databases may require significant memory
- **Database Building**: Building custom databases requires additional steps
- **Coverage Threshold**: Appropriate coverage cutoff selection affects results
- **Taxonomic Resolution**: Limited by reference database completeness

## Examples

### Display help
**Args:** `slimm --help`
**Explanation:** Shows available options and usage information.

### Build database
**Args:** `slimm build -i reference_genomes/ -o slimm_db.sldb`
**Explanation:** Build SLIMM database from reference genomes.

### Classify reads
**Args:** `slimm classify -d slimm_db.sldb -i aligned.bam -o results.txt`
**Explanation:** Perform species-level classification on aligned reads.

### With coverage cutoff
**Args:** `slimm classify -d slimm_db.sldb -i aligned.bam -c 0.1 -o results.txt`
**Explanation:** Set minimum coverage cutoff for species detection.

### Generate coverage map
**Args:** `slimm coverage -d slimm_db.sldb -i aligned.bam -o coverage.txt`
**Explanation:** Generate species-level coverage map.

### Batch processing
**Args:** `slimm batch -d slimm_db.sldb -i bam_dir/ -o results_dir/`
**Explanation:** Process multiple BAM files in batch.

### Custom output format
**Args:** `slimm classify -d slimm_db.sldb -i aligned.bam -f kraken -o results.txt`
**Explanation:** Output results in Kraken-compatible format.