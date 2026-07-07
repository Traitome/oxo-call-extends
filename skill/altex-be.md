---
name: altex-be
category: genome-editing
description: Automated sgRNA design for exon skipping using Base Editing technology
tags: [altex-be, sgRNA, exon-skipping, base-editing, CRISPR, genome-editing]
author: oxo-call-community
source_url: "https://github.com/kinari-labwork/AltEx-BE"
---

## Concepts

- **Tool Overview**: AltEx-BE (Alternate Exon Skipping by Base Editing) is a command-line bioinformatics tool that designs sgRNAs to induce targeted exon skipping using Base Editing technology. It automates the workflow from target identification to sgRNA design and off-target evaluation.
- **Core Function**: Parses transcript structures from refFlat files to identify potential exon skipping targets, designs sgRNAs compatible with various base editors (ABE/CBE), and evaluates off-target risk to provide ranked candidate lists.
- **Input/Output**: Inputs: refFlat file, genome FASTA file, gene symbols/RefSeq IDs; Outputs: CSV summary table with sgRNA candidates, BED file for UCSC genome browser visualization.
- **Installation**: Available via Bioconda (`conda install -c conda-forge -c bioconda altex-be`) or PyPI (`pip install AltEx-BE`).
- **Base Editor Support**: Supports custom base editors via command-line parameters or preset editors (target-AID, BE4max, ABE8e), allowing specification of PAM sequence and editing window.

## Pitfalls

- **Genome Assembly Compatibility**: Ensure refFlat and FASTA files correspond to the same genome assembly (e.g., hg38, mm39).
- **FASTA File Completeness**: FASTA files must contain all chromosomes; missing chromosomes will cause processing failures.
- **Editing Window Specification**: The `--be-start` and `--be-end` flags are 1-indexed from the base next to the PAM, not from the start of the sgRNA.
- **Gene Symbol Ambiguity**: Multiple transcripts may exist for a single gene symbol; AltEx-BE analyzes all known transcripts.
- **Off-Target Evaluation**: Output includes off-target metrics but does not perform experimental validation; verify candidates experimentally.

## Examples

### Design sgRNAs using preset base editor
**Args:** `altex-be --refflat-path refFlat.txt --fasta-path genome.fa --output-dir results --gene-symbols BRCA1 --assembly-name hg38 --be-preset ABE8e`
**Explanation:** Designs sgRNAs for the BRCA1 gene using the ABE8e base editor preset, outputting results to the specified directory.

### Design sgRNAs with custom base editor parameters
**Args:** `altex-be --refflat-path refFlat.txt --fasta-path genome.fa --output-dir results --gene-symbols MYGENE --assembly-name hg38 --be-name custom-editor --be-type cbe --be-pam NGG --be-start 17 --be-end 19`
**Explanation:** Designs sgRNAs using a custom CBE editor with NGG PAM and editing window spanning positions 17-19.

### Batch processing multiple genes from file
**Args:** `altex-be --refflat-path refFlat.txt --fasta-path genome.fa --output-dir results --gene-file genes.txt --assembly-name mm39 --be-preset BE4max`
**Explanation:** Processes multiple genes listed in genes.txt (one gene symbol per line) using the BE4max base editor for mouse genome (mm39).

### Using multiple base editors simultaneously
**Args:** `altex-be --refflat-path refFlat.txt --fasta-path genome.fa --output-dir results --gene-symbols TP53 --assembly-name hg38 --be-files editors.csv`
**Explanation:** Designs sgRNAs using multiple base editors defined in editors.csv, allowing comparison across different editor types.

### Using RefSeq IDs instead of gene symbols
**Args:** `altex-be --refflat-path refFlat.txt --fasta-path genome.fa --output-dir results --refseq-ids NM_000546 --assembly-name hg38 --be-preset ABE8e`
**Explanation:** Designs sgRNAs using a RefSeq transcript ID instead of a gene symbol, analyzing all transcripts of the corresponding gene.