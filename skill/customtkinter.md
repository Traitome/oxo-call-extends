---
name: customtkinter
category: programming
description: Create modern looking GUIs with Python
tags: [customtkinter, programming, GUI, Python, tkinter]
author: oxo-call-community
source_url: "https://customtkinter.tomschimansky.com"
---

## Concepts

- **Tool Overview**: customtkinter (v5.2.2+) is a Python library for creating modern, customizable GUI applications using Tkinter as the backend.
- **Core Function**: Provides enhanced widgets and themes for building professional-looking graphical interfaces.
- **Input/Output**: Input: Python code with widget definitions. Output: Interactive GUI applications.
- **Key Features**: Modern widgets (buttons, frames, progress bars), customizable themes, dark/light mode support, native look-and-feel.
- **Installation**: `conda install -c bioconda customtkinter`

## Pitfalls

- **Tkinter Dependency**: Requires Tkinter to be installed in Python environment.
- **Version Compatibility**: Widgets may behave differently across versions; check changelogs.
- **Platform Differences**: Appearance may vary across operating systems.
- **Documentation**: Refer to official documentation for widget-specific parameters.
- **Event Handling**: Proper event binding requires understanding of Tkinter event system.

## Examples

### Create simple GUI window
**Args:**
```python
import customtkinter as ctk
app = ctk.CTk()
app.title("My App")
app.geometry("400x300")
label = ctk.CTkLabel(app, text="Hello World")
label.pack(pady=20)
app.mainloop()
```
**Explanation:** Create a basic window with a label using customtkinter.

### Create button with command
**Args:**
```python
import customtkinter as ctk

def button_callback():
    print("Button clicked!")

app = ctk.CTk()
button = ctk.CTkButton(app, text="Click Me", command=button_callback)
button.pack(pady=20)
app.mainloop()
```
**Explanation:** Create a button with click event handler.

### Set dark mode
**Args:**
```python
import customtkinter as ctk
ctk.set_appearance_mode("dark")
app = ctk.CTk()
app.title("Dark Mode App")
app.mainloop()
```
**Explanation:** Create application with dark mode appearance.
