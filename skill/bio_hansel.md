---
name: bio_hansel
category: annotation
description: Subtype Salmonella enterica genomes using 33bp k-mer typing schemes
tags: [salmonella, subtyping, k-mer, typing]
author: oxo-call-community
source_url: "https://github.com/phac-nml/biohansel"
---

## Concepts
- **Tool Overview**: bio_hansel subtypes Salmonella enterica genomes using 33bp k-mer typing schemes. It includes schemes for Heidelberg and Enteritidis subtyping.
- **K-mer Typing**: Uses unique 33bp k-mers as subtype signatures for rapid classification.
- **Schemes**: Includes pre-built typing schemes for common Salmonella serovars.
- **Applications**: Foodborne outbreak investigation, epidemiological surveillance, source tracking.

## Pitfalls
- **Scheme Coverage**: Only covers serovars with available typing schemes.
- **Genome Quality**: Incomplete or low-quality genomes may have missing k-mers, affecting typing confidence.
- **Novel Strains**: Novel or divergent strains may not match existing schemes.

## Examples
### Subtype Salmonella genome
**Args:** `bio_hansel -i genome.fa -o subtype_results.tsv`
**Explanation:** Subtypes a Salmonella genome using available typing schemes.

### Use specific scheme
**Args:** `bio_hansel -i genome.fa -s heidelberg -o results.tsv`
**Explanation:** Subtypes using the Heidelberg-specific typing scheme.

### Batch processing
**Args:** `bio_hansel -i genomes/ -o batch_results.tsv`
**Explanation:** Subtypes multiple Salmonella genomes in batch.
