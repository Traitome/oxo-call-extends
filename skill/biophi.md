---
name: biophi
category: annotation
description: BioPhi open-source antibody design platform
tags: [antibody, design, protein-engineering]
author: oxo-call-community
source_url: "https://github.com/Merck/BioPhi"
---

## Concepts
- **Tool Overview**: BioPhi is an open-source antibody design platform for humanizing antibodies, designing antibody sequences, and analyzing antibody properties.
- **Antibody Humanization**: Sapiens method for humanizing antibody sequences while maintaining binding affinity.
- **Design**: OASis method for designing antibody CDR sequences using observed antibody sequences database.
- **Applications**: Therapeutic antibody development, antibody engineering, immunogenicity assessment.

## Pitfalls
- **Database Dependency**: Requires OAS (Observed Antibody Space) database for design features.
- **Experimental Validation**: Computational designs require experimental validation.

## Examples
### Humanize antibody
**Args:** `sapiens humanize --input antibody.fa --output humanized.fa`
**Explanation:** Humanizes an antibody sequence using Sapiens method.

### Design CDR sequences
**Args:** `oasis design --input framework.fa --output designed.fa`
**Explanation:** Designs CDR sequences for a given antibody framework.
