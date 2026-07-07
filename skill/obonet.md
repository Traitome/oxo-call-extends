---
name: obonet
category: formatting
description: obonet parses OBO-formatted ontologies into NetworkX graph objects for analysis.
tags: [obonet, formatting, ontology, networkx]
author: oxo-call-community
source_url: "https://github.com/dhimmel/obonet"
---

## Concepts

- **Tool Overview**: obonet parses OBO ontology files into NetworkX graph structures.
- **Core Function**: Converts OBO format to NetworkX graphs for analysis.
- **Algorithm**: Parses OBO syntax and builds graph representations.
- **Input Format**: Accepts OBO-formatted ontology files.
- **Output**: Produces NetworkX graph objects.
- **Use Case**: Ontology analysis, graph traversal, and semantic reasoning.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **OBO Format**: Requires proper OBO format compliance.
- **Memory Usage**: Large ontologies require memory.
- **Complexity**: Very large ontologies may be slow to parse.
- **Dependency Issues**: Requires NetworkX library.
- **Validation**: Results should be validated for correctness.

## Examples

### Import and use
**Args:** `python -c "import obonet; print(obonet.__version__)"`
**Explanation:** Checks obonet version.

### Parse OBO file
**Args:** `python -c "import obonet; graph = obonet.read_obo('ontology.obo')"`
**Explanation:** Parses OBO file into NetworkX graph.

### Get nodes
**Args:** `python -c "nodes = list(graph.nodes())"`
**Explanation:** Gets list of ontology terms.

### Get edges
**Args:** `python -c "edges = list(graph.edges())"`
**Explanation:** Gets list of relationships.

### Find parents
**Args:** `python -c "parents = [n for n in graph.predecessors('GO:0005886')]"`
**Explanation:** Finds parent terms for a given node.

### Export to graphML
**Args:** `python -c "nx.write_graphml(graph, 'ontology.graphml')"`
**Explanation:** Exports graph to GraphML format.

### Count nodes
**Args:** `python -c "print(len(graph.nodes()))"`
**Explanation:** Counts number of ontology terms.