---
name: prophane
category: annotation
description: prophane annotates metaproteomic search results.
tags: [prophane, annotation, metaproteomics, proteomics]
author: oxo-call-community
source_url: "https://gitlab.com/s.fuchs/prophane/"
---

## Concepts

- **Tool Overview**: prophane annotates proteomics data.
- **Core Function**: Metaproteomic annotation.
- **Algorithm**: Uses database matching methods.
- **Input Format**: Accepts search result files.
- **Output**: Produces annotated results.
- **Use Case**: Metaproteomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Database Quality**: Affects annotation accuracy.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prophane --help`
**Explanation:** Shows available options and usage instructions.

### Annotate results
**Args:** `prophane -i search_results.mzid -o annotated.txt`
**Explanation:** Annotates metaproteomic search results.

### With parameters
**Args:** `prophane -i search_results.mzid -p params.yaml -o annotated.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prophane -v -i search_results.mzid -o annotated.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prophane -t 4 -i search_results.mzid -o annotated.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prophane -i search_results.mzid -o annotated.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `prophane -i search_results.mzid -o annotated.txt --report report.html`
**Explanation:** Generates HTML report.