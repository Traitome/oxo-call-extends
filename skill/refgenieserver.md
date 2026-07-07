---
name: refgenieserver
category: programming
description: RefGenieServer provides a web interface and RESTful API for exploring and downloading archived genome indexes.
tags: [refgenieserver, programming, web-server, rest-api]
author: oxo-call-community
source_url: "https://refgenie.databio.org"
---

## Concepts

- **Tool Overview**: refgenieserver serves genomes.
- **Core Function**: Genome index serving.
- **Algorithm**: Uses web methods.
- **Input Format**: Accepts genome data.
- **Output**: Produces API responses.
- **Use Case**: Genome sharing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Server Load**: Affects performance.
- **Parameters**: Must be configured.
- **Runtime**: Serving may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `refgenieserver --help`
**Explanation:** Shows available options and usage instructions.

### Start server
**Args:** `refgenieserver start -d genome_db -p 8080`
**Explanation:** Starts genome server.

### With parameters
**Args:** `refgenieserver start -d genome_db -p params.yaml -o log.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `refgenieserver -v start -d genome_db -p 8080`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `refgenieserver -t 4 start -d genome_db -p 8080`
**Explanation:** Uses 4 threads for parallel processing.

### With SSL
**Args:** `refgenieserver start -d genome_db -p 443 --ssl --cert cert.pem`
**Explanation:** Uses SSL encryption.

### Generate report
**Args:** `refgenieserver start -d genome_db -p 8080 --report report.html`
**Explanation:** Generates HTML report.