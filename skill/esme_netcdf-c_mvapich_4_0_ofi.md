---
name: esme_netcdf-c_mvapich_4_0_ofi
category: hpc
description: netCDF-C library with MVAPICH 4.0 and OFI for high-performance parallel I/O in scientific applications on InfiniBand networks.
tags: [esme_netcdf-c_mvapich_4_0_ofi, netCDF, hpc, parallel, MVAPICH, OFI]
author: oxo-call-community
source_url: "https://www.unidata.ucar.edu/software/netcdf/"
---

## Concepts

- **Tool Overview**: netCDF-C is the C implementation of the network Common Data Form, providing platform-independent storage for array-oriented scientific data with MVAPICH 4.0 MPI and OFI support.
- **MPI Support**: Built with MVAPICH 4.0 for high-performance parallel computing on InfiniBand networks via OFI.
- **Data Formats**: Supports netCDF classic, 64-bit offset, and netCDF-4/HDF5 formats.
- **Installation**: `conda install -c bioconda esme_netcdf-c_mvapich_4_0_ofi`
- **Parallel I/O**: Enables efficient parallel access to netCDF files using MPI-IO with OFI transport.
- **Use Cases**: Climate modeling, atmospheric science, oceanography, Earth system simulations.

## Pitfalls

- **MPI Environment**: Requires proper MPI environment setup with MVAPICH 4.0 and OFI drivers installed.
- **File Format**: Ensure proper selection of netCDF format based on data size and compatibility requirements.
- **Network Configuration**: OFI requires compatible network hardware and drivers (e.g., InfiniBand).
- **Parallel I/O**: Improper file access patterns can lead to performance degradation in parallel applications.
- **Version Conflicts**: Different MPI implementations (OpenMPI, MPICH) are not compatible; use matching MPI stack.

## Examples

### Compile a netCDF program
**Args:** `mpicc my_program.c -o my_program $(nc-config --libs --cflags)`
**Explanation:** Compile a C program using netCDF-C and MVAPICH MPI with proper linking flags.

### Run parallel netCDF application
**Args:** `mpiexec -n 8 ./my_program input.nc output.nc`
**Explanation:** Execute a parallel netCDF application using 8 MPI processes with MVAPICH.

### Check netCDF version
**Args:** `nc-config --version`
**Explanation:** Display the installed netCDF-C library version.

### Create netCDF file
**Args:** `ncdump -h example.nc`
**Explanation:** View the header information of a netCDF file.

### List netCDF utilities
**Args:** `ls /opt/conda/bin/nc*`
**Explanation:** List all available netCDF utility programs installed in the system.