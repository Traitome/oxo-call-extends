---
name: genbank
category: formatting
description: Python library for parsing and working with GenBank sequence format files.
tags: [genbank, sequence-analysis, bioinformatics, file-parsing]
author: oxo-call-community
source_url: "https://github.com/deprekate/genbank"
---

## Concepts
- **GenBank Parsing**: Parses GenBank flat file format sequences.
- **Sequence Extraction**: Extracts sequence data from GenBank records.
- **Feature Annotation**: Handles gene annotations and features.
- **File Conversion**: Converts GenBank format to other sequence formats.
- **Metadata Extraction**: Extracts metadata like organism, accession, and publication info.

## Pitfalls
- **Format Variations**: GenBank format has multiple variations.
- **Large Files**: Large GenBank files can be memory-intensive.
- **Parsing Errors**: Malformed GenBank files can cause parsing errors.
- **Version Compatibility**: Different NCBI GenBank versions may have format changes.
- **Encoding Issues**: May encounter character encoding issues with some files.

## Examples
### Parse GenBank file
**Args:** `python -c "from genbank import GenBank; gb = GenBank('sequence.gb'); print(gb.accession)"`
**Explanation:** Parses a GenBank file and extracts accession number.

### Extract sequence
**Args:** `python -c "from genbank import GenBank; gb = GenBank('sequence.gb'); print(gb.sequence[:100])"`
**Explanation:** Extracts the first 100 nucleotides from the sequence.

### Get features
**Args:** `python -c "from genbank import GenBank; gb = GenBank('sequence.gb'); print([f.type for f in gb.features])"`
**Explanation:** Lists all feature types in the GenBank record.

### Convert to FASTA
**Args:** `genbank_to_fasta -i input.gb -o output.fasta`
**Explanation:** Converts GenBank file to FASTA format.

### Extract metadata
**Args:** `python -c "from genbank import GenBank; gb = GenBank('sequence.gb'); print(gb.organism)"`
**Explanation:** Extracts organism information from GenBank record.