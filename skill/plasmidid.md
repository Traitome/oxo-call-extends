---
name: plasmidid
category: annotation
description: plasmidid identifies and reconstructs plasmids.
tags: [plasmidid, annotation, plasmid, reconstruction]
author: oxo-call-community
source_url: "https://github.com/BU-ISCIII/plasmidID"
---

## Concepts

- **Tool Overview**: plasmidid identifies plasmids.
- **Core Function**: Plasmid identification and reconstruction.
- **Algorithm**: Uses mapping-based assembly methods.
- **Input Format**: Accepts BAM/SAM files.
- **Output**: Produces plasmid reconstruction results.
- **Use Case**: Plasmid analysis, bacterial genomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Assembly Accuracy**: May have assembly errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plasmidid --help`
**Explanation:** Shows available options and usage instructions.

### Identify plasmids
**Args:** `plasmidid -i mapping.bam -o plasmids.txt`
**Explanation:** Identifies and reconstructs plasmids.

### With parameters
**Args:** `plasmidid -i mapping.bam -p params.yaml -o plasmids.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plasmidid -v -i mapping.bam -o plasmids.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plasmidid -t 4 -i mapping.bam -o plasmids.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plasmidid -i mapping.bam -o plasmids.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `plasmidid -i mapping.bam -o plasmids.txt --report report.html`
**Explanation:** Generates HTML report.