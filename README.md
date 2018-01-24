libedax4py
============

libedax4py is a python wrapper for libedax. With using libedax4py, you
can execute functions equivalent to edax commands from python.

To use libedax4py, you need libedax (C library).

https://github.com/lavox/edax-reversi/releases

Installation
-------------
You can install libedax4py with pip.

```sh
pip install libedax4py-0.1.0.tar.gz
```

API documentation
------------------
(TBD)

Currently, see C-library documentation.

https://lavox.github.io/libedax4py/html/libedax_8c.html

You can use `DLL_API` function in `libedax.c`, `board.c` and `bit.c` via libedax4py. 

Java documentation for libedax4j is available. Basically, libedax4py and libedax4j have same interface.

https://lavox.github.io/libedax4j/javadoc/

Also, see examples in example folder.

Usage
------
To execute your python script, you must set;

* path to libedax.dylib as environment variable `DYLD_LIBRARY_PATH`. (OSX)
* path to libedax-x86.dll as environment variable `PATH`. (Windows 32-bit)

You can specify book file and eval file with `libedax_initialize()` function.

Example
--------
Windows:
```
C:¥
+-- libedax¥
    +-- bin¥
    |   +-- libedax-x86.dll
    +-- data¥
    |   +-- book.dat
    |   +-- eval.dat
    +-- example¥
        +-- example1.py
```
If directory structure is as above, execute the following commands in `C:¥libedax¥example` directory.

```sh
set PATH=%PATH%;C:¥libedax¥bin
python example1.py
```

OSX
```
HOME_DIRECTORY
+-- libedax/
    +-- bin/
    |   +-- libedax.dylib
    +-- data/
    |   +-- book.dat
    |   +-- eval.dat
    +-- example/
        +-- example1.py
```
If directory structure is as above, execute the following commands in `HOME_DIRECTORY/libedax/example` directory.
```sh
export DYLD_LIBRARY_PATH=~/libedax/bin
python example1.py
```

