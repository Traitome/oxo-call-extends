---
name: behst
category: annotation
description: BEHST - Genomic set enrichment analysis enhanced through chromatin long-range interactions
tags: [enrichment, chromatin, hi-c, gene-regulation, go-analysis]
author: oxo-call-community
source_url: "https://bitbucket.org/hoffmanlab/behst"
---

## Concepts
- **Tool Overview**: BEHST (Binding Element Enrichment in Hi-C Segments Tool) performs gene set enrichment analysis enhanced by integrating chromatin long-range interactions from Hi-C data. It connects genomic regions to genes through 3D chromatin structure.
- **Workflow**: BEHST takes genomic regions (e.g., ChIP-seq peaks), intersects them with Hi-C chromatin interactions, identifies genes whose regulatory regions are in contact with the input regions, and performs Gene Ontology enrichment analysis via g:Profiler.
- **Regulatory Regions**: Uses APPRIS principal isoform annotations and defines cis-regulatory regions based on transcription start sites with upstream/downstream extensions.
- **Integration**: Combines 1D genomic annotation with 3D chromatin architecture for more biologically relevant enrichment results.

## Pitfalls
- **Hi-C Data Dependency**: Requires appropriate Hi-C dataset for the cell type/tissue being studied.
- **Resolution**: Hi-C interaction resolution affects the accuracy of gene-region associations.
- **Reference Genome**: Must use consistent reference genome versions for all inputs (regions, Hi-C, gene annotations).

## Examples
### Run BEHST analysis
**Args:** `behst --regions peaks.bed --hic interactions.txt --output results/`
**Explanation:** Performs enrichment analysis connecting peaks to genes through Hi-C interactions.

### Specify regulatory region extension
**Args:** `behst --regions peaks.bed --hic interactions.txt --upstream 5000 --downstream 1000`
**Explanation:** Defines regulatory regions as TSS +/- specified distances.
