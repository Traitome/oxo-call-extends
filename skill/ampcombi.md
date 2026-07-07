---
name: ampcombi
category: formatting
description: Parsing tool to convert and summarise outputs from multiple antimicrobial peptide (AMP) detection tools
tags: [ampcombi, AMP, antimicrobial-peptides, macrel, ampir, hmmsearch, DRAMP]
author: oxo-call-community
source_url: "https://github.com/paleobiotechnology/AMPcombi"
---

## Concepts

- **Tool Overview**: AMPcombi is a parsing, filtering and annotation workflow for tools predicting AntiMicrobial Peptide (AMP) genes, providing a unified interface to multiple prediction tools.
- **Core Function**: Parses results from multiple AMP prediction tools into a single table, aligns hits against reference AMP databases for functional classification, filters by physio-chemical properties, and clusters AMP hits into families.
- **Input/Output**: Inputs: Protein FASTA files, output files from AMP prediction tools (Ampir, AMPlify, Macrel, HMMsearch, etc.); Outputs: Combined results table, filtered hits, functional annotations, cluster information.
- **Installation**: Available via Bioconda (`conda install -c bioconda ampcombi`) or from source.
- **Supported Tools**: Ampir, AMPlify, Macrel, HMMsearch, EnsembleAMPpred, NeuBI, AMPgram, AMPTransformer.

## Pitfalls

- **Database Availability**: If no database is provided, AMPcombi automatically downloads DRAMP; ensure network connectivity.
- **Input Format**: Input file names must contain sample names for proper tracking.
- **Tool Compatibility**: Requires specific versions of AMP prediction tools; check compatibility before use.
- **SignalP Integration**: SignalP must be installed separately for signal peptide prediction (academic use only).
- **Memory Requirements**: Large datasets may require significant memory; consider splitting large inputs.

## Examples

### Parse AMP prediction results
**Args:** `ampcombi parse -i predictions/ -o results/ -f proteins.faa`
**Explanation:** Parses results from multiple AMP prediction tools in the input directory and generates a combined results table.

### Parse with custom database
**Args:** `ampcombi parse -i predictions/ -o results/ -f proteins.faa --db DRAMP`
**Explanation:** Uses DRAMP database for functional classification of AMP hits.

### Filter by physio-chemical properties
**Args:** `ampcombi filter -i parsed_results.tsv -o filtered.tsv --min-length 10 --max-length 100`
**Explanation:** Filters AMP hits based on length criteria (10-100 amino acids).

### Cluster AMP hits
**Args:** `ampcombi cluster -i filtered.tsv -o clusters/ --min-size 2`
**Explanation:** Clusters AMP hits into families with minimum cluster size of 2.

### Complete workflow
**Args:** `ampcombi full -i predictions/ -o complete_results/ -f proteins.faa --db DRAMP`
**Explanation:** Runs the complete AMPcombi workflow including parsing, filtering, annotation, and clustering.

### Add metadata to results
**Args:** `ampcombi annotate -i parsed.tsv -m metadata.tsv -o annotated.tsv`
**Explanation:** Adds sample metadata to the parsed results table.

### Predict signal peptides
**Args:** `ampcombi signalp -i filtered.tsv -o signalp_results.tsv`
**Explanation:** Predicts signal peptides in AMP sequences using SignalP (requires separate installation).