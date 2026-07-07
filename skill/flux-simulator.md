---
name: flux-simulator
category: expression
description: "FLUX Simulator models RNA-Seq experiments in silico, generating realistic synthetic sequencing data for testing and validation."
tags: [flux-simulator, expression, rna-seq, simulation, bioinformatics, sequencing]
author: oxo-call-community
source_url: "http://sammeth.net/confluence/display/SIM/Home"
---

## Concepts
- **Tool Overview**: FLUX Simulator generates realistic synthetic RNA-Seq reads by modeling the entire sequencing process from transcription to sequencing.
- **Core Function**: Simulates RNA-Seq experiments to create synthetic datasets for testing bioinformatics tools and pipelines.
- **Input/Output**: Input: Genome annotation (GTF), expression profiles, sequencing parameters. Output: Synthetic FASTQ reads, expression truth values.
- **Biological Realism**: Models biological processes including transcription, splicing, polyadenylation, and degradation.
- **Technical Variation**: Simulates sequencing errors, GC bias, fragment length distribution, and sequencing depth variations.
- **Expression Profiles**: Supports both uniform and realistic expression distributions based on real data.
- **Installation**: `conda install -c bioconda flux-simulator` or download from official website.

## Pitfalls
- **Annotation Requirements**: Requires high-quality genome annotation. Incomplete annotations produce unrealistic simulations.
- **Parameter Complexity**: Many parameters require careful tuning for realistic results. Start with defaults.
- **Computational Time**: Complex simulations can be computationally intensive. Use appropriate resources.
- **Memory Usage**: Large genomes or high coverage simulations require significant memory.
- **Read Length**: Simulated read length must match the target sequencing platform.
- **Fragment Size**: Fragment size distribution affects simulation realism. Validate against real data.

## Examples
### Basic RNA-Seq simulation
**Args:** `flux-simulator -g genome.fa -a annotation.gtf -o simulated_reads`
**Explanation:** Generates synthetic RNA-Seq reads using default parameters.

### Custom coverage
**Args:** `flux-simulator -g genome.fa -a annotation.gtf -o simulated_reads -c 50`
**Explanation:** Simulates RNA-Seq with 50x coverage.

### Strand-specific simulation
**Args:** `flux-simulator -g genome.fa -a annotation.gtf -o simulated_reads --strand-specific`
**Explanation:** Generates strand-specific RNA-Seq reads.

### Paired-end simulation
**Args:** `flux-simulator -g genome.fa -a annotation.gtf -o simulated_reads --paired-end --read-length 150`
**Explanation:** Simulates paired-end reads with 150bp read length.

### With expression profile
**Args:** `flux-simulator -g genome.fa -a annotation.gtf -o simulated_reads -e expression.txt`
**Explanation:** Uses custom expression profile for simulation.
