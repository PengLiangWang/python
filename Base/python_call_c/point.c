#include <stdio.h>
#include <string.h>

//用指针才可以

struct point
{
    int x;
    char *y;
};


void point_print(struct point *p)
{
    p->x = p->x + p->x;
    printf("p->x = %d\np->y = %s\n", p->x, p->y);
}
