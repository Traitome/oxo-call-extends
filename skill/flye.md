---
name: flye
category: assembly
description: "Flye is a fast and accurate de novo assembler for single molecule sequencing reads using repeat graphs."
tags: [flye, assembly, de-novo, long-read, nanopore, pacbio, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/mikolmogorov/Flye"
---

## Concepts
- **Tool Overview**: Flye is a de novo assembler designed specifically for long-read sequencing data from Oxford Nanopore and PacBio platforms.
- **Core Function**: Assembles long reads into complete genomes using repeat graphs to handle complex genomic repeats.
- **Input/Output**: Input: FASTQ files with long reads. Output: Assembled contigs/scaffolds in FASTA format, assembly graphs.
- **Repeat Graph Algorithm**: Builds and resolves repeat graphs to correctly assemble repetitive regions.
- **Polishing**: Includes built-in polishing step using minimap2 for consensus accuracy improvement.
- **Heterozygosity Handling**: Supports assembly of heterozygous genomes with phase-aware assembly.
- **Installation**: `conda install -c bioconda flye` or clone from GitHub. Requires Python 3.x and minimap2.

## Pitfalls
- **Read Quality**: Low-quality reads affect assembly accuracy. Use basecallers with high accuracy (e.g., Guppy high-accuracy mode).
- **Coverage Depth**: Minimum coverage required for reliable assembly (typically 20x+).
- **Repeat Complexity**: Extremely complex repeats may cause misassemblies. Manual curation may be needed.
- **Memory Requirements**: Large genomes require significant memory. Use --threads and --memory options appropriately.
- **Polishing Steps**: Multiple polishing rounds improve accuracy but increase runtime.
- **Circular Genomes**: For circular genomes (plasmids, mitochondria), use --circular option.

## Examples
### Basic assembly
**Args:** `flye --nano-raw reads.fastq --out-dir assembly --genome-size 5m`
**Explanation:** Assembles ONT raw reads with estimated genome size of 5 million bases.

### PacBio HiFi assembly
**Args:** `flye --pacbio-hifi reads.fastq --out-dir assembly --genome-size 3g`
**Explanation:** Assembles PacBio HiFi reads from a 3Gb genome.

### With polishing
**Args:** `flye --nano-hq reads.fastq --out-dir assembly --genome-size 5m --polish-target polished.fasta`
**Explanation:** Performs additional polishing step on assembled contigs.

### Scaffold with mate-pairs
**Args:** `flye --nano-raw reads.fastq --out-dir assembly --genome-size 5m --scaffold-mates mates.bam`
**Explanation:** Uses mate-pair information to scaffold contigs.

### Assembly graph visualization
**Args:** `flye --nano-raw reads.fastq --out-dir assembly --genome-size 5m --write-graph`
**Explanation:** Outputs assembly graph in GFA format for visualization.
