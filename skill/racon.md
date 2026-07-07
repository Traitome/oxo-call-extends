---
name: racon
category: assembly
description: Racon is an ultrafast consensus module for raw de novo genome assembly of long uncorrected reads.
tags: [racon, assembly, consensus, long-reads]
author: oxo-call-community
source_url: "https://github.com/lbcb-sci/racon/blob/1.5.0/README.md"
---

## Concepts

- **Tool Overview**: racon generates consensus sequences.
- **Core Function**: Consensus assembly.
- **Algorithm**: Uses partial order alignment.
- **Input Format**: Accepts reads and mappings.
- **Output**: Produces consensus sequences.
- **Use Case**: Genome assembly.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Coverage**: Must be sufficient.
- **Parameters**: Must be configured.
- **Runtime**: Assembly may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `racon --help`
**Explanation:** Shows available options and usage instructions.

### Run consensus
**Args:** `racon consensus -i reads.fastq -m mappings.paf -d draft.fasta -o consensus.fasta`
**Explanation:** Generates consensus sequence.

### With parameters
**Args:** `racon consensus -i reads.fastq -p params.yaml -o consensus.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `racon -v consensus -i reads.fastq -o consensus.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `racon -t 4 consensus -i reads.fastq -o consensus.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Multiple rounds
**Args:** `racon consensus -i reads.fastq -r 3 -o consensus.fasta`
**Explanation:** Runs multiple polishing rounds.

### Generate report
**Args:** `racon consensus -i reads.fastq -o consensus.fasta --report report.html`
**Explanation:** Generates HTML report.