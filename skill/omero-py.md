---
name: omero-py
category: programming
description: OMERO Python client library for accessing OMERO servers.
tags: [omero-py, programming, image-analysis, omero]
author: oxo-call-community
source_url: "https://www.openmicroscopy.org/"
---

## Concepts

- **Tool Overview**: omero-py provides Python bindings for OMERO server access.
- **Core Function**: Interacts with OMERO servers for image data management.
- **Algorithm**: Uses OMERO API for server communication.
- **Input Format**: Accepts OMERO server credentials and queries.
- **Output**: Produces image data and metadata.
- **Use Case**: Image analysis, data management, and bioinformatics workflows.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Server Connection**: Requires OMERO server access.
- **Authentication**: Requires proper credentials.
- **Network Issues**: Dependent on network connectivity.
- **Data Transfer**: Large data transfers can be slow.
- **Version Compatibility**: Requires matching server/client versions.

## Examples

### Display help
**Args:** `python -m omero --help`
**Explanation:** Shows available options and usage instructions.

### Connect to server
**Args:** `python -c "from omero.gateway import BlitzGateway; conn = BlitzGateway('user', 'pass', host='server')"`
**Explanation:** Connects to OMERO server.

### List projects
**Args:** `python -c "projects = conn.listProjects(); print([p.getName() for p in projects])"`
**Explanation:** Lists all projects on server.

### Download image
**Args:** `python -c "image = conn.getObject('Image', id=123); pixels = image.getPrimaryPixels()"`
**Explanation:** Downloads image pixels from server.

### Upload image
**Args:** `python -c "conn.createImageFromFile('image.tiff', dataset)"`
**Explanation:** Uploads image to OMERO server.

### Query data
**Args:** `python -c "images = conn.getObjects('Image', opts={'name': 'example'})"`
**Explanation:** Queries images by name.

### Close connection
**Args:** `python -c "conn.close()"`
**Explanation:** Closes OMERO connection.