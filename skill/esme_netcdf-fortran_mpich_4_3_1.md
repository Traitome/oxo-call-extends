---
name: esme_netcdf-fortran_mpich_4_3_1
category: hpc
description: netCDF-Fortran library with MPICH 4.3.1 for high-performance parallel I/O in scientific applications.
tags: [esme_netcdf-fortran_mpich_4_3_1, netCDF, Fortran, hpc, parallel, MPICH]
author: oxo-call-community
source_url: "https://www.unidata.ucar.edu/software/netcdf/"
---

## Concepts

- **Tool Overview**: netCDF-Fortran is the Fortran interface to netCDF, providing platform-independent storage for array-oriented scientific data with MPICH 4.3.1 support.
- **MPI Support**: Built with MPICH 4.3.1 for high-performance parallel computing.
- **Data Formats**: Supports netCDF classic, 64-bit offset, and netCDF-4/HDF5 formats.
- **Installation**: `conda install -c bioconda esme_netcdf-fortran_mpich_4_3_1`
- **Parallel I/O**: Enables efficient parallel access to netCDF files using MPI-IO.
- **Use Cases**: Climate modeling, atmospheric science, oceanography, Earth system simulations.

## Pitfalls

- **MPI Environment**: Requires proper MPI environment setup with MPICH 4.3.1.
- **File Format**: Ensure proper selection of netCDF format based on data size and compatibility requirements.
- **Parallel I/O**: Improper file access patterns can lead to performance degradation in parallel applications.
- **Version Conflicts**: Different MPI implementations (OpenMPI, MVAPICH) are not compatible; use matching MPI stack.
- **Fortran Compatibility**: Ensure Fortran compiler compatibility with netCDF-Fortran.

## Examples

### Compile a netCDF-Fortran program
**Args:** `mpif90 my_program.f90 -o my_program $(nf-config --libs --cflags)`
**Explanation:** Compile a Fortran program using netCDF-Fortran and MPICH with proper linking flags.

### Run parallel netCDF-Fortran application
**Args:** `mpiexec -n 8 ./my_program input.nc output.nc`
**Explanation:** Execute a parallel netCDF-Fortran application using 8 MPI processes with MPICH.

### Check netCDF-Fortran version
**Args:** `nf-config --version`
**Explanation:** Display the installed netCDF-Fortran library version.

### Create netCDF file
**Args:** `ncdump -h example.nc`
**Explanation:** View the header information of a netCDF file.

### List netCDF utilities
**Args:** `ls /opt/conda/bin/nc* /opt/conda/bin/nf*`
**Explanation:** List all available netCDF utility programs installed in the system.