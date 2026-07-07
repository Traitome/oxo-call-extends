---
name: pretextgraph
category: alignment
description: pretextgraph embeds bedgraph data into Pretext contact maps.
tags: [pretextgraph, alignment, bedgraph, hi-c]
author: oxo-call-community
source_url: "https://github.com/sanger-tol/PretextGraph"
---

## Concepts

- **Tool Overview**: pretextgraph integrates bedgraph data.
- **Core Function**: Bedgraph embedding.
- **Algorithm**: Uses overlay methods.
- **Input Format**: Accepts BEDGRAPH files.
- **Output**: Produces enhanced contact maps.
- **Use Case**: Hi-C analysis, data visualization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Overlay Accuracy**: May have alignment issues.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `PretextGraph --help`
**Explanation:** Shows available options and usage instructions.

### Embed bedgraph
**Args:** `PretextGraph -i contact_map.pretext -b data.bedgraph -o enhanced.pretext`
**Explanation:** Embeds bedgraph data into contact map.

### With parameters
**Args:** `PretextGraph -i contact_map.pretext -b data.bedgraph -p params.yaml -o enhanced.pretext`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `PretextGraph -v -i contact_map.pretext -b data.bedgraph -o enhanced.pretext`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `PretextGraph -t 4 -i contact_map.pretext -b data.bedgraph -o enhanced.pretext`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `PretextGraph -i contact_map.pretext -b data.bedgraph -o enhanced.txt --txt`
**Explanation:** Outputs in text format.

### Generate report
**Args:** `PretextGraph -i contact_map.pretext -b data.bedgraph -o enhanced.pretext --report report.html`
**Explanation:** Generates HTML report.