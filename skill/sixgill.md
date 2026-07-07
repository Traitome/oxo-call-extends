---
name: sixgill
category: proteomics
description: sixgill - Six-frame genome-inferred libraries for LC-MS/MS
tags: ["sixgill", "proteomics", "mass-spectrometry", "genome"]
author: oxo-call-community
source_url: "https://github.com/searleb/sixgill"
---

## Concepts

- **Tool Overview**: sixgill (v0.2.4) generates six-frame translation libraries for LC-MS/MS.
- **Core Function**: Creates protein databases from genome sequences.
- **Algorithm**: Translates all six reading frames of genomic DNA.
- **Input/Output**: Accepts genome FASTA and produces protein databases.
- **Six-frame Translation**: Specialized for proteogenomics analysis.
- **Applications**: Proteomics, metaproteomics, proteogenomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large genomes.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on genome quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Generate library
**Args:** `sixgill -i genome.fasta -o protein_db.fasta`
**Explanation:** `-i` input genome; `-o` output protein database.

### With filtering
**Args:** `sixgill -i genome.fasta -m 50 -o protein_db.fasta`
**Explanation:** `-m 50` minimum peptide length.

### Add decoys
**Args:** `sixgill -i genome.fasta -d -o protein_db.fasta`
**Explanation:** `-d` add decoy sequences.

### Help command
**Args:** `sixgill --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sixgill --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sixgill -v -i genome.fasta -o protein_db.fasta`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sixgill -t 8 -i genome.fasta -o protein_db.fasta`
**Explanation:** `-t 8` uses 8 threads.
