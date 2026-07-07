---
name: bcbiogff
category: annotation
description: bcbiogff - Read and write GFF/GTF annotation formats with Biopython integration
tags: [bcbiogff, annotation, GFF, GTF, Biopython]
author: oxo-call-community
source_url: "https://github.com/chapmanb/bcbb/blob/master/gff"
---

## Concepts

- **Tool Overview**: bcbiogff (v0.6.6) provides Python utilities for reading and writing Generic Feature Format (GFF) and General Transfer Format (GTF) files with Biopython integration.
- **Core Function**: Parse and generate GFF/GTF annotation files for genomic feature analysis.
- **Biopython Integration**: Seamlessly integrates with Biopython's SeqRecord objects.
- **Format Support**: Supports GFF versions 2, 3 and GTF formats.
- **Feature Manipulation**: Enables filtering, modification, and extraction of genomic features.
- **Input/Output**: Accepts GFF/GTF files; outputs GFF/GTF files or Biopython objects.
- **Installation**: `conda install -c bioconda bcbiogff`.

## Pitfalls

- **Format Variants**: GFF version differences (v2 vs v3) may cause parsing issues.
- **Coordinate Systems**: GFF uses 1-based coordinates; be careful with conversion.
- **Attribute Parsing**: GFF attribute format varies; ensure correct parsing.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Parse GFF file
**Args:** `python -c "from BCBio import GFF; with open('annotation.gff') as f: recs = list(GFF.parse(f))"`
**Explanation:** Parses GFF file into Biopython SeqRecord objects.

### Write GFF file
**Args:** `python -c "from BCBio import GFF; GFF.write(recs, open('output.gff', 'w'))"`
**Explanation:** Writes SeqRecord objects to GFF format.

### Filter by feature type
**Args:** `python -c "from BCBio import GFF; recs = GFF.parse(open('input.gff')); filtered = [r for r in recs if any(f.type == 'exon' for f in r.features)]"`
**Explanation:** Filters records to include only those with exon features.

### Parse with specific GFF version
**Args:** `python -c "from BCBio import GFF; recs = GFF.parse(open('input.gff'), gff_version=3)"`
**Explanation:** Explicitly specifies GFF version 3 for parsing.

### Combine multiple GFF files
**Args:** `python -c "from BCBio import GFF; recs = GFF.parse([open('file1.gff'), open('file2.gff')])"`
**Explanation:** Parses and combines multiple GFF files.

### Convert GFF to GTF
**Args:** `python -c "from BCBio import GFF; recs = GFF.parse(open('input.gff')); GFF.write(recs, open('output.gtf', 'w'), gtf=True)"`
**Explanation:** Converts GFF to GTF format.

### Display help
**Args:** `python -c "from BCBio import GFF; help(GFF.parse)"`
**Explanation:** Shows documentation for the parse function.