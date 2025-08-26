#include<iostream>
#include<vector>
using namespace std;

int partition(vector<int> &arr, int st, int end){
    int idx = st-1, pivot = arr[end];
    for (int j = st; j <= end-1; j++){
       if(arr[j] <= pivot){
        idx++;
        swap(arr[j],arr[idx]);
       }
    }
    idx++;
    swap(arr[end],arr[idx]);
    return idx; 
}


void quickSort(vector<int> &arr, int st , int end){
    if(st<end){
        int idx;
        idx = partition(arr,st,end);
        quickSort(arr,st,idx-1);
        quickSort(arr,idx+1,end);
    }
}

void printArray(vector<int> &arr){
    for(int val : arr){
        cout<<val<<" ";
    }
    cout<<endl;
}

int main(){

    vector<int> arr = {3,22,11,2,56,33};

    quickSort(arr,0,arr.size()-1);
    printArray(arr);
    return 0;
}