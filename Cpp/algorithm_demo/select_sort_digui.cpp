#include<iostream>
using namespace std;

void swap(int &x,int &y){
    int temp = x;
    x = y;
    y = temp;
}

void display(int a[],int n){
    int i;
    for(i = 0;i<n;i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
}

void SelectSort(int a[],int n,int i){
    int j,k;
    if(i == n - 1) return;
    else{
        k = i;
        for(j=i+1;j<n;j++){
            if(a[j] < a[k]){
                k = j;
            }
        }
        if(k != i){
            swap(a[i],a[k]);
        }
        SelectSort(a,n,i+1);
    }
}


int main(){
    int a[] = {2,5,1,7,10,6,9,4,3,8};
    cout<<"排序前: ";display(a,sizeof(a)/sizeof(int));
    SelectSort(a,sizeof(a)/sizeof(int),0);
    cout<<"排序后: ";display(a,sizeof(a)/sizeof(int));
    

    return 0;
}