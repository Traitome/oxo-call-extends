---
name: pretextmap
category: alignment
description: pretextmap converts SAM read pairs into genome contact maps.
tags: [pretextmap, alignment, sam, hi-c]
author: oxo-call-community
source_url: "https://github.com/sanger-tol/PretextMap"
---

## Concepts

- **Tool Overview**: pretextmap creates contact maps from SAM data.
- **Core Function**: Contact map generation.
- **Algorithm**: Uses paired-end mapping methods.
- **Input Format**: Accepts SAM/BAM files.
- **Output**: Produces Pretext contact maps.
- **Use Case**: Hi-C data processing, genome mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Mapping Accuracy**: May have false contacts.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `PretextMap --help`
**Explanation:** Shows available options and usage instructions.

### Generate contact map
**Args:** `PretextMap -i aligned.sam -o contact_map.pretext`
**Explanation:** Converts SAM read pairs to contact map.

### With parameters
**Args:** `PretextMap -i aligned.sam -p params.yaml -o contact_map.pretext`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `PretextMap -v -i aligned.sam -o contact_map.pretext`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `PretextMap -t 4 -i aligned.sam -o contact_map.pretext`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `PretextMap -i aligned.sam -o contact_map.txt --txt`
**Explanation:** Outputs in text format.

### Generate report
**Args:** `PretextMap -i aligned.sam -o contact_map.pretext --report report.html`
**Explanation:** Generates HTML report.