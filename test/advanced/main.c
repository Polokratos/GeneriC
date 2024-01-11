#include<stdio.h>

#include "helpers.c"

struct MyStruct
{
    int x;
    int y;
}; typedef struct MyStruct MyStruct;


int main()
{
    int i = 10;
    printf("intId - not Generic: %d == %d",i,intId(i));
    int* i_adr = &i;
    int* i_adr_cpy = id(i_adr);

    printf("\n id - generic: %d == %d", *i_adr, *i_adr_cpy);

    int j = 20;     
    int* j_adr = &j;

    printf("\ni:%d j:%d",*i_adr,*j_adr);
    swap(&i_adr,&j_adr);
    printf("\ni:%d j:%d",*i_adr,*j_adr);

    MyStruct p;
    p.x = 100;
    p.y = 200;
    MyStruct q;
    q.x = -100;
    q.y = -200;

    MyStruct* p_adr = &p;
    MyStruct* q_adr = &q;

    printf("\nP:%d;%d Q:%d%d",p_adr->x,p_adr->y,q_adr->x,q_adr->y);
    swap(&p_adr,&q_adr);
    printf("\nP:%d;%d Q:%d%d",p_adr->x,p_adr->y,q_adr->x,q_adr->y);

    printf("\n DoubleSwap");
    doubleSwap(&i_adr,&j_adr,&p_adr,&q_adr);
    printf("\ni:%d j:%d",*i_adr,*j_adr);
    printf("\nP:%d;%d Q:%d%d",p_adr->x,p_adr->y,q_adr->x,q_adr->y);

    printf("\nBubbleSort");

    int* c[10] = {4,6,1,3,2,8,9,0,5,7};

    printf("\n");
    for (int i = 0; i < 10; i++)
    {
        printf("%d at %d ",(int)c[i],i);
    }

    bubbleSort(&c,10);

    printf("\n");
    for (int i = 0; i < 10; i++)
    {
        printf("%d at %d ",(int)c[i],i);
    }

    printf("\n");
    return 0;    
}