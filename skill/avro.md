---
name: avro
category: utility
description: Apache Avro - Data serialization framework for efficient data exchange
tags: [avro, serialization, data-exchange, schema, big-data]
author: oxo-call-community
source_url: "https://avro.apache.org/"
---

## Concepts

- **Tool Overview**: Apache Avro is a data serialization framework that provides rich data structures and a compact, fast binary data format. Version 1.8.0.
- **Core Function**: Enables efficient data serialization and deserialization with schema-based data representation.
- **Schema Definition**: Uses JSON-based schemas to define data structures, enabling dynamic typing and schema evolution.
- **Data Serialization**: Supports both binary (compact) and JSON (human-readable) serialization formats.
- **RPC Framework**: Includes built-in Remote Procedure Call (RPC) support for distributed computing.
- **Language Support**: Available for multiple programming languages including Python, Java, C++, and more.
- **Integration**: Widely used in big data processing frameworks like Hadoop, Spark, and Kafka for data exchange.
- **Installation**: `conda install -c bioconda avro` or `pip install avro`.

## Pitfalls

- **Schema Compatibility**: Schema changes require careful management. Use schema evolution features properly.
- **Binary vs JSON**: Binary format is compact but not human-readable. JSON is readable but larger.
- **Schema Registry**: For distributed systems, consider using a schema registry for version management.
- **Performance Considerations**: Binary serialization is faster but requires schema knowledge for interpretation.
- **Version Mismatch**: Ensure all components use compatible Avro versions to avoid deserialization errors.

## Examples

### Create Avro data file
**Args:** `python -c "from avro.datafile import DataFileWriter; from avro.io import DatumWriter; schema = {'type': 'record', 'name': 'Variant', 'fields': [{'name': 'chrom', 'type': 'string'}, {'name': 'pos', 'type': 'int'}, {'name': 'ref', 'type': 'string'}, {'name': 'alt', 'type': 'string'}]}; writer = DataFileWriter(open('variants.avro', 'wb'), DatumWriter(), schema); writer.append({'chrom': 'chr1', 'pos': 12345, 'ref': 'A', 'alt': 'T'}); writer.close()"`
**Explanation:** Creates Avro file with variant records using JSON schema definition.

### Read Avro data file
**Args:** `python -c "from avro.datafile import DataFileReader; from avro.io import DatumReader; reader = DataFileReader(open('variants.avro', 'rb'), DatumReader()); [print(r) for r in reader]; reader.close()"`
**Explanation:** Reads and prints all records from Avro file.

### Binary serialization to buffer
**Args:** `python -c "from avro.io import BinaryEncoder, DatumWriter; import io; schema = {'type': 'record', 'name': 'Gene', 'fields': [{'name': 'id', 'type': 'string'}, {'name': 'expression', 'type': 'float'}]}; writer = DatumWriter(schema); buf = io.BytesIO(); encoder = BinaryEncoder(buf); writer.write({'id': 'ENSG000001', 'expression': 12.5}, encoder); print(buf.getvalue())"`
**Explanation:** Serializes gene expression data to binary format for efficient storage.

### Parse Avro schema
**Args:** `python -c "from avro.schema import parse; schema = parse('{\"type\": \"record\", \"name\": \"Sample\", \"fields\": [{\"name\": \"name\", \"type\": \"string\"}, {\"name\": \"coverage\", \"type\": \"float\"}]}'); print('Schema parsed successfully:', schema.name)"`
**Explanation:** Parses JSON schema definition and validates its structure.

### Schema evolution
**Args:** `python -c "old_schema = parse('{\"type\": \"record\", \"name\": \"Sample\", \"fields\": [{\"name\": \"name\", \"type\": \"string\"}]}'); new_schema = parse('{\"type\": \"record\", \"name\": \"Sample\", \"fields\": [{\"name\": \"name\", \"type\": \"string\"}, {\"name\": \"batch\", \"type\": [\"null\", \"string\"], \"default\": null}]}'); print('Schemas compatible:', old_schema.can_read(new_schema))"`
**Explanation:** Demonstrates schema evolution with backward-compatible field addition.

### RPC server setup
**Args:** `python -c "from avro.ipc import AvroResponder, HTTPHandler; import socketserver; protocol = parse(open('protocol.avpr').read()); responder = AvroResponder(protocol, {'method': lambda params: 'Result: ' + str(params)}); server = socketserver.TCPServer(('localhost', 9090), HTTPHandler(responder)); server.serve_forever()"`
**Explanation:** Starts Avro RPC server with custom protocol and handler.

### Convert JSON to Avro
**Args:** `python -c "from avro.datafile import DataFileWriter; from avro.io import DatumWriter; import json; schema = parse('{\"type\": \"record\", \"name\": \"Data\", \"fields\": [{\"name\": \"value\", \"type\": \"int\"}]}'); writer = DataFileWriter(open('output.avro', 'wb'), DatumWriter(), schema); [writer.append(json.loads(line)) for line in open('input.json')]; writer.close()"`
**Explanation:** Converts JSON lines file to Avro format for efficient processing.