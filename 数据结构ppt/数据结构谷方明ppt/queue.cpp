#include<iostream>
#include<vector>
#include<queue>
#include<cctype>
#include<limits>
using namespace std;
struct point{
    int x,y,step=0;
};
struct pos{
    int x1=0,y1=0;
    int x2=0,y2=0;
    int flag=0;
}alph [26];

int main(void)
{
    int N,M;
    cin>>N>>M;

    point start,end;
    vector<vector<char>> map(N+3,vector<char>(M+3));
    for(int i=1;i<=N;i++)
    {
        for(int j=1;j<=M;j++)
        {
            cin>>map[i][j];
            if(isalpha(map[i][j]))
            {
               int num=map[i][j]-'A';
               if(alph[num].x1==0)
               {
                   alph[num].x1=i;
                   alph[num].y1=j;
               }
               else
               {
                   alph[num].x2=i;
                   alph[num].y2=j;                    
               }
            }
            else if(map[i][j]=='@')
            {
                start.x=i;
                start.y=j;
                start.step=0;
            }
            else if(map[i][j]=='=')
            {
                end.x=i;
                end.y=j;
            }
        }
    }

    queue<point> q;
    q.push(start);
    int dx[]={1,0,-1,0};
    int dy[]={0,-1,0,1};
    int ans=INT_MAX;

    map[start.x][start.y]='#';
    while(!q.empty())
    {
        point tmp1=q.front();
        q.pop();

        int nx=tmp1.x;
        int ny=tmp1.y;
        
        for(int i=0;i<4;i++)
        {
            nx=tmp1.x+dx[i];
            ny=tmp1.y+dy[i];

           if(map[nx][ny]=='#') 
               continue;
            else if(map[nx][ny]=='.'||(isalpha(map[nx][ny])&&alph[map[nx][ny]-'A'].flag))
            {   

                //cout<<"BBB:"<<tmp1.x<<" "<<tmp1.y<<"->"<<nx<<" "<<ny<<" "<<tmp1.step+1<<endl;
                point tmp2={nx,ny,tmp1.step+1};
                q.push(tmp2);
                map[nx][ny]='#';
            }
            else if(map[nx][ny]<='Z'&&map[nx][ny]>='A')
            {
                alph[map[nx][ny]-'A'].flag=1;
                //cout<<"AAA:"<<tmp1.x<<" "<<tmp1.y<<"->"<<nx<<" "<<ny<<" "<<tmp1.step+1<<endl;
                char tmp3=map[nx][ny];
                map[nx][ny]='#';
                if(alph[tmp3-'A'].x1==nx)
                {
                    point tmp4={alph[tmp3-'A'].x2,alph[tmp3-'A'].y2,tmp1.step+1};
                    q.push(tmp4);
                }
                else
                {
                    point tmp4={alph[tmp3-'A'].x1,alph[tmp3-'A'].y1,tmp1.step+1};
                    q.push(tmp4);   
                }
            }
            else
            {
                 cout<<tmp1.step+1;
                 return 0;
            }
        }
    }

    return 0;
}