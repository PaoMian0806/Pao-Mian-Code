#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main()
{
    float a,b,c;
    cin>>a>>b;
    if (b == 1){
        c = (a - 80) * 0.7;
    }
    else if(b == 2){
        c = (a - 70) * 0.6;
    }
    cout<<fixed<<setprecision(1)<<c;
    return 0;
}
