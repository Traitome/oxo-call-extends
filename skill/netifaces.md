---
name: netifaces
category: programming
description: Netifaces is a Python library for getting network interface addresses.
tags: [netifaces, programming, network, python, interface]
author: oxo-call-community
source_url: "https://bitbucket.org/al45tair/netifaces"
---

## Concepts

- **Tool Overview**: Netifaces is a Python library for network interface address retrieval.
- **Core Function**: Provides cross-platform access to network interface information.
- **Algorithm**: Interfaces with system network configuration APIs.
- **Input Format**: Python API calls to query network interfaces.
- **Output**: Returns network interface addresses and configuration details.
- **Use Case**: Network programming, system administration, and network diagnostics.

## Pitfalls

- **Version Differences**: API may change between versions.
- **Platform Specificity**: Behavior may vary across operating systems.
- **Permission Requirements**: May require elevated privileges.
- **Network Changes**: Results may become stale if network configuration changes.
- **Python Version**: May require specific Python version for compatibility.
- **Documentation**: Limited documentation requires code exploration.

## Examples

### Display help
**Args:** `python -c "import netifaces; help(netifaces)"`
**Explanation:** Shows available methods and usage instructions.

### Get interfaces
**Args:** `import netifaces; ifaces = netifaces.interfaces()`
**Explanation:** Gets list of network interfaces.

### Get addresses
**Args:** `addrs = netifaces.ifaddresses('eth0')`
**Explanation:** Gets addresses for specific interface.

### Get IPv4 addresses
**Args:** `ipv4 = netifaces.ifaddresses('eth0')[netifaces.AF_INET]`
**Explanation:** Gets IPv4 addresses for interface.

### Get gateway
**Args:** `gateway = netifaces.gateways()['default'][netifaces.AF_INET]`
**Explanation:** Gets default gateway.

### Get all addresses
**Args:** `for iface in netifaces.interfaces(): print(netifaces.ifaddresses(iface))`
**Explanation:** Prints all interface addresses.