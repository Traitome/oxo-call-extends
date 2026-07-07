---
name: gene-fetch
category: data-retrieval
description: GeneFetch - High-throughput NCBI Sequence Retrieval Tool for downloading sequences from NCBI databases.
tags: [gene-fetch, ncbi, sequence-retrieval, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bge-barcoding/gene_fetch"
---

## Concepts
- **NCBI Database Access**: Accesses NCBI sequence databases.
- **Batch Retrieval**: Supports high-throughput sequence retrieval.
- **Sequence Download**: Downloads sequences in various formats.
- **Accession Handling**: Processes GenBank accession numbers.
- **Format Conversion**: Converts sequences to different formats.

## Pitfalls
- **Network Dependency**: Requires internet connection.
- **Rate Limiting**: NCBI imposes rate limits on downloads.
- **Large Datasets**: May require significant storage.
- **Format Compatibility**: Ensure output format matches downstream tools.
- **Accession Validation**: Invalid accessions can cause errors.

## Examples
### Fetch single sequence
**Args:** `gene-fetch -a NM_000518 -o BRCA1.fasta`
**Explanation:** Downloads sequence for BRCA1 gene.

### Batch fetch sequences
**Args:** `gene-fetch -l accessions.txt -o sequences/`
**Explanation:** Downloads multiple sequences from accession list.

### Fetch in GenBank format
**Args:** `gene-fetch -a NM_000518 -f genbank -o BRCA1.gb`
**Explanation:** Downloads sequence in GenBank format.

### Fetch protein sequences
**Args:** `gene-fetch -a NP_000509 -db protein -o BRCA1_protein.fasta`
**Explanation:** Downloads protein sequence from Protein database.

### Fetch with taxonomy filter
**Args:** `gene-fetch -l accessions.txt -t 9606 -o human_sequences/`
**Explanation:** Filters sequences by taxonomy ID (human).

