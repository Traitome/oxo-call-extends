---
name: sbt
category: build
description: sbt - interactive build tool for Scala and Java projects
tags: ["sbt", "build", "Scala", "Java"]
author: oxo-call-community
source_url: "http://www.scala-sbt.org/"
---

## Concepts

- **Tool Overview**: sbt (v0.13.12) is the interactive build tool for Scala and Java projects, providing dependency management, compilation, testing, and deployment.
- **Core Function**: Builds, tests, and packages Scala/Java applications with automatic dependency resolution.
- **Build Automation**: Supports incremental compilation, parallel testing, and continuous integration.
- **Input/Output**: Works with build.sbt configuration files and project source code.
- **Plugin System**: Extensible through plugins for additional functionality.
- **Applications**: Scala/Java project building, testing, and deployment automation.

## Pitfalls

- **Scala Specific**: Primarily designed for Scala projects, limited Java-only support.
- **Memory Usage**: Can consume significant memory for large projects.
- **Dependency Resolution**: May have issues with complex dependency graphs.
- **Learning Curve**: Complex build configuration for beginners.
- **Version Compatibility**: Different sbt versions may have incompatible syntax.
- **Slow Startup**: Initial project loading can be slow for large codebases.

## Examples

### Compile project
**Args:** `sbt compile`
**Explanation:** Compiles the project source code.

### Run tests
**Args:** `sbt test`
**Explanation:** Runs all project tests.

### Package JAR
**Args:** `sbt package`
**Explanation:** Packages project into JAR file.

### Run application
**Args:** `sbt run`
**Explanation:** Runs the main class of the application.

### Interactive mode
**Args:** `sbt`
**Explanation:** Starts interactive sbt shell for multiple commands.

### Clean build
**Args:** `sbt clean compile`
**Explanation:** Cleans previous build artifacts and recompiles.

### Generate documentation
**Args:** `sbt doc`
**Explanation:** Generates API documentation using Scaladoc.