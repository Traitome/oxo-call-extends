---
name: gfastats
category: assembly
description: gfastats - The swiss army knife for genome assembly statistics.
tags: [gfastats, assembly, statistics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vgl-hub/gfastats"
---

## Concepts
- **Assembly Statistics**: Computes genome assembly statistics.
- **Sequence Analysis**: Analyzes assembly sequences.
- **Quality Assessment**: Assesses assembly quality.
- **Contig Analysis**: Analyzes contig properties.
- **Data Reporting**: Generates comprehensive reports.

## Pitfalls
- **Input Quality**: Requires high-quality assembly data.
- **Format Compatibility**: Requires correct input format.
- **Memory Usage**: Large assemblies require significant memory.
- **Computational Resources**: May require computational resources.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Compute assembly stats
**Args:** `gfastats assembly.fasta -o stats.txt`
**Explanation:** Computes statistics for assembly.

### Detailed output
**Args:** `gfastats assembly.fasta -d -o stats.txt`
**Explanation:** Generates detailed statistics.

### With plot
**Args:** `gfastats assembly.fasta -p -o plot.png`
**Explanation:** Generates assembly statistics plot.

### Batch processing
**Args:** `gfastats -l assemblies.txt -o ./stats/`
**Explanation:** Processes multiple assemblies.

### Compare assemblies
**Args:** `gfastats -c ref.fasta query.fasta -o comparison.txt`
**Explanation:** Compares two assemblies.