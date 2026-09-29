#include<iostream>
using namespace std;
int main(){
    int p;
    cout<<"Enter the number of elements:";
    cin>>p;
    int arr[p];
    cout<<"Enter the element:";
    for(int i=0;i<p;i++){
        cin>>arr[i];
    }

    for(int i=0;i<p;i++){
        for(int j=i+1;j<p;j++){
            if(arr[i]>arr[j]){
                swap(arr[i],arr[j]);
            }
        }
    }
    for (int i = 0; i <p; i++)
    {
        cout<<arr[i]<<" ";
    }
    
}