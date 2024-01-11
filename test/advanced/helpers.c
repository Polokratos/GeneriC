
 void* id ( void* arg ) { return arg ; } 
 void swap ( void** src , void** dst ) { void* tmp ; tmp = *src ; *src = *dst ; *dst = tmp ; } 
 void doubleSwap ( void** ta , void** tb , void** qa , void** qb ) { void* tx ; tx = *ta ; void* qx ; qx = *qa ; *ta = *tb ; *qa = *qb ; *tb = tx ; *qb = qx ; } 
 int intId ( int val ) { return val ; } 