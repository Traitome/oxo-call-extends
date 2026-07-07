---
name: libdb
category: database
description: Berkeley DB embedded database system
tags: [libdb, database, berkeley-db, embedded, key-value]
author: oxo-call-community
source_url: "http://www.oracle.com/technology/software/products/berkeley-db/index.html"
---

## Concepts

- **Embedded Database**: Embedded key-value store
- **Transaction Support**: ACID-compliant transactions
- **Multiple Data Models**: Supports B-tree, hash, queue, and recno
- **High Performance**: Optimized for speed
- **Concurrent Access**: Multi-threaded access support
- **Recovery**: Automatic recovery from crashes

## Pitfalls

- **Memory Management**: Manual memory handling required
- **Locking Issues**: Deadlocks possible with concurrent access
- **File Corruption**: Database corruption possible
- **Backup Strategy**: Requires proper backup procedures
- **Version Migration**: Database format may change between versions
- **Size Limitations**: Database size limits depending on configuration

## Examples

### Create database
**Args:** `db_create -d btree -h database/`
**Explanation:** Creates B-tree database.

### Insert record
**Args:** `db_put -h database/ -k key1 -v value1`
**Explanation:** Inserts key-value pair.

### Retrieve record
**Args:** `db_get -h database/ -k key1`
**Explanation:** Retrieves value by key.

### Delete record
**Args:** `db_del -h database/ -k key1`
**Explanation:** Deletes record by key.

### Backup database
**Args:** `db_backup -h database/ -o backup/`
**Explanation:** Creates database backup.

### Statistics
**Args:** `db_stat -h database/`
**Explanation:** Shows database statistics.