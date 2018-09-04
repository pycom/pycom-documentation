# MicroPython Modules

The following list contains the standard Python libraries, MicroPython-specific libraries and Pycom specific modules that are available on the Pycom devices.

The standard Python libraries have been "micro-ified" to fit in with the philosophy of MicroPython. They provide the core functionality of that module and are intended to be a drop-in replacement for the standard Python library.

{% hint style="info" %}
Some modules are available by an u-name, and also by their non-u-name. The non-u-name can be overridden by a file of that name in your package path. For example, `import json` will first search for a file `json.py` or directory `json` and load that package if it's found. If nothing is found, it will fallback to loading the built-in `ujson` module.
{% endhint %}

