#include<iostream>
#include<stack>

using namespace std;

int main(){
    char s[300];
    cin>>s;
    int len = strlen(s);
    stack<char> st;
    for(int i=0;i<len;i++){
        if(!st.empty()){
            char now = st.top();
            if((s[i] == ')' && now=='(') || (s[i] == ']' && now=='['))
                st.pop();
            else st.push(s[i]);
        }
        else{
            st.push(s[i]);
        }
    }
    if(!st.empty()) printf("NO\n");
    else printf("YES\n");
    return 0;
}