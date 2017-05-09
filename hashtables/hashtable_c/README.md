Simple hash table in C
======================
The code in `hashtable.h` and `hashtable.c` implements a simple fixed-size hash table.
This is a high-performance hash table with a lossy behaviour--new entries will
overwrite older entries.


Install
-------
Requires just a C compiler (gcc / clang).  No external libraries are required.


Compile and run
---------------

    gcc -o hashmain hash_main.c hashtable.c 
    ./hashmain


Run detailed tests
------------------

    gcc -o hashtests hash_tests.c hashtable.c 
    ./hashtests


