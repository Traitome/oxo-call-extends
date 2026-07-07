---
name: dammit
category: expression
description: Simple de novo transcriptome annotator
tags: [dammit, expression, transcriptome, annotation, de-novo]
author: oxo-call-community
source_url: "http://dib-lab.github.io/dammit/"
---

## Concepts

- **Tool Overview**: dammit (v1.2+) is a simple de novo transcriptome annotator for quick functional annotation of assembled transcriptomes.
- **Core Function**: Annotates assembled transcripts with protein families, Pfam domains, and functional descriptions.
- **Input/Output**: Input: FASTA transcriptome assembly. Output: Annotations, GFF3 files, statistics.
- **Algorithm**: Uses sequence similarity and profile hidden Markov models (HMMs) for annotation.
- **Key Features**: Quick annotation, multiple databases, BUSCO quality assessment.
- **Installation**: `conda install -c bioconda dammit`

## Pitfalls

- **Database Download**: Requires downloading reference databases (can be large).
- **Transcriptome Quality**: Works best with high-quality transcriptome assemblies.
- **Memory Usage**: Large transcriptomes may require significant memory.
- **Annotation Confidence**: Results depend on database completeness.
- **Naming Conventions**: Output naming may need customization for specific uses.

## Examples

### Annotate transcriptome
**Args:** `dammit annotate transcriptome.fasta --busco`
**Explanation:** Annotate assembled transcriptome with functional annotations.

### Use custom database
**Args:** `dammit annotate assembly.fasta --database custom_db/`
**Explanation:** Annotate using custom reference database.

### Skip BUSCO
**Args:** `dammit annotate assembly.fasta --no-busco`
**Explanation:** Run annotation without BUSCO quality assessment.
