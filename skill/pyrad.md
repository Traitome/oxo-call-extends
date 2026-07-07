---
name: pyrad
category: assembly
description: PyRAD assembles and analyzes RADseq (Restriction Site Associated DNA sequencing) data sets.
tags: [pyrad, assembly, radseq, population-genomics]
author: oxo-call-community
source_url: "https://github.com/dereneaton/pyrad"
---

## Concepts

- **Tool Overview**: pyrad assembles RADseq data.
- **Core Function**: RADseq assembly.
- **Algorithm**: Uses sequence clustering.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces loci.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Parameter Tuning**: Affects assembly.
- **Runtime**: Assembly may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyrad --help`
**Explanation:** Shows available options and usage instructions.

### Run assembly
**Args:** `pyrad assemble -i reads.fastq -o output/`
**Explanation:** Assembles RADseq data.

### With parameters
**Args:** `pyrad assemble -i reads.fastq -p params.yaml -o output/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyrad -v assemble -i reads.fastq -o output/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyrad -t 4 assemble -i reads.fastq -o output/`
**Explanation:** Uses 4 threads for parallel processing.

### Demultiplex
**Args:** `pyrad demultiplex -i raw.fastq -b barcodes.txt -o demultiplexed/`
**Explanation:** Separates samples by barcode.

### Generate report
**Args:** `pyrad assemble -i reads.fastq -o output/ --report report.html`
**Explanation:** Generates HTML report.