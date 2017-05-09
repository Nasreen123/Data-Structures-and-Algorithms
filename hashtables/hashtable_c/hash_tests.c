/* hash_tests.c   inspired by http://www.jera.com/techinfo/jtns/jtn002.html   */
#include <stdio.h>
#include <stdlib.h> //malloc
#include "minunit.h"
#include "hashtable.h"

int tests_run = 0;



/* COPY OF TESTS FROM hash_main.c 
   ************************************************************************** */

static char * tests_on_stack() {
    int result;

    Table table;  // exists on stack

    // sizof check
    mu_assert("error, unexpected size of table",
              (int) sizeof(table) == TABLE_SIZE*2*((int)sizeof(int)) );

    // set a value
    set(&table, 5, 10);
    result = get(&table, 5);
    mu_assert("incorrect value returned", result == 10);

    // set another value
    set(&table, 21, 27);
    result = get(&table, 21);
    mu_assert("incorrect value returned", result == 27);

    return 0;
}

static char * tests_on_heap() {
    int result;

    Table* table2ptr;                   // make a pointer to table2
    table2ptr = malloc(sizeof (Table)); // assign space in heap memory for table2

    // set a value
    set(table2ptr, 5, 10);
    result = get(table2ptr, 5);
    mu_assert("incorrect value returned", result == 10);

    // set another value
    set(table2ptr, 21, 27);
    result = get(table2ptr, 21);
    mu_assert("incorrect value returned", result == 27);

    free(table2ptr);

    // access after free (undefined behavior)
    set(table2ptr, 5, 9);                         // <- we can still write to it
    result = get(table2ptr, 5);
    mu_assert("incorrect value returned", result == 9);     // <- still there!!!

    return 0;
}




/* NEW TESTS (EXTRA QUALITY CONTROL CHECKS BECAUSE 10H TRAIN RIDE)
   ************************************************************************** */

static char * tests_extra() {
    int result;
    Table table;  // exists on stack

    // test large key
    set(&table, 563321134, 10);
    result = get(&table, 563321134);
    mu_assert("incorrect value returned", result == 10);

    // test large value
    set(&table, 12, 1092934282);
    result = get(&table, 12);
    mu_assert("incorrect value returned", result == 1092934282);

    // test missing key should return -1
    result = get(&table, 1212);
    mu_assert("missing key should return -1", result == -1);

    return 0;
}




static char * all_tests() {
    mu_run_test(tests_on_stack);
    mu_run_test(tests_on_heap);
    mu_run_test(tests_extra);   // new
    return 0;
}

int main(int argc, char **argv) {
    char *result = all_tests();
    if (result != 0) {
        printf("%s\n", result);
    }
    else {
        printf("\033[32;1mALL TESTS PASSED \033[0m\n");
    }
    printf("Tests run: %d\n", tests_run);

    return result != 0;
}

