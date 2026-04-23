---
name: beav
category: annotation
description: BEAV - Bacterial genome and mobile element annotation pipeline
tags: [bacterial-annotation, mobile-elements, prophage, plasmid]
author: oxo-call-community
source_url: "https://github.com/weisberglab/beav"
---

## Concepts

- **Tool Overview**: BEAV (Bacterial genome and mobile element Annotation Pipeline) annotates bacterial genomes with focus on mobile genetic elements.

- **Mobile Elements**: Specializes in identifying and annotating mobile genetic elements including plasmids, prophages, and integrative elements.

- **Comprehensive Annotation**: Provides standard gene annotation plus mobile element-specific features.

- **Integration Sites**: Identifies integration sites and attachment sites for mobile elements.

## Pitfalls

- **Assembly Quality**: Requires complete or near-complete assemblies for accurate mobile element annotation.

- **Database Dependencies**: Results depend on database completeness for mobile element detection.

- **Novel Elements**: Novel mobile elements may be missed if not in reference databases.

## Examples

### Basic annotation
**Args:** `beav annotate --genome genome.fasta --output annotation/`
**Explanation:** Annotates bacterial genome with mobile element focus.

### Specify output format
**Args:** `beav annotate --genome genome.fasta --format gff3 --output annotation/`
**Explanation:** Outputs annotation in GFF3 format.

### Focus on prophages
**Args:** `beav prophage --genome genome.fasta --output prophages/`
**Explanation:** Identifies and annotates prophage regions specifically.
