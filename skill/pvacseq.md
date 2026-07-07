---
name: pvacseq
category: variant-calling
description: pVAC-Seq identifies personalized neoantigens from cancer sequencing data for immunotherapy.
tags: [pvacseq, variant-calling, neoantigens, cancer-immunotherapy]
author: oxo-call-community
source_url: "http://pvac-seq.readthedocs.io/"
---

## Concepts

- **Tool Overview**: pvacseq predicts neoantigens.
- **Core Function**: Neoantigen identification.
- **Algorithm**: Uses epitope prediction.
- **Input Format**: Accepts VCF files.
- **Output**: Produces candidate neoantigens.
- **Use Case**: Cancer immunotherapy.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **HLA Typing**: Affects prediction accuracy.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pvacseq --help`
**Explanation:** Shows available options and usage instructions.

### Run pVAC-Seq
**Args:** `pvacseq run -i variants.vcf -e epitopes.txt -o results/`
**Explanation:** Identifies neoantigens from variants.

### With parameters
**Args:** `pvacseq run -i variants.vcf -e epitopes.txt -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pvacseq -v run -i variants.vcf -e epitopes.txt -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pvacseq -t 4 run -i variants.vcf -e epitopes.txt -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Filter by binding affinity
**Args:** `pvacseq run -i variants.vcf -e epitopes.txt -b 500 -o results/`
**Explanation:** Filters by binding affinity threshold.

### Generate report
**Args:** `pvacseq run -i variants.vcf -e epitopes.txt -o results/ --report report.html`
**Explanation:** Generates HTML report.