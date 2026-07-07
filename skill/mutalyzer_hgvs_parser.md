---
name: mutalyzer_hgvs_parser
category: annotation
description: Mutalyzer HGVS variant description parser.
tags: [mutalyzer_hgvs_parser, annotation, hgvs, variant, parser, variant-description]
author: oxo-call-community
source_url: "https://github.com/mutalyzer/hgvs-parser"
---

## Concepts

- **Tool Overview**: Mutalyzer HGVS Parser v0.4.0 is a Python library and command-line tool for parsing and validating HGVS (Human Genome Variation Society) variant description strings. It provides programmatic access to HGVS nomenclature parsing, which is the standard for describing sequence variants.
- **Core Function**: Takes HGVS variant description strings (e.g., `NM_004006.2:c.4375C>T`) and parses them into structured components including reference sequence, variant type, position, and change. Validates syntax against HGVS nomenclature rules.
- **HGVS Nomenclature**: HGVS describes variants using a specific syntax: `Reference:ChangeType.NewPosition`. Examples include `c.` for coding DNA, `g.` for genomic, `p.` for protein, `n.` for non-coding RNA.
- **Input Format**: Accepts any valid HGVS variant string. Examples: `NM_004006.2:c.4375C>T` (substitution), `NM_004006.2:c.4375_4376insG` (insertion), `NM_004006.2:c.4375_4376delGC` (deletion).
- **Output**: Returns structured parsed output including reference sequence ID, variant type, start/end positions, lengths, and variant effect. Also indicates whether the variant is valid according to HGVS rules.
- **Use Case**: Essential for variant database curation, clinical variant interpretation pipelines, and any application requiring standardized variant descriptions.

## Pitfalls

- **HGVS Syntax Complexity**: HGVS has many rules and variant types. Not all valid biological variants have valid HGVS descriptions. The parser will reject syntactically invalid descriptions.
- **Reference Sequence Requirement**: HGVS descriptions require a valid reference sequence accession (e.g., NM_004006.2). The parser validates syntax but does not validate against the actual sequence.
- **Version-Specific**: HGVS descriptions include version numbers (e.g., `NM_004006.2` vs `NM_004006.3`). The parser accepts both but does not check if the variant exists in that version.
- ** Genomic vs Coding**: Genomic (`g.`) and coding (`c.`) coordinates are different. `c.4375` and `g.4375` refer to different positions. Ensure correct coordinate system.
- **Reverse Complement**: For variants on the reverse strand, HGVS descriptions require special notation. The parser handles this but users must be aware of strand conventions.
- **Python Library Usage**: Beyond CLI, Mutalyzer can be imported as a Python library for integration into larger variant processing pipelines.

## Examples

### Parse a substitution variant
**Args:** `parse "NM_004006.2:c.4375C>T"`
**Explanation:** Parses a simple substitution. The variant is on coding DNA sequence NM_004006.2 at position 4375, where C is changed to T.

### Parse an insertion variant
**Args:** `parse "NM_004006.2:c.4375_4376insGTTT"`
**Explanation:** Parses an insertion of GTTT between positions 4375 and 4376. The parser extracts both the position range and inserted sequence.

### Parse a deletion variant
**Args:** `parse "NM_004006.2:c.4375_4378delGTT"`
**Explanation:** Parses a deletion of GTT from positions 4375 to 4378. The parser identifies the deleted sequence and coordinate range.

### Validate variant syntax
**Args:** `parse "chr1:g.12345G>A" --validate`
**Explanation:** Validates whether the variant description follows HGVS syntax rules. Reports specific syntax violations if invalid.

### Python API usage
**Args:** `from mutalyzer_hgvs_parser import parse; result = parse("NM_004006.2:c.4375C>T")`
**Explanation:** Import the parser as a Python module for programmatic use in variant processing pipelines.
