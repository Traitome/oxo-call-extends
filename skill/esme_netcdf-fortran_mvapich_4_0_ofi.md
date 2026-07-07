---
name: esme_netcdf-fortran_mvapich_4_0_ofi
category: hpc
description: netCDF-Fortran library with MVAPICH 4.0 and OFI for high-performance parallel I/O in scientific applications on InfiniBand networks.
tags: [esme_netcdf-fortran_mvapich_4_0_ofi, netCDF, Fortran, hpc, parallel, MVAPICH, OFI]
author: oxo-call-community
source_url: "https://www.unidata.ucar.edu/software/netcdf/"
---

## Concepts

- **Tool Overview**: netCDF-Fortran is the Fortran interface to netCDF, providing platform-independent storage for array-oriented scientific data with MVAPICH 4.0 and OFI support.
- **MPI Support**: Built with MVAPICH 4.0 for high-performance parallel computing on InfiniBand networks via OFI.
- **Data Formats**: Supports netCDF classic, 64-bit offset, and netCDF-4/HDF5 formats.
- **Installation**: `conda install -c bioconda esme_netcdf-fortran_mvapich_4_0_ofi`
- **Parallel I/O**: Enables efficient parallel access to netCDF files using MPI-IO with OFI transport.
- **Use Cases**: Climate modeling, atmospheric science, oceanography, Earth system simulations.

## Pitfalls

- **MPI Environment**: Requires proper MPI environment setup with MVAPICH 4.0 and OFI drivers installed.
- **File Format**: Ensure proper selection of netCDF format based on data size and compatibility requirements.
- **Network Configuration**: OFI requires compatible network hardware and drivers (e.g., InfiniBand).
- **Parallel I/O**: Improper file access patterns can lead to performance degradation in parallel applications.
- **Fortran Compatibility**: Ensure Fortran compiler compatibility with netCDF-Fortran.

## Examples

### Compile a netCDF-Fortran program
**Args:** `mpif90 my_program.f90 -o my_program $(nf-config --libs --cflags)`
**Explanation:** Compile a Fortran program using netCDF-Fortran and MVAPICH with proper linking flags.

### Run parallel netCDF-Fortran application
**Args:** `mpiexec -n 8 ./my_program input.nc output.nc`
**Explanation:** Execute a parallel netCDF-Fortran application using 8 MPI processes with MVAPICH.

### Check netCDF-Fortran version
**Args:** `nf-config --version`
**Explanation:** Display the installed netCDF-Fortran library version.

### Create netCDF file
**Args:** `ncdump -h example.nc`
**Explanation:** View the header information of a netCDF file.

### List netCDF utilities
**Args:** `ls /opt/conda/bin/nc* /opt/conda/bin/nf*`
**Explanation:** List all available netCDF utility programs installed in the system.