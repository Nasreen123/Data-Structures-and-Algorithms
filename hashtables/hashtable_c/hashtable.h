#ifndef HEASHTABLEHEADER //not necessary but good practice
#define HEASHTABLEHEADER

#define TABLE_SIZE  16

// define table struct
typedef struct //put the name here too if recursive/ self referencing struct
{
  int keys[TABLE_SIZE];
  int values[TABLE_SIZE];
} Table;

// dec has func
int ourhash(int key);

// dec get func
int get(Table* tableptr, int key);

// dec set func
void set(Table* tableptr, int key, int value); //tableptr is a reference to a Table instance

// dec print table
void print_table(Table* tableptr);

#endif
