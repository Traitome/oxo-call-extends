---
name: gffutils
category: database
description: gffutils - Work with GFF and GTF files in a flexible database framework.
tags: [gffutils, database, GFF, GTF, bioinformatics]
author: oxo-call-community
source_url: "http://daler.github.io/gffutils/"
---

## Concepts
- **Database Framework**: Uses database for GFF processing.
- **GFF/GTF Handling**: Handles GFF and GTF formats.
- **Feature Management**: Manages genomic features.
- **Transcript Analysis**: Analyzes transcript data.
- **SQLite Backend**: Uses SQLite for efficient storage.

## Pitfalls
- **Database Size**: Large annotations create large databases.
- **Memory Usage**: Requires significant memory.
- **Format Compatibility**: Requires correct input format.
- **Version Updates**: Database may need updates.
- **Performance**: Complex queries may be slow.

## Examples
### Create database
**Args:** `python -c "import gffutils; db = gffutils.create_db('annotations.gtf', dbf='annotation.db')"`
**Explanation:** Creates GFFutils database.

### Feature iteration
**Args:** `python -c "import gffutils; db = gffutils.Database('annotation.db'); genes = list(db.features_of_type('gene'))"`
**Explanation:** Iterates over genes.

### Get transcripts
**Args:** `python -c "import gffutils; db = gffutils.Database('annotation.db'); transcripts = list(db.features_of_type('transcript'))"`
**Explanation:** Gets transcript features.

### Find by location
**Args:** `python -c "import gffutils; db = gffutils.Database('annotation.db'); features = db.region('chr1:1-10000')"`
**Explanation:** Finds features in region.

### Export to GFF
**Args:** `python -c "import gffutils; db = gffutils.Database('annotation.db'); db.update_db('new.gtf'); db.to_gff('output.gtf')"`
**Explanation:** Exports to GFF format.