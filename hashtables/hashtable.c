#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE  16

// define table struct
typedef struct //put the name here too if recursive/ self referencing struct
{
  int keys[TABLE_SIZE];
  int values[TABLE_SIZE];
} Table;

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


void main()
{

int result;

// call table
Table table;  //exists on stack

///////////////// PRINT ADDRESS

printf("\n size of table: %d address of table: %p \n", (int) sizeof table, &table);

set(&table, 5, 10);

printf("\n value of key 5 in table: %d \n", get(&table, 5));

set(&table, 21, 27);

printf("\n value of key 5 in table: %d \n", get(&table, 5));

print_table(&table);

Table* table2ptr;  //make a pointer to table2

table2ptr = malloc(sizeof (Table)); //assign space in memory for table2 (connect to table2ptr)
//exists in heap

///////////////// PRINT ADDRESS

printf("\n size of table: %d address of table: %p \n", (int) sizeof *table2ptr, table2ptr);

set(table2ptr, 5, 27);

printf("\n value of key 5 in table2ptr %d \n", get(table2ptr, 5));

free(table2ptr); //the memory can now be used for something else - doesn't remove

set(table2ptr, 5, 9); //<- we can still write to it

printf("\n value of key 5 in  table2ptr %d \n", get(table2ptr, 5)); // <- still there!!!


}
