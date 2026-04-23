---
name: amrfior
category: annotation
description: AMRfíor - Customisable multi-tool approach for antimicrobial resistance gene detection with coverage-based validation
tags: [amr, antimicrobial-resistance, blast, diamond, bowtie2, bwa, minimap2]
author: oxo-call-community
source_url: "https://github.com/NickJD/AMRfior"
---

## Concepts

- **Tool Overview**: AMRfíor orchestrates multiple alignment tools (BLAST, DIAMOND, Bowtie2, BWA, Minimap2) to search DNA and protein sequences against AMR databases with transparent, coverage-based validation. Version 0.5.1.
- **Multi-Tool Approach**: Uses multiple alignment algorithms to cross-validate AMR gene detections, reducing false positives from any single tool.
- **Coverage-Based Validation**: Validates AMR hits based on alignment coverage, not just sequence identity. Ensures detected genes are substantially present, not just partial matches.
- **Supported Aligners**: BLAST (classic), DIAMOND (fast protein search), Bowtie2 (DNA read mapping), BWA (DNA alignment), Minimap2 (long-read alignment).
- **Database Support**: Compatible with standard AMR databases (CARD, ResFinder, NCBI AMRFinderPlus) in FASTA format.
- **Transparent Reporting**: Provides detailed reports showing which tools detected each AMR gene and alignment coverage metrics.
- **Flexible Configuration**: Customizable thresholds for coverage, identity, and tool agreement requirements.

## Pitfalls

- **Tool Dependencies**: Requires installation of all alignment tools (BLAST, DIAMOND, Bowtie2, BWA, Minimap2) or at least the ones you plan to use.
- **Database Preparation**: AMR databases must be pre-formatted for each aligner (e.g., BLAST database, DIAMOND database, BWA index).
- **Runtime**: Running all five aligners on large datasets is computationally expensive. Consider using subset of tools for faster results.
- **Memory Requirements**: Multiple simultaneous database searches require substantial RAM, especially for large AMR databases.
- **Coverage Thresholds**: Default coverage thresholds may need adjustment based on assembly quality and expected gene completeness.
- **Partial Genes**: Low-coverage hits may represent genuine partial genes (e.g., truncated by assembly boundaries) or false positives.

## Examples

### Basic AMR detection with all tools
**Args:** `amrfior -i assembly.fasta -d card_database.fasta -o results/ --tools blast,diamond,bowtie2,bwa,minimap2`
**Explanation:** Runs all five alignment tools against CARD database. Most comprehensive detection but slowest. Cross-validates results across tools.

### Fast protein-based detection only
**Args:** `amrfior -i proteins.faa -d resfinder_db.fasta -o results/ --tools diamond --min_coverage 0.8 --min_identity 0.9`
**Explanation:** Uses only DIAMOND for fast protein-based AMR detection. 80% minimum coverage and 90% minimum identity thresholds. Fastest option for protein input.

### DNA sequence screening with BLAST
**Args:** `amrfior -i contigs.fasta -d ncbi_amr.fasta -o results/ --tools blast --min_coverage 0.6`
**Explanation:** Screens DNA contigs against NCBI AMRFinderPlus database using BLAST. Lower coverage threshold (60%) for detecting partial genes in fragmented assemblies.

### Long-read based detection
**Args:** `amrfior -i reads.fastq -d card_db.fasta -o results/ --tools minimap2 --min_coverage 0.7`
**Explanation:** Uses Minimap2 for AMR detection directly from long reads (ONT/PacBio). Useful for rapid screening without assembly.

### Combined short-read and assembly analysis
**Args:** `amrfior -i assembly.fasta -d card_db.fasta -o results/ --tools blast,diamond,bowtie2 --reads reads_R1.fastq reads_R2.fastq`
**Explanation:** Combines assembly-based (BLAST, DIAMOND) and read-mapping (Bowtie2) approaches. Read mapping validates assembly-based calls with coverage evidence.

### Adjust validation strictness
**Args:** `amrfior -i assembly.fasta -d card_db.fasta -o results/ --tools blast,diamond --min_tools_agree 2 --min_coverage 0.9`
**Explanation:** Requires at least 2 tools to agree on AMR call and 90% minimum coverage. Stricter validation reduces false positives but may miss genuine partial genes.

### Custom output format
**Args:** `amrfior -i assembly.fasta -d card_db.fasta -o results/ --output_format detailed --include_alignments`
**Explanation:** Detailed output format including full alignment information for each tool. Useful for manual review and validation of borderline calls.