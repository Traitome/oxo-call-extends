---
name: orthomcl
category: utility
description: OrthoMCL identifies orthologous groups of protein sequences across multiple species.
tags: [orthomcl, utility, orthology, comparative-genomics]
author: oxo-call-community
source_url: "http://orthomcl.org/orthomcl/"
---

## Concepts

- **Tool Overview**: OrthoMCL clusters orthologous proteins into groups.
- **Core Function**: Identifies ortholog groups across species.
- **Algorithm**: Uses Markov Clustering (MCL) algorithm.
- **Input Format**: Accepts FASTA files of protein sequences.
- **Output**: Produces ortholog group assignments.
- **Use Case**: Comparative genomics, gene family analysis, and functional annotation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Database Setup**: Requires MySQL database.
- **Parameter Tuning**: MCL inflation parameter affects results.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `orthomcl --help`
**Explanation:** Shows available options and usage instructions.

### Setup database
**Args:** `orthomclSetupSchema orthomcl.config`
**Explanation:** Sets up OrthoMCL database.

### Load sequences
**Args:** `orthomclLoadBlast orthomcl.config blast_results.txt`
**Explanation:** Loads BLAST results into database.

### Run MCL
**Args:** `orthomclMclToGroups orthomcl.config groups.txt`
**Explanation:** Runs MCL clustering.

### Output groups
**Args:** `orthomclGroupsToFiles orthomcl.config groups.txt fastas/`
**Explanation:** Exports groups to FASTA files.

### Verbose mode
**Args:** `orthomcl -v orthomcl.config`
**Explanation:** Runs with verbose output.

### Cleanup
**Args:** `orthomclCleanup orthomcl.config`
**Explanation:** Cleans up temporary files.