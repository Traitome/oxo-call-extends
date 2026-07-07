---
name: goblin
category: annotation
description: Goblin generates trusted proteins to supplement bacterial genome annotation by identifying conserved hypothetical proteins.
tags: [goblin, annotation, bacterial, proteins, genome]
author: oxo-call-community
source_url: "https://github.com/rpetit3/goblin"
---

## Concepts

- **Trusted Protein Generation**: Goblin identifies and generates trusted protein sequences from conserved hypothetical proteins in bacterial genomes, improving annotation completeness.

- **Conserved Hypothetical Proteins**: Focuses on proteins that are conserved across multiple species but lack functional annotation, leveraging evolutionary conservation as evidence for functionality.

- **Homology Detection**: Uses BLAST-based homology searches to identify conserved protein domains and motifs that suggest functional roles.

- **Annotation Integration**: Integrates with existing genome annotation pipelines to add functional predictions for previously unannotated proteins.

- **Phylogenetic Context**: Considers evolutionary relationships when evaluating protein conservation, ensuring annotations are biologically meaningful.

- **Quality Filtering**: Applies quality thresholds to ensure only high-confidence predictions are added to the annotation.

## Pitfalls

- **Database Dependencies**: Requires access to comprehensive protein databases (e.g., UniProt, RefSeq). Outdated databases may reduce prediction accuracy.

- **Conservation Bias**: May miss lineage-specific proteins that are not conserved across multiple species.

- **False Positives**: Highly conserved but non-functional sequences (e.g., pseudogenes) may be incorrectly annotated as functional.

- **Computational Resources**: Large-scale analyses may require significant computational resources for BLAST searches.

- **Annotation Conflicts**: Generated annotations may conflict with existing annotations. Manual review is recommended for critical genes.

## Examples

### Run Goblin on a single genome
**Args:** `goblin -i genome.faa -o annotations.txt`
**Explanation:** Processes a FASTA file of protein sequences and generates functional annotations for conserved hypothetical proteins.

### Use custom database
**Args:** `goblin -i genome.faa -d custom_db.fasta -o results.txt`
**Explanation:** Uses a custom protein database instead of the default database for homology searches.

### Set conservation threshold
**Args:** `goblin -i genome.faa -t 0.8 -o annotations.txt`
**Explanation:** Sets a minimum conservation threshold of 80% identity for considering proteins as conserved.

### Batch process multiple genomes
**Args:** `goblin -d genomes_dir/ -o output_dir/`
**Explanation:** Processes all FASTA files in the genomes_dir directory and saves individual results to output_dir.

### Include domain analysis
**Args:** `goblin -i genome.faa --domains -o annotations_with_domains.txt`
**Explanation:** Performs protein domain analysis in addition to homology searches for more detailed functional predictions.

### Generate summary report
**Args:** `goblin -i genome.faa --summary -o summary.txt`
**Explanation:** Generates a summary report with statistics on annotation improvements and prediction confidence.

### Filter by protein length
**Args:** `goblin -i genome.faa --min-length 50 --max-length 1000 -o filtered.txt`
**Explanation:** Filters proteins by length, only analyzing proteins between 50 and 1000 amino acids long.