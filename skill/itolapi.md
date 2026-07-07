---
name: itolapi
category: visualization
description: Python API for interacting with the Interactive Tree of Life (iTOL) web service.
tags: [itolapi, visualization, phylogenetics, tree annotation]
author: oxo-call-community
source_url: "https://github.com/albertyw/itolapi"
---

## Concepts

- **iTOL Integration**: Programmatic interface for the Interactive Tree of Life web service.
- **Tree Upload**: Upload phylogenetic trees to iTOL for visualization.
- **Annotation Management**: Add annotations (color strips, labels, metadata) to trees.
- **Image Generation**: Generate publication-quality tree images programmatically.
- **Batch Processing**: Handle multiple trees and annotations efficiently.
- **API Authentication**: Support for iTOL account authentication.

## Pitfalls

- **Internet Connection**: Requires active internet connection to access iTOL service.
- **Rate Limiting**: iTOL API has rate limits for requests.
- **Authentication**: Requires API key for certain operations.
- **Tree Size**: Large trees may exceed iTOL's size limits.
- **Annotation Complexity**: Complex annotations may require careful formatting.
- **Service Availability**: Dependent on iTOL server availability.

## Examples

### Upload tree to iTOL
**Args:** `itolapi upload --tree tree.nwk --name "My Tree" --project "Phylogenomics"`
**Explanation:** Uploads a Newick tree to iTOL with specified name and project.

### Add color strip annotation
**Args:** `itolapi annotate --tree-id 12345 --annotation colors.txt --type colorstrip`
**Explanation:** Adds color strip annotation to an existing iTOL tree.

### Download tree image
**Args:** `itolapi download --tree-id 12345 --format png --output tree.png`
**Explanation:** Downloads tree visualization as PNG image.

### Batch upload
**Args:** `itolapi batch --trees trees/ --annotations annotations/ --output report.txt`
**Explanation:** Uploads multiple trees with their annotations in batch.

### Create project
**Args:** `itolapi create-project --name "My Project" --description "Phylogenetic analysis"`
**Explanation:** Creates a new project on iTOL for organizing trees.

### Delete tree
**Args:** `itolapi delete --tree-id 12345`
**Explanation:** Deletes a tree from iTOL.