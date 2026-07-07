---
name: synapseclient
category: data-management
description: Python client for Synapse collaborative data platform.
tags: [synapseclient, data-management, python, collaboration]
author: oxo-call-community
source_url: "https://python-docs.synapse.org"
---

## Concepts

- **Tool Overview**: synapseclient (v4.12.0) is a Python client for Synapse.
- **Core Function**: Access and manage data on the Synapse platform.
- **Algorithm**: REST API client for Synapse data operations.
- **Input/Output**: Input: API calls; Output: Data objects, metadata.
- **Applications**: Data sharing, collaborative research, data management.
- **Installation**: `conda install -c bioconda synapseclient` or pip install.

## Pitfalls

- **Authentication**: Requires Synapse account and proper authentication.
- **Network Access**: Requires internet connection to Synapse.
- **API Limits**: May hit API rate limits with frequent calls.
- **Data Size**: Large files require proper handling.
- **Versioning**: Data versioning requires careful management.
- **Permissions**: Requires appropriate access permissions.

## Examples

### Display help
**Args:** `python -c "import synapseclient; help(synapseclient)"`
**Explanation:** Shows available options and usage information.

### Basic login
**Args:** `python -c "import synapseclient; syn = synapseclient.Synapse(); syn.login()"`
**Explanation:** Login to Synapse platform.

### Download data
**Args:** `python -c "import synapseclient; syn = synapseclient.Synapse(); syn.login(); syn.get('syn12345')"`
**Explanation:** Download data from Synapse.

### Upload data
**Args:** `python -c "import synapseclient; syn = synapseclient.Synapse(); syn.login(); syn.store(synapseclient.File('data.txt', parentId='syn1234'))"`
**Explanation:** Upload data to Synapse.

### Query data
**Args:** `python -c "import synapseclient; syn = synapseclient.Synapse(); syn.login(); results = syn.tableQuery('SELECT * FROM syn1234')"`
**Explanation:** Query data from Synapse tables.

### Batch processing
**Args:** `python -c "import synapseclient; syn = synapseclient.Synapse(); syn.login(); [syn.get(id) for id in ids]"`
**Explanation:** Download multiple files.

### Create project
**Args:** `python -c "import synapseclient; syn = synapseclient.Synapse(); syn.login(); project = syn.store(synapseclient.Project('My Project'))"`
**Explanation:** Create a new Synapse project.

### Share data
**Args:** `python -c "import synapseclient; syn = synapseclient.Synapse(); syn.login(); syn.share('syn1234', users=['user@example.com'], accessType='READ')"`
**Explanation:** Share data with other users.

### Generate report
**Args:** `python -c "import synapseclient; syn = synapseclient.Synapse(); syn.login(); # Generate usage report"`
**Explanation:** Generate data usage report.
