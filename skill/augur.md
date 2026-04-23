---
name: augur
category: variant-calling
description: Augur - Bioinformatics toolkit for phylogenetic analysis of pathogen genomes in Nextstrain pipeline
tags: [nextstrain, phylogenetics, pathogen-evolution, outbreak-tracking, viral-genomics]
author: oxo-call-community
source_url: "https://github.com/nextstrain/augur"
---

## Concepts

- **Tool Overview**: Augur is a bioinformatics toolkit for processing pathogen genome data as part of the Nextstrain platform. It provides modular commands for filtering, aligning, building phylogenetic trees, and annotating evolutionary analyses.

- **Workflow Pipeline**: Standard workflow follows: parse → filter → align → tree → refine → ancestral → translate → export. Each step is a separate augur command that can be combined in workflows.

- **Modular Design**: Each augur command performs a specific task and can be used independently or combined in Snakemake/Nextflow workflows for reproducible analyses.

- **Auspice Integration**: Output is designed to be visualized by Auspice, the Nextstrain visualization tool, producing interactive phylogenetic displays.

- **Multiple Entry Points**: Can start from different stages - raw sequences, pre-aligned sequences, or existing phylogenetic trees, allowing flexibility in analysis pipelines.

- **Temporal Analysis**: Includes tools for time-resolved phylogenetic analysis, estimating molecular clock rates, and dating internal nodes.

- **Metadata Integration**: Works with tabular metadata files containing sample information (dates, locations, host information) to enable rich contextual analysis.

## Pitfalls

- **Date Format Requirements**: Sample dates must be in ISO format (YYYY-MM-DD) or ambiguous formats (YYYY-MM-XX, YYYY-XX-XX) for proper temporal analysis.

- **Sequence Naming**: Sequence names in FASTA files must match exactly with strain names in metadata files. Case sensitivity matters.

- **Reference Sequence**: Alignment requires a reference sequence. Ensure the reference is appropriate for your pathogen and analysis goals.

- **Tree Rooting**: Time-resolved trees require proper rooting. Use --root option or let augur infer the root, but verify biological plausibility.

- **Genetic Diversity**: For highly diverse datasets, standard alignment parameters may fail. Adjust --min-length and other filtering parameters.

- **Memory Usage**: Large datasets (thousands of sequences) can require significant memory, especially for tree building steps.

- **Metadata Completeness**: Missing metadata (especially dates and locations) reduces the utility of temporal and geographic analyses.

## Examples

### Filter sequences by date and region
**Args:** `augur filter --sequences sequences.fasta --metadata metadata.tsv --output filtered.fasta --min-date 2020-01-01 --region Asia --max-date 2020-12-31`
**Explanation:** Filters sequences to include only those from Asia collected between January and December 2020.

### Subsample sequences for diversity
**Args:** `augur filter --sequences sequences.fasta --metadata metadata.tsv --output subsampled.fasta --group-by country year --sequences-per-group 50`
**Explanation:** Subsamples up to 50 sequences per country per year to maintain geographic and temporal diversity while reducing dataset size.

### Multiple sequence alignment
**Args:** `augur align --sequences filtered.fasta --reference-sequence reference.fasta --output aligned.fasta --fill-gaps`
**Explanation:** Aligns sequences to reference genome, filling gaps to maintain consistent coordinates across all sequences.

### Build phylogenetic tree
**Args:** `augur tree --alignment aligned.fasta --output tree.nwk --method iqtree --nthreads 8`
**Explanation:** Constructs maximum-likelihood phylogenetic tree using IQ-TREE with 8 threads for parallel computation.

### Refine tree with temporal information
**Args:** `augur refine --tree tree.nwk --alignment aligned.fasta --metadata metadata.tsv --output-tree refined_tree.nwk --output-node-data node_data.json --timetree --coalescent opt --date-confidence`
**Explanation:** Refines tree with temporal resolution, estimates molecular clock, and calculates confidence intervals for node dates.

### Ancestral sequence reconstruction
**Args:** `augur ancestral --tree refined_tree.nwk --alignment aligned.fasta --output-node-data ancestral.json --inference joint`
**Explanation:** Reconstructs ancestral sequences at internal nodes using joint maximum likelihood inference.

### Translate to amino acids
**Args:** `augur translate --tree refined_tree.nwk --ancestral-sequences ancestral.json --reference-sequence reference.gb --output-node-data aa_muts.json --genes S N M`
**Explanation:** Translates nucleotide sequences to amino acids for specified genes (S, N, M), identifying amino acid mutations.

### Export for Auspice visualization
**Args:** `augur export --tree refined_tree.nwk --metadata metadata.tsv --node-data node_data.json ancestral.json aa_muts.json --output auspice.json --title "SARS-CoV-2 Evolution"`
**Explanation:** Exports all analysis results in JSON format compatible with Auspice visualization, with custom title.

### Mask problematic sites
**Args:** `augur mask --sequences sequences.fasta --mask mask.bed --output masked.fasta`
**Explanation:** Masks problematic sites (e.g., homoplasic sites, primer regions) specified in BED file before alignment.

### Calculate clade frequencies
**Args:** `augur frequencies --method kde --tree refined_tree.nwk --metadata metadata.tsv --output frequencies.json`
**Explanation:** Estimates clade frequencies over time using kernel density estimation for temporal dynamics analysis.
