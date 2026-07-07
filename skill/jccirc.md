---
name: jccirc
category: assembly
description: circRNA assembler through integrated junction contigs.
tags: [jccirc, assembly, circRNA, RNA-seq, splicing]
author: oxo-call-community
source_url: "https://github.com/cbbzhang/JCcirc/blob/master/README.md"
---

## Concepts

- **Tool Overview**: jccirc (v1.0.0) - A tool for assembling circular RNA (circRNA) sequences from RNA-Seq data using integrated junction contigs.
- **circRNA Detection**: Identifies circular RNA molecules formed by back-splicing events.
- **Junction Contigs**: Constructs contigs spanning splice junctions to identify circular structures.
- **Back-splicing Detection**: Identifies non-linear splicing events characteristic of circRNAs.
- **Assembly Validation**: Validates assembled circRNAs using multiple lines of evidence.
- **Integration**: Integrates with existing RNA-Seq analysis workflows.

## Pitfalls

- **False Positives**: May detect false circRNAs from trans-splicing or artifacts.
- **Low Expression**: Lowly expressed circRNAs may be missed.
- **Complex Splicing**: Complex alternative splicing patterns can confound detection.
- **Reference Genome**: Requires well-annotated reference genome.
- **Read Coverage**: Requires sufficient read coverage across splice junctions.
- **Computational Resources**: Assembly requires significant computational resources.

## Examples

### Assemble circRNAs from RNA-Seq
**Args:** `jccirc -i reads.fastq -g ref.gtf -o circRNAs/`
**Explanation:** Assembles circRNAs from RNA-Seq reads using reference annotation.

### Include novel junctions
**Args:** `jccirc -i reads.fastq -g ref.gtf -o circRNAs/ --novel`
**Explanation:** Includes novel circRNAs not present in reference annotation.

### Specify k-mer size
**Args:** `jccirc -i reads.fastq -g ref.gtf -o circRNAs/ -k 25`
**Explanation:** Uses k-mer size of 25 for assembly.

### Filter by read support
**Args:** `jccirc -i reads.fastq -g ref.gtf -o circRNAs/ --min-reads 3`
**Explanation:** Requires minimum 3 supporting reads per circRNA.

### Output in BED format
**Args:** `jccirc -i reads.fastq -g ref.gtf -o circRNAs/ --format bed`
**Explanation:** Outputs circRNA coordinates in BED format.

### Generate visualization
**Args:** `jccirc -i reads.fastq -g ref.gtf -o circRNAs/ --visualize`
**Explanation:** Generates visualization of detected circRNAs.