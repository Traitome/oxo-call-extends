---
name: gdal
category: utility
description: GDAL (Geospatial Data Abstraction Library) is a translator library for raster and vector geospatial data formats.
tags: [gdal, geospatial, raster, vector, gis]
author: oxo-call-community
source_url: "https://gdal.org"
---

## Concepts
- **Geospatial Data Handling**: GDAL provides a unified interface for reading and writing various geospatial data formats.
- **Raster Formats**: Supports over 200 raster formats including GeoTIFF, NetCDF, HDF, and JPEG2000.
- **Vector Formats**: Handles vector formats like Shapefile, GeoJSON, KML, and GML through OGR library.
- **Spatial Transformations**: Supports coordinate system transformations and reprojection.
- **Data Warping**: Provides tools for resampling and warping raster data.

## Pitfalls
- **Format Compatibility**: Not all format drivers support both read and write operations.
- **Coordinate System Issues**: Requires careful handling of coordinate reference systems (CRS).
- **Memory Management**: Large raster files can consume significant memory.
- **Version Differences**: Driver capabilities may vary between GDAL versions.
- **Projection Errors**: Incorrect CRS specification can lead to misaligned data.

## Examples
### Convert GeoTIFF to NetCDF
**Args:** `gdal_translate input.tif output.nc -of NetCDF`
**Explanation:** Converts a GeoTIFF file to NetCDF format. The -of flag specifies the output format.

### Reproject raster
**Args:** `gdalwarp -t_srs EPSG:4326 input.tif output_wgs84.tif`
**Explanation:** Reprojects a raster to WGS84 coordinate system (EPSG:4326).

### Get raster information
**Args:** `gdalinfo input.tif`
**Explanation:** Displays detailed information about a raster file including dimensions, CRS, and band statistics.

### Create virtual raster
**Args:** `gdalbuildvrt mosaic.vrt input1.tif input2.tif input3.tif`
**Explanation:** Creates a virtual raster mosaic from multiple input rasters without copying data.

### Resample raster
**Args:** `gdal_translate -outsize 50% 50% input.tif output_resampled.tif`
**Explanation:** Resamples a raster to 50% of its original size using nearest neighbor resampling.