#include <stdio.h>

int calculate(int a, int b,int c, int d, int *sum, int *diff, int *prod, int *quot) {
    *sum = a + b + c + d;
    *diff = a - b - c - d;
    *multi = a * b * c * d;
    *div = ((a/b)/c)/d;


}

}

int main() {
    int w, x, y, z;
    int s, d, m, div;
    printf("Press input Data : ");
    scanf("%d %d %d %d", &w, &x, &y, &z);
    calculate(w, x, y, z, &s, &d, &m, &div);
    printf("Sum: %d,Difference: %d, multi=%d, Div =%d);

    return 0;

}