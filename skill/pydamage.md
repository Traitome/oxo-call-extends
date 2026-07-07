---
name: pydamage
category: utility
description: pydamage estimates damage parameters for ancient DNA sequencing data.
tags: [pydamage, utility, ancient-dna, damage-analysis]
author: oxo-call-community
source_url: "https://github.com/maxibor/pydamage"
---

## Concepts

- **Tool Overview**: pydamage analyzes DNA damage.
- **Core Function**: Damage parameter estimation.
- **Algorithm**: Uses statistical modeling.
- **Input Format**: Accepts BAM files.
- **Output**: Produces damage estimates.
- **Use Case**: Ancient DNA analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **Data Quality**: Results depend on input quality.
- **Sample Age**: Affects damage patterns.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pydamage --help`
**Explanation:** Shows available options and usage instructions.

### Run damage analysis
**Args:** `pydamage analyze -i aligned.bam -o damage_results/`
**Explanation:** Analyzes DNA damage patterns.

### With parameters
**Args:** `pydamage analyze -i aligned.bam -p params.yaml -o damage_results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pydamage -v analyze -i aligned.bam -o damage_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pydamage -t 4 analyze -i aligned.bam -o damage_results/`
**Explanation:** Uses 4 threads for parallel processing.

### Plot damage
**Args:** `pydamage plot -i damage_results/ -o plot.png`
**Explanation:** Generates damage plot.

### Generate report
**Args:** `pydamage analyze -i aligned.bam -o damage_results/ --report report.html`
**Explanation:** Generates HTML report.