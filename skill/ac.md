---
name: ac
category: utility
description: A lossless compression tool for amino acid sequences using finite-context models
tags: [compression, amino-acid, protein, sequence, lossless]
author: oxo-call-community
source_url: "https://github.com/cobilab/ac"
---

## Concepts

- **Tool Overview**: AC is a state-of-the-art lossless compressor specifically designed for amino acid sequences (proteins), using cooperation between multiple context and substitutional tolerant context models.
- **Core Function**: Compress and decompress protein/amino acid sequence files with high compression ratios while maintaining lossless data integrity.
- **Input/Output**: Input: FASTA or plain text amino acid sequences. Output: `.co` compressed files, decompress back to original format with `AD` tool.
- **Compression Models**: Uses finite-context models with configurable context order, alpha values, and gamma decay factors for both reference and target models.
- **Installation**: Install via bioconda: `conda install -c bioconda ac`

## Pitfalls

- **Two-Step Process**: Compression uses `AC` command, decompression uses `AD` command - they are separate executables.
- **Reference Required**: Compression requires a reference file (`-r`) to load the reference model parameters.
- **Model Parameter Format**: Model parameters must follow exact format: `<c>:<d>:<g>/<m>:<e>:<a>` where c=context order, d=alpha divisor, g=gamma, m=max mutations, e=estimator, a=tolerant gamma.
- **File Extension**: Compressed files get `.co` extension; decompressed files get `.de` extension by default.

## Examples

### Display help and version information
**Args:** `-h`
**Explanation:** Shows all available command line options and usage information.

### Compress a protein sequence file with default settings
**Args:** `-v -l 2 protein_sequences.fasta`
**Explanation:** Compresses the input file with compression level 2 and verbose output for progress monitoring.

### Compress with custom reference model
**Args:** `-v -rm 5:90:0.9/1:50:0.8 -tm 7:100:0.9/2:10:0.85 -r reference.fasta target.fasta`
**Explanation:** Uses custom reference model (context=5, alpha=1/90, gamma=0.9) and target model (context=7, alpha=1/100, gamma=0.9) for compression.

### Compress multiple files
**Args:** `-v -r ref.fasta file1.fasta:file2.fasta:file3.fasta`
**Explanation:** Compresses multiple target files using colon separator, all using the same reference model.

### Create information content file during compression
**Args:** `-e -v -l 3 sequences.fasta`
**Explanation:** Creates an additional `.iae` file containing information content values for each position, useful for analysis.

### Decompress a compressed file
**Args:** `-v sequences.fasta.co`
**Explanation:** Decompresses the `.co` file back to original format using the AD decompression tool.
