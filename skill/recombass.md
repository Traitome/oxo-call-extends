---
name: recombass
category: variant-calling
description: Recombass detects recombination hot/cold spots from SNP matrices using wavelet denoising for population genetics.
tags: [recombass, variant-calling, recombination, wavelet-denoising]
author: oxo-call-community
source_url: "https://github.com/xyfans111/recombass"
---

## Concepts

- **Tool Overview**: recombass detects recombination.
- **Core Function**: Recombination hotspot detection.
- **Algorithm**: Uses wavelet methods.
- **Input Format**: Accepts SNP matrices.
- **Output**: Produces recombination spots.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **SNP Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recombass --help`
**Explanation:** Shows available options and usage instructions.

### Detect recombination
**Args:** `recombass detect -i snp_matrix.txt -o recombination_spots.txt`
**Explanation:** Detects recombination hot/cold spots.

### With parameters
**Args:** `recombass detect -i snp_matrix.txt -p params.yaml -o recombination_spots.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recombass -v detect -i snp_matrix.txt -o recombination_spots.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recombass -t 4 detect -i snp_matrix.txt -o recombination_spots.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With wavelet parameters
**Args:** `recombass detect -i snp_matrix.txt -w daubechies -o recombination_spots.txt`
**Explanation:** Uses wavelet parameters.

### Generate report
**Args:** `recombass detect -i snp_matrix.txt -o recombination_spots.txt --report report.html`
**Explanation:** Generates HTML report.