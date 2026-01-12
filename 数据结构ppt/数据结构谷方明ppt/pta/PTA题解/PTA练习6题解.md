##                                    **7-1 等价性问题**

分数 100

作者 谷方明

单位 吉林大学

等价性问题就是：给定集合*S*及其上的若干等价元素对，询问*S*上的两个元素是否等价。常见的等价性问题有亲戚关系等。等价性问题的一种模型是等价关系和等价类。

### 输入格式:

输入由两部分组成。

第一部分以N，M开始。N为问题涉及的元素个数，元素的编号为1,2,3,…, N。M表示等价元素对个数，1<=N,M<=100000，接下来M行，每行有两个元素ai和bi，表示ai和bi等价。

第二部分以一个整数P(1<=P<=100000)开始,表示有P次询问，接下来P行，每行有两个元素ci和di，表示询问ci和di是否等价。

### 输出格式:

若干行。每行表示一个询问的结果。若ci和di等价，则输出“Yes”，否则输出“No”。

### 输入样例:

在这里给出一组输入。例如：

```in
6 4
1 2
1 3
5 4
5 3
3
1 4
2 3
5 6
```

### 输出样例:

在这里给出相应的输出。例如：

```out
Yes
Yes
No
```

代码长度限制

16 KB

时间限制

50 ms

内存限制

1 MB

栈限制

8192 KB



### 思路

#### 查集模板题，理解并熟背模板即可，在此我才用按秩路径压缩写法



### 代码

```C++
#include<iostream>
#include<vector>
using namespace std;
vector<int> parent,rnk;

int finds(int x)
{
    int root=x;
    while(root!=parent[root])
        root=parent[root];
    
    while(x!=root)
    {
        int fa=parent[x];
        fa[x]=root;
        x=fa;
    }
    
    return root;
}

void unions(int x,int y)
{
    int a=finds(x);
    int b=finds(y);
    
    if(a==b)
        return;
    if(rnk[a]>rnk[b])
    	parent[b]=a;
    else if(rnk[b]>rnk[a])
        parent[a]=b;
    else
    {
        parent[a]=b;
        rnk[b]++;
    }
}


int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n,m;
    cin>>n>>m;
    rnk.resize(n+1,0);
    for(int i=0;i<=n;i++)
        parent.push_back(i);
    
    for(int i=0;i<m;i++)
    {
        int x,y;
        cin>>x>>y;
        unions(x,u);
    }
    
    int p;
    cin>>p;
    for(int i=0;i<n;i++)
    {
        int x,y;
        cin>>x>>y;
        if(finds(x)==finds(y))
            cout<<"Yes\n";
        else
            cout<<"No\n";
    }
    
    return 0;
}
```













## 										**7-2 连通分量**

分数 100

作者 谷方明

单位 吉林大学

无向图 G 有 n 个顶点和 m 条边。求 G 的连通分量的数目。

### 输入格式:

第1行，2个整数n和m，用空格分隔，分别表示顶点数和边数， 1≤n≤50000， 1≤m≤100000.

第2到m+1行，每行两个整数u和v，用空格分隔，表示顶点u到顶点v有一条边，u和v是顶点编号，1≤u,v≤n.

### 输出格式:

1行，1个整数，表示所求连通分量的数目。

### 输入样例:

在这里给出一组输入。例如：

```in
6 5
1 3
1 2
2 3
4 5
5 6
```

### 输出样例:

在这里给出相应的输出。例如：

```out
2
```

代码长度限制

16 KB

时间限制

200 ms

内存限制

10 MB

栈限制

8192 KB





### 思路

#### 一个连通分量内的每个点之间互相连通，一个连通分量可看作一个集合

#### 初始的n个点可看作n个连通分量，合并m次。合并成功则连通分量数减一，否则若欲合并的两点本就在一个连通分量内，连通分量数不变



```C++
#include<iostream>
#include<vector>
using namespace std;
vector<int> parent,rnk;

int finds(int x)
{
    int root=x;
    while(root!=parent[root])
        root=parent[root];
    
    while(x!=root)
    {
        int fa=parent[x];
        fa[x]=root;
        x=fa;
    }
    
    return root;
}

int unions(int x,int y)
{
    int a=finds(x);
    int b=finds(y);
    
    if(a==b)
        return 0;
    if(rnk[a]>rnk[b])
    	parent[b]=a;
    else if(rnk[b]>rnk[a])
        parent[a]=b;
    else
    {
        parent[a]=b;
        rnk[b]++;
    }
    
    return 1;
}


int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    rnk.resize(n+1,0);
    for(int i=0;i<=n;i++)
        parent.push_back(i);
    
    
    int n,m;
    cin>>n>>m;
    
    int cnt=n;//初始连通分量为n
    
    for(int i=0;i<m;i++)
    {
        int x,y;
        cin>>x>>y;
        if(unios(x,y))//合并成功则连通分量数减1
            cnt--;
    }
    
    cout<<cnt;//输出最终的连通分量数
    return 0;
}
```









## 							**7-3 图的深度优先搜索I**

分数 100

作者 谷方明

单位 吉林大学

   无向图 G 有 n 个顶点和 m 条边。求图G的深度优先搜索树(森林)以及每个顶点的发现时间和完成时间。每个连通分量从编号最小的结点开始搜索，邻接顶点选择顺序遵循边的输入顺序。

   在搜索过程中，第一次遇到一个结点，称该结点被发现；一个结点的所有邻接结点都搜索完，该结点的搜索被完成。深度优先搜索维护一个时钟，时钟从0开始计数，结点被搜索发现或完成时，时钟计数增1，然后为当前结点盖上时间戳。一个结点被搜索发现和完成的时间戳分别称为该结点的发现时间和完成时间

### 输入格式:

第1行，2个整数n和m，用空格分隔，分别表示顶点数和边数， 1≤n≤50000， 1≤m≤100000.

第2到m+1行，每行两个整数u和v，用空格分隔，表示顶点u到顶点v有一条边，u和v是顶点编号，1≤u,v≤n.

### 输出格式:

第1到n行，每行两个整数di和fi，用空格分隔，表示第i个顶点的发现时间和完成时间1≤i≤n 。

第n+1行，1个整数 k ，表示图的深度优先搜索树(森林)的边数。

第n+2到n+k+1行，每行两个整数u和v,表示深度优先搜索树(森林)的一条边<u,v>，边的输出顺序按 v 结点编号从小到大。

### 输入样例:

在这里给出一组输入。例如：

```in
6 5
1 3
1 2
2 3
4 5
5 6
```

### 输出样例:

在这里给出相应的输出。例如：

```out
1 6
3 4
2 5
7 12
8 11
9 10
4
3 2
1 3
4 5
5 6
```

代码长度限制

16 KB

时间限制

200 ms

内存限制

10 MB

栈限制

8192 KB



### 思路

#### 使用邻接表存储每一条边，设置全局时钟变量idx=0，对图进行深度优先搜索，记录每个点的发现和完成时间，记录每条搜索树边



```C++
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
struct edge{
    int u,v;
};

vector<int> s,e;//记录初次访问和完成访问
vector<vector<int>> G;//记录图
vector<int> vis;//标记该点是否被访问
vector<edge> ans;//记录搜索树
int idx=0;//计时器

void dfs(int x)
{
    if(vis[x])//如果已经访问过则返回
        return ;

	s[x]=++idx;//初次发现此点，记录时间戳
    vis[x]=1;//标记已经访问
    for(int i=0;i<G[x].size();i++)
    {
        if(!vis[G[x][i]])//只访问未被访问的节点
        {
            ans.push_back({x,G[x][i]});//记录搜索树的每一条边
            dfs(G[x][i]);
        }
    }    
    
    e[x]=++idx;//记录访问完成时间戳
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n,m;
    cin>>n>>m;
    s.resize(n+1);
    e.resize(n+1);
    vis.resize(n+1,0);
    
    G.resize(n+1);
    
 	for(int i=0;i<m;i++)
    {
    	int u,v;
        cin>>u>>v;//将无向边<u,v>记录入图G中
        G[u].push_back(v);
    	G[v].push_back(u);
    }
    
 	for(int i=1;i<=n;i++)
        dfs(i);//对每个点进行搜索
    
    for(int i=1;i<=n;i++)
        cout<<s[i]<<" "<<e[i]<<"\n";
   
    cout<<ans.size()<<"\n";//搜索树数组的大小为搜索树边数
    
    sort(ans.begin(),ans.end(),[](const edge& a,const edge& b){
       return a.v<b.v; 
    });//按v进行排序
    
    for(int i=0;i<ans.size();i++)
        cout<<ans[i].u<<" "<<ans[i].v<<"\n";
    
    return 0;
}
```







## 									**7-4 图着色问题**

分数 25

作者 陈越	

单位 浙江大学

图着色问题是一个著名的NP完全问题。给定无向图*G*=(*V*,*E*)，问可否用*K*种颜色为*V*中的每一个顶点分配一种颜色，使得不会有两个相邻顶点具有同一种颜色？

但本题并不是要你解决这个着色问题，而是对给定的一种颜色分配，请你判断这是否是图着色问题的一个解。

### 输入格式：

输入在第一行给出3个整数*V*（0<*V*≤500）、*E*（≥0）和*K*（0<*K*≤*V*），分别是无向图的顶点数、边数、以及颜色数。顶点和颜色都从1到*V*编号。随后*E*行，每行给出一条边的两个端点的编号。在图的信息给出之后，给出了一个正整数*N*（≤20），是待检查的颜色分配方案的个数。随后*N*行，每行顺次给出*V*个顶点的颜色（第*i*个数字表示第*i*个顶点的颜色），数字间以空格分隔。题目保证给定的无向图是合法的（即不存在自回路和重边）。

### 输出格式：

对每种颜色分配方案，如果是图着色问题的一个解则输出`Yes`，否则输出`No`，每句占一行。

### 输入样例：

```in
6 8 3
2 1
1 3
4 6
2 5
2 4
5 4
5 6
3 6
4
1 2 3 3 1 2
4 5 6 6 4 5
1 2 3 4 5 6
2 3 4 2 3 4
```

### 输出样例：

```out
Yes
Yes
No
No
```

代码长度限制

16 KB

时间限制

300 ms

内存限制

64 MB

栈限制

8192 KB



### 思路

#### 本题无弯弯绕内容，按照题目思路模拟即可



```C++
#include<iostream>
#include<vector>
#include<set>
using namespace std;
vector<vector<int>> G;//记录图

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int V,E,K;
    cin>>V>>E>>K;

    G.resize(V+1);

    for(int i=0;i<E;i++)
    {
        int u,v;//输入每条边
        cin>>u>>v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    int N;
    cin>>N;
    for(int i=0;i<N;i++)
    {
        vector<int> color;//记录每个点对应的color
        set<int> num;//记录不重样的颜色数目
        int flag=1;//标记是否有边的两点颜色相同，0为相同

        color.resize(V+1);
        for(int i=1;i<=V;i++)
        {
            cin>>color[i];
            num.insert(color[i]);
        }

        if(num.size()!=K)//如果不重样的颜色数目不等于K，则该情况不成立
        {
            cout<<"No\n";
            continue;
        }

        for(int i=1;i<=V;i++)
        {
            for(int j=0;j<G[i].size();j++)
            {
                if(color[i]==color[G[i][j]])//若有相邻两点颜色相同则将flag=0，break
                {
                    flag=0;
                    break;
                }

            }
            
            if(!flag)//再次break，避免后序判断
            break;
        }

        if(flag)//输出最终判断结果
            cout<<"Yes\n";
        else
            cout<<"No\n";
    }

    return 0;
}
```





## 											**7-5 全排列**

分数 100

作者 陈宇璟

单位 浙江大学

按照字典序输出自然数 1 到 n 所有不重复的排列，即 n 的全排列，要求所产生的任一数字序列中不允许出现重复的数字。

### 输入格式:

一个整数 n(n<=5)。

### 输出格式:

由 1~n 组成的所有不重复的数字序列，每行一个序列。

### 输入样例:

```in
3
```

### 输出样例:

```out
1 2 3 
1 3 2 
2 1 3 
2 3 1 
3 1 2 
3 2 1 
```

代码长度限制

16 KB

时间限制

2000 ms

内存限制

128 MB

栈限制

8192 KB



```C
#include <stdio.h>
int n;
int a[10], used[10];

void dfs(int step)
{
    if (step == n)//等于n说明已经收集完毕n个数字
    {
        for (int i = 0; i < n; i++)
            printf("%d ", a[i]);//输出每个数字
        printf("\n");
        return;
    }

    for (int i = 1; i <= n; i++)
    {
        if (!used[i])//已经访问过的数字不再访问
        {
            a[step] = i;//记录访问的数字  a数组回退时不必将元素pop出，可直接覆盖写入
            used[i] = 1;//标记已经访问
            dfs(step + 1);//进入下一层访问
            used[i] = 0;//回退
        }
    }
}

int main(void)
{
    scanf("%d", &n);
    dfs(0);//从第0层开始
    return 0;
}

```

