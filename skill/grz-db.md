---
name: grz-db
category: bioinformatics
description: grz-db provides SQL models and database utilities for GRZ applications including grz-cli and grz-watchdog.
tags: [grz-db, database, SQL, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BfArM-MVH/grz-tools"
---

## Concepts

- **SQL Models**: grz-db defines SQL models for GRZ application data.

- **Database Schema**: Defines the database schema for submission tracking.

- **ORM Integration**: Integrates with Object-Relational Mapping frameworks.

- **Data Migration**: Supports database schema migrations.

- **Query Utilities**: Provides utility functions for database queries.

- **Transaction Management**: Handles database transactions safely.

## Pitfalls

- **Database Connection**: Requires proper database connection configuration.

- **Schema Migrations**: Carefully plan and test database migrations.

- **Performance**: Optimize queries for large datasets.

- **Backup**: Regularly backup database to prevent data loss.

- **Version Compatibility**: Ensure compatibility with database backend version.

## Examples

### Import models
**Args:** `from grz_db.models import Submission, Sample`
**Explanation:** Imports database models.

### Create session
**Args:** `from grz_db.session import create_session`
**Explanation:** Creates a database session.

### Query submissions
**Args:** `submissions = session.query(Submission).all()`
**Explanation:** Retrieves all submission records.

### Add new record
**Args:** `session.add(Submission(id='123', status='pending'))`
**Explanation:** Adds a new submission record.

### Commit transaction
**Args:** `session.commit()`
**Explanation:** Commits pending database changes.

### Rollback transaction
**Args:** `session.rollback()`
**Explanation:** Rolls back pending changes.

### Execute raw SQL
**Args:** `session.execute('SELECT COUNT(*) FROM submissions')`
**Explanation:** Executes raw SQL query.