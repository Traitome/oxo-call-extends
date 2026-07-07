---
name: phasius
category: formatting
description: phasius creates phase-block maps from phased BAM/CRAM files.
tags: [phasius, formatting, phasing, phase-blocks]
author: oxo-call-community
source_url: "https://github.com/wdecoster/phasius"
---

## Concepts

- **Tool Overview**: phasius maps phase blocks.
- **Core Function**: Creates phase-block visualizations.
- **Algorithm**: Uses phased alignment analysis.
- **Input Format**: Accepts phased BAM/CRAM files.
- **Output**: Produces phase-block map files.
- **Use Case**: Phasing visualization, phase-block analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Phasing Quality**: Results depend on phasing quality.
- **Block Detection**: May miss small phase blocks.
- **Runtime**: Mapping may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phasius --help`
**Explanation:** Shows available options and usage instructions.

### Create phase blocks
**Args:** `phasius -i phased.bam -o phase_blocks.txt`
**Explanation:** Creates phase-block map.

### With parameters
**Args:** `phasius -i phased.bam -p params.yaml -o phase_blocks.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phasius -v -i phased.bam -o phase_blocks.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phasius -t 4 -i phased.bam -o phase_blocks.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phasius -i phased.bam -o phase_blocks.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phasius -i phased.bam -o phase_blocks.txt --report report.html`
**Explanation:** Generates HTML report.