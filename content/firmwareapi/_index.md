---
title: "Introduction"
aliases:
    - firmwareapi/expansionboards/_index.html
    - firmwareapi/expansionboards/_index.html

---

This chapter describes modules (function and class libraries) that are built into MicroPython. There are a number of categories for the available modules:

* [implemented by Pycom](/firmwareapi/pycom/)
* [Implemented by Micropython](/firmwareapi/micropython/)
* External or custom modules and libraries

## Note about the availability of modules and their contents

This documentation in general aspires to describe all modules and functions/classes which are implemented in MicroPython. However, MicroPython is highly configurable, and each port to a particular board/embedded system makes available only a subset of MicroPython libraries. For officially supported ports, there is an effort to either filter out non-applicable items, or mark individual descriptions with “Availability:” clauses describing which ports provide a given feature. With that in mind, please still be warned that some functions/classes in a module (or even the entire module) described in this documentation may be unavailable in a particular build of MicroPython on a particular board. The best place to find general information of the availability/non-availability of a particular feature is the “General Information” section which contains information pertaining to a specific port.

Beyond the built-in libraries described in this documentation, many more modules from the Python standard library, as well as further MicroPython extensions to it, can be found in the [micropython-lib](https://github.com/micropython/micropython-lib) repository.
