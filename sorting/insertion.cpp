#include<iostream>
#include<vector>
using namespace std;
void insertionsort(vector<int>& arr){
    int n=arr.size();
    for (int i = 1; i <n; i++)
    {
        int key=arr[i];
        int j=i-1;
        while(j>=0 && arr[i]>key){
            arr[j+1]=arr[j];
            j--;
        }
        arr[j+1]=key;

    }
    
}
int main(){
    vector<int>arr={5,3,8,7,4,1};
    insertionsort(arr);
    
}