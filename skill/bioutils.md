---
name: bioutils
category: utility
description: Miscellaneous bioinformatics utilities, lookup tables, and data access
tags: [utilities, bioinformatics, lookup-tables, sequence]
author: oxo-call-community
source_url: "https://github.com/biocommons/bioutils"
---

## Concepts

- **Tool Overview**: BioUtils provides a collection of miscellaneous bioinformatics utilities, lookup tables, and data access functions.
- **Codon Tables**: Standard and alternative genetic code lookup tables.
- **Sequence Utilities**: Common sequence manipulation and conversion functions.
- **Data Access**: Access to reference sequences and standard bioinformatics data.
- **Applications**: Tool development, scripting, data preprocessing.

## Pitfalls

- **Scope**: Not comprehensive; specialized functions may require other tools.
- **Data Versions**: Lookup tables should match reference database versions.

## Examples

### Get codon table
**Args:** `from bioutils import codon_table; print(codon_table.get_codons("ATG")`
**Explanation:** Looks up the amino acid encoded by ATG codon.

### Get genetic code
**Args:** `from bioutils import genetic_codes; print(genetic_codes.get(1))`
**Explanation:** Returns the standard genetic code as a dictionary.

### Get amino acid properties
**Args:** `from bioutils import amino_acid; print(amino_acid.ishydrophobic("VLI"))`
**Explanation:** Checks if amino acid sequence is hydrophobic.