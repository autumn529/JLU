**7-1 查询子序列和**

分数 100

作者 谷方明

单位 吉林大学

对N个整数的序列，查询子序列和∑*k*=*i**j**A**k* , (1≤i,j≤N).

### 输入格式:

第1行，两个整数：N和Q，表示整数的个数和查询的次数，1≤N≤100000，0≤Q≤100000.

第2行，N个用空格分开的整数 x ， │x│≤20000.

第3至Q+2行，每行两个整数i和j，表示所求子序列和的区间[i，j]，1≤i≤j≤N，保证所有区间都合法。

### 输出格式:

Q行,每行一个整数，表示相应子序列的和 

### 输入样例:

```in
5 3
1 2 3 4 5
1 5
2 4
3 5
```

### 输出样例:

在这里给出相应的输出。例如：

```out
15
9
12
```

代码长度限制

16 KB

时间限制

200 ms

内存限制

2 MB

栈限制

8192 KB



### 思路

#### 在输入时就构造前缀和序列，一边输入一边加



```C++
#include<iostream>
#include<vector>
using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N,Q;
    cin>>N>>Q;
    
    vector<int> num(n+1,0);
    for(int i=0;i<N;i++)
    {
        int tmp;
        cin>>tmp;
        num[i+1]=num[i]+tmp;
    }
    
    while(Q)
    {
        Q--;
        int x,y;
        cin>>x>>y;
        cout<<num[y]-num[x-1]<<"\n";
    }
    
    return 0;
}
```







### 										**7-2 二叉树先根序列**

分数 100

作者 谷方明

单位 吉林大学

给出一棵二叉树的中根序列和后根序列。求其先根序列。

约定树结点用不同的大写字母表示；

序列长度≤26.

### 输入格式:

一行，用空格隔开的两个字符串，表示二叉树的中根序列和后根序列。

### 输出格式:

一行，二叉树的先根序列。

### 输入样例:

在这里给出一组输入。例如：

```in
CA CA
```

### 输出样例:

在这里给出相应的输出。例如：

```out
AC
```

代码长度限制

16 KB

时间限制

400 ms

内存限制

64 MB

栈限制

8192 KB





### 思路

#### 根据中根和后根序列来确定每次子序列的根节点和左右子树，递归完成



```C++
#include<iostream>
#include<vector>
#include<string>
using namespace std;
void build(string& str1,string& str2,int l1,int r1,int l2,int r2)
{
    if(l1>r1)
        return;
    
    char root=str2[r2];
    int k=str1.find(root);
    int len=k-l1;
    cout<<root;
    
    build(str1,str2,l1,k-1,l2,l2+len-1);
    build(str1,str2,k+1,r1,l2+len,r2-1);
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    string in,next;
    cin>>in>>next;
    
    int len=in.size();
    build(in,next,0,len-1,0,len-1);
    
    return 0;
}
```











### 												**7-3 二叉树遍历I**

分数 100

作者 谷方明

单位 吉林大学

给定一棵二叉树T的扩展先根序列，求T中的中根序列和后根序列。

### 输入格式:

第1行，1个整数n，表示二叉树有n个结点， 1≤n≤50000.

第2行，2n + 1个整数，用空格分隔，表示T的扩展先根序列， -1表示空指针，结点用编号1到n表示。

### 输出格式:

两行。

第1行，中根遍历序列，以空格分隔。

第2行，后根遍历序列，以空格分隔。

### 输入样例:

在这里给出一组输入。例如：

```in
3
1 2 -1 -1 3 -1 -1
```

### 输出样例:

在这里给出相应的输出。例如：

```out
2 1 3
2 3 1
```

代码长度限制

16 KB

时间限制

50 ms

内存限制

10 MB

栈限制

8192 KB





### 思路

#### 递归建树



```C++
#include<iostream>
#include<vector>
using namespace std;
struct node{
   int val;
   node *l=nullptr,*r=nullptr;
};

node* build()
{
    int val;
    cin>>val;
    if(val==-1)
        return nullptr;
    
    node* tmp=new node;
    tmp->val=val;
    
    tmp->build();
    tmp->build();
    
    return tmp;
}

void in(node* root)
{
    if(!root)
        return;
    
    in(root->l);
    cout<<root->val<<" ";
    in(root->l);
}

void next(node* root)
{
    if(!root)
        return;
    
    next(root->l);
    next(root->r);
    cout<<root->val<<" ";
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin>>n;
    
    node* root=build();
    in(root);
    cout<<"\n";
    next(root);
    
    return 0;
}
```











### 										**7-5 玩转二叉树**

分数 25

作者 陈越

单位 浙江大学

给定一棵二叉树的中序遍历和前序遍历，请你先将树做个镜面反转，再输出反转后的层序遍历的序列。所谓镜面反转，是指将所有非叶结点的左右孩子对换。这里假设键值都是互不相等的正整数。

### 输入格式：

输入第一行给出一个正整数`N`（≤30），是二叉树中结点的个数。第二行给出其中序遍历序列。第三行给出其前序遍历序列。数字间以空格分隔。

### 输出格式：

在一行中输出该树反转后的层序遍历的序列。数字间以1个空格分隔，行首尾不得有多余空格。

### 输入样例：

```in
7
1 2 3 4 5 6 7
4 1 3 2 6 5 7
```

### 输出样例：

```out
4 6 1 7 5 3 2
```

代码长度限制

16 KB

时间限制

400 ms

内存限制

64 MB

栈限制

8192 KB



### 思路

#### 先按给出的序列递归建树，之后再递归将树进行逐分支反转，最后对树进行层序遍历即可





```C++
#include<iostream>
#include<vector>
#include<stack>
#include<queue>
using namespace std;
struct node{
    int val;
    node *l=nullptr,*r=nullptr;
};
int n;

node* build(vector<int>& num1,vector<int>& num2,int l1,int r1,int l2,int r2)
{
    if(l1>r1)
    return nullptr;

    int root=num2[l2];
    int k;
    for(int x=l1;x<=r1;x++)
    {
        if(num1[x]==root)
        {
            k=x;
            break;
        }
    }

    node* tmp=new node;
    tmp->val=root;

    int len=k-l1;
    tmp->l=build(num1,num2,l1,k-1,l2+1,l2+len);
    tmp->r=build(num1,num2,k+1,r1,l2+len+1,r2);

    return tmp;
}

void mirror(node* root)
{
    if(!root)
    return;

    swap(root->l,root->r);

    mirror(root->l);
    mirror(root->r);
}

void pre(node* root)
{
    if(!root)
    return;

    cout<<root->val;
    pre(root->l);
    pre(root->r);
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n;

    vector<int> num1(n),num2(n);
    for(int i=0;i<n;i++)
        cin>>num1[i];

    for(int i=0;i<n;i++)
        cin>>num2[i];

    node* root=build(num1,num2,0,n-1,0,n-1);

    pre(root);
    cout<<"\n";
    mirror(root);
    pre(root);
    cout<<"\n";

    queue<node*> s;//层序遍历用的queue
    s.push(root);

    while(!s.empty())
    {
        node* tmp=s.front();
        s.pop();

        cout<<tmp->val<<" ";

        if(tmp->l)
        s.push(tmp->l);
        if(tmp->r)
        s.push(tmp->r);
    }

    return 0;
}
```









### 									**7-6 完全二叉树的层序遍历**

分数 25

作者 陈越

单位 浙江大学

一个二叉树，如果每一个层的结点数都达到最大值，则这个二叉树就是**完美二叉树**。对于深度为 *D* 的，有 *N* 个结点的二叉树，若其结点对应于相同深度完美二叉树的层序遍历的前 *N* 个结点，这样的树就是**完全二叉树**。

给定一棵完全二叉树的后序遍历，请你给出这棵树的层序遍历结果。

### 输入格式：

输入在第一行中给出正整数 *N*（≤30），即树中结点个数。第二行给出后序遍历序列，为 *N* 个不超过 100 的正整数。同一行中所有数字都以空格分隔。

### 输出格式：

在一行中输出该树的层序遍历序列。所有数字都以 1 个空格分隔，行首尾不得有多余空格。

### 输入样例：

```in
8
91 71 2 34 10 15 55 18
```

### 输出样例：

```out
18 34 55 71 2 10 15 91
```

代码长度限制

16 KB

时间限制

400 ms

内存限制

64 MB

栈限制

8192 KB





### 思路

#### 完全二叉树后序遍历性质，长度/2=左子树序列长度，根节点是最后一个



```c++
#include<iostream>
#include<vector>
#include<queue>
using namespace std;
struct node{
    int val;
    node *l=nullptr,*r=nullptr;
};
vector<int> num;
int n;

node* build(vector<int>& num,int l,int r)
{
    if(l>r)
    return nullptr;

    int root=num[r];
    int len=(r-l+1)/2;
    node* tmp=new node;
    tmp->val=root;

    tmp->l=build(num,l,l+len-1);
    tmp->r=build(num,l+len,r-1);

    return tmp;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n;
    num.resize(n);

    for(int i=0;i<n;i++)
    cin>>num[i];

    node* root=build(num,0,n-1);

    queue<node*> q;
    q.push(root);
    while(!q.empty())
    {
        node* tmp=q.front();
        q.pop();

        cout<<tmp->val<<" ";

        if(tmp->l)
        q.push(tmp->l);
        if(tmp->r)
        q.push(tmp->r);
    }

    return 0;
}
```

