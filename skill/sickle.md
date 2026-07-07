---
name: sickle
category: programming
description: sickle - Lightweight OAI client library for Python
tags: ["sickle", "programming", "oai", "python"]
author: oxo-call-community
source_url: "http://github.com/mloesch/sickle"
---

## Concepts

- **Tool Overview**: sickle (v0.7.0) is a lightweight OAI-PMH client library for Python.
- **Core Function**: Interacts with OAI-PMH repositories to harvest metadata.
- **Algorithm**: Implements OAI-PMH protocol for metadata retrieval.
- **Input/Output**: Accepts repository URL and produces metadata records.
- **Metadata Harvesting**: Focuses on OAI-PMH protocol implementation.
- **Applications**: Digital library integration, metadata harvesting, and academic publishing.

## Pitfalls

- **Dependency Issues**: Requires Python environment.
- **Network Requirements**: Requires internet connection for remote repositories.
- **Rate Limiting**: May be subject to rate limits by repositories.
- **Version Compatibility**: Different versions may have breaking changes.
- **Repository Compatibility**: Not all OAI-PMH repositories are fully compliant.
- **Documentation**: Limited documentation available.

## Examples

### Create client
**Args:** `python -c "from sickle import Sickle; s = Sickle('http://example.com/oai')"`
**Explanation:** Creates Sickle client for OAI-PMH repository.

### List records
**Args:** `python -c "s.ListRecords(metadataPrefix='oai_dc')"`
**Explanation:** Lists records with OAI-DC metadata format.

### Get record
**Args:** `python -c "s.GetRecord(identifier='oai:example:123', metadataPrefix='oai_dc')"`
**Explanation:** Gets specific record by identifier.

### Help command
**Args:** `python -c "from sickle import Sickle; help(Sickle)"`
**Explanation:** Shows available methods and usage.

### Version check
**Args:** `python -c "import sickle; print(sickle.__version__)"`
**Explanation:** Shows current version.

### List identifiers
**Args:** `python -c "s.ListIdentifiers(metadataPrefix='oai_dc')"`
**Explanation:** Lists record identifiers only.

### With timeout
**Args:** `python -c "s = Sickle('http://example.com/oai', timeout=30)"`
**Explanation:** Sets connection timeout to 30 seconds.
