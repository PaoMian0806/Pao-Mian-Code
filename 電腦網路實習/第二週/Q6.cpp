#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main()
{
    char a[5];
    char b[5];
    int A = 0;
    int B = 0;
    int C = 0;
    int C1 = 0;
    
    cin.getline(a,5);
    while (C1 == 0){
        A = 0;
        B = 0;
        C = 0;
        
        cin.getline(b,5);
        
        for (int i = 0; i < 4; i++){
                int b2 = b[i] - '0';
                if (b2 == 0){
                    if (C != 4){
                        C+=1;
                    }
                }
            }
            if (C == 4){
                C1 == 1;
                break;
            }
        for (int i = 0; i < 4; i++){
            int a1 = a[i] - '0';
            for (int j = 0; j < 4; j++){
                int b1 = b[j] - '0';
                if (a1 == b1){
                    if (i == j){
                        A+=1;
                        break;
                    }
                    if (i != j){
                        B+=1;
                        break;
                    }
                }
            }
        }
        cout<<A<<"A"<<B<<"B"<<endl;
    }
    return 0;
}
