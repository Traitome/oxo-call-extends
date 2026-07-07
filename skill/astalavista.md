---
name: astalavista
category: expression
description: AStalavista - Extract alternative splicing events from genomic annotations
tags: [astalavista, expression, alternative-splicing, splicing-events, bioinformatics]
author: oxo-call-community
source_url: "http://sammeth.net/confluence/display/ASTA/Home"
---

## Concepts

- **Tool Overview**: AStalavista extracts alternative splicing (AS) events from genomic annotations of exon-intron gene coordinates. Version 4.0.
- **Core Function**: Detects variations in splicing structures by comparing transcript annotations and assigns standardized AS codes to each detected event.
- **Alternative Splicing Detection**: Identifies various types of alternative splicing events including exon skipping, alternative donor sites, alternative acceptor sites, mutually exclusive exons, and retained introns.
- **AS Code System**: Assigns standardized AS codes to each detected splicing event for consistent classification and comparison.
- **Annotation Analysis**: Processes gene annotations to compare transcript structures and identify splicing variations.
- **Input/Output**: Accepts GFF/GTF annotation files, outputs detected splicing events with AS codes.
- **Installation**: `conda install -c bioconda astalavista` or download from project website.

## Pitfalls

- **Annotation Quality**: Requires high-quality gene annotations. Poor annotations produce unreliable results.
- **Format Requirements**: Input must be properly formatted GFF/GTF files. Invalid formats cause parsing errors.
- **Transcript Coverage**: Requires comprehensive transcript annotations to detect all splicing events.
- **Version Compatibility**: Different annotation versions may produce different results.
- **Complex Loci**: Highly complex gene loci with many transcripts may be challenging to analyze.
- **Memory Requirements**: Large annotation files may require significant memory.

## Examples

### Display help
**Args:** `astalavista --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic alternative splicing analysis
**Args:** `astalavista -i genes.gtf -o splicing_events.txt`
**Explanation:** Analyzes GTF annotation file and outputs detected alternative splicing events with AS codes.

### Specify output format
**Args:** `astalavista -i genes.gtf -o splicing_events.txt -f csv`
**Explanation:** Outputs results in CSV format instead of default tab-delimited format.

### Filter by event type
**Args:** `astalavista -i genes.gtf -o exon_skipping.txt -t ES`
**Explanation:** Detects only exon skipping events (ES). Other types include AD (alternative donor), AA (alternative acceptor), etc.

### Include flanking exons
**Args:** `astalavista -i genes.gtf -o splicing_events.txt -flank`
**Explanation:** Includes flanking exon information in output for contextual analysis.

### Set minimum intron length
**Args:** `astalavista -i genes.gtf -o splicing_events.txt -minintron 50`
**Explanation:** Sets minimum intron length to 50bp for detecting retained introns.

### Output detailed information
**Args:** `astalavista -i genes.gtf -o splicing_events.txt -detail`
**Explanation:** Provides detailed output including genomic coordinates and transcript IDs.

### Process multiple files
**Args:** `astalavista -i genes1.gtf genes2.gtf -o combined_events.txt`
**Explanation:** Processes multiple annotation files and combines results.

### Generate statistics
**Args:** `astalavista -i genes.gtf -o splicing_events.txt -stats stats.txt`
**Explanation:** Generates summary statistics of detected splicing events.