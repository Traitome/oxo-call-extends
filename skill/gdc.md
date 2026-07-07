---
name: gdc
category: formatting
description: GDC is a utility designed for compression of genome collections from the same species.
tags: [gdc, genome-compression, sequence-data, bioinformatics]
author: oxo-call-community
source_url: "http://sun.aei.polsl.pl/REFRESH/index.php?page=projects&project=gdc&subpage=about"
---

## Concepts
- **Genome Compression**: Specialized compression algorithm for genomic sequence collections.
- **Reference-based Compression**: Uses reference genome to compress related sequences efficiently.
- **Species-specific**: Optimized for compressing multiple genomes from the same species.
- **High Compression Ratio**: Achieves better compression than general-purpose tools.
- **Fast Decompression**: Maintains fast decompression speed while achieving high compression.

## Pitfalls
- **Species Restriction**: Designed specifically for collections from the same species.
- **Reference Dependence**: Requires a reference genome for compression.
- **Format Limitations**: May not support all sequence formats.
- **Memory Usage**: Compression of large genome collections requires significant memory.
- **Preprocessing Required**: Input sequences may need preprocessing (e.g., alignment).

## Examples
### Compress genome collection
**Args:** `gdc compress -r reference.fasta -i genomes/ -o compressed.gdc`
**Explanation:** Compresses a collection of genomes using a reference genome.

### Decompress genome collection
**Args:** `gdc decompress -i compressed.gdc -o decompressed/`
**Explanation:** Decompresses a GDC compressed file to the specified directory.

### Compress with multiple threads
**Args:** `gdc compress -r reference.fasta -i genomes/ -o compressed.gdc -t 4`
**Explanation:** Compresses genome collection using 4 threads for parallel processing.

### Check compressed file info
**Args:** `gdc info -i compressed.gdc`
**Explanation:** Displays information about a compressed GDC file.

### Extract specific genome
**Args:** `gdc extract -i compressed.gdc -n genome_name -o extracted.fasta`
**Explanation:** Extracts a specific genome from the compressed collection.