#include<iostream>
using namespace std;
int main(){
    int arr[5]={2,5,4,6,1};
    int size=5;

    for(int i=0;i<5;i++){
        int minindex=i;
        for(int j=i+1;j<5;j++){
            if(arr[j]<arr[minindex]){
                minindex=j;
            }
        }
        swap(arr[i],arr[minindex]);
    }
    for(int i=0;i<5;i++){
        cout<<arr[i]<<" ";
    }
}