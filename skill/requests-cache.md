---
name: requests-cache
category: programming
description: Requests-cache provides persistent caching for the requests library.
tags: [requests-cache, programming, http-caching, python]
author: oxo-call-community
source_url: "https://github.com/reclosedev/requests-cache"
---

## Concepts

- **Tool Overview**: requests-cache caches HTTP requests.
- **Core Function**: HTTP request caching.
- **Algorithm**: Uses storage methods.
- **Input Format**: Accepts HTTP requests.
- **Output**: Produces cached responses.
- **Use Case**: Web scraping.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Cache Size**: Large caches require storage.
- **Expiration**: Must be managed.
- **Parameters**: Must be configured.
- **Runtime**: Caching may have overhead.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "import requests_cache; help(requests_cache)"`
**Explanation:** Shows available options and usage instructions.

### Basic caching
**Args:** `requests_cache.install_cache('my_cache')`
**Explanation:** Installs cache for requests.

### With backend
**Args:** `requests_cache.install_cache('my_cache', backend='sqlite')`
**Explanation:** Uses SQLite backend.

### Expiration time
**Args:** `requests_cache.install_cache('my_cache', expire_after=3600)`
**Explanation:** Cache expires after 1 hour.

### Session usage
**Args:** `session = requests_cache.CachedSession('my_cache')`
**Explanation:** Creates cached session.

### Cache control
**Args:** `session.get(url, expire_after=60)`
**Explanation:** Per-request expiration.

### Clear cache
**Args:** `requests_cache.clear()`
**Explanation:** Clears all cached data.