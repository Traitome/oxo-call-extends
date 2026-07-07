---
name: keggcharter
category: expression
description: Visualizes genomic potential and transcriptomic expression into KEGG pathways.
tags: [keggcharter, expression, KEGG, pathways, visualization]
author: oxo-call-community
source_url: "https://github.com/iquasere/KEGGCharter/blob/master/README.md"
---

## Concepts

- **Tool Overview**: keggcharter (v1.1.2) - Visualizes omics data on KEGG pathways.
- **KEGG Integration**: Maps data to KEGG pathway maps.
- **Multi-omics Support**: Handles genomic and transcriptomic data.
- **Visualization**: Generates pathway visualizations with expression data.
- **Pathway Analysis**: Provides pathway enrichment analysis.
- **Interactive Output**: Generates interactive visualizations.

## Pitfalls

- **KEGG Database**: Requires access to KEGG database.
- **Gene Annotation**: Requires proper gene annotation.
- **Data Format**: Specific input format requirements.
- **Internet Access**: May require internet for KEGG access.
- **Memory Usage**: Large datasets require memory.
- **Pathway Coverage**: Not all pathways may be available.

## Examples

### Map expression to KEGG pathways
**Args:** `keggcharter -i expression.txt -o pathways/`
**Explanation:** Maps expression data to KEGG pathways.

### Specify organism
**Args:** `keggcharter -i expression.txt -o pathways/ -o hsa`
**Explanation:** Uses human (hsa) KEGG pathways.

### Generate HTML report
**Args:** `keggcharter -i expression.txt -o report.html -f html`
**Explanation:** Generates HTML report with pathway visualizations.

### Pathway enrichment
**Args:** `keggcharter enrich -i genes.txt -o enrichment.txt`
**Explanation:** Performs KEGG pathway enrichment analysis.

### Custom color scheme
**Args:** `keggcharter -i expression.txt -o pathways/ -c viridis`
**Explanation:** Uses viridis color scheme for visualization.

### Batch processing
**Args:** `keggcharter batch -i samples.txt -o output/`
**Explanation:** Processes multiple samples in batch.