---
name: evidencemodeler
category: annotation
description: "Evidence Modeler combines ab intio gene predictions, protein alignments, and transcript alignments into weighted consensus gene structures."
tags: [evidencemodeler, annotation, gene-prediction, consensus-gene-models, gene-structure]
author: oxo-call-community
source_url: "https://github.com/EVidenceModeler/EVidenceModeler"
---

## Concepts

- **Tool Overview**: Evidence Modeler (EVM) is a software tool that integrates multiple sources of evidence to generate consensus gene structure predictions.
- **Core Function**: Combines ab initio gene predictions, protein alignments, and transcript alignments into weighted consensus gene models.
- **Input/Output**: Input: Gene predictions (GFF/GTF), protein alignments, transcript alignments, weight configuration file. Output: Consensus gene models (GFF/GTF), evidence support metrics.
- **Algorithm**: Uses a weighted consensus approach to integrate different types of evidence, producing more accurate gene structure predictions.
- **Key Features**: Multi-evidence integration, weighted scoring, consensus building, support for multiple input types, detailed reporting.
- **Installation**: `conda install -c bioconda evidencemodeler`

## Pitfalls

- **Evidence Quality**: Results depend on the quality of input evidence.
- **Parameter Tuning**: Weight configuration requires careful tuning.
- **Computation Resources**: Large datasets require significant computational resources.
- **Memory Usage**: May require substantial RAM for large genomes.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic consensus gene prediction
**Args:** `evm --genome genome.fasta --weights weights.txt --output genes.gff`
**Explanation:** Generates consensus gene models from multiple evidence sources.

### With ab initio predictions
**Args:** `evm --genome genome.fasta --weights weights.txt --predictions augustus.gff --output genes.gff`
**Explanation:** Includes ab initio gene predictions in consensus building.

### With protein alignments
**Args:** `evm --genome genome.fasta --weights weights.txt --proteins proteins.gff --output genes.gff`
**Explanation:** Includes protein alignments in consensus building.

### With transcript alignments
**Args:** `evm --genome genome.fasta --weights weights.txt --transcripts transcripts.gff --output genes.gff`
**Explanation:** Includes transcript alignments in consensus building.

### Batch processing
**Args:** `evm --genome genome.fasta --weights weights.txt --input inputs/ --output genes.gff`
**Explanation:** Processes multiple evidence files in batch mode.