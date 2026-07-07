---
name: pretextannotate
category: annotation
description: pretextannotate annotates Pretext snapshots with size and chromosome information.
tags: [pretextannotate, annotation, hi-c, visualization]
author: oxo-call-community
source_url: "https://github.com/sanger-tol/pretextannotate"
---

## Concepts

- **Tool Overview**: pretextannotate adds annotations to Pretext snapshots.
- **Core Function**: Contact map annotation.
- **Algorithm**: Uses coordinate-based methods.
- **Input Format**: Accepts Pretext snapshot files.
- **Output**: Produces annotated snapshots.
- **Use Case**: Hi-C visualization, genome mapping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Annotation Accuracy**: May have errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pretextannotate --help`
**Explanation:** Shows available options and usage instructions.

### Annotate snapshot
**Args:** `pretextannotate -i snapshot.pretext -o annotated.pretext`
**Explanation:** Annotates Pretext snapshot with chromosome information.

### With parameters
**Args:** `pretextannotate -i snapshot.pretext -p params.yaml -o annotated.pretext`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pretextannotate -v -i snapshot.pretext -o annotated.pretext`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pretextannotate -t 4 -i snapshot.pretext -o annotated.pretext`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pretextannotate -i snapshot.pretext -o annotated.txt --txt`
**Explanation:** Outputs in text format.

### Generate report
**Args:** `pretextannotate -i snapshot.pretext -o annotated.pretext --report report.html`
**Explanation:** Generates HTML report.