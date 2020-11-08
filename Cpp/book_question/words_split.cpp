#include<map>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

void solve(string str,vector<string> & words){
    string w;
    int i = 0;
    int j = str.find(" ");
    while(j != -1){
        w = str.substr(i,j-1);
        words.push_back(w);
        i = j + 1;
        j = str.find(" ",i);
    }
    if(i < str.length() - 1){
        w = str.substr(i);
        words.push_back(w);
    }
}
bool isUnique(string &str){
    map<char,int> mymap;
    for(int i=0;i<str.length();i++){
        mymap[str[i]]++;
        if(mymap[str[i]] > 1){
            return false;
        }
    }
    return true;
}

int main(){
    // string str = "The Following code computes the intersection of two arrays";
    // vector<string> words;
    // solve(str,words);
    // cout<<"Every Words:"<<endl;
    // vector<string> :: iterator it;
    // for(it = words.begin();it != words.end();++it){
    //     cout<<" "<<*it<<endl;
    // }
    string str = "abc";
    cout<<isUnique(str)<<endl;;
    return 0;
}