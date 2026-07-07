---
name: lsd
category: utility
description: The LAPPS Grid Services DSL (LSD). Used to invoke LAPPS web services from the command line.
tags: [lsd, utility, LAPPS, web-services]
author: oxo-call-community
source_url: "http://github.com/lappsgrid-incubator/org.anc.lapps.dsl"
---

## Concepts

- **Tool Overview**: lsd v2.2.3 is a Domain Specific Language (DSL) for invoking LAPPS Grid web services from the command line.
- **Core Function**: Provides a simplified interface for accessing bioinformatics web services in the LAPPS Grid.
- **Service Integration**: Connects to various LAPPS services including annotation, parsing, and analysis tools.
- **Input/Output**: Input: Text files or command-line arguments; Output: Processed results from web services.
- **Installation**: `conda install -c bioconda lsd`
- **Key Features**: Simplifies web service invocation, supports workflow composition, integrates with LAPPS Grid ecosystem.

## Pitfalls

- **Network Dependency**: Requires internet connection to access LAPPS Grid services.
- **Service Availability**: Dependent on remote service availability; may fail if services are down.
- **Authentication**: Some services may require authentication or API keys.
- **Response Time**: Web service calls can be slow depending on server load.
- **Version Compatibility**: Service APIs may change over time.
- **Error Handling**: Error messages from remote services may be unclear or unhelpful.

## Examples

### Run basic analysis
**Args:** `lsd run -s service_name -i input.txt -o output.txt`
**Explanation:** Runs specified LAPPS service on input file.

### List available services
**Args:** `lsd list`
**Explanation:** Lists all available LAPPS Grid services.

### Service info
**Args:** `lsd info -s service_name`
**Explanation:** Shows detailed information about a specific service.

### Workflow composition
**Args:** `lsd workflow -f workflow.json -i input.txt -o output.txt`
**Explanation:** Executes a workflow composed of multiple services.

### Verbose mode
**Args:** `lsd run -s service_name -i input.txt -o output.txt -v`
**Explanation:** Outputs detailed log information during processing.

### Help documentation
**Args:** `lsd --help`
**Explanation:** Displays all available commands and options.