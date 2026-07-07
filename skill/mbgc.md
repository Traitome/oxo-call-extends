---
name: mbgc
category: formatting
description: Compresses collections of genomes in FASTA format for efficient storage.
tags: [mbgc, genome-compression, FASTA]
author: oxo-call-community
source_url: "https://github.com/kowallus/mbgc"
---

## Concepts

- **Tool Overview**: mbgc compresses genome collections in FASTA format.
- **Core Function**: Efficiently compresses multiple FASTA sequences.
- **Reference-Based Compression**: Uses reference sequences for compression.
- **Decompression**: Supports lossless decompression.
- **Input/Output**: Accepts FASTA files, produces compressed archives.
- **Installation**: `conda install -c bioconda mbgc`

## Pitfalls

- **Reference Selection**: Reference choice affects compression ratio.
- **Memory Requirements**: Large genome sets require memory.
- **Compression Time**: May be slow for very large datasets.
- **Decompression Speed**: Decompression may be slower than compression.
- **Format Compatibility**: Only supports FASTA format.
- **Parallel Processing**: May not fully utilize multiple cores.

## Examples

### Compress genomes
**Args:** `mbgc compress -i genomes.fasta -o compressed.mbgc`
**Explanation:** Compresses FASTA file.

### Decompress
**Args:** `mbgc decompress -i compressed.mbgc -o genomes.fasta`
**Explanation:** Decompresses archive to FASTA.

### With reference
**Args:** `mbgc compress -i genomes.fasta -r ref.fasta -o compressed.mbgc`
**Explanation:** Uses reference for better compression.

### Compress directory
**Args:** `mbgc compress -d genomes/ -o compressed.mbgc`
**Explanation:** Compresses all FASTA files in directory.

### Help documentation
**Args:** `mbgc --help`
**Explanation:** Displays available commands and options.
