---
name: rebar
category: variant-calling
description: ReBAR detects genomic recombination using mutational barcodes for population genetics.
tags: [rebar, variant-calling, recombination, population-genetics]
author: oxo-call-community
source_url: "https://github.com/phac-nml/rebar"
---

## Concepts

- **Tool Overview**: rebar detects recombination.
- **Core Function**: Recombination detection.
- **Algorithm**: Uses barcode methods.
- **Input Format**: Accepts variant data.
- **Output**: Produces recombination events.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Variant Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rebar --help`
**Explanation:** Shows available options and usage instructions.

### Detect recombination
**Args:** `rebar detect -i variants.vcf -o recombination_events.txt`
**Explanation:** Detects recombination events.

### With parameters
**Args:** `rebar detect -i variants.vcf -p params.yaml -o recombination_events.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rebar -v detect -i variants.vcf -o recombination_events.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rebar -t 4 detect -i variants.vcf -o recombination_events.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With barcode file
**Args:** `rebar detect -i variants.vcf -b barcodes.txt -o recombination_events.txt`
**Explanation:** Uses mutational barcodes.

### Generate report
**Args:** `rebar detect -i variants.vcf -o recombination_events.txt --report report.html`
**Explanation:** Generates HTML report.