---
name: hgvs
category: bioinformatics
description: HGVS provides parsing, formatting, mapping, and validation of sequence variants following HGVS nomenclature.
tags: [hgvs, variant-nomenclature, bioinformatics]
author: oxo-call-community
source_url: "https://hgvs.readthedocs.io"
---

## Concepts

- **HGVS Nomenclature**: hgvs implements the Human Genome Variation Society nomenclature.

- **Variant Parsing**: Parses variant descriptions into structured objects.

- **Variant Formatting**: Formats variants according to HGVS standards.

- **Variant Mapping**: Maps variants between different reference sequences.

- **Variant Validation**: Validates variant descriptions.

- **Genomic Variants**: Handles various types of genomic variants.

## Pitfalls

- **Reference Sequence**: Requires appropriate reference sequence.

- **Version Compatibility**: Ensure compatibility with reference genome versions.

- **Complex Variants**: Complex variants may require special handling.

- **Ambiguity**: Some variant descriptions may be ambiguous.

- **Database Access**: Some operations require database access.

## Examples

### Parse variant
**Args:** `python -c "import hgvs; var = hgvs.parse('NM_000518.4:c.123A>T')"`
**Explanation:** Parses an HGVS variant description.

### Format variant
**Args:** `python -c "import hgvs; var = hgvs.parse('NM_000518.4:c.123A>T'); print(hgvs.format(var))"`
**Explanation:** Formats a variant object.

### Map variant
**Args:** `python -c "import hgvs; am = hgvs.AssemblyMapper('GRCh37'); var = hgvs.parse('NM_000518.4:c.123A>T'); print(am.c_to_g(var))"`
**Explanation:** Maps coding variant to genomic coordinates.

### Validate variant
**Args:** `python -c "import hgvs; var = hgvs.parse('NM_000518.4:c.123A>T'); print(hgvs.validate(var))"`
**Explanation:** Validates variant description.

### Batch processing
**Args:** `for var in 'c.123A>T', 'c.456del', 'c.789insG'; do python -c "import hgvs; print(hgvs.parse('NM_000518.4:'+var))"; done`
**Explanation:** Processes multiple variants.

### Help command
**Args:** `python -c "import hgvs; help(hgvs)"`
**Explanation:** Shows available functions and usage.