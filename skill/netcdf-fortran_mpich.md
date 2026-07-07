---
name: netcdf-fortran_mpich
category: programming
description: NetCDF-Fortran provides Fortran language bindings for netCDF with MPICH support.
tags: [netcdf-fortran_mpich, programming, netcdf, fortran, parallel]
author: oxo-call-community
source_url: "http://www.unidata.ucar.edu/software/netcdf/"
---

## Concepts

- **Tool Overview**: NetCDF-Fortran provides Fortran bindings for the netCDF library.
- **Core Function**: Enables Fortran programs to read and write scientific data in netCDF format.
- **Algorithm**: Implements netCDF API for Fortran with parallel I/O via MPICH.
- **Input Format**: Accepts netCDF files (.nc) and array data from Fortran programs.
- **Output**: Produces netCDF files with structured scientific data.
- **Use Case**: Fortran-based scientific computing, climate modeling, and HPC applications.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **MPI Configuration**: Requires proper MPICH setup for parallel operations.
- **Fortran Standards**: Requires Fortran 90+ compiler.
- **Memory Usage**: Large datasets require memory management.
- **API Complexity**: Fortran API has learning curve.
- **Parallel I/O**: Requires careful configuration for optimal performance.

## Examples

### Display help
**Args:** `nf-config --help`
**Explanation:** Shows available options and usage instructions.

### Compile Fortran program
**Args:** `gfortran program.f90 $(nf-config --fflags --libs) -o program`
**Explanation:** Compiles Fortran program with netCDF.

### Create netCDF file
**Args:** `./program create output.nc`
**Explanation:** Runs Fortran program to create netCDF file.

### Read netCDF file
**Args:** `./program read input.nc`
**Explanation:** Runs Fortran program to read netCDF file.

### Parallel I/O
**Args:** `mpirun -n 4 ./parallel_program`
**Explanation:** Runs parallel Fortran netCDF application.

### Check file
**Args:** `ncdump -h input.nc`
**Explanation:** Displays file header information.

### Convert format
**Args:** `nccopy -k 4 input.nc output.nc`
**Explanation:** Converts to netCDF-4 format.