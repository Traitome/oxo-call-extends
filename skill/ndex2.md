---
name: ndex2
category: programming
description: NDEx2 is a Python client library for the NDEx (Network Data Exchange) platform for biological network data.
tags: [ndex2, programming, ndex, networks, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ndexbio/ndex2-client"
---

## Concepts

- **Tool Overview**: NDEx2 is a Python client for interacting with the NDEx network data exchange platform.
- **Core Function**: Enables programmatic access to biological network data stored in NDEx.
- **Algorithm**: Provides REST API wrappers for network upload, download, and query operations.
- **Input Format**: Accepts network data in CX format or various network representation formats.
- **Output**: Returns network objects and metadata from the NDEx platform.
- **Use Case**: Biological network analysis, pathway visualization, and data sharing.

## Pitfalls

- **Network Dependency**: Requires internet access to NDEx servers.
- **Authentication**: Requires API keys for certain operations.
- **Version Compatibility**: API may change between versions.
- **Data Volume**: Large networks can consume significant memory.
- **Rate Limiting**: NDEx may enforce rate limits on API requests.
- **CX Format**: Requires understanding of CX network format.

## Examples

### Display help
**Args:** `python -c "import ndex2; help(ndex2)"`
**Explanation:** Shows available methods and usage instructions.

### Connect to NDEx
**Args:** `client = ndex2.Ndex2(username='user', password='pass')`
**Explanation:** Creates authenticated NDEx client.

### Download network
**Args:** `network = client.get_network('network_uuid')`
**Explanation:** Downloads network from NDEx by UUID.

### Upload network
**Args:** `client.save_network(network_cx)`
**Explanation:** Uploads network to NDEx server.

### Search networks
**Args:** `results = client.search_networks('cancer')`
**Explanation:** Searches NDEx for networks matching query.

### Get network summary
**Args:** `summary = client.get_network_summary('network_uuid')`
**Explanation:** Retrieves metadata for specific network.