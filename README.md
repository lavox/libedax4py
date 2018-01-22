libedax4py
============

libedax4py is a python wrapper for libedax. With using libedax4py, you
can execute functions equivalent to edax commands from python.

To use libedax4py, you need libedax (C library).

https://github.com/lavox/edax-reversi/tree/libedax

Installation
-------------
You can install libedax4py with pip.

```sh
pip install libedax4py-0.1.0.tar.gz
```

API documentation
------------------
(TBD)

Currently, see Java documentation.

https://github.com/lavox/libedax4j/tree/master/docs/javadoc

and see examples in example folder.

Usage
------
To execute your python script, you must set;

* path to libedax.dylib as environment variable `DYLD_LIBRARY_PATH`. (OSX)
* path to libedax-x86.dll as environment variable `PATH`. (Windows 32-bit)


Windows:
```sh
set PATH=%PATH%;C:¥libedax¥bin
python example1.py
```

OSX
```sh
export DYLD_LIBRARY_PATH=~/libedax/bin
python example1.py
```

