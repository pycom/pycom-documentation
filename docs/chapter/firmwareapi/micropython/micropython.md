# class micropython – MicroPython Internals Controls

### Functions
<function>micropython.alloc_emergency_exception_buf(size)</function>

Allocate size bytes of RAM for the emergency exception buffer (a good size is around 100 bytes). The buffer is used to create exceptions in cases when normal RAM allocation would fail (eg within an interrupt handler) and therefore give useful traceback information in these situations.

A good way to use this function is to place it at the start of a main script (eg boot.py or main.py) and then the emergency exception buffer will be active for all the code following it.
