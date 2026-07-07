---
name: pyomero-upload
category: programming
description: pyomero-upload provides helper methods for uploading data to an OMERO server.
tags: [pyomero-upload, programming, omero, imaging]
author: oxo-call-community
source_url: "http://www.synthsys.ed.ac.uk/"
---

## Concepts

- **Tool Overview**: pyomero-upload uploads to OMERO.
- **Core Function**: Data upload.
- **Algorithm**: Uses OMERO API.
- **Input Format**: Accepts image files.
- **Output**: Uploaded data.
- **Use Case**: Image management.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Server Connection**: Must be available.
- **Authentication**: Requires credentials.
- **Network Speed**: Affects upload.
- **File Size**: Large files take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyomero-upload --help`
**Explanation:** Shows available options and usage instructions.

### Upload image
**Args:** `pyomero-upload upload -i image.tif -s server:4064 -u user -p pass -o dataset_id`
**Explanation:** Uploads image to OMERO server.

### With parameters
**Args:** `pyomero-upload upload -i image.tif -p params.yaml -o dataset_id`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyomero-upload -v upload -i image.tif -o dataset_id`
**Explanation:** Runs with verbose output.

### Batch upload
**Args:** `pyomero-upload batch -d images/ -o dataset_id`
**Explanation:** Uploads multiple images.

### Create dataset
**Args:** `pyomero-upload create -n "My Dataset" -o project_id`
**Explanation:** Creates new dataset.

### Generate report
**Args:** `pyomero-upload upload -i image.tif -o dataset_id --report report.html`
**Explanation:** Generates HTML report.