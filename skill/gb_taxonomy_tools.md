---
name: gb_taxonomy_tools
category: utility
description: Four utilities for manipulating and visualizing GenBank taxonomic information
tags: [gb_taxonomy_tools, utility, taxonomy, genbank, ncbi, visualization]
author: oxo-call-community
source_url: "https://github.com/spond/gb_taxonomy_tools"
---

## Concepts

- **Tool Overview**: gb_taxonomy_tools is a suite of four C programs that perform manipulations and visualizations on GenBank taxonomic information. The tools convert GenBank IDs to taxonomy IDs, expand taxonomy IDs to full hierarchical classifications, convert classifications to phylogenetic trees, and render trees as PostScript images.
- **Tool 1 - gid-taxid**: Converts GenBank sequence IDs (GIDs) to NCBI Taxonomy IDs. Takes a file mapping GIDs to read counts and outputs triplets (gid, taxid, count). Requires the NCBI-maintained gi_taxid_nucl.dmp.gz mapping file containing millions of entries.
- **Tool 2 - taxonomy-reader**: Takes gid-taxid output and expands each taxonomy ID into the full 22-level NCBI hierarchy (root, superkingdom, kingdom, phylum, class, order, family, genus, species, etc.). Requires NCBI names.dmp and nodes.dmp files from the taxdump.tar.gz archive.
- **Tool 3 - taxonomy2tree**: Converts taxonomy-reader output into two formats: (1) a Newick-formatted tree file with branch lengths representing sample counts, and (2) a tab-separated summary file with counts per taxonomic level. The tree represents the evolutionary hierarchy of the samples.
- **Tool 4 - tree2ps**: Renders Newick trees as PostScript images with configurable depth (how many taxonomic levels to show), font size, maximum leaves to display, and coloring by sample counts. Produces publication-ready vector graphics.
- **Input/Output Chaining**: The tools are designed to be piped together: `gid-taxid input.gid gi_taxid_nucl.dmp | taxonomy-reader names.dmp nodes.dmp | taxonomy2tree output.tree output.summary`. This enables efficient processing without intermediate files.
- **NCBI Taxonomy Files**: All tools require NCBI taxonomy database files downloadable from ftp://ftp.ncbi.nih.gov/pub/taxonomy/. These include gi_taxid_nucl.dmp.gz (22GB+, updated daily), names.dmp (taxonomy names), and nodes.dmp (taxonomy hierarchy).
- **Installation**: Build from source using CMake (`cmake ./ && make install`) or install via Bioconda (`conda install -c bioconda gb_taxonomy_tools`). Requires a C compiler and CMake.

## Pitfalls

- **Large NCBI Files**: The gi_taxid_nucl.dmp.gz file is extremely large (22GB+ compressed). Downloading and decompressing requires significant disk space and time. Ensure you have 50GB+ free space for the full taxdump.
- **File Format Expectations**: gid-taxid expects tab-separated input with format "gid count" (space or tab between fields). The output format is "gid taxid count" (tab-separated). Mismatches cause parsing errors.
- **Memory Consumption**: taxonomy-reader loads names.dmp and nodes.dmp entirely into memory for fast lookups. Ensure adequate RAM (4GB+ recommended) when processing large datasets.
- **Taxonomy Updates**: NCBI taxonomy database is updated daily. Different samples analyzed with outdated taxonomy files may show inconsistent or missing taxonomy assignments. Re-download periodically for longitudinal studies.
- **PostScript Viewer Requirements**: tree2ps produces PostScript (.ps) files which require Ghostscript, Adobe Illustrator, or other PostScript-compatible software to view. Not suitable for direct web display without conversion.

## Examples

### Basic GID to TaxID conversion
**Args:** `gid-taxid test/data/test.gid path/to/gi_taxid_nucl.dmp > test.taxid`
**Explanation:** The fundamental gid-taxid operation reads a file containing GenBank IDs and counts, looks up each GID in the NCBI mapping file, and outputs triplets of gid-taxid-count. For example, input line "160338813 160" becomes "160338813 436308 160" where 436308 is the taxonomy ID for the organism.

### Pipe-based taxonomy expansion
**Args:** `cat input.gid | gid-taxid stdin gi_taxid_nucl.dmp | taxonomy-reader names.dmp nodes.dmp > output.taxonomy`
**Explanation:** This pipeline processes data entirely in memory without intermediate files. First, GIDs are converted to taxonomy IDs, then each taxonomy ID is expanded to the full 22-level NCBI hierarchy. The final output contains one line per input record with the complete lineage from root to species.

### Generate phylogenetic tree from taxonomy
**Args:** `taxonomy2tree taxonomy_output.txt 0 species.tree species.summary 0`
**Explanation:** taxonomy2tree takes taxonomy-reader output and generates two files: a Newick tree file (species.tree) with branch lengths representing sample counts, and a tab-separated summary (species.summary) with counts at each taxonomic level. The "0" parameters mean use all taxonomic levels and no count threshold filtering.

### Visualize tree with depth limit
**Args:** `tree2ps species.tree tree_depth5.ps 5 10 0 1`
**Explanation:** tree2ps renders the Newick tree as PostScript. Parameters: max depth of 5 levels from root, 10pt font size, no limit on leaf count (0), and enable duplicate taxid counting for node coloring. This produces a compact tree showing only higher taxonomic ranks (superkingdom to family).

### Full pipeline for metagenomic sample classification
**Args:** `cat sample.gid | gid-taxid stdin gi_taxid_nucl.dmp | taxonomy-reader names.dmp nodes.dmp | taxonomy2tree stdin 0 sample.tree sample.summary 0 && tree2ps sample.tree sample.ps 0 8 256 0`
**Explanation:** Complete analysis pipeline for converting GID-based metagenomic results into a taxonomic tree and visualization. The sample.gid contains sequence counts from a metagenomic classification, the final PostScript shows the full taxonomic tree with all leaves visible (depth 0 = unlimited) using 8pt font.

### Parse tree output for downstream analysis
**Args:** `awk -F'\t' '{print $2, $3}' species.summary | sort | uniq -c | sort -rn | head -20`
**Explanation:** After running taxonomy2tree, the summary file contains one line per taxonomic group with counts. This awk pipeline extracts the superkingdom and count columns, aggregates duplicate entries, and shows the top 20 most abundant taxonomic groups in the sample.
