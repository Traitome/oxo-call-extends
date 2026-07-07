---
name: sift4g
category: annotation
description: SIFT4G - Scalable SIFT for variant effect prediction
tags: ["sift4g", "annotation", "variant", "prediction"]
author: oxo-call-community
source_url: "https://sift.bii.a-star.edu.sg/sift4g"
---

## Concepts

- **Tool Overview**: SIFT4G (v2.0.0) is a faster version of SIFT for variant effect prediction.
- **Core Function**: Predicts whether amino acid substitutions affect protein function.
- **Algorithm**: Uses sequence homology and conservation for predictions.
- **Input/Output**: Accepts VCF/FASTA files and produces effect predictions.
- **Variant Analysis**: Specialized for missense variant interpretation.
- **Applications**: Variant prioritization, clinical genetics, and functional genomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Database Requirements**: Requires pre-built database for predictions.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Species Specificity**: Performance varies by organism.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Predict variant effects
**Args:** `sift4g -i variants.vcf -d database/ -o predictions.txt`
**Explanation:** `-i` input VCF; `-d` database; `-o` output predictions.

### With FASTA input
**Args:** `sift4g -f protein.fasta -d database/ -o predictions.txt`
**Explanation:** `-f` input FASTA file.

### With cutoff
**Args:** `sift4g -i variants.vcf -d database/ -c 0.05 -o predictions.txt`
**Explanation:** `-c 0.05` SIFT score cutoff.

### Help command
**Args:** `sift4g --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sift4g --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sift4g -v -i variants.vcf -d database/ -o predictions.txt`
**Explanation:** `-v` verbose output.

### Build database
**Args:** `sift4g_build -i genome.fasta -o database/`
**Explanation:** Builds SIFT4G database from genome.
