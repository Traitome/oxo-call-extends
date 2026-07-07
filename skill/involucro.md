---
name: involucro
category: containerization
description: Build and Deliver Software with Containers
tags: [involucro, containerization, docker, deployment, devops]
author: oxo-call-community
source_url: "https://github.com/involucro/involucro"
---

## Concepts

- **Tool Overview**: Involucro (v1.1.2) is a tool for building and delivering software using Docker containers. It simplifies container image creation and deployment through a declarative configuration approach.

- **Declarative Container Building**: Uses YAML-based configuration files to define container builds, eliminating the need for complex Dockerfiles.

- **Multi-stage Builds**: Supports multi-stage container builds to optimize image size and security by separating build and runtime environments.

- **Configuration Management**: Centralizes container configuration, making it easier to maintain consistent builds across different environments.

- **Integration with CI/CD**: Designed to integrate seamlessly with continuous integration and deployment pipelines, automating container image creation and distribution.

- **Security Scanning**: Includes built-in security scanning features to detect vulnerabilities in container images before deployment.

## Pitfalls

- **Docker Dependency**: Requires Docker to be installed and running. Ensure Docker daemon is available before using involucro.

- **Configuration Complexity**: While declarative, complex builds may require detailed configuration. Start with simple configurations and gradually add complexity.

- **Image Size Optimization**: Without proper multi-stage configuration, images can become bloated. Use appropriate base images and cleanup steps.

- **Network Requirements**: Building containers may require downloading large base images and dependencies. Ensure network connectivity and consider local image caching.

- **Version Compatibility**: Container images built with newer Docker features may not run on older Docker versions. Target the appropriate Docker API version.

- **Security Considerations**: Container images may inherit vulnerabilities from base images. Regularly update base images and scan for security issues.

## Examples

### Basic container build
**Args:** `involucro build --config involucro.yml --tag myapp:latest`
**Explanation:** Builds a container image using the specified configuration file and tags it with the latest version.

### Multi-stage build for production
**Args:** `involucro build --config prod.yml --tag myapp:prod --push registry.example.com/myapp`
**Explanation:** Builds a production-ready container image and pushes it to a container registry.

### Local development environment
**Args:** `involucro run --config dev.yml --mount ./src:/app --port 8080:80`
**Explanation:** Runs a development container with local source code mounted and port forwarding enabled.

### Security scan before deployment
**Args:** `involucro scan --image myapp:latest --severity high`
**Explanation:** Scans the container image for high-severity vulnerabilities before deployment.

### Build and test pipeline
**Args:** `involucro build --config test.yml && involucro test --image myapp:test`
**Explanation:** Builds a test image and runs automated tests inside the container.

### Export container image
**Args:** `involucro export --image myapp:latest --output myapp.tar`
**Explanation:** Exports the container image to a tar archive for offline distribution or backup.