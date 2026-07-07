---
name: itero
category: assembly
description: Iterative guided contig assembly pipeline integrating SPAdes, BWA, and SAMtools.
tags: [itero, assembly, SPAdes, BWA, SAMtools]
author: oxo-call-community
source_url: "https://github.com/faircloth-lab/itero"
---

## Concepts

- **Iterative Assembly**: Performs iterative rounds of contig assembly and mapping.
- **Reference-Guided**: Uses reference sequences to guide contig assembly.
- **Multi-Tool Integration**: Combines SPAdes, BWA, and SAMtools into a single pipeline.
- **Contig Improvement**: Iteratively improves contig quality through mapping and reassembly.
- **Automated Workflow**: Automates the entire assembly process from raw reads to final contigs.
- **Quality Control**: Includes quality checks at each assembly iteration.

## Pitfalls

- **Reference Quality**: Poor quality reference sequences affect assembly accuracy.
- **Computational Resources**: Multiple iterations require significant computational resources.
- **Memory Requirements**: Memory usage increases with dataset size and iteration count.
- **Time Complexity**: Iterative assembly can be time-consuming for large datasets.
- **Parameter Tuning**: Optimal parameters may vary between datasets.
- **Assembly Artifacts**: Iterative processes can introduce assembly artifacts.

## Examples

### Basic iterative assembly
**Args:** `itero --reads reads.fastq --reference ref.fasta --output contigs.fasta`
**Explanation:** Performs iterative guided contig assembly using reference sequence.

### Multiple iterations
**Args:** `itero --reads reads.fastq --reference ref.fasta --iterations 5 --output contigs.fasta`
**Explanation:** Runs 5 iterations of assembly and mapping.

### With quality filtering
**Args:** `itero --reads reads.fastq --reference ref.fasta --quality-filter --output contigs.fasta`
**Explanation:** Applies quality filtering before assembly.

### Parallel processing
**Args:** `itero --reads reads.fastq --reference ref.fasta --threads 8 --output contigs.fasta`
**Explanation:** Uses multiple threads for faster processing.

### Generate statistics
**Args:** `itero --reads reads.fastq --reference ref.fasta --stats --output contigs.fasta`
**Explanation:** Generates assembly statistics at each iteration.

### Batch processing
**Args:** `itero --batch samples.txt --reference ref.fasta --output-dir results/`
**Explanation:** Processes multiple samples in batch mode.