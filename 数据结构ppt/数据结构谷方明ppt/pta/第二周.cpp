#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main(void)
{
    string str;
    cin>>str;

    stack<char> q;
    for(int i=0;i<str.size();i++)
    {
        if(str[i]=='('||str[i]=='{')
            q.push(str[i]);
        else if(str[i]==')')
        {
            if(!q.empty()||q.top()!='(')
            {
                cout<<"no";
                return 0;
            }
            q.pop();
        }
        else if(str[i]=='}')
        {
            if(!q.empty()||q.top()!='{')
            {
                cout<<"no";
                return 0;
            }
            q.pop();
        }
        else
            continue;
    }

    cout<<"yes";
    return 0;
}
/*#include<iostream>
#include<deque>
#include<vector>
using namespace std;

int main(void)
{
    int n,m;
    cin>>n>>m;

    vector<int> num(n);
    for(int i=0;i<n;i++)
        cin>>num[i];

    deque<int> q;
    for(int i=0;i<n;i++)
    {
        while(!q.empty()&&num[q.back()]>=num[i])
            q.pop_back();
        
        while(!q.empty()&&i-q.front()>=m)
            q.pop_front();

        q.push_back(i);
        if(i>=m-1)
            cout<<num[q.front()]<<" ";
    }

    return 0;
}*/




/*#include<iostream>
#include<vector>
using namespace std;

int main(void)
{
    int n;
    cin>>n;
    vector<int> num;

    for(int i=0;i<n;i++)
    {
        int tmp;
        cin>>tmp;
        if(num.empty())
        {
            cout<<"-1 ";
            num.push_back(tmp);
            continue;
        }
        else
        {
            while(!num.empty()&&num.back()>=tmp)
                num.pop_back();
            if(num.empty())
                cout<<"-1 ";
            else
            cout<<num.back()<<" ";
        }
        num.push_back(tmp);
    }

    return 0;
}*/
