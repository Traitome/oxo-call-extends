---
name: mykrobe
category: annotation
description: Mykrobe - Rapid antibiotic resistance prediction from genome sequence data
tags: [mykrobe, annotation, antibiotic-resistance, bacteria, prediction, tuberculosis, staph]
author: oxo-call-community
source_url: "https://github.com/Mykrobe-tools/mykrobe"
---

## Concepts

- **Tool Overview**: Mykrobe v0.13.0 is a rapid antibiotic resistance prediction tool that analyzes genome sequencing data to predict resistance in bacterial pathogens. It can complete analysis in minutes from raw sequencing reads.
- **Core Function**: Uses curated mutation catalogs to identify genetic variants associated with antibiotic resistance and predict phenotypic resistance. Supports both FASTQ reads and assembled genomes as input.
- **Species Support**: Primarily supports Mycobacterium tuberculosis complex (TB), Staphylococcus aureus, Shigella sonnei, and Salmonella typhi. Each species has species-specific resistance prediction models.
- **Algorithm**: Maps reads to species-specific references, calls variants, and checks against known resistance mutations. Machine learning models integrate multiple mutations for improved prediction accuracy.
- **Input Format**: Accepts raw FASTQ files (gzipped or uncompressed) or pre-assembled FASTA contigs. Works with both short-read (Illumina) and long-read (Nanopore) sequencing data.
- **Output**: Produces JSON files containing predicted resistance phenotypes, detected mutations with nucleotide changes, and quality metrics for each sample.
- **Use Case**: Clinical TB diagnostics, drug resistance surveillance, outbreak investigation, and antimicrobial stewardship in resource-limited settings.

## Pitfalls

- **Species Specification**: Must correctly specify species using `--species` flag. Wrong species leads to incorrect predictions.
- **Mutation Catalog Limitations**: Only detects resistance caused by catalogued mutations. Novel resistance mechanisms not in the database will be missed.
- **Quality Thresholds**: Low sequencing depth or quality may produce unreliable predictions. Check coverage and quality metrics in output.
- **Mixed Infections**: Cannot reliably distinguish between mixed infections and infections with a single strain. May give misleading results.
- **Long-Read Assembly**: When using assembled contigs, assembly quality affects variant detection. Poor assemblies may miss resistance mutations.
- **Database Currency**: Resistance mutation catalogs are updated as new research emerges. Ensure using current versions for accurate clinical predictions.

## Examples

### Predict resistance for Staphylococcus aureus
**Args:** `mykrobe predict --sample S_aureus_001 --species staph_aureus -i reads.fastq.gz -o results.json`
**Explanation:** Standard Mykrobe workflow for S. aureus. Analyzes FASTQ and outputs resistance predictions for common antibiotics.

### Predict resistance for Mycobacterium tuberculosis
**Args:** `mykrobe predict --sample TB_001 --species tuberculosis -i TB_reads.fastq.gz -o tb_resistance.json`
**Explanation:** Standard TB workflow. Predicts resistance to first-line and second-line anti-tuberculosis drugs.

### Genotype from assembly
**Args:** `mykrobe genotype --sample sample1 --species tuberculosis -i assembly.fasta -o genotypes.json`
**Explanation:** When you already have an assembly, use genotype mode to predict resistance from contigs.

### Panel-based prediction (specific drugs)
**Args:** `mykrobe predict --species staph_aureus -i reads.fastq -o results.json --panel beta_lactams`
**Explanation:** Run prediction only for specific drug classes to speed up analysis when interested in particular antibiotics.

### Display version and available species
**Args:** `mykrobe --version`
**Explanation:** Shows version and lists all supported species for resistance prediction.
