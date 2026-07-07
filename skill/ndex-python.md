---
name: ndex-python
category: programming
description: NDEx Python is the original Python client library for the NDEx (Network Data Exchange) platform.
tags: [ndex-python, programming, ndex, networks, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ndexbio/ndex-python"
---

## Concepts

- **Tool Overview**: NDEx Python is the original Python client for the NDEx network data exchange platform.
- **Core Function**: Enables programmatic access to biological networks stored in the NDEx database.
- **Algorithm**: Provides REST API wrappers for network operations including upload, download, and search.
- **Input Format**: Accepts network data in various formats including CX, GraphML, and GML.
- **Output**: Returns network objects and metadata from the NDEx platform.
- **Use Case**: Biological network analysis, pathway data integration, and collaborative research.

## Pitfalls

- **Deprecated**: Consider using ndex2 instead for updated features.
- **Network Dependency**: Requires internet access to NDEx servers.
- **Authentication**: Requires NDEx account for certain operations.
- **Version Compatibility**: Older API may not support latest NDEx features.
- **Data Volume**: Large networks require significant memory.
- **Error Handling**: Limited error handling requires careful implementation.

## Examples

### Display help
**Args:** `python -c "import ndex; help(ndex)"`
**Explanation:** Shows available methods and usage instructions.

### Connect to NDEx
**Args:** `client = ndex.Ndex('http://public.ndexbio.org', 'user', 'pass')`
**Explanation:** Creates authenticated NDEx client.

### Download network
**Args:** `network = client.get_network('network_uuid')`
**Explanation:** Downloads network from NDEx by UUID.

### Upload network
**Args:** `client.save_network(network)`
**Explanation:** Uploads network to NDEx server.

### Search networks
**Args:** `results = client.search_networks('keyword')`
**Explanation:** Searches NDEx for networks matching query.

### Delete network
**Args:** `client.delete_network('network_uuid')`
**Explanation:** Deletes network from NDEx account.