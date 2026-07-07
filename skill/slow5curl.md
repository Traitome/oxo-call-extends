---
name: slow5curl
category: utility
description: Tool for accessing remote BLOW5 files over HTTP(S) for efficient streaming of nanopore raw signal data
tags: [slow5curl, nanopore, blow5, remote-access, streaming]
author: oxo-call-community
source_url: "https://github.com/BonsonW/slow5curl"
---

## Concepts

- **Tool Overview**: slow5curl (v0.3.0) - A tool for accessing remote BLOW5 files via HTTP(S)
- **Core Function**: Enables streaming access to nanopore raw signal data stored remotely
- **Input/Output**: Accepts URL to remote BLOW5 file; outputs raw signal data or processed reads
- **Algorithm**: Implements HTTP range requests for efficient data retrieval
- **Installation**: `conda install -c bioconda slow5curl`
- **Key Features**: Supports HTTPS, authentication, and seamless integration with slow5tools

## Pitfalls

- **Network Dependency**: Requires stable network connection for remote access
- **Authentication**: May require API keys or credentials for private resources
- **File Size**: Very large BLOW5 files may have streaming overhead
- **Server Requirements**: Remote server must support range requests
- **Rate Limiting**: May be subject to API rate limits
- **Data Integrity**: Verify downloaded data for completeness

## Examples

### Display help
**Args:** `slow5curl --help`
**Explanation:** Shows available options and usage information.

### Download remote BLOW5
**Args:** `slow5curl https://example.com/data/sample.blow5 -o local.blow5`
**Explanation:** Download remote BLOW5 file to local filesystem.

### Stream reads
**Args:** `slow5curl https://example.com/data/sample.blow5 | slow5tools view`
**Explanation:** Stream remote BLOW5 data to slow5tools for viewing.

### With authentication
**Args:** `slow5curl -u user:pass https://private.example.com/data.blow5 -o local.blow5`
**Explanation:** Access authenticated remote BLOW5 resource.

### Download specific reads
**Args:** `slow5curl -r "read1,read2,read3" https://example.com/data.blow5 -o subset.blow5`
**Explanation:** Download only specific reads from remote file.

### Progress bar
**Args:** `slow5curl -p https://example.com/data.blow5 -o local.blow5`
**Explanation:** Show download progress bar.

### Resume download
**Args:** `slow5curl -c https://example.com/data.blow5 -o local.blow5`
**Explanation:** Resume interrupted download.