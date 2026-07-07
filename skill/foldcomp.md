---
name: foldcomp
category: formatting
description: "Foldcomp: a library and format for compressing and indexing large protein structure sets."
tags: [foldcomp, protein structure, compression, indexing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/steineggerlab/foldcomp"
---
## Concepts
- **Protein Structure Compression**: Efficiently compresses 3D protein structures (PDB, mmCIF) into compact binary format.
- **Structure Indexing**: Creates searchable indexes for large structure databases like AlphaFold DB.
- **Similarity Search**: Enables fast structural similarity searches using compressed representations.
- **MMseqs2 Integration**: Built on the MMseqs2 framework for scalable sequence and structure analysis.
- **Lossy/Lossless Modes**: Supports both lossy (for faster search) and lossless (for exact preservation) compression.

## Pitfalls
- **Compression Artifacts**: Lossy compression modes may introduce small structural deviations.
- **Memory Requirements**: Indexing very large structure databases requires significant RAM.
- **Format Conversion**: Some specialized PDB formats may require preprocessing before compression.
- **Search Sensitivity**: Fast search modes may miss distant structural homologs.
- **Output Compatibility**: Compressed .fc format requires foldcomp for decompression.

## Examples
### Compress a single PDB file
**Args:** `foldcomp compress input.pdb output.fc`
**Explanation:** Compresses a PDB file into the foldcomp binary format.

### Create database index
**Args:** `foldcomp index structures/ db_index --threads 8`
**Explanation:** Creates an indexed database from a directory of structure files using 8 threads.

### Search for similar structures
**Args:** `foldcomp search query.pdb db_index results.tsv`
**Explanation:** Searches for structurally similar proteins in the indexed database.

### Decompress structures
**Args:** `foldcomp decompress compressed.fc output.pdb`
**Explanation:** Decompresses a foldcomp file back to PDB format.

### Batch compress multiple files
**Args:** `foldcomp compress --batch input_dir/ output_dir/`
**Explanation:** Batch compresses all structure files in a directory.