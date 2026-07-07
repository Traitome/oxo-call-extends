---
name: suds-jurko
category: utility
description: Lightweight SOAP client (Jurko's fork) for accessing web services.
tags: [suds-jurko, soap, web-services, python]
author: oxo-call-community
source_url: "http://bitbucket.org/jurko/suds"
---

## Concepts

- **Tool Overview**: suds-jurko (v0.6) is a lightweight SOAP client library for Python.
- **Core Function**: Provides SOAP client functionality for accessing web services.
- **Algorithm**: Parses WSDL files and generates Python bindings for SOAP operations.
- **Input/Output**: Input: WSDL URL, SOAP requests; Output: SOAP responses.
- **Applications**: Web service access, API integration, bioinformatics web services.
- **Installation**: `conda install -c bioconda suds-jurko` or pip install.

## Pitfalls

- **WSDL Compatibility**: May not support all WSDL features.
- **Network Dependencies**: Requires network access for web services.
- **Version Compatibility**: May not work with all SOAP versions.
- **Error Handling**: SOAP errors require proper handling.
- **Complex Types**: Complex data types may require special handling.
- **Performance**: Large SOAP messages may be slow.

## Examples

### Display help
**Args:** `python -c "from suds.client import Client; help(Client)"`
**Explanation:** Shows available options and usage information.

### Basic SOAP client
**Args:** `python -c "from suds.client import Client; c = Client('http://example.com/service?wsdl'); print(c.service.method())"`
**Explanation:** Create SOAP client and call method.

### With authentication
**Args:** `python -c "from suds.client import Client; c = Client('http://example.com/service?wsdl', username='user', password='pass')"`
**Explanation:** Create SOAP client with authentication.

### Verbose mode
**Args:** `python -c "from suds.client import Client; c = Client('http://example.com/service?wsdl', cache=None, faults=True)"`
**Explanation:** Run with detailed logging.

### Batch processing
**Args:** `python -c "from suds.client import Client; c = Client('http://example.com/service?wsdl'); [c.service.process(i) for i in items]"`
**Explanation:** Process multiple requests together.

### Error handling
**Args:** `python -c "from suds.client import Client; from suds import WebFault; c = Client('http://example.com/service?wsdl'); try: c.service.method() except WebFault as e: print(e)"`
**Explanation:** Handle SOAP faults gracefully.

### Timeout configuration
**Args:** `python -c "from suds.client import Client; c = Client('http://example.com/service?wsdl', timeout=30)"`
**Explanation:** Set timeout for SOAP requests.

### Custom headers
**Args:** `python -c "from suds.client import Client; c = Client('http://example.com/service?wsdl'); c.set_options(soapheaders={'Header': 'value'})"`
**Explanation:** Add custom SOAP headers.

### Generate report
**Args:** `python -c "from suds.client import Client; c = Client('http://example.com/service?wsdl'); print(c)"`
**Explanation:** Print service description and methods.
