---
name: panchip
category: epigenomics
description: PanChIP performs pan-ChIP-seq analysis of peak sets.
tags: [panchip, epigenomics, chip-seq, peaks]
author: oxo-call-community
source_url: "https://github.com/hanjunlee21/PanChIP"
---

## Concepts

- **Tool Overview**: PanChIP analyzes multiple ChIP-seq peak sets together.
- **Core Function**: Identifies common and unique peaks across samples.
- **Algorithm**: Uses statistical methods for peak comparison.
- **Input Format**: Accepts peak files in BED or narrowPeak format.
- **Output**: Produces consensus peaks and differential binding analysis.
- **Use Case**: Epigenomics, transcription factor binding, and histone modification analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Peak Quality**: Results depend on input peak quality.
- **Normalization**: Requires proper normalization between samples.
- **Threshold Selection**: Results depend on significance thresholds.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `panchip --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `panchip -i peaks/*.bed -o results/`
**Explanation:** Analyzes multiple ChIP-seq peak sets.

### With control
**Args:** `panchip -i peaks/*.bed -c controls/*.bed -o results/`
**Explanation:** Uses control samples for comparison.

### Consensus peaks
**Args:** `panchip -i peaks/*.bed -o results/ --consensus`
**Explanation:** Generates consensus peak set.

### Verbose mode
**Args:** `panchip -v -i peaks/*.bed -o results/`
**Explanation:** Runs with verbose output.

### Statistical test
**Args:** `panchip -i peaks/*.bed -t fisher -o results/`
**Explanation:** Uses Fisher's exact test for significance.

### Output format
**Args:** `panchip -i peaks/*.bed -o results.gff --gff`
**Explanation:** Outputs in GFF format.