#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int partition(vector<int>& arr,int m,int n)
{
    int K=arr[m],L=m+1,G=n;
    while(L<=G)
    {
        while(L<=n&&arr[L]<K)
            L++;
        while(arr[G]>K)
            G--;
        if(L<G)
        {
            swap(arr[L],arr[G]);
            L++;
            G--;
        }
    }
    swap(arr[m],arr[G]);
    return G;
}

void quicksort(vector<int>& arr,int m,int n)
{
    if(m<n)
    {
        int k=partition(arr,m,n);
        for(int i=0;i<arr.size();i++)
            cout<<arr[i]<<" ";
        cout<<endl;
        quicksort(arr,m,k-1);
        quicksort(arr,k+1,n);
    }
}

void QuickSort(vector<int> &arr, int m, int n){
    while(m < n)
    {
        int k=partition(arr,m,n);
        for(int i=0;i<arr.size();i++)
            cout<<arr[i]<<" ";
        cout<<endl;
        if(k-m < n-k)
        { //左区间短
            QuickSort(arr,m,k-1);
            m=k+1;
        }
        else
        { //右区间短
            QuickSort(arr,k+1,n);
            n=k-1;
        }
    }
}

int main(void)
{
    vector<int> arr;
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int x;
        cin>>x;
        arr.push_back(x);
    }

    QuickSort(arr,0,n-1);
    for(int i=0;i<arr.size();i++)
        cout<<arr[i]<<" ";
    return 0;
}


