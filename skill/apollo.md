---
name: apollo
category: annotation
description: python-apollo - Python API library for interacting with WebApollo genome annotation editor
tags: [apollo, webapollo, genome-annotation, api, python]
author: oxo-call-community
source_url: "https://github.com/galaxy-genome-annotation/python-apollo"
---

## Concepts

- **Tool Overview**: python-apollo (v4.2.13) - A Python library for interacting with the WebApollo genome annotation editor API.
- **Core Function**: Provides programmatic access to WebApollo for automated genome annotation management, user administration, and data import/export.
- **WebApollo**: A browser-based, evidence-driven genome annotation editor built on JBrowse, enabling collaborative annotation workflows.
- **Key Modules**:
  - **annotations**: Manage genomic annotations (genes, transcripts, features)
  - **organisms**: Organism and genome management
  - **users**: User management and permissions
  - **groups**: Group management
  - **io**: Import/export annotations (GFF3, FASTA)
  - **metrics**: Annotation metrics collection
- **Installation**: `conda install -c bioconda apollo`

## Pitfalls

- **Apollo Server Required**: Requires access to a running WebApollo server
- **API Rate Limiting**: Apollo may return 500 errors if APIs are called too quickly; use retry logic
- **Version Compatibility**: API may differ between WebApollo versions
- **Authentication**: Requires valid username and password for the Apollo instance
- **Permissions**: Operations require appropriate permissions (read/write/export)

## Examples

### Connect to Apollo instance
**Args:** `from apollo import ApolloInstance; wa = ApolloInstance(url='https://apollo.example.org', username='user', password='pass')`
**Explanation:** Establishes connection to a WebApollo server.

### Create organism
**Args:** `wa.organisms.add_organism('MyOrganism', genus='Genus', species='species', public=False)`
**Explanation:** Creates a new organism in Apollo with specified metadata.

### Upload genome sequence
**Args:** `wa.organisms.add_sequence('MyOrganism', 'chr1', sequence_fasta='genome.fa')`
**Explanation:** Uploads a genome sequence to an existing organism.

### Import annotations from GFF3
**Args:** `wa.annotations.load_gff3('MyOrganism', 'annotations.gff3')`
**Explanation:** Imports annotations from a GFF3 file.

### Update user permissions
**Args:** `wa.users.update_organism_permissions('user@example.com', 'MyOrganism', write=True, read=True, export=True)`
**Explanation:** Sets permissions for a user on a specific organism.

### Export annotations
**Args:** `annotations = wa.annotations.export_gff3('MyOrganism')`
**Explanation:** Exports annotations from Apollo in GFF3 format.