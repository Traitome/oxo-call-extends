---
name: getorganelle
category: genome-assembly
description: GetOrganelle - Get organelle genomes from genome skimming data.
tags: [getorganelle, genome-assembly, organelle, chloroplast, mitochondria]
author: oxo-call-community
source_url: "https://github.com/Kinggerm/GetOrganelle/wiki"
---

## Concepts
- **Organelle Assembly**: Assembles organelle genomes.
- **Genome Skimming**: Processes genome skimming data.
- **Chloroplast Assembly**: Assembles chloroplast genomes.
- **Mitochondrial Assembly**: Assembles mitochondrial genomes.
- **Sequence Recovery**: Recovers organelle sequences from low-coverage data.

## Pitfalls
- **Input Quality**: Requires high-quality sequencing data.
- **Reference Selection**: Requires appropriate reference sequences.
- **Contamination**: May encounter nuclear contamination.
- **Assembly Completeness**: May not assemble complete genomes.
- **Parameter Tuning**: Requires careful parameter adjustment.

## Examples
### Assemble chloroplast genome
**Args:** `get_organelle_from_reads.py -1 reads_1.fastq -2 reads_2.fastq -o chloroplast/ -R 15`
**Explanation:** Assembles chloroplast genome from paired-end reads.

### Assemble mitochondrial genome
**Args:** `get_organelle_from_reads.py -1 reads_1.fastq -2 reads_2.fastq -o mitochondria/ -t animal_mt`
**Explanation:** Assembles mitochondrial genome.

### With reference
**Args:** `get_organelle_from_reads.py -1 reads_1.fastq -2 reads_2.fastq -r ref.fasta -o result/`
**Explanation:** Uses reference-guided assembly.

### Batch processing
**Args:** `get_organelle_from_reads.py -l samples.txt -o ./results/`
**Explanation:** Processes multiple samples.

### Generate report
**Args:** `get_organelle_from_reads.py -1 reads_1.fastq -2 reads_2.fastq -r -o report.html`
**Explanation:** Generates assembly report.