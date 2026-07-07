---
name: fuma
category: expression
description: "FuMa: reporting overlap in RNA-seq detected fusion genes."
tags: [fuma, gene fusion, RNA-seq, fusion detection]
author: oxo-call-community
source_url: "https://github.com/yhoogstrate/fuma/"
---
## Concepts
- **Fusion Gene Detection**: Identifies gene fusions from RNA-seq data.
- **Overlap Reporting**: Reports overlapping fusion calls from multiple tools.
- **Integration**: Combines results from different fusion detection tools.
- **Filtering**: Filters and prioritizes fusion calls.
- **Annotation**: Annotates fusion genes with functional information.

## Pitfalls
- **Input Format**: Requires specific input format from fusion tools.
- **Tool Dependence**: Works with specific fusion detection tools.
- **False Positives**: May report false positive fusions.
- **Memory Usage**: Large datasets require significant memory.
- **Output Interpretation**: Requires careful interpretation of results.

## Examples
### Run fusion analysis
**Args:** `fuma -i fusion_calls.txt -o results/`
**Explanation:** Analyzes fusion calls and generates results.

### With multiple tools
**Args:** `fuma -i tool1.txt tool2.txt tool3.txt -o results/`
**Explanation:** Combines results from multiple fusion detection tools.

### Filter by confidence
**Args:** `fuma -i fusion_calls.txt -c high -o filtered.txt`
**Explanation:** Filters fusion calls to keep only high-confidence calls.

### Annotate fusions
**Args:** `fuma -i fusion_calls.txt --annotate -o annotated.txt`
**Explanation:** Annotates fusion calls with gene information.

### Generate report
**Args:** `fuma -i fusion_calls.txt --report -o report.html`
**Explanation:** Generates HTML report of fusion analysis.