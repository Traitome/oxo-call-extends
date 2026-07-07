---
name: gencube
category: annotation
description: GenCube - Unified search and retrieval of genome assemblies and annotations for sequencing-based experimental data.
tags: [gencube, genome-assembly, annotation, data-retrieval]
author: oxo-call-community
source_url: "https://github.com/snu-cdrc/gencube"
---

## Concepts
- **Genome Assembly Retrieval**: Searches and downloads genome assemblies.
- **Annotation Integration**: Unifies diverse types of genome annotations.
- **Metadata Retrieval**: Retrieves comprehensive metadata for genomes.
- **Data Standardization**: Standardizes genome data formats.
- **Cross-species Comparison**: Facilitates comparative genomics analysis.

## Pitfalls
- **Large Data Downloads**: Genome assemblies can be very large.
- **Internet Dependency**: Requires network access for data retrieval.
- **Format Conversion**: May require format conversion for downstream tools.
- **Version Management**: Multiple genome versions can be confusing.
- **Storage Requirements**: Requires significant storage space.

## Examples
### Search genome assemblies
**Args:** `gencube search -s "Homo sapiens"`
**Explanation:** Searches for human genome assemblies.

### Download genome
**Args:** `gencube download -a GRCh38 -o genome.fasta`
**Explanation:** Downloads GRCh38 genome assembly.

### Get annotations
**Args:** `gencube annotations -a GRCh38 -t gene -o genes.gff`
**Explanation:** Retrieves gene annotations for GRCh38 assembly.

### List available assemblies
**Args:** `gencube list -s "Mus musculus"`
**Explanation:** Lists available mouse genome assemblies.

### Download with metadata
**Args:** `gencube download -a GRCh38 -o genome.fasta -m metadata.json`
**Explanation:** Downloads genome with associated metadata.