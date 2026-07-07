---
name: phyphy
category: utility
description: phyphy executes and parses HyPhy analyses.
tags: [phyphy, utility, hyphy, analysis]
author: oxo-call-community
source_url: "https://github.com/sjspielman/phyphy"
---

## Concepts

- **Tool Overview**: phyphy executes HyPhy analyses.
- **Core Function**: HyPhy analysis execution and parsing.
- **Algorithm**: Uses HyPhy analysis methods.
- **Input Format**: Accepts HyPhy data files.
- **Output**: Produces HyPhy analysis results.
- **Use Case**: Phylogenetics, HyPhy analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **HyPhy Analysis**: May have analysis errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phyphy --help`
**Explanation:** Shows available options and usage instructions.

### Execute HyPhy
**Args:** `phyphy -i hyphy_data.txt -o analysis_results.txt`
**Explanation:** Executes HyPhy analysis.

### With parameters
**Args:** `phyphy -i hyphy_data.txt -p params.yaml -o analysis_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phyphy -v -i hyphy_data.txt -o analysis_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phyphy -t 4 -i hyphy_data.txt -o analysis_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phyphy -i hyphy_data.txt -o analysis_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phyphy -i hyphy_data.txt -o analysis_results.txt --report report.html`
**Explanation:** Generates HTML report.