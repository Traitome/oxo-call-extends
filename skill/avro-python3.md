---
name: avro-python3
category: programming
description: Apache Avro - Python 3 serialization framework
tags: [avro-python3, serialization, python3, data-exchange]
author: oxo-call-community
source_url: "http://avro.apache.org/"
---

## Concepts

- **Tool Overview**: avro-python3 is the Python 3 compatible version of Apache Avro, a data serialization framework for efficient data exchange. Version 1.9.0.
- **Core Function**: Enables schema-based data serialization and deserialization for Python 3 environments.
- **Schema Definition**: Uses JSON-based schemas to define data structures with strong typing.
- **Data Serialization**: Supports binary and JSON serialization formats for flexible data representation.
- **Python 3 Support**: Specifically designed for Python 3.x environments with full compatibility.
- **RPC Framework**: Includes Remote Procedure Call capabilities for distributed computing.
- **Installation**: `conda install -c bioconda avro-python3` or `pip install avro`.

## Pitfalls

- **Schema Compatibility**: Ensure schema compatibility between producer and consumer applications.
- **Version Mismatch**: Different Avro versions may have incompatible serialization formats.
- **Binary vs JSON**: Binary format is compact but not human-readable. JSON is readable but larger.
- **Schema Registry**: For distributed systems, consider using a schema registry for version management.

## Examples

### Create Avro data file
**Args:** `python3 -c "from avro.datafile import DataFileWriter; from avro.io import DatumWriter; schema = {'type': 'record', 'name': 'Test', 'fields': [{'name': 'value', 'type': 'int'}]}; writer = DataFileWriter(open('output.avro', 'wb'), DatumWriter(), schema); writer.append({'value': 42}); writer.close()"`
**Explanation:** Creates Avro file with simple record using Python 3.

### Read Avro data file
**Args:** `python3 -c "from avro.datafile import DataFileReader; from avro.io import DatumReader; reader = DataFileReader(open('input.avro', 'rb'), DatumReader()); [print(r) for r in reader]; reader.close()"`
**Explanation:** Reads and prints records from Avro file using Python 3.

### Schema definition
**Args:** `python3 -c "from avro.schema import parse; schema = parse('{\"type\": \"record\", \"name\": \"Gene\", \"fields\": [{\"name\": \"name\", \"type\": \"string\"}]}'); print(schema)"`
**Explanation:** Parses and validates Avro schema in Python 3.

### RPC client
**Args:** `python3 -c "from avro.ipc import HTTPTransceiver; client = HTTPTransceiver('localhost', 9090); requestor = avro.ipc.Requestor(parse(open('protocol.avpr').read()), client); result = requestor.request('method', {'param': 'value'})"`
**Explanation:** Makes RPC call using Python 3 Avro library.

### Binary serialization
**Args:** `python3 -c "from avro.io import BinaryEncoder, DatumWriter; import io; schema = {'type': 'record', 'name': 'Data', 'fields': [{'name': 'id', 'type': 'int'}]}; writer = DatumWriter(schema); buf = io.BytesIO(); encoder = BinaryEncoder(buf); writer.write({'id': 100}, encoder); print(buf.getvalue())"`
**Explanation:** Serializes data to binary format for compact storage.

### Schema evolution
**Args:** `python3 -c "from avro.schema import parse; old = parse('{\"type\": \"record\", \"name\": \"Sample\", \"fields\": [{\"name\": \"name\", \"type\": \"string\"}]}'); new = parse('{\"type\": \"record\", \"name\": \"Sample\", \"fields\": [{\"name\": \"name\", \"type\": \"string\"}, {\"name\": \"value\", \"type\": [\"null\", \"int\"], \"default\": null}]}'); print('Backward compatible:', old.can_read(new))"`
**Explanation:** Checks schema compatibility for evolution.