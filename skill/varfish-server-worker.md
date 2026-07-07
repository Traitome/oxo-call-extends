---
name: varfish-server-worker
category: bioinformatics
description: VarFish Server Worker - Background worker for VarFish server.
tags: [varfish-server-worker, varfish, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/varfish-org/varfish-server"
---

## Concepts

- **Tool Overview**: VarFish Server Worker - Background worker process for VarFish server.
- **Core Function**: Processes variant analysis jobs in background.
- **Input**: Job queue.
- **Output**: Analysis results.
- **Installation**: Install via pip
- **Use Case**: Server administration, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for processing.
- **Configuration**: Requires proper server configuration.

## Examples

### Start worker
**Args:** `varfish-server-worker --queue default --workers 4`
**Explanation:** Start background worker.

### With options
**Args:** `varfish-server-worker --queue default --workers 4 --timeout 3600`
**Explanation:** Set timeout to 1 hour.
