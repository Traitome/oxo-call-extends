---
name: fiji-omero_ij
category: image-analysis
description: "Fiji/ImageJ plugin that enables connection to OMERO servers for visualizing, importing, and manipulating microscopy image data and metadata."
tags: [fiji-omero_ij, image-analysis, OMERO, Fiji, ImageJ, plugin, Java, microscopy, bioimaging, server, client]
author: oxo-call-community
source_url: "https://github.com/ome/omero-insight"
---

## Concepts

- **Tool Overview**: OMERO.insight-ij is an ImageJ/Fiji plugin that enables connection to OMERO servers, allowing users to visualize, import, and manipulate both image data and metadata maintained on an OMERO server directly from within Fiji.
- **Core Function**: Provides seamless integration between Fiji/ImageJ and OMERO, enabling users to browse OMERO servers, open images in Fiji for processing, and save analysis results (ROIs, measurements) back to OMERO.
- **Input/Output**: Input: OMERO server connection (host, port, username, password). Output: Images loaded into Fiji, ROIs and measurement tables saved back to OMERO.
- **Algorithm**: Java-based OMERO client plugin that uses the OMERO API to communicate with the server. Images are transferred via Bio-Formats when opening from OMERO, and results are uploaded via OMERO.tables.
- **Key Features**: Connect to OMERO server from Fiji, browse and open images from OMERO, import images with Bio-Formats options, perform analysis in Fiji, save ROIs and measurements back to OMERO, batch processing support via scripting.
- **Installation**: `conda install -c bioconda fiji-omero_ij` or download `omero_ij-5.x.x-all.jar` from https://www.openmicroscopy.org/omero/downloads/ and place in Fiji's plugins folder.

## Pitfalls

- **Fiji Dependency**: Requires Fiji or ImageJ to be installed. The plugin is not a standalone tool and cannot run without the ImageJ/Fiji framework.
- **Login Credentials**: Requires valid OMERO server credentials. Contact your OMERO administrator to obtain an account before attempting to connect.
- **Network Latency**: Large images may take time to transfer from the OMERO server. Consider using a fast network connection for large microscopy datasets.
- **Bio-Formats Import**: Images from OMERO are imported using Bio-Formats, which may have specific import options. Configure these appropriately for your analysis.
- **Plugin Version Compatibility**: Ensure the OMERO plugin version is compatible with both your Fiji installation and the OMERO server version.

## Examples

### Connect to OMERO server from Fiji
**Args:** `Plugins > OMERO > Connect to OMERO`
**Explanation:** Launch Fiji, then go to Plugins > OMERO > Connect to OMERO. Enter the server address, your username, and password. Click Login to establish the connection and open the OMERO.insight-like interface within Fiji.

### Open an image from OMERO
**Args:** `Double-click image in OMERO browser`
**Explanation:** After connecting to OMERO, browse to the desired image in the OMERO hierarchy (Projects > Datasets > Images). Double-click an image to open it in Fiji. The Bio-Formats Import Options dialog will appear; configure settings as needed and click OK.

### Process an image and save ROIs to OMERO
**Args:** `Plugins > OMERO > Save ROIs to OMERO`
**Explanation:** Open an image from OMERO in Fiji. Perform your analysis (e.g., thresholding, particle analysis). When done, click Plugins > OMERO > Save ROIs to OMERO. Select whether to save ROIs, Measurements, or both. Choose the destination Project/Dataset and click Save.

### Batch process images from OMERO
**Args:** `python omero_batch_script.py --server HOST --user USER --dataset ID`
**Explanation:** Use the OMERO Python API or the provided example scripts (https://github.com/bramalingam/Omero-Imagej-Scripts) to automate batch processing. Configure the script with your server credentials and dataset ID, then run the macro on multiple images.

### Install OMERO plugin manually
**Args:** `cp omero_ij-*.jar $FIJI/plugins/`
**Explanation:** Download the latest `omero_ij-5.x.x-all.jar` from https://www.openmicroscopy.org/omero/downloads/. Also download `simple-omero-client.jar` and `omero-batch-plugin.jar` if needed. Copy all JAR files to the `plugins` folder of your Fiji installation and restart Fiji.

### Save measurement results to OMERO
**Args:** `Plugins > OMERO > Save Results to OMERO`
**Explanation:** After performing measurements in Fiji (Analyze > Measure), click Plugins > OMERO > Save Results to OMERO. Enter a name for the measurements table and select where to save it in the OMERO hierarchy.

### Use OMERO.tables for large-scale results
**Args:** `omero.tables.create(file_id, columns)`
**Explanation:** For large datasets, results can be saved as OMERO.tables, which support efficient querying and retrieval. Use the OMERO Python client to create and populate tables with analysis results.

### Configure Bio-Formats import options
**Args:** `Bio-Formats Import Options > Customize`
**Explanation:** When opening images from OMERO, the Bio-Formats Import Options dialog allows customization of how the image is displayed. Enable options like "cropped", "virtual", or specify specific series/channels to import based on your analysis needs.
