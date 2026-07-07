---
name: evigene
category: programming
description: "A genome informatics project for Evidence Directed Gene Construction for Eukaryotes"
tags: [evigene, programming, gene-prediction, genome-annotation, eukaryotes]
author: oxo-call-community
source_url: "http://arthropods.eugenes.org/EvidentialGene/"
---

## Concepts

- **Tool Overview**: EvidentialGene is a genome informatics project for evidence-directed gene construction in eukaryotes, developed for constructing high-quality gene sets for animals and plants.
- **Core Function**: Integrates multiple sources of evidence including transcript alignments, protein homology, and ab initio predictions to build accurate gene models.
- **Input/Output**: Input: Transcript sequences, protein sequences, genome assembly. Output: Consensus gene models (FASTA, GFF), annotation reports.
- **Algorithm**: Uses evidence-based gene prediction with weighted integration of multiple data types to produce consensus gene structures.
- **Key Features**: Evidence integration, consensus gene building, eukaryotic gene prediction, transcript clustering, alternative splicing analysis.
- **Installation**: `conda install -c bioconda evigene`

## Pitfalls

- **Perl Dependencies**: Requires Perl environment with specific modules.
- **Path Configuration**: Scripts require proper path configuration (EVIGENEHOME).
- **Computation Resources**: Large genomes require significant computational resources.
- **Memory Usage**: May require substantial RAM for large datasets.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Transcript clustering
**Args:** `$EVIGENEHOME/scripts/prot/tr2aacds.pl -i transcripts.fasta -o clustered/`
**Explanation:** Clusters and processes transcript sequences.

### Gene model construction
**Args:** `$EVIGENEHOME/scripts/evigene.pl -g genome.fasta -t transcripts.fasta -p proteins.fasta -o genes.gff`
**Explanation:** Constructs gene models from multiple evidence sources.

### Alternative splicing analysis
**Args:** `$EVIGENEHOME/scripts/as/altSplice.pl -i transcripts.fasta -o splicing_report.txt`
**Explanation:** Analyzes alternative splicing events.

### Batch processing
**Args:** `$EVIGENEHOME/scripts/batch/runEvigene.sh -c config.txt`
**Explanation:** Processes multiple genomes in batch mode.

### Quality assessment
**Args:** `$EVIGENEHOME/scripts/qc/genevalid.pl -i genes.gff -r reference.gff -o validation.txt`
**Explanation:** Validates gene models against reference annotations.