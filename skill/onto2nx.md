---
name: onto2nx
category: formatting
description: onto2nx parses OWL and OBO ontologies into NetworkX graphs for analysis.
tags: [onto2nx, formatting, ontology, networkx]
author: oxo-call-community
source_url: "https://github.com/cthoyt/onto2nx"
---

## Concepts

- **Tool Overview**: onto2nx converts ontology formats to NetworkX graphs.
- **Core Function**: Parses OWL and OBO files into graph structures.
- **Algorithm**: Uses ontology parsing libraries for graph construction.
- **Input Format**: Accepts OWL and OBO ontology files.
- **Output**: Produces NetworkX graphs for analysis.
- **Use Case**: Ontology analysis, semantic reasoning, and graph traversal.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Ontology Complexity**: Complex ontologies may be slow to parse.
- **Memory Usage**: Large ontologies require memory.
- **Dependency Issues**: Requires NetworkX and ontology libraries.
- **Format Compatibility**: May not support all ontology features.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `python -c "from onto2nx import parse_ontology; help(parse_ontology)"`
**Explanation:** Shows available options and usage instructions.

### Parse OBO
**Args:** `python -c "from onto2nx import parse_ontology; G = parse_ontology('go.obo')"`
**Explanation:** Parses OBO ontology file.

### Parse OWL
**Args:** `python -c "G = parse_ontology('ontology.owl')"`
**Explanation:** Parses OWL ontology file.

### Graph statistics
**Args:** `python -c "print(G.number_of_nodes(), G.number_of_edges())"`
**Explanation:** Prints graph statistics.

### Save graph
**Args:** `python -c "nx.write_graphml(G, 'ontology.graphml')"`
**Explanation:** Saves graph to GraphML format.

### Query nodes
**Args:** `python -c "nodes = [n for n in G.nodes if 'gene' in n.lower()]"`
**Explanation:** Queries nodes matching criteria.

### Traverse graph
**Args:** `python -c "paths = nx.shortest_path(G, source, target)"`
**Explanation:** Finds shortest path between nodes.