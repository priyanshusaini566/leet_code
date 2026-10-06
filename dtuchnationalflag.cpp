#include<iostream>
using namespace std;
int main(){

    int arr[]={1,0,1,2,0,1,2,0,1};
    int low=0;
    int high=8;
    int mid=0;

    while(mid<=high)
    {
        if(arr[mid]==0){
            swap(arr[low],arr[mid]);
            low++;
            mid++;
        }
        else if(arr[mid]==1)  mid++;
        else{
            swap(arr[mid],arr[high]);
            high--;
        }
    }
    for(int i=0;i<=8;i++){
        cout<<arr[i]<<" ";
    }
    
}