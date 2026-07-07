---
name: taxonkit
category: metagenomics
description: Cross-platform and efficient NCBI Taxonomy Toolkit for querying, filtering, and reformating taxonomy data.
tags: [taxonkit, ncbi, taxonomy, metagenomics, taxid, lineage]
author: oxo-call-community
source_url: "https://github.com/shenwei356/taxonkit"
---

## Concepts

- **Tool Overview**: taxonkit (v0.20.0) - A Cross-platform and Efficient NCBI Taxonomy Toolkit written in Go. Provides fast command-line access to NCBI Taxonomy database for querying lineage, filtering by rank, and converting between taxids and species names.
- **Core Functions**: Main subcommands include: `list` (list all taxa under a given taxid), `lineage` (get full lineage for taxids), `reformat` (format lineage output), `name2taxid` (convert names to taxids), `filter` (filter taxids by rank), `lca` (compute lowest common ancestor).
- **Input/Output**: Most commands accept input from stdin (pipe-friendly) or positional arguments. Output goes to stdout by default or via `-o/--out-file` flag. Supports gzip compression for both input and output.
- **Installation**: `conda install -c bioconda taxonkit` or download binary from GitHub releases
- **Database Setup**: Requires NCBI taxdump.tar.gz data in `$HOME/.taxonkit/` directory. Download from `ftp://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz`
- **Data Format**: Input is typically single-column taxids or names, with `-i/--taxid-field` to specify column for piped data.

## Pitfalls

- **Missing Database**: taxonkit requires taxdump files in `$HOME/.taxonkit/` - without them, all commands will fail. Run `mkdir -p $HOME/.taxonkit && tar -zxvf taxdump.tar.gz -C $HOME/.taxonkit` to set up.
- **Taxid vs Name Input**: `lineage`, `reformat`, `name2taxid`, `filter`, and `lca` commands can take either taxids or species names as input - taxonkit auto-detects based on whether input is numeric.
- **Column Specification**: When piping data, use `-i/--taxid-field` to specify which column contains the taxid/name, otherwise taxonkit expects single-column input.
- **Rank Names in reformat**: The `-r/--rank` flag in `reformat` expects actual NCBI rank names (superkingdom, kingdom, phylum, class, order, family, genus, species, etc.), not arbitrary strings.
- **Empty Results**: Some taxids may have no lineage (like deleted nodes) - these will output empty fields. Use `csvtk` to filter if needed.
- **Threading Overhead**: The `-j/--threads` flag helps with large batch processing but adds overhead for small inputs - use appropriately.

## Examples

### Get lineage for taxids
**Args:** `echo 9606 | taxonkit lineage`
**Explanation:** Simple lineage query for human taxid (9606). Output includes taxid and full lineage chain from root to species.

### Get reformatted lineage with ranks
**Args:** `echo 9606 | taxonkit lineage | taxonkit reformat -r -P`
**Explanation:** Pipeline to get pretty-formatted lineage showing ranks and phylum/species info. The `-r` flag shows rank names, `-P` shows full lineage path.

### List all species under a genus
**Args:** `taxonkit list -i 9606 --show-name --show-rank`
**Explanation:** List all taxa under Homo (taxid 9606), showing scientific names and ranks. Good for getting all subspecies and variants.

### Convert species name to taxid
**Args:** `echo "Homo sapiens" | taxonkit name2taxid`
**Explanation:** Convert scientific name to NCBI taxid. Output includes both genus-level and species-level matches.

### Filter taxids by taxonomic rank
**Args:** `cat taxids.txt | taxonkit filter -L genus -E genus`
**Explanation:** Filter input taxids to only keep those at genus rank. `-L` is lower bound, `-E` is expected rank.

### Compute lowest common ancestor
**Args:** `echo -e "9606\n10090" | taxonkit lca`
**Explanation:** Calculate LCA for human (9606) and mouse (10090). Returns taxid of their common ancestor.

### Batch process with output file
**Args:** `taxonkit lineage -i taxids.txt -o lineages.tsv`
**Explanation:** Process all taxids in file with output to specified file instead of stdout. Supports `.gz` extension for compression.

### Show version and check for updates
**Args:** `taxonkit version`
**Explanation:** Display current version and check if newer version is available on GitHub.

### Generate shell auto-completion
**Args:** `taxonkit genautocomplete bash`
**Explanation:** Generate bash auto-completion script for faster subcommand and flag entry.

### Export lineage with taxonomic ranks
**Args:** `echo 9606 | taxonkit lineage -r -n -L`
**Explanation:** Get lineage with `-r` (show ranks), `-n` (show names), `-L` (show taxids) for comprehensive taxonomy info.
