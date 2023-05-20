#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main()
{
    int a = 0; int b = 0; int c = 1;
    cin>>a;
    for (int i = 1; i <= a; i++){
        b = a % i;
        if (a == 1){
            c = 0;
            break;
        }
        else if (b == 0){
            if (i != 1 && i != a){
              c = 0;
              break;   
            }
        }
    }
    if (c == 1){
        cout<<"Yes";
    }
    else{
        cout<<"No";
    }
    return 0;
}
