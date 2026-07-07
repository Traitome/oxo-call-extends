---
name: metanovo
category: utility
description: Produce targeted databases for mass spectrometry analysis.
tags: [metanovo, utility, mass-spectrometry, proteomics]
author: oxo-call-community
source_url: "https://github.com/uct-cbio/proteomics-pipelines"
---

## Concepts

- **Tool Overview**: MetaNovo v1.9.4 is a tool for producing targeted databases for mass spectrometry-based proteomics analysis.
- **Core Function**: Generates custom protein sequence databases for targeted mass spectrometry experiments.
- **Database Generation**: Creates targeted databases from genomic or transcriptomic sequences.
- **Mass Spectrometry Integration**: Optimized for use with mass spectrometry proteomics workflows.
- **Input/Output**: Accepts FASTA sequences and metadata; outputs targeted search databases.
- **Customization**: Supports customization of database content based on experimental needs.

## Pitfalls

- **Sequence Quality**: Database quality depends on input sequence quality.
- **Contamination**: May include contaminant sequences if not properly filtered.
- **Database Size**: Large databases can increase search time.
- **Parameter Tuning**: May require parameter adjustment for optimal database generation.
- **Memory Requirements**: Processing large datasets may require significant memory.
- **False Positives**: Poorly curated databases can increase false positive identifications.

## Examples

### Generate targeted database
**Args:** `metanovo -i proteins.fasta -o target_db.fasta`
**Explanation:** Generates a targeted database from input protein sequences.

### With metadata
**Args:** `metanovo -i proteins.fasta -m metadata.csv -o target_db.fasta`
**Explanation:** Incorporates metadata into database generation.

### Filter by length
**Args:** `metanovo -i proteins.fasta -o target_db.fasta -l 50`
**Explanation:** Filters sequences to minimum length of 50 amino acids.

### Generate decoy database
**Args:** `metanovo -i proteins.fasta -o target_db.fasta -d`
**Explanation:** Generates decoy sequences for false discovery rate estimation.

### Batch processing
**Args:** `metanovo -i fasta/ -o databases/`
**Explanation:** Processes multiple FASTA files in batch.