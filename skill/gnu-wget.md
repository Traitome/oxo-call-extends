---
name: gnu-wget
category: utility
description: GNU Wget is a robust command-line utility for retrieving files from the web using HTTP, HTTPS, and FTP protocols.
tags: [gnu-wget, download, HTTP, HTTPS, FTP, utility]
author: oxo-call-community
source_url: "http://www.gnu.org/software/wget/"
---

## Concepts

- **Protocol Support**: Wget supports HTTP, HTTPS, and FTP protocols for downloading files from web servers and FTP sites.

- **Recursive Download**: Capable of recursively downloading entire directories or website mirroring, preserving directory structure.

- **Resume Downloads**: Can resume interrupted downloads, saving bandwidth and time when large files are partially downloaded.

- **Non-interactive Operation**: Designed to work without user intervention, making it ideal for scripts and automated workflows.

- **Proxy Support**: Configurable proxy server support for accessing resources through firewalls or network proxies.

- **Bandwidth Limiting**: Allows limiting download speed to avoid saturating network connections.

## Pitfalls

- **SSL Certificate Issues**: HTTPS downloads may fail if certificates are invalid or not properly configured. Use --no-check-certificate for testing, but avoid in production.

- **Redirect Handling**: Some servers use complex redirect chains that Wget may not handle correctly. Use --max-redirect to limit redirect attempts.

- **Rate Limiting**: Some servers block repeated requests. Use --wait or --random-wait to avoid being blocked.

- **File Overwriting**: By default, Wget overwrites existing files with the same name. Use -nc (no-clobber) to prevent overwriting.

- **Recursive Depth**: Recursive downloads can quickly become too broad. Always specify --level to limit recursion depth.

## Examples

### Download a single file
**Args:** `wget https://example.com/file.txt`
**Explanation:** Downloads file.txt from the specified URL and saves it in the current directory with the original filename.

### Download and rename file
**Args:** `wget -O output_name.txt https://example.com/file.txt`
**Explanation:** Downloads file.txt and saves it as output_name.txt in the current directory.

### Resume interrupted download
**Args:** `wget -c https://example.com/large_file.iso`
**Explanation:** Resumes downloading large_file.iso if the previous download was interrupted.

### Recursive download with depth limit
**Args:** `wget -r --level=2 https://example.com/docs/`
**Explanation:** Recursively downloads files from the docs directory up to 2 levels deep.

### Download in background
**Args:** `wget -b https://example.com/large_file.tar.gz`
**Explanation:** Starts the download in the background and logs output to wget-log.

### Limit download speed
**Args:** `wget --limit-rate=100k https://example.com/file.zip`
**Explanation:** Limits download speed to 100 KB/s to avoid saturating the network connection.

### Download via proxy
**Args:** `wget --proxy=http://proxy.example.com:8080 https://example.com/file.txt`
**Explanation:** Uses the specified HTTP proxy server to download the file, useful for networks behind firewalls.