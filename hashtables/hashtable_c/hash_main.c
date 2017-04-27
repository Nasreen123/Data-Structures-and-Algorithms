#include <stdio.h>  //prinf
#include <stdlib.h> //malloc
#include "hashtable.h"


void main()
{

      int result;

      // call table
      Table table;  //exists on stack

      printf("\n size of table: %d address of table: %p \n", (int) sizeof table, &table);

      set(&table, 5, 10);

      printf("\n value of key 5 in table: %d \n", get(&table, 5));

      set(&table, 21, 27);

      printf("\n value of key 5 in table: %d \n", get(&table, 5));

      print_table(&table);

      Table* table2ptr;  //make a pointer to table2

      table2ptr = malloc(sizeof (Table)); //assign space in memory for table2 (connect to table2ptr)
      //exists in heap

      printf("\n size of table: %d address of table: %p \n", (int) sizeof *table2ptr, table2ptr);

      set(table2ptr, 5, 27);

      printf("\n value of key 5 in table2ptr %d \n", get(table2ptr, 5));

      free(table2ptr); //the memory can now be used for something else - doesn't remove

      set(table2ptr, 5, 9); //<- we can still write to it

      printf("\n value of key 5 in  table2ptr %d \n", get(table2ptr, 5)); // <- still there!!!


}
