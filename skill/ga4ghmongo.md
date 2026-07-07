---
name: ga4ghmongo
category: variant-calling
description: A document based Variant database inspired by ga4gh Variants schema.
tags: [ga4ghmongo, variant database, MongoDB, GA4GH]
author: oxo-call-community
source_url: "https://github.com/Phelimb/ga4gh-mongo"
---

## Concepts
- **Variant Database**: Stores genetic variants in MongoDB.
- **GA4GH Schema**: Based on GA4GH variant schema.
- **Document-based**: Uses MongoDB document model.
- **Query Support**: Supports complex variant queries.
- **Scalability**: Scalable for large variant datasets.

## Pitfalls
- **MongoDB Dependence**: Requires MongoDB server.
- **Database Setup**: Complex database setup required.
- **Performance**: Query performance depends on indexing.
- **Data Migration**: Migrating data can be complex.
- **Version Compatibility**: MongoDB version compatibility.

## Examples
### Import VCF to database
**Args:** `ga4ghmongo import -v variants.vcf -d my_database`
**Explanation:** Imports VCF file into MongoDB.

### Query variants
**Args:** `ga4ghmongo query -d my_database -c chr1 -s 100000 -e 200000`
**Explanation:** Queries variants in specified region.

### Export to VCF
**Args:** `ga4ghmongo export -d my_database -o variants.vcf`
**Explanation:** Exports variants from database to VCF.

### Create index
**Args:** `ga4ghmongo index -d my_database -f position`
**Explanation:** Creates index on position field.

### List databases
**Args:** `ga4ghmongo list`
**Explanation:** Lists all available databases.