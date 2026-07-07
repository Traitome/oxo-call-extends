---
name: proteomiqon-proteininference
category: alignment
description: proteomiqon-proteininference maps identified peptides to their putative proteins in shotgun proteomics.
tags: [proteomiqon-proteininference, alignment, proteomics, protein-inference]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/ProteinInference.html"
---

## Concepts

- **Tool Overview**: proteomiqon-proteininference performs protein inference.
- **Core Function**: Peptide-to-protein mapping.
- **Algorithm**: Uses inference algorithms.
- **Input Format**: Accepts PSM results.
- **Output**: Produces protein identifications.
- **Use Case**: Shotgun proteomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Ambiguity**: Shared peptides may cause ambiguity.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `proteomiqon-proteininference --help`
**Explanation:** Shows available options and usage instructions.

### Infer proteins
**Args:** `proteomiqon-proteininference -i psm_results.txt -o protein_inference.txt`
**Explanation:** Maps peptides to proteins.

### With parameters
**Args:** `proteomiqon-proteininference -i psm_results.txt --params params.yaml -o protein_inference.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `proteomiqon-proteininference -v -i psm_results.txt -o protein_inference.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `proteomiqon-proteininference -t 4 -i psm_results.txt -o protein_inference.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `proteomiqon-proteininference -i psm_results.txt -o protein_inference.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `proteomiqon-proteininference -i psm_results.txt -o protein_inference.txt --report report.html`
**Explanation:** Generates HTML report.