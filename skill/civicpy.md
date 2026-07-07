---
name: civicpy
category: variant-calling
description: CIViC variant knowledgebase analysis toolkit
tags: [civicpy, variant-annotation, cancer, knowledgebase, bioinformatics]
author: oxo-call-community
source_url: "https://docs.civicpy.org/en/latest"
---

## Concepts

- **Tool Overview**: civicpy is a Python toolkit for accessing and analyzing the CIViC (Clinical Interpretation of Variants in Cancer) knowledgebase, which contains expert-curated interpretations of cancer variants.
- **Core Function**: Provides programmatic access to CIViC database, enabling querying of variant annotations, clinical interpretations, and evidence items.
- **Features**: Variant lookup, evidence retrieval, clinical significance assessment, and integration with other bioinformatics tools.
- **Input**: Variant identifiers (HGVS, VCF, or genomic coordinates).
- **Output**: Structured variant data with clinical interpretations, evidence levels, and supporting citations.
- **Application**: Cancer variant analysis, precision medicine, and clinical variant interpretation.
- **Installation**: Install via bioconda: `conda install -c bioconda civicpy` or pip: `pip install civicpy`

## Pitfalls

- **Network Access**: Requires internet access to query CIViC database.
- **Database Updates**: Data may not reflect the latest CIViC updates immediately.
- **Variant Format**: Requires proper variant representation (HGVS or VCF format).
- **Evidence Quality**: Clinical interpretations should be validated with primary sources.
- **API Rate Limits**: May be subject to API rate limits for frequent queries.

## Examples

### Query variant by HGVS
**Args:** `from civicpy import civic; variant = civic.get_variant_by_hgvs("BRAF p.V600E")`
**Explanation:** Retrieves CIViC information for BRAF V600E variant.

### Search variants by gene
**Args:** `from civicpy import civic; variants = civic.get_variants_by_gene("EGFR")`
**Explanation:** Retrieves all CIViC variants for the EGFR gene.

### Get clinical evidence
**Args:** `from civicpy import civic; evidence = civic.get_evidence_items(variant_id=123)`
**Explanation:** Retrieves clinical evidence items for a specific variant.

### Export to VCF
**Args:** `from civicpy import civic; civic.export_to_vcf(variants, "output.vcf")`
**Explanation:** Exports variants to VCF format with CIViC annotations.