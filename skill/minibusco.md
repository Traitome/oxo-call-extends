---
name: minibusco
category: utility
description: "minibusco: a faster and more accurate reimplementation of BUSCO"
tags: [minibusco, utility, quality-control]
author: oxo-call-community
source_url: "https://github.com/huangnengCSU/minibusco"
---
## Concepts

- **Tool Overview**: miniBUSCO v0.2.1 is a faster reimplementation of BUSCO.
- **Core Function**: Assesses genome assembly completeness using conserved orthologs.
- **BUSCO Assessment**: Evaluates genome assembly completeness.
- **Speed Optimized**: Faster than original BUSCO implementation.
- **Input/Output**: Accepts genome assemblies; outputs completeness scores.
- **Quality Control**: Supports genome assembly quality assessment.

## Pitfalls

- **BUSCO Dependency**: Requires BUSCO databases.
- **Computational Resources**: Assessment may require significant resources.
- **Memory Requirements**: Memory usage depends on database size.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Data Quality**: Assessment depends on input assembly quality.
- **Database Compatibility**: Requires compatible BUSCO database.

## Examples

### Assess genome completeness
**Args:** `minibusco -i genome.fasta -o busco_result -l odb10`
**Explanation:** Assesses genome assembly completeness.

### With custom database
**Args:** `minibusco -i genome.fasta -o busco_result -d custom_db/`
**Explanation:** Uses custom BUSCO database.

### Detailed output
**Args:** `minibusco -i genome.fasta -o busco_result -l odb10 -v`
**Explanation:** Generates detailed assessment report.

### Batch processing
**Args:** `minibusco -i fasta/ -o busco_results/ -l odb10`
**Explanation:** Processes multiple genome assemblies.

### Resume run
**Args:** `minibusco -i genome.fasta -o busco_result -l odb10 --resume`
**Explanation:** Resumes interrupted BUSCO run.