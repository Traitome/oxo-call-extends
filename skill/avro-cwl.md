---
name: avro-cwl
category: programming
description: Avro-CWL - Avro serialization framework fork for Common Workflow Language
tags: [avro-cwl, serialization, cwl, workflow, data-exchange]
author: oxo-call-community
source_url: "https://pypi.python.org/pypi?:action=display&name=avro-cwl"
---

## Concepts

- **Tool Overview**: avro-cwl is a specialized fork of the Apache Avro serialization framework, modified by the CWL (Common Workflow Language) team to address specific compatibility issues with CWL workflows. Version 1.8.9.
- **Core Function**: Provides data serialization and deserialization capabilities optimized for CWL workflow tool communications and data exchange.
- **Avro Schema**: Uses Avro's schema-based serialization format for efficient data storage and exchange between workflow components.
- **CWL Integration**: Specifically designed to work seamlessly with CWL workflows, fixing compatibility issues present in standard Avro.
- **Data Serialization**: Supports binary and JSON serialization formats for flexible data representation.
- **RPC Framework**: Includes Remote Procedure Call (RPC) capabilities for distributed workflow execution.
- **Installation**: `conda install -c bioconda avro-cwl` or `pip install avro-cwl`.

## Pitfalls

- **Version Compatibility**: This is a specialized fork for CWL. Not recommended for general-purpose Avro usage.
- **CWL Dependency**: Primarily useful within CWL workflow contexts. Standard Avro may be better for other use cases.
- **Schema Evolution**: Avro schemas evolve over time. Ensure schema compatibility between producer and consumer.
- **Binary vs JSON**: Binary format is more compact but not human-readable. Choose appropriate format based on use case.
- **Python Version**: Verify Python version compatibility before installation.

## Examples

### Basic serialization to JSON
**Args:** `python -c "from avro.datafile import DataFileWriter; from avro.io import DatumWriter; schema = {'type': 'record', 'name': 'Test', 'fields': [{'name': 'value', 'type': 'int'}]}; writer = DataFileWriter(open('output.avro', 'wb'), DatumWriter(), schema); writer.append({'value': 42}); writer.close()"`
**Explanation:** Creates Avro file with simple record using JSON encoding.

### Deserialize Avro file
**Args:** `python -c "from avro.datafile import DataFileReader; from avro.io import DatumReader; reader = DataFileReader(open('input.avro', 'rb'), DatumReader()); [print(record) for record in reader]; reader.close()"`
**Explanation:** Reads and prints records from Avro file.

### Binary serialization
**Args:** `python -c "from avro.io import BinaryEncoder, DatumWriter; import io; schema = {'type': 'record', 'name': 'Test', 'fields': [{'name': 'value', 'type': 'int'}]}; writer = DatumWriter(schema); bytes_writer = io.BytesIO(); encoder = BinaryEncoder(bytes_writer); writer.write({'value': 100}, encoder); print(bytes_writer.getvalue())"`
**Explanation:** Serializes data to binary format for compact storage.

### Schema definition
**Args:** `python -c "from avro.schema import parse; schema = parse('{\"type\": \"record\", \"name\": \"Gene\", \"fields\": [{\"name\": \"name\", \"type\": \"string\"}, {\"name\": \"length\", \"type\": \"int\"}]}'); print(schema)"`
**Explanation:** Parses and validates Avro schema definition.

### RPC client usage
**Args:** `python -c "from avro.ipc import AvroRemoteException, HTTPTransceiver; client = HTTPTransceiver('localhost', 9090); requestor = avro.ipc.Requestor(parse(open('protocol.avpr').read()), client); result = requestor.request('method', {'param': 'value'}); print(result)"`
**Explanation:** Makes RPC call to Avro server using HTTP transport.

### CWL workflow integration
**Args:** `cwltool --avro output.cwl input.yml`
**Explanation:** Runs CWL workflow with Avro serialization for intermediate data exchange.