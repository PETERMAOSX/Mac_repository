#include<iostream>
#include<vector>
using namespace std;

void movezeroes(vector<int> &nums){
    int n = nums.size();
    
    //Count zero
    int zeros_count = 0;
    for(int i=0;i<n;i++){
        zeros_count += (nums[i] == 0);
    }
    //Make non-zeros
    vector<int> ans;
    for(int i=0;i<n;i++){
        if(nums[i] != 0){
            ans.push_back(nums[i]);
        }
    }
    while(zeros_count--){
        ans.push_back(0);
    }
    for(int i=0;i<n;i++){
        nums[i] = ans[i];
    }
}

void moveZeros_01(vector<int> &nums){
    int lastNonZeroFoundAt = 0;
    for(int = 0;i<nums.size();i++){
        if(nums[i] != 0){
            nums[lastNonZeroFoundAt++] = nums[i];
        }
    }
    for(int i=lastNonZeroFoundAt;i<nums.size();i++){
        nums[i] = 0;
    }
}

int main(){
    vector<int> vec;
    vec.push_back(0);
    vec.push_back(1);
    vec.push_back(3);
    vec.push_back(5);
    vec.push_back(0);
    vec.push_back(2);
    movezeroes(vec);
    for(int i =0;i<vec.size();i++){
        cout<<vec[i]<<endl;
    }
    return 0;
}