---
name: ragtag
category: assembly
description: RagTag provides fast reference-guided genome assembly scaffolding and correction.
tags: [ragtag, assembly, scaffolding, reference-guided]
author: oxo-call-community
source_url: "https://github.com/malonge/RagTag/wiki"
---

## Concepts

- **Tool Overview**: ragtag scaffolds assemblies.
- **Core Function**: Reference-guided scaffolding.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts contigs/scaffolds.
- **Output**: Produces improved assemblies.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Reference Quality**: Affects scaffolding.
- **Parameters**: Must be configured.
- **Runtime**: Scaffolding may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ragtag --help`
**Explanation:** Shows available options and usage instructions.

### Run scaffolding
**Args:** `ragtag scaffold -i contigs.fasta -r reference.fasta -o scaffolds.fasta`
**Explanation:** Scaffolds contigs using reference.

### With parameters
**Args:** `ragtag scaffold -i contigs.fasta -p params.yaml -o scaffolds.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `ragtag -v scaffold -i contigs.fasta -o scaffolds.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `ragtag -t 4 scaffold -i contigs.fasta -o scaffolds.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Correct assembly
**Args:** `ragtag correct -i assembly.fasta -r reference.fasta -o corrected.fasta`
**Explanation:** Corrects assembly using reference.

### Generate report
**Args:** `ragtag scaffold -i contigs.fasta -o scaffolds.fasta --report report.html`
**Explanation:** Generates HTML report.