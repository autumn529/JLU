#include <iostream>
#include <queue>
using namespace std;

struct Pos { int x, y; };
const int INF = 1e9;
int n, m;
char mp[805][805];
int ghost[805][805], timeM[805][805], timeG[805][805];
int dx[4] = {1,-1,0,0};
int dy[4] = {0,0,1,-1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T; cin >> T;
    while(T--) {
        cin >> n >> m;
        queue<Pos> qGhost;
        Pos M, G;

        for(int i=0;i<n;i++){
            cin >> mp[i];
            for(int j=0;j<m;j++){
                ghost[i][j] = INF;
                timeM[i][j] = timeG[i][j] = -1;
                if(mp[i][j]=='Z'){ ghost[i][j]=0; qGhost.push({i,j}); }
                if(mp[i][j]=='M') M = {i,j};
                if(mp[i][j]=='G') G = {i,j};
            }
        }

        // BFS 计算鬼魂时间
        while(!qGhost.empty()){
            Pos p = qGhost.front(); qGhost.pop();
            for(int d=0; d<4; d++){
                int nx=p.x+dx[d], ny=p.y+dy[d];
                if(nx<0||ny<0||nx>=n||ny>=m) continue;
                if(ghost[nx][ny] > ghost[p.x][p.y]+1){
                    ghost[nx][ny] = ghost[p.x][p.y]+1;
                    qGhost.push({nx,ny});
                }
            }
        }
        // 转换为秒数，每秒扩散 2 步
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                ghost[i][j] = (ghost[i][j]+1)/2;

        // BFS M
        queue<Pos> qM;
        qM.push(M); timeM[M.x][M.y]=0;
        // BFS G
        queue<Pos> qG;
        qG.push(G); timeG[G.x][G.y]=0;

        int sec = 0;
        bool meet = false;
        int ans = -1;

        while(!meet && (!qM.empty() || !qG.empty())) {
            sec++;

            // 扩展 M 每秒 3 步
            for(int step=0; step<3; step++){
                int sz = qM.size();
                while(sz--){
                    Pos p = qM.front(); qM.pop();
                    for(int d=0; d<4; d++){
                        int nx=p.x+dx[d], ny=p.y+dy[d];
                        if(nx<0||ny<0||nx>=n||ny>=m) continue;
                        if(mp[nx][ny]=='X') continue;
                        if(timeM[nx][ny]!=-1) continue;
                        if(sec >= ghost[nx][ny]) continue;
                        timeM[nx][ny] = sec;
                        qM.push({nx,ny});
                    }
                }
            }

            // 扩展 G 每秒 1 步
            int szG = qG.size();
            while(szG--){
                Pos p = qG.front(); qG.pop();
                for(int d=0; d<4; d++){
                    int nx=p.x+dx[d], ny=p.y+dy[d];
                    if(nx<0||ny<0||nx>=n||ny>=m) continue;
                    if(mp[nx][ny]=='X') continue;
                    if(timeG[nx][ny]!=-1) continue;
                    if(sec >= ghost[nx][ny]) continue;
                    timeG[nx][ny] = sec;
                    qG.push({nx,ny});
                }
            }

            // 检查同秒相遇
            for(int i=0;i<n && !meet;i++)
                for(int j=0;j<m;j++)
                    if(timeM[i][j]==sec && timeG[i][j]==sec){
                        meet = true;
                        ans = sec;
                        break;
                    }
        }

        cout << ans << "\n";
    }

    return 0;
}
