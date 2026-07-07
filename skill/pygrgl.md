---
name: pygrgl
category: programming
description: pygrgl is the Genotype Representation Graph Library for efficient storage of large genetic datasets.
tags: [pygrgl, programming, genotype, graph-library]
author: oxo-call-community
source_url: "https://grgl.readthedocs.io/en/stable/"
---

## Concepts

- **Tool Overview**: pygrgl handles genotype data.
- **Core Function**: Genotype storage/query.
- **Algorithm**: Uses graph representation.
- **Input Format**: Accepts VCF/PLINK files.
- **Output**: Produces genotype queries.
- **Use Case**: Genetic data analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Graph Construction**: May take time.
- **Query Complexity**: Affects performance.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pygrgl --help`
**Explanation:** Shows available options and usage instructions.

### Build graph
**Args:** `pygrgl build -i genotypes.vcf -o graph.grgl`
**Explanation:** Builds genotype graph from VCF.

### With parameters
**Args:** `pygrgl build -i genotypes.vcf -p params.yaml -o graph.grgl`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pygrgl -v build -i genotypes.vcf -o graph.grgl`
**Explanation:** Runs with verbose output.

### Query graph
**Args:** `pygrgl query -g graph.grgl -r chr1:1-100000 -o results.txt`
**Explanation:** Queries genotype graph.

### Export data
**Args:** `pygrgl export -g graph.grgl -o genotypes.vcf`
**Explanation:** Exports graph to VCF.

### Generate report
**Args:** `pygrgl build -i genotypes.vcf -o graph.grgl --report report.html`
**Explanation:** Generates HTML report.