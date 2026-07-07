---
name: gfinisher
category: genome-finishing
description: GFinisher - Refinement and finalization of prokaryotic genome assemblies using GC Skew.
tags: [gfinisher, genome-finishing, prokaryote, assembly, GC-skew]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/gfinisher/"
---

## Concepts
- **Genome Finishing**: Refines and finalizes genome assemblies.
- **GC Skew Analysis**: Uses GC skew for error identification.
- **Contig Organization**: Organizes contigs/scaffolds.
- **Prokaryotic Genomes**: Specialized for prokaryotic genomes.
- **Reference Comparison**: Compares with reference genomes.

## Pitfalls
- **Prokaryote Only**: Designed for prokaryotic genomes.
- **Assembly Quality**: Requires good initial assembly.
- **Reference Dependency**: May require reference genomes.
- **Error Detection**: May miss some assembly errors.
- **Validation**: Results should be validated.

## Examples
### Finish genome
**Args:** `gfinisher -i assembly.fasta -o finished.fasta`
**Explanation:** Finishes prokaryotic genome assembly.

### With reference
**Args:** `gfinisher -i assembly.fasta -r reference.fasta -o finished.fasta`
**Explanation:** Uses reference for finishing.

### Generate report
**Args:** `gfinisher -i assembly.fasta -r reference.fasta -o finished.fasta -report`
**Explanation:** Generates finishing report.

### Identify errors
**Args:** `gfinisher -i assembly.fasta -e -o errors.txt`
**Explanation:** Identifies assembly errors.

### Batch processing
**Args:** `gfinisher -l assemblies.txt -o ./finished/`
**Explanation:** Processes multiple assemblies.