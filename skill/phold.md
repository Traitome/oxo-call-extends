---
name: phold
category: metagenomics
description: phold annotates phages using protein structures.
tags: [phold, metagenomics, phage, annotation]
author: oxo-call-community
source_url: "https://github.com/gbouras13/phold"
---

## Concepts

- **Tool Overview**: phold annotates phage proteins.
- **Core Function**: Phage annotation tool.
- **Algorithm**: Uses protein structure analysis.
- **Input Format**: Accepts phage protein files.
- **Output**: Produces phage annotation results.
- **Use Case**: Phage annotation, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Protein Quality**: Results depend on protein quality.
- **Structure Prediction**: May have prediction errors.
- **Runtime**: Annotation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phold --help`
**Explanation:** Shows available options and usage instructions.

### Annotate phages
**Args:** `phold -i phage_proteins.fasta -o annotation_results.txt`
**Explanation:** Annotates phage proteins.

### With parameters
**Args:** `phold -i phage_proteins.fasta -p params.yaml -o annotation_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phold -v -i phage_proteins.fasta -o annotation_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phold -t 4 -i phage_proteins.fasta -o annotation_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phold -i phage_proteins.fasta -o annotation_results.gff --gff`
**Explanation:** Outputs in GFF format.

### Generate report
**Args:** `phold -i phage_proteins.fasta -o annotation_results.txt --report report.html`
**Explanation:** Generates HTML report.