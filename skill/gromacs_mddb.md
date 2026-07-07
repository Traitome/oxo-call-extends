---
name: gromacs_mddb
category: bioinformatics
description: GROMACS with mddb (Molecular Dynamics DataBase) support for efficient trajectory analysis and storage.
tags: [gromacs_mddb, molecular-dynamics, database, bioinformatics]
author: oxo-call-community
source_url: "https://manual.gromacs.org/"
---

## Concepts

- **Molecular Dynamics Database**: gromacs_mddb provides database support for MD trajectory storage and analysis.

- **Efficient Storage**: Stores trajectory data in a structured database format.

- **Rapid Query**: Enables fast querying of trajectory data.

- **Parallel I/O**: Supports parallel input/output for large simulations.

- **Trajectory Compression**: Compresses trajectory data for efficient storage.

- **Integration**: Integrates with standard GROMACS simulation workflow.

## Pitfalls

- **Database Size**: Large simulations may produce large databases.

- **Performance**: Database operations may have overhead compared to direct file I/O.

- **Compatibility**: Ensure compatibility with GROMACS version.

- **Memory Usage**: Loading large databases may require significant memory.

- **Backup Strategy**: Regularly backup trajectory databases.

## Examples

### Initialize database
**Args:** `gmx mddb init -o trajectory.db`
**Explanation:** Creates a new MD trajectory database.

### Add trajectory to database
**Args:** `gmx mddb add -i trajectory.xtc -d trajectory.db`
**Explanation:** Adds trajectory data to the database.

### Query database
**Args:** `gmx mddb query -d trajectory.db -q "SELECT * WHERE time > 1000"`
**Explanation:** Queries the database for specific trajectory data.

### Export trajectory
**Args:** `gmx mddb export -d trajectory.db -o subset.xtc -r 0-100`
**Explanation:** Exports a subset of trajectory data.

### Compress database
**Args:** `gmx mddb compress -d trajectory.db`
**Explanation:** Compresses the trajectory database.

### Generate statistics
**Args:** `gmx mddb stats -d trajectory.db -o stats.txt`
**Explanation:** Generates statistics about the database contents.

### Merge databases
**Args:** `gmx mddb merge -d1 db1.db -d2 db2.db -o merged.db`
**Explanation:** Merges two trajectory databases.