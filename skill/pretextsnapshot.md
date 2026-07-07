---
name: pretextsnapshot
category: alignment
description: pretextsnapshot generates images from Pretext Hi-C contact maps.
tags: [pretextsnapshot, alignment, visualization, hi-c]
author: oxo-call-community
source_url: "https://github.com/wtsi-hpag/PretextSnapshot"
---

## Concepts

- **Tool Overview**: pretextsnapshot creates visualizations.
- **Core Function**: Image generation.
- **Algorithm**: Uses rendering methods.
- **Input Format**: Accepts Pretext files.
- **Output**: Produces image files.
- **Use Case**: Hi-C visualization, publication.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Rendering Quality**: May have artifacts.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `PretextSnapshot --help`
**Explanation:** Shows available options and usage instructions.

### Generate image
**Args:** `PretextSnapshot -i contact_map.pretext -o image.png`
**Explanation:** Generates image from contact map.

### With parameters
**Args:** `PretextSnapshot -i contact_map.pretext -p params.yaml -o image.png`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `PretextSnapshot -v -i contact_map.pretext -o image.png`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `PretextSnapshot -t 4 -i contact_map.pretext -o image.png`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `PretextSnapshot -i contact_map.pretext -o image.pdf --pdf`
**Explanation:** Outputs in PDF format.

### Generate report
**Args:** `PretextSnapshot -i contact_map.pretext -o image.png --report report.html`
**Explanation:** Generates HTML report.