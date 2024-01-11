
 void* id ( void* arg ) { return arg ; } 
 void swap ( void** src , void** dst ) { void* tmp ; tmp = *src ; *src = *dst ; *dst = tmp ; } 
 void doubleSwap ( void** ta , void** tb , void** qa , void** qb ) { void* tx ; tx = *ta ; void* qx ; qx = *qa ; *ta = *tb ; *qa = *qb ; *tb = tx ; *qb = qx ; } 
 int intId ( int val ) { return val ; } 
 void bubbleSort ( void** array , int length ) { for ( int i = 0 ; i < length ; i ++ ) { int j = i ; while ( j < length ) { if ( array[i] > array[j] ) { void* val = array[i] ; void* rep = array[j] ; array[j] = val ; array[i] = rep ; } j ++ ; } } } 