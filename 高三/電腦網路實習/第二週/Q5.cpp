#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main()
{
    char a[5];
    cin.getline(a, 5);
    for (int i = 0; i < 4; i++){
        int p = a[i] - '0';
        while (p % 3 != 0){
            p += 10;   
        }
        cout<<p/3;
    }
    return 0;
}
