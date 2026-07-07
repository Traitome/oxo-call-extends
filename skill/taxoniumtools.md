---
name: taxoniumtools
category: population-genomics
description: Tools for generating Taxonium-compatible files from UShER protobuf or Newick format for large tree visualization.
tags: [taxoniumtools, phylogenetics, tree-visualization, covid, sars-cov-2, usher, newick, jsonl]
author: oxo-call-community
source_url: "https://github.com/theosanderson/taxonium"
---

## Concepts

- **Tool Overview**: taxoniumtools (v2.x) - Python toolkit for generating Taxonium-compatible files from phylogenetic tree inputs. Taxonium is a web-based tool for exploring large trees with millions of nodes interactively.
- **Core Functions**: Two main utilities: `usher_to_taxonium` converts UShER protobuf files to Taxonium JSONL format; `newick_to_taxonium` converts Newick format trees for Taxonium visualization.
- **Input Formats**: UShER protobuf (.pb/.pb.gz) or Newick (.nw/.tree) format phylogenetic trees, with optional metadata in TSV/CSV format.
- **Output Format**: Taxonium JSONL format - JSON Lines where first line contains tree metadata, subsequent lines contain node information.
- **Installation**: `pip install taxoniumtools` or `conda install -c bioconda taxoniumtools`
- **Key Features**: Supports metadata annotation, time tree construction with Chronumental, clade typing, tree shearing for error cleanup, and large genome optimization.

## Pitfalls

- **JSON vs JSONL Extension**: Must use `.jsonl` extension (not `.json`) for output files, otherwise Taxonium may try to parse as NextStrain JSON format.
- **Metadata Key Column**: The `--key_column` parameter must match the naming convention in your metadata file. Default is "strain" but often needs adjustment for different datasets.
- **Single Chromosome Limitation**: GenBank reference genome input via `--genbank` currently supports only one chromosome - multi-chromosome genomes will only process the first.
- **Chronumental Requirements**: Using `--chronumental` requires date information in the metadata TSV file - without dates, time tree construction will fail.
- **Shearing Side Effects**: Tree shearing (`--shear`) removes low-frequency branches which may represent real recombinants or rare evolutionary events - review before removing.
- **Large Genome Performance**: For large genomes (like MPXV), use `--only_variable_sites` to reduce index size and improve loading speed.

## Examples

### Convert UShER protobuf to Taxonium
**Args:** `usher_to_taxonium --input tree.pb --output tree.jsonl.gz --metadata samples.tsv --genbank reference.gb --columns strain,country,date`
**Explanation:** Basic conversion with metadata annotation. The metadata TSV should have a column matching the sequence names in the protobuf file.

### Add time tree with Chronumental
**Args:** `usher_to_taxonium --input tree.pb --output tree.jsonl.gz --metadata samples.tsv --genbank reference.gb --columns strain,country,date --chronumental`
**Explanation:** Enables Chronumental time tree construction. Requires date column in metadata. The resulting tree can be explored temporally in Taxonium.

### Shear tree to remove rare branches
**Args:** `usher_to_taxonium --input tree.pb --output tree.jsonl.gz --shear --shear_threshold 500`
**Explanation:** Removes branches representing fewer than 1/500 of total descendants. Useful for cleaning up sequencing errors while preserving real low-frequency lineages.

### Convert Newick format tree
**Args:** `newick_to_taxonium --input tree.nw --output tree.jsonl.gz --metadata samples.tsv --columns strain,source`
**Explanation:** Convert a standard Newick tree file with associated metadata. Useful for taxonomies or non-genome-based phylogenetic trees.

### Large genome optimization
**Args:** `usher_to_taxonium --input large_tree.pb --output tree.jsonl.gz --only_variable_sites`
**Explanation:** For genomes with many positions (like monkeypox), this flag stores only variable positions, dramatically reducing file size and improving Taxonium loading speed.

### Custom clade types
**Args:** `usher_to_taxonium --input tree.pb --output tree.jsonl.gz --clade_types nextstrain,pango`
**Explanation:** When UShER file contains clade annotations, specify them here to preserve classification in Taxonium visualization.

### Use with multiple metadata columns
**Args:** `usher_to_taxonium --input tree.pb --output tree.jsonl.gz --metadata samples.tsv --columns strain,country,date,pangolineage,vaccine_status`
**Explanation:** Multiple metadata columns can be specified as a comma-separated list to enrich node information in Taxonium.
