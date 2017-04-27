#include <stdio.h>
#include <stdlib.h>
#include "hashtable.h" //best practice to include own header, nn=eeded here because of table size

// define table struct - in header file

// def has func
int ourhash(int key)
{
  return key % TABLE_SIZE;
}

// def get func
int get(Table* tableptr, int key)
{
  int slot; //can declare vars at the top and add comments

  slot = ourhash(key);

  if (tableptr->keys[slot]==key) { //use arrow when table is a pointer
    return tableptr->values[slot];
  }
  else {
    return -1;
  }

}

// def set func
void set(Table* tableptr, int key, int value) //tableptr is a reference to a Table instance
{
  int slot;

  slot = ourhash(key);
  tableptr->keys[slot] = key;
  tableptr->values[slot] = value;
}


// def print table
void print_table(Table* tableptr)
{
  printf("\n size of table: %d address of table: %p", (int) sizeof *tableptr, tableptr);
  int i;
  for(i=0; i<TABLE_SIZE; i++) {
    int key;
    int val;
    key = tableptr->keys[i];
    val = tableptr->values[i];
    printf("\n key: %d    at %p    value: %d    at %p", key, &key, val, &val);
  };
}
