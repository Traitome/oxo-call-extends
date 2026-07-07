---
name: ervdetective
category: annotation
description: "An efficient pipeline for identification and annotation of endogenous retroviruses (ERVs)."
tags: [ervdetective, annotation, ERV, retrotransposons, genome-annotation]
author: oxo-call-community
source_url: "https://github.com/ZhijianZhou01/ervdetective"
---

## Concepts

- **Tool Overview**: ERVdetective is a comprehensive pipeline for identifying and annotating endogenous retroviruses (ERVs) in eukaryotic genomes.
- **Core Function**: Detects ERV sequences in genome assemblies, classifies them into families, and provides detailed annotation including LTRs, gag, pol, and env regions.
- **Input/Output**: Input: Genome assembly (FASTA). Output: ERV annotations (GFF/GTF), consensus sequences, classification reports.
- **Algorithm**: Uses homology-based detection and de novo prediction to identify ERV elements, with classification based on sequence similarity to known ERV families.
- **Key Features**: ERV detection, classification, LTR identification, internal domain annotation, consensus sequence generation, visualization support.
- **Installation**: `conda install -c bioconda ervdetective`

## Pitfalls

- **Genome Quality**: Requires high-quality genome assembly.
- **Database Completeness**: Detection depends on reference ERV database.
- **Computation Time**: Large genomes may require significant processing time.
- **Memory Usage**: May require substantial RAM for large datasets.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic ERV detection
**Args:** `ervdetective -i genome.fasta -o erv_annotations.gff`
**Explanation:** Detects and annotates ERVs in genome assembly.

### With custom database
**Args:** `ervdetective -i genome.fasta -o erv_annotations.gff -d custom_erv_db.fasta`
**Explanation:** Uses custom ERV database for detection.

### Generate consensus sequences
**Args:** `ervdetective -i genome.fasta -o erv_annotations.gff -c consensus.fasta`
**Explanation:** Generates consensus sequences for detected ERVs.

### Detailed annotation
**Args:** `ervdetective -i genome.fasta -o erv_annotations.gff --detailed`
**Explanation:** Outputs detailed annotation with domain information.

### Batch processing
**Args:** `ervdetective -i genomes/ -o results/ --batch`
**Explanation:** Processes multiple genomes in batch mode.