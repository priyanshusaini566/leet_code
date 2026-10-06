
#include<iostream>
using namespace std;
int main(){
    int arr[]={1,0,1,0,2,1,0,2,1};
    int zero=0;
    int one=0;
    int two=0;

    for (int i = 0; i <size(arr); i++)
    {
        if (arr[i]==0)
        {
            zero++;
        }
        else if (arr[i]==1)
        {
            one++;
        }
        else{
            two++;
        }
        
        
    }
    int index=0;

    for(int i=0;i<zero;i++){
    arr[i]=0;
    index++;
    }
    for(int i=0;i)
    
}