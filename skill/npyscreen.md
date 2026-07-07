---
name: npyscreen
category: programming
description: npyscreen is a Python library for creating text-based user interfaces (TUI).
tags: [npyscreen, programming, tui, user-interface]
author: oxo-call-community
source_url: "http://www.npcole.com/npyscreen/"
---

## Concepts

- **Tool Overview**: npyscreen provides components for building text-based user interfaces.
- **Core Function**: Creates interactive terminal applications with forms and widgets.
- **Algorithm**: Implements TUI components with event-driven architecture.
- **Input Format**: Accepts Python code for UI definition.
- **Output**: Produces interactive terminal interfaces.
- **Use Case**: Terminal applications, command-line tools, and interactive scripts.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Terminal Compatibility**: Requires terminal with proper ANSI support.
- **Learning Curve**: May require learning new API.
- **Limited Features**: Less feature-rich than GUI frameworks.
- **Documentation**: Limited documentation.
- **Cross-platform**: May have platform-specific issues.

## Examples

### Install package
**Args:** `pip install npyscreen`
**Explanation:** Installs npyscreen package.

### Import module
**Args:** `import npyscreen`
**Explanation:** Imports npyscreen module.

### Create application
**Args:** `class MyApp(npyscreen.NPSAppManaged): pass`
**Explanation:** Creates basic application class.

### Add form
**Args:** `self.addForm('MAIN', npyscreen.Form, name='My App')`
**Explanation:** Adds main form to application.

### Add widget
**Args:** `self.addWidget(npyscreen.TitleText, name='Name:')`
**Explanation:** Adds text input widget.

### Run application
**Args:** `MyApp().run()`
**Explanation:** Runs the application.

### Modal dialog
**Args:** `npyscreen.notify_confirm('Hello World')`
**Explanation:** Shows confirmation dialog.