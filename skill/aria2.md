---
name: aria2
category: utility
description: Aria2 - Lightweight multi-protocol command-line download utility
tags: [aria2, utility, download, http, ftp, bittorrent, metalink]
author: oxo-call-community
source_url: "https://aria2.github.io/"
---

## Concepts

- **Tool Overview**: Aria2 is a lightweight multi-protocol and multi-source command-line download utility supporting HTTP/HTTPS, FTP, SFTP, BitTorrent, and Metalink. Version 1.34.0.
- **Core Function**: Downloads files from multiple sources simultaneously with segmented downloading for improved speed.
- **Multi-Protocol Support**: Supports HTTP, HTTPS, FTP, SFTP, BitTorrent, and Metalink protocols in a single tool.
- **Segmented Downloading**: Downloads files in multiple segments from multiple sources for maximum speed.
- **Resume Capability**: Supports resuming interrupted downloads for large files.
- **Bandwidth Control**: Allows limiting download/upload speeds to manage network usage.
- **Command-Line Interface**: Operates entirely from command line for scripting and automation.
- **Installation**: `conda install -c bioconda aria2` or install from package manager.

## Pitfalls

- **Network Configuration**: May require proxy settings for restricted network environments.
- **Bandwidth Limits**: Default unlimited bandwidth may saturate network connections.
- **Disk Space**: Segmented downloading requires temporary disk space for partial downloads.
- **Connection Limits**: Too many simultaneous connections may be blocked by servers.
- **BitTorrent Seeding**: Default behavior may continue seeding after download completes.

## Examples

### Basic file download
**Args:** `aria2c http://example.com/file.zip`
**Explanation:** Downloads file from URL using default settings.

### Download with multiple connections
**Args:** `aria2c -x 16 -s 16 http://example.com/largefile.zip`
**Explanation:** Uses 16 connections and 16 segments for faster download of large files.

### Resume interrupted download
**Args:** `aria2c -c http://example.com/largefile.zip`
**Explanation:** Continues interrupted download from where it left off.

### Download from multiple URLs
**Args:** `aria2c http://mirror1.com/file.zip http://mirror2.com/file.zip`
**Explanation:** Downloads same file from multiple sources simultaneously.

### BitTorrent download
**Args:** `aria2c --seed-ratio=1.0 torrent_file.torrent`
**Explanation:** Downloads torrent file and seeds until ratio of 1.0 reached.

### Limit download speed
**Args:** `aria2c --max-download-limit=1M http://example.com/file.zip`
**Explanation:** Limits download speed to 1 MB/s to manage network usage.

### Download from URL list
**Args:** `aria2c -i urls.txt`
**Explanation:** Downloads all URLs listed in text file sequentially.