---
name: gnparser
category: utility
description: GNparser normalizes scientific names and extracts semantic elements for biodiversity informatics applications.
tags: [gnparser, scientific-names, taxonomy, parsing, biodiversity]
author: oxo-call-community
source_url: "https://github.com/gnames/gnparser"
---

## Concepts

- **Scientific Name Parsing**: GNparser parses scientific names into their semantic components (genus, species, infraspecific epithets, authorship, year) and normalizes different lexical variants to a canonical form.

- **Canonical Form Generation**: The parser extracts the canonical form of names by stripping authorship and rank information, enabling comparison of name variants from different sources.

- **Parsing Quality Assessment**: Returns a parsing quality score indicating confidence in the parsed result, useful for filtering low-quality name strings.

- **Multiple Output Formats**: Supports output in JSON (compact and pretty), CSV, and TSV formats for integration with various bioinformatics pipelines.

- **API Integration**: Provides REST API access for programmatic parsing, supporting both GET and POST requests for single and batch processing.

- **Name Type Classification**: Identifies different types of names including binomial, trinomial, hybrid, and cultivar names.

## Pitfalls

- **Name Complexity**: Highly complex names with multiple authors, hybrid indicators, or unusual formatting may produce unexpected results. Validate challenging names manually.

- **Authorship Parsing**: Authors with special characters or non-ASCII characters may not parse correctly. Use canonical form for comparison when authorship is ambiguous.

- **Ambiguous Names**: Homonyms (same name for different taxa) cannot be resolved by parsing alone. Use verification services for taxonomic resolution.

- **Case Sensitivity**: Scientific names follow specific capitalization rules. Ensure input names follow standard botanical or zoological nomenclature conventions.

- **Rate Limits**: The public API has rate limits. For high-volume parsing, consider local installation or batching requests.

## Examples

### Parse a single scientific name
**Args:** `gnparser "Homo sapiens Linnaeus, 1758"`
**Explanation:** Parses the scientific name and returns its semantic components including canonical form, authorship, and parsing quality.

### Output in pretty JSON format
**Args:** `gnparser -f pretty "Quadrella steyermarkii (Standl.) Iltis"`
**Explanation:** Returns parsing results in human-readable JSON format with proper indentation, helpful for debugging and manual inspection.

### Parse names from file
**Args:** `gnparser -i names.txt -o results.json`
**Explanation:** Reads names from a text file (one name per line) and writes parsed results to a JSON output file.

### Batch parse multiple names
**Args:** `gnparser "Pinus sylvestris" "Quercus robur" "Betula pendula"`
**Explanation:** Parses multiple names provided as command-line arguments and returns results for each.

### Get canonical form only
**Args:** `gnparser --format compact "Canis lupus familiaris"`
**Explanation:** Outputs only the compact JSON with canonical form, suitable for programmatic processing and quick comparisons.

### Parse and validate names
**Args:** `gnparser --with-validation "Invalid name"`
**Explanation:** Returns validation information along with parsing results, indicating whether the name conforms to nomenclatural rules.

### Start REST API server
**Args:** `gnparser serve`
**Explanation:** Starts a local REST API server for programmatic name parsing. Access via http://localhost:8778/api/v1/<name>.
