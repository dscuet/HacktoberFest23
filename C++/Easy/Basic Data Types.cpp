#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    // Declared variables
    int a;
    long b;
    char c;
    float d;
    double e;
    
    // Take input
    scanf("%d %ld %c %f %lf", &a, &b, &c, &d, &e);
    
    // Output it
    printf("%d\n%ld\n%c\n%.3f\n%.9lf", a, b, c, d, e);
    
    return 0;
}