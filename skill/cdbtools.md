---
name: cdbtools
category: sequence-analysis
description: CDB (Constant DataBase) indexing and retrieval tools for FASTA files
tags: [cdbtools, fasta, database, indexing, retrieval]
author: oxo-call-community
source_url: "http://compbio.dfci.harvard.edu/tgi"
---

## Concepts

- **Tool Overview**: cdbtools provides CDB (Constant DataBase) indexing and fast retrieval for FASTA sequence files.
- **Core Function**: Creates indexed databases from FASTA files for rapid sequence lookup.
- **Algorithm**: Uses constant database (CDB) format for fast key-value lookups.
- **Input**: FASTA sequence files.
- **Output**: CDB index files and retrieved sequences.
- **Application**: Rapid sequence retrieval from large sequence databases.
- **Installation**: Install via bioconda: `conda install -c bioconda cdbtools`

## Pitfalls

- **Index Size**: CDB index files can be large for big FASTA databases.
- **One-time Indexing**: Index needs to be rebuilt when FASTA file changes.
- **Memory Usage**: Large databases may require significant memory.
- **FASTA Format**: Requires properly formatted FASTA input.

## Examples

### Create CDB index
**Args:** `cdbfasta input.fasta`
**Explanation:** Creates CDB index for FASTA file, generates .cdb and .idx files.

### Retrieve sequence by ID
**Args:** `cdbyank -a "seq_id" input.fasta.cdb`
**Explanation:** Retrieves sequence with specified ID from CDB index.

### Batch retrieval
**Args:** `cdbyank -f ids.list input.fasta.cdb > retrieved.fasta`
**Explanation:** Retrieves multiple sequences listed in ids.list file.

### Display help
**Args:** `cdbfasta --help`
**Explanation:** Shows available options for cdbfasta.