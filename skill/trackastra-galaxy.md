---
name: trackastra-galaxy
category: utility
description: TrackAstra-Galaxy - Galaxy tool wrapper for TrackAstra.
tags: [trackastra-galaxy, galaxy, trackastra, visualization, genome-browser]
author: oxo-call-community
source_url: "https://github.com/compbio/trackastra-galaxy"
---

## Concepts

- **Tool Overview**: TrackAstra-Galaxy - A Galaxy tool wrapper for the TrackAstra genome browser.
- **Core Function**: Provides Galaxy integration for visualizing and analyzing genomic tracks.
- **Input**: Genomic track files (BED, BigWig, VCF), genome annotations.
- **Output**: Interactive genome browser sessions, visualization outputs.
- **Installation**: Install via Galaxy ToolShed
- **Use Case**: Genome visualization, data exploration, collaborative analysis.

## Pitfalls

- **Galaxy Dependency**: Requires Galaxy platform for usage.
- **Track Formats**: Supports specific track formats only.

## Examples

### Upload tracks
**Args:** `trackastra-galaxy upload --input track.bed --name "My Track"`
**Explanation:** Upload genomic track to TrackAstra browser.

### Create session
**Args:** `trackastra-galaxy session create --tracks tracks.txt --output session.json`
**Explanation:** Create browser session with multiple tracks.
