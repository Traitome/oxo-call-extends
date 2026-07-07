---
name: taxonomy_ranks
category: metagenomics
description: Retrieve taxonomy rank information (genus, family, order, etc.) for NCBI taxids or species names using ETE3.
tags: [taxonomy_ranks, ete3, ncbi, taxonomy, taxid, lineage, ranks]
author: oxo-call-community
source_url: "https://github.com/linzhi2013/taxonomy_ranks"
---

## Concepts

- **Tool Overview**: taxonomy_ranks (v0.0.10) - Python tool using ETE3 to retrieve taxonomic rank information (genus, family, order, phylum, etc.) for given NCBI taxonomy IDs or species names. Provides simple interface to ETE3's NCBI Taxonomy functionality.
- **Core Function**: Takes input taxids or species names and outputs lineage information including the rank (superkingdom, kingdom, phylum, class, order, family, genus, species) for each input.
- **Input Types**: Accepts a file with taxids, species names, or higher taxonomic ranks (like "Hominidae" or "Primates") - can be mixed in the same file.
- **Database**: Uses ETE3's NCBI Taxonomy database, which auto-downloads on first use from NCBI. Database stored in `~/.ete3toolkit/` after initial download.
- **Installation**: `pip install taxonomy_ranks` - requires Python 3 and ETE3 package as dependency.
- **Output**: Tab-separated output to stdout or specified file, with optional error file for unresolvable inputs.

## Pitfalls

- **Ambiguous Names**: A name like "Pieris" could refer to butterflies (animals) or plants - taxonomy_ranks will search lineages for all matches and report them separately.
- **Name Fallback**: If exact species name isn't found, taxonomy_ranks tries just the first word (genus name) as a fallback search.
- **First-Run Download**: ETE3 downloads ~600MB database on first run - ensure stable internet connection and wait for completion.
- **Error Output**: Inputs without valid lineage information are written to the error output file (specified with `-e` flag) rather than causing failures.
- **Database Updates**: NCBI Taxonomy updates frequently - use `ete3-ncbiquery --update` to refresh local database for current taxonomy data.
- **Taxid vs Name Mixing**: While the tool accepts both taxids and names, be aware that name lookups are slower than taxid lookups.

## Examples

### Basic help display
**Args:** `taxaranks -h`
**Explanation:** Show all available command-line options and their descriptions.

### Get ranks for taxids in file
**Args:** `taxaranks -i taxids.txt -o lineage.txt`
**Explanation:** Read taxids from input file (one per line) and write lineage information to output file.

### Include taxid in output
**Args:** `taxaranks -i taxids.txt -o lineage.txt -t`
**Explanation:** Add `-t` flag to include the taxid for each rank in the output, making it easier to track which rank belongs to which taxon.

### Verbose mode
**Args:** `taxaranks -i taxids.txt -o lineage.txt -v`
**Explanation:** Enable verbose output to see progress and detailed processing information during execution.

### Handle missing lineages
**Args:** `taxaranks -i taxids.txt -o lineage.txt -e errors.txt`
**Explanation:** Use `-e` flag to specify error output file where inputs without valid lineage will be written.

### Use with species names
**Args:** `echo -e "Homo sapiens\nMus musculus\nArabidopsis thaliana" | taxaranks -o lineage.txt`
**Explanation:** Species names can be input via stdin as well. Each line is resolved to its full taxonomic lineage.

### Query higher taxonomic ranks
**Args:** `echo "Hominidae" | taxaranks -o lineage.txt`
**Explanation:** Query by family or other higher-rank names. Returns lineage for all taxa under that rank.

### Python module usage
**Args:** `from taxonomy_ranks import TaxonomyRanks; tr = TaxonomyRanks("Homo sapiens"); print(tr.get_lineage_taxids_and_taxanames())`
**Explanation:** Can be imported as Python module for programmatic access to taxonomy data.

### Batch processing with taxids
**Args:** `taxaranks -i taxids.tsv -o lineage.tsv -t`
**Explanation:** Input file can be TSV with taxid in first column, output includes corresponding lineages with taxids.
