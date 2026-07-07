---
name: schemarefinery
category: typing
description: SchemaRefinery - Tool to refine cg/wgMLST Schemas
tags: ["schemarefinery", "typing", "MLST", "genotyping"]
author: oxo-call-community
source_url: "https://schema-refinery.readthedocs.io/en/latest/index.html"
---

## Concepts

- **Tool Overview**: SchemaRefinery (v0.5.0) is a tool for refining core genome (cgMLST) and whole genome (wgMLST) schemas.
- **Core Function**: Refines and optimizes MLST schemas for bacterial typing.
- **Algorithm**: Uses sequence comparison and allele calling to refine schema definitions.
- **Input/Output**: Accepts genome sequences and MLST schemas, produces refined schemas.
- **MLST Focus**: Specifically designed for multilocus sequence typing schemas.
- **Applications**: Bacterial typing, epidemiological surveillance, and microbial genomics.

## Pitfalls

- **Schema Dependence**: Requires existing MLST schema as input.
- **Sequence Quality**: Results depend on input sequence quality.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Allele Calling**: Accurate allele calling is critical for schema refinement.
- **Database Updates**: May require regular database updates.

## Examples

### Basic schema refinement
**Args:** `schemarefinery refine -i genomes.fasta -s schema.csv -o refined_schema.csv`
**Explanation:** `-i` input genomes; `-s` existing schema; `-o` refined schema.

### Add new loci
**Args:** `schemarefinery add_loci -i genomes.fasta -s schema.csv -n 10 -o updated_schema.csv`
**Explanation:** `-n 10` adds 10 new loci to the schema.

### Validate schema
**Args:** `schemarefinery validate -s schema.csv -o validation_report.txt`
**Explanation:** Validates MLST schema for consistency.

### Export alleles
**Args:** `schemarefinery export -s schema.csv -o alleles.fasta`
**Explanation:** Exports allele sequences from schema.

### Verbose logging
**Args:** `schemarefinery refine -i genomes.fasta -s schema.csv -v -o refined_schema.csv`
**Explanation:** `-v` enables verbose output for debugging.

### Quality filtering
**Args:** `schemarefinery refine -i genomes.fasta -s schema.csv -q 95 -o refined_schema.csv`
**Explanation:** `-q 95` requires 95% sequence identity.

### Batch processing
**Args:** `schemarefinery refine -i genomes/*.fasta -s schema.csv -o refined_schema.csv`
**Explanation:** Processes multiple genome files.