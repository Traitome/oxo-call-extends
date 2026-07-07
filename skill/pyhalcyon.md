---
name: pyhalcyon
category: utility
description: pyhalcyon is an accurate basecaller using encoder-decoder model with monotonic attention.
tags: [pyhalcyon, utility, basecalling, nanopore]
author: oxo-call-community
source_url: "https://github.com/relastle/halcyon"
---

## Concepts

- **Tool Overview**: pyhalcyon performs basecalling.
- **Core Function**: Nanopore basecalling.
- **Algorithm**: Uses encoder-decoder model.
- **Input Format**: Accepts FAST5 files.
- **Output**: Produces FASTQ sequences.
- **Use Case**: Sequencing data processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large models require memory.
- **Model Availability**: Requires trained model.
- **GPU Acceleration**: May need GPU.
- **Runtime**: Basecalling may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyhalcyon --help`
**Explanation:** Shows available options and usage instructions.

### Run basecalling
**Args:** `pyhalcyon basecall -i reads.fast5 -o reads.fastq`
**Explanation:** Performs basecalling on nanopore data.

### With parameters
**Args:** `pyhalcyon basecall -i reads.fast5 -p params.yaml -o reads.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyhalcyon -v basecall -i reads.fast5 -o reads.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyhalcyon -t 4 basecall -i reads.fast5 -o reads.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Use GPU
**Args:** `pyhalcyon --gpu basecall -i reads.fast5 -o reads.fastq`
**Explanation:** Uses GPU for acceleration.

### Generate report
**Args:** `pyhalcyon basecall -i reads.fast5 -o reads.fastq --report report.html`
**Explanation:** Generates HTML report.