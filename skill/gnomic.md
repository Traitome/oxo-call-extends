---
name: gnomic
category: utility
description: Gnomic is a human- and computer-readable grammar for describing microbial genotypes and phenotypes across multiple generations.
tags: [gnomic, utility, genotype, phenotype, microbiology, grammar]
author: oxo-call-community
source_url: "https://github.com/biosustain/gnomic"
---

## Concepts

- **Genotype-Phenotype Grammar**: Gnomic provides a standardized grammar for describing microbial genotypes (genetic changes) and phenotypes (observed traits). The syntax is designed to be both human-readable (like a natural description) and machine-parseable for computational analysis.

- **Feature Description**: The grammar supports describing genomic features with their variants using notation like `feature(variant)`. Multiple variants can be described for a single feature using `feature(variant1+variant2)`.

- **Microbial Genetic Nomenclature**: Gnomic follows established conventions for microbial genetic nomenclature, building on decades of bacterial genetics standards for describing mutations, insertions, deletions, and other genetic changes.

- **Multi-Generation Tracking**: The grammar can track changes across multiple generations, making it suitable for describing evolutionary trajectories, adaptation experiments, or strain lineage information.

- **Python Package**: Gnomic is implemented as a Python package with a parser that can interpret gnomic descriptions programmatically, enabling integration into larger bioinformatics workflows and automated analysis pipelines.

- **Interoperability**: The grammar is designed to bridge experimental notation and computational representation, allowing biologists to write intuitive descriptions that can be directly parsed by analysis scripts.

## Pitfalls

- **Grammar Syntax Strictness**: Gnomic descriptions must follow the defined grammar precisely. Minor syntax errors (missing parentheses, incorrect variant separators) will cause parsing failures.

- **Variant Format Conventions**: Different types of variants (point mutations, insertions, deletions) have specific notation requirements. Using incorrect variant format will result in parsing errors or incorrect interpretation.

- **Feature Naming**: Feature names should follow standard microbial genetics conventions. Non-standard or ambiguous gene names may not be recognized by the parser.

- **Evolutionary Context**: While Gnomic can describe multi-generation changes, it does not infer evolutionary relationships - users must explicitly encode generation information if tracking lineage across experiments.

- **Python API Familiarity**: Effective use of Gnomic as a computational tool requires familiarity with Python programming and the Gnomic package API. Command-line usage may be limited.

## Examples

### Parse a simple genotype description
**Args:** `from gnomic import parse; parse("geneA")`
**Explanation:** The simplest Gnomic expression describes a single feature (gene). This Python API call parses a basic genotype consisting of one gene name, which is interpreted as the presence or reference state of that gene.

### Describe a gene with a point mutation
**Args:** `parse("geneA(mutation)")`
**Explanation:** To describe a variant within a gene, use the format feature(variant). This describes geneA with a mutation variant. The specific mutation details would be encoded according to the variant syntax conventions.

### Describe multiple variants in one gene
**Args:** `parse("geneA(snpA+insertionB)")`
**Explanation:** When a gene has multiple variants, they can be combined using the + separator. This describes geneA with both snpA and insertionB variants present, useful for tracking complex genotypes.

### Track multi-generation changes
**Args:** `parse("geneA>geneA(snp)")`
**Explanation:** The > operator indicates changes across generations. This describes a transition from geneA to geneA with snp, useful for evolutionary or adaptation experiment documentation.

### Compare two genotypes
**Args:** `parse("geneA+geneB")`
**Explanation:** Using + between features describes a genotype with multiple features. This can represent either a pathway (geneA and geneB both present) or a comparison between parental and evolved strains depending on context.

### Use with phenotype descriptions
**Args:** `parse("geneA(snp)>geneA(conserved) phenotype:resistant")`
**Explanation:** Gnomic can combine genotype and phenotype descriptions. This syntax describes geneA changing to a conserved state and associates it with a resistant phenotype, useful for linking genetic changes to observed traits.
