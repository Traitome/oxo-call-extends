---
name: pedesigner
category: utility
description: pedesigner designs prime-editing guideRNAs (pegRNAs).
tags: [pedesigner, utility, prime-editing, grna]
author: oxo-call-community
source_url: "https://github.com/VeredKunik/pedesigner"
---

## Concepts

- **Tool Overview**: pedesigner designs pegRNAs.
- **Core Function**: Generates prime-editing guide RNAs.
- **Algorithm**: Uses pegRNA design algorithms.
- **Input Format**: Accepts target sequence files.
- **Output**: Produces pegRNA designs.
- **Use Case**: Prime editing, genome editing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large target sets require memory.
- **Target Quality**: Results depend on target sequence.
- **Editing Efficiency**: Efficiency predictions may vary.
- **Runtime**: Design may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pedesigner --help`
**Explanation:** Shows available options and usage instructions.

### Design pegRNA
**Args:** `pedesigner -i target.fasta -o pegRNA_designs.txt`
**Explanation:** Designs pegRNAs for targets.

### With mutation
**Args:** `pedesigner -i target.fasta -m mutation.txt -o pegRNA_designs.txt`
**Explanation:** Designs pegRNAs for specific mutation.

### Verbose mode
**Args:** `pedesigner -v -i target.fasta -o pegRNA_designs.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pedesigner -t 4 -i target.fasta -o pegRNA_designs.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pedesigner -i target.fasta -o pegRNA_designs.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pedesigner -i target.fasta -o pegRNA_designs.txt --report report.html`
**Explanation:** Generates HTML report.