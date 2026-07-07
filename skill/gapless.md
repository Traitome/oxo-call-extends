---
name: gapless
category: assembly
description: Gapless assembly improvement tool using long reads.
tags: [gapless, genome assembly, long reads, assembly improvement]
author: oxo-call-community
source_url: "https://github.com/schmeing/gapless"
---

## Concepts
- **Long-read Improvement**: Improves assemblies using long reads.
- **Scaffolding**: Combines scaffolding and gap-closing.
- **Assembly Correction**: Corrects assembly errors.
- **Long-read Technology**: Optimized for PacBio and Oxford Nanopore.
- **Integrated Pipeline**: Combines multiple improvement steps.

## Pitfalls
- **Long-read Quality**: Requires high-quality long reads.
- **Computational Resources**: High computational requirements.
- **Dependency Management**: Requires external tools (minimap2, racon).
- **Assembly Size**: Memory-intensive for large genomes.
- **Error Profile**: Results depend on long-read error profile.

## Examples
### Run gapless
**Args:** `gapless.sh -i assembly.fasta -r reads.fastq -o improved.fasta`
**Explanation:** Improves assembly with long reads.

### Specify minimap2
**Args:** `gapless.sh -i assembly.fasta -r reads.fastq --minimap2 minimap2 -o improved.fasta`
**Explanation:** Specifies minimap2 path.

### Set iterations
**Args:** `gapless.sh -i assembly.fasta -r reads.fastq -n 3 -o improved.fasta`
**Explanation:** Runs 3 improvement iterations.

### With error correction
**Args:** `gapless.sh -i assembly.fasta -r reads.fastq --correct -o improved.fasta`
**Explanation:** Includes error correction step.

### Quiet mode
**Args:** `gapless.sh -i assembly.fasta -r reads.fastq -q -o improved.fasta`
**Explanation:** Runs in quiet mode.