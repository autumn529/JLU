[TOC]

# 一、概念

## （一）数据结构的基本概念

#### 1、数据

数据的含义：计算机程序处理的对象统称为数据（Data）

数据有：数字、字符串、图像、音频、视频、程序...

数据的组成：数据元素（数据成分、结点、顶点...）

数据元素的组成：描述其属性的多个数据项（域、字段）

#### 2、结构

**（1）数据的逻辑结构：数据由多个数据元素组成，数据的逻辑结构讨论的是数据元素之间**

**的逻辑关系。**

​		[1]可以用前驱与后继的概念来刻画元素之间的逻辑关系。

![image-20251212141754595](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251212141754595.png)

​		==**[2]逻辑结构的分类：线性结构（线性表）、非线性结构（层次结构，即树；网状结构，即图；集合，即无边点集）**==



**（2）数据的存储结构：数据及其逻辑关系在计算机的存储表示**

​		[1]需要考虑：如何存储数据元素与如何存储逻辑关系

​		==**[2]存储结构的分类：顺序存储(vector)、链接存储list、散列存储unordered_map、索引存储map**==

#### 3、操作

==**基本操作：插入、删除、修改、查找、排序、遍历**==

#### 4、数据结构

（1）概念：按照某种逻辑关系将一批数据元素组织起来，按照一定的存储方式将他们存储起来，并在数据元素上定义一个操作集合，就能得到一个特定的数据结构。（逻辑+存储+操作）

（2）基本组成部分：数据的逻辑结构，数据的存储结构，施加在数据上的操作。

## （二）算法

#### 1、概念

计算机中，算法泛指解决问题时采用的方法或步骤。算法由有限条指令构成，规定了解决问题的一系列操作。

#### 2、特性

**（1）有限性：**

​		==必须在执行有限个步骤之后停止==

**（2）确定性：**

​		每条指令都有明确的含义，==无二义性，相同的输入一定能得到一个相同的结果==

**（3）输入：**

​		具有>=0个外界提供的量

**（4）输出：**

​		产生>=1个结果

**（5）可行性：**

算法中描述的操作都是可以通过==已经实现的基本运算==执行==有限次==来完成的，原则上人们用纸和笔都可在有穷时间内完成它们

#### 3、评价准则

**（1）正确性：**

​		对于一切合法的输入数据，该算法在==有限次==时间的执行都能产生==符合预期==的结果

**（2）可读性：**

​		易于证明&测试其正确性，便于阅读、实现、调试和维护。添加注释可提高可读性。

**（3）健壮性/鲁棒性：**

​		尽可能充分地应对、处理各种==极端的输入==

**（4）时间复杂性：**

​		反映算法的==时间==效率

**（5）空间复杂性：**

​		反映算法在运行过程中所占用的==存储空间==的大小

#### 4、描述语言

可采用ADL语言（需要看懂），C/C++、JAVA、Python、ADL等任意语言



```pseudocode
算法SelectMaxMin(A,n.max,min) //第一行写出算法名，之后多个输入，‘.’之后是多个输出
	max<-min<-A[1].			 //赋值用的是<-  当然，交换用的是<->。 每个语句以.结束
	FOR i=2 TO n DO					//循环用FOR i=2 TO n DO()
	(	IF A[i]>max THEN max<-A[i].	//IF 用 IF THEN语句
		IF A[i]<min THEN min<-A[i].
	)▌						//算法以▌结束
```

#### 5、时间复杂性

算法的时间复杂性与算法的实现语言和运行环境无关

**（1）基本操作：**

​		加减乘除、比较、赋值、移动

**（2）时间复杂性：**

​		算法中基本运算的次数，往往是问题规模的函数

​		1、平均复杂性：$T(n) = \sum_{I \in D_n} P(I)\times C(I)$  <!--各种可能出现的输入的可能性x基本运算次数-->

​		2、最好复杂性：$min(C(I))$

​		3、最坏复杂性：$max(C(I))$

​		注意：给定的==**基本运算**==是什么，例如给定**元素的比较**是基本运算，那么IF i = j就不算在里面，i++也不算在里面

**（3）渐进表示法：**

​		当输入规模n较大时，难以得到T与n之间的精确关系，因此我们只需要T(n)的数量级即可

​		$T(n)=n^2 + 100n + \log_{10} n + 1000$ --->  $g(n)=n^2 $

| 符号        | 含义   | 一句话概括                     |
| ----------- | ------ | ------------------------------ |
| **O(g(n))** | 上界   | 最差情况下不比 g(n) × C 更慢   |
| **Ω(g(n))** | 下界   | 最好情况下不比 g(n) × C 更快   |
| **Θ(g(n))** | 精确阶 | 速度和 g(n) 一样（上下界夹住） |

​		若 $T(n)=3logn+loglogn$ 则有$T(n)=O(logn)=Ω(logn)=Θ(logn)$

​		$O(1) < O(loglog n) < O(log n) < O(n) < O(n log n) < O(n^2)) < O(n^3) < O(2^n)$

**（4）神必小性质：**

> ​		$1^x+2^x+3^x+...+n^x = O(n^{x+1})$
>
> ​		$1 + \frac{1}{2} + \frac{1}{3} + \cdots + \frac{1}{n} \approx \ \ln n = O(\log n)$
>
> ​		$T(n) = n^{\log \log \log n} \;=\; O(\lfloor \log n \rfloor !)$
>

## （三）线性表

> **线性表 = 顺序存储+链接存储（单链表+循环链表+双向链表）** 

哨位节点作用：避免对第一个元素操作与对其他元素操作的代码不一样

**链接存储与顺序存储比较：**

| 数据结构                 | 额外空间开销                         | 查找复杂度                       | 插入/删除复杂度              | 特点总结                       |
| ------------------------ | ------------------------------------ | -------------------------------- | ---------------------------- | ------------------------------ |
| **顺序表（数组 Array）** | 有冗余空间（连续空间，需要预留容量） | **O(1)**（随机访问直接通过下标） | **O(n)**（需要移动大量元素） | 访问快、增删慢、空间必须连续   |
| **链表（Linked List）**  | 每个节点需额外的指针域，有额外开销   | **O(n)**（必须从头/尾遍历）      | **O(1)**（已知节点位置时）   | 访问慢、增删快、不需要连续空间 |











# 二、关键算法



## （一）栈

**栈的数组实现：**

```cpp
const int MAXSIZ = 1e4+10;
template <class T>
class stack{
private:
    T A[MAXSIZ];
    int top = -1;
public:
    bool empty(){ return top==-1; }
    bool full(){ return top==MAXSIZ-1; }
    void push(T k){ assert(!full()); A[++top] = k; }
    T pop(){ assert(!empty()); return A[top--]; }
    T peek(){ assert(!empty()); return A[top]; }
};
```

#### 1、能实现操作：

**1、进制转换**

因为可以倒序把转换后的数字取出，并push到目标字符串内。

**2、括号匹配**

左括号push，遇到右括号时检测栈顶的左括号是否与之匹配即可

 若只有一种括号，则有$T(n)  = \frac{1}{n+1}\binom{2n}{n}$种括号匹配的方式

**3、表达式求值**

> **（1）后缀表达式：**
>
> ​		IF运算符：取出栈顶两个元素并运算，再把算完的元素push回去
>
> ​		IF数字：直接入栈
>
> ​		最后栈内剩下的数字就是答案

> **（2）中缀表达式转后缀表达式**
>
> ​		IF数字：直接放入后缀表达式
>
> ​		IF运算符或括号：	
>
> ​				IF栈空：入栈
>
> ​				IF当前优先级较高：入栈
>
> ​				IF当前优先级较低或相同：弹栈直到遇到优先级更低的，并入栈
>
> ​				【优先级越低，越需要让优先级高的排在他之前】

```cpp
inline void solve(){
    string s;
    cin>>s;
    stack<char> st;
    map<char,int> mp;
    mp['('] = 0 ;
    mp['+'] = 1 ;
    mp['-'] = 1 ;
    mp['*'] = 2 ;
    mp['/'] = 2 ;
    string ans ;
    for(char& ch:s){
        //数字
        if(ch!=')' && mp.count(ch)==0){
            ans.push_back(ch);
        }else if(ch==')'){				//右括号->一直找左括号
            while(st.top()!='('){
                ans.push_back(st.top());
                st.pop();
            }
            st.pop();
        }else if(ch=='('){				//左括号->直接入
            st.push(ch);
        }else{						//把该算的先算掉（比如比自己高或相同的）
            while( !st.empty() && mp[ch]<=mp[st.top()]){
                ans.push_back(st.top());
                st.pop();
            }
            st.push(ch);
        }
    }
    while(!st.empty()){
        ans.push_back(st.top());
        st.pop();
    }
    cout<<ans;
}
```

#### 2、弹栈合法性判断：

合法种数： $T(n)  = \frac{1}{n+1}\binom{2n}{n}$（因为入栈可以视为(，弹栈可以视为)。）

```cpp
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        stack<int> st;
        int i = 0 ;
        for(auto e:pushed){
            st.push(e);
            while(!st.empty() && st.top()==popped[i]){
                st.pop();
                i++;
            }
        }
        return st.empty();
    }
};
```

**栈扩容（不考）**

可以类似vector一样，倍增扩容

#### 3、递归&栈

> **递归的实现**
>
> 栈区记录了程序的调用关系，其中有：**返回地址、参数、局部变量**等信息存在**栈帧**里。
>
> 每一次递归调用，都会产生一个栈帧，因此有可能导致**栈溢出**

**利用递归解决的题目**

**1、走迷宫**，记录有多少种走法能到终点（利用递归vis[u,v]记录走过的路，同样也能保证不会有转圈圈的情况）。

如果消递归的话，（1）栈内元素`{int x,int y,int dir}`（2）操作：出栈当前元素，并入栈一个`dir+1`的元素（直到dir超过4再将`vis[i,j]`重置），另外，根据当前dir情况，选择下一个入栈的元素

**2、N皇后**



#### 4、消递归

> **1、尾递归**
>
> ​		若递归直接在函数末尾，则可以直接用循环代替递归

> **2、多个递归入口**
>
> ​		若有多个递归入口，则
>
> ​				1、外函数需要设计标志值，使得递归后，能找到返回地址 
>
> ​				2、先递归的后入栈，后递归的先入栈
>
> 



## （二）队列

**队列的数组实现——循环数组**

方案一、有count无浪费

```cpp
const int MAXSIZ = 1e5+7;
class queue{
private:
	T A[MAXSIZ];
	int front = 0 , rear = 0 , count =  0 ;
public:
	bool empty(){ return count == 0; }
    bool full(){ return count == MAXSIZ; }
	void push(T k){ A[rear] = k ; rear = (rear+1)%m; count++; }
	void pop(){ front = (front+1)%MAXSIZ; count++; }
    T peek(){ return A[front]; }
};

```

方案二、浪费一个，无count

```cpp
const int MAXSIZ = 1e5+7;
class queue{
private:
	T A[MAXSIZ];
	int front = 0 , rear = 0 ;
public:
	bool empty(){ return front == rear ; }
    bool full(){ return (rear+1)%MAXSIZ == front ; }
	void push(T k){ A[rear] = k ; rear = (rear+1)%MAXSIZ; }
	void pop(){ front = (front+1)%MAXSIZ; }
    T peek(){ return A[front]; }
    int size(){ return (rear - front + MAXSIZ ) % MAXSIZ;
};

```

**用一个queue模拟stack**

```cpp
class MyStack {
public:
    queue<int> q;
    
    void push(int x) {
        int n = q.size();
        q.push(x);
        for (int i = 0; i < n; i++) {
            q.push(q.front());
            q.pop();
        }
    }
    
    int pop() {
        int r = q.front();
        q.pop();
        return r;
    }
    
    int top() {
        int r = q.front();
        return r;
    }
    
    bool empty() {
        return q.empty();
    }
};
```



## （三）数组与矩阵



#### 1、存储与地址计算

> **1、按行优先**
>
> 例子：`A[3][5][11][3]`中地址`a[i][j][k][l]`的的计算是$Loc(A )+i*5*11*13+j*11*13+k*3+k$
>



> **2、按列优先**
>
> 例子：`A[3][5][11][3]`中地址`a[i][j][k][l]`的的计算是$Loc(A)+i+j*3+k*3*5+l*3*5*11$
>



> **3、对角矩阵的压缩存储**
>
> `M[i][j] = i==j ? d[i-1] : 0`



> **4、三角矩阵的压缩存储**
>
> 这部分我认为可以先举个例子，之后观察一下，很容易就能推导出公式了。注意元素的阶数。
>
> 对称矩阵：`M[i][j] = i>=j ? d[i(i-1)/2+j-1] : d[j(j-1)+i-1]`（按行存储）
>
> 下三角：` M[i][j] = i>=j ? d[i(i-1)/2+j-1] : 0`（按行存储）
>
> 上三角：`M[i][j] = i<=j ? d[j(j-1)+i-1] : 0`（按列存储）
>
> 三对角：`M[i][j] = abs(i-j)<=1 ? d[2*i+j-3]: 0`（按行存储）
>



> **5、稀疏矩阵的压缩存储**
>
> 三元组：`i,j,a[i][j]`
>
> **（1）顺序存储：三元组表**  节省空间，但对于非零元位置与个数经常发生变化时就不适合
>
> **（2）链接存储：十字链表**  
>
> 可以按行遍历，按列遍历。

#### 2、三元组稀疏矩阵转置

```cpp
void transpose(const vector<tuple<int,int,int>>& a,int n, int m) // n行 m列
{
    vector<int> col(m, 0);

    // 1. 统计每一列的非零元素个数
    for (auto& [x, y, val] : a) {
        col[y]++;
    }

    // 2. 前缀和：求每一行在 b 中的起始位置
    for (int i = 1; i < m; i++) {
        col[i] += col[i - 1];
    }

    // 3. 转换为起始下标
    for (int i = m - 1; i > 0; i--) {
        col[i] = col[i - 1];
    }
    col[0] = 0;

    // 4. 按原数组顺序放入（稳定）
    b.resize(a.size());
    for (auto& [x, y, val] : a) {
        int pos = col[y]++;
        b[pos] = {y, x, val};
    }
}

```

#### 3、十字链表

**单元素**

```cpp
struct ListNode{
    int row ; int col ; int val ;
	ListNode* left ; ListNode* up ;
};
```

**每一行列都有头指针，若一行/列没有元素，则`headRow[i]->left = headRow[i]`**

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251216122410974.png" alt="image-20251216122410974" style="zoom:67%;" />

```cpp
      列 →
        1   2   3   4   5   6
行 1    +   5   +   +   8   +
↓  2    3   +   +   6   +   +
   3    +   +   7   +   +   4
   4    +   2   ·   +   +   1
   5    9   +   +   5   +   +
（每个元素都有两个指针，分别向右和向下）
行头：R[1] R[2] R[3] R[4] R[5]
列头：C[1] C[2] C[3] C[4] C[5] C[6]
R[1] --> (1,2,5) --> (1,5,8) --> NULL
R[2] --> (2,1,3) --> (2,4,6) --> NULL
R[3] --> (3,3,7) --> (3,6,4) --> NULL
R[4] --> (4,2,2) --> (4,6,1) --> NULL
R[5] --> (5,1,9) --> (5,4,5) --> NULL
C[1] --> (2,1,3) --> (5,1,9) --> NULL
C[2] --> (1,2,5) --> (4,2,2) --> NULL
C[3] --> (3,3,7) --> NULL
C[4] --> (2,4,6) --> (5,4,5) --> NULL
C[5] --> (1,5,8) --> NULL
C[6] --> (3,6,4) --> (4,6,1) --> NULL
          列方向 (down)
             ↓
R[i] --> [ i,j ] --> [ i,k ] --> ...
             |
             v
          [ x,j ]
             |
             v
            ...

```

#### 4、动态规划

> **1、复杂问题分解**
>
> ​		将一个复杂问题分解成若干个子问题，通过综合子问题的解来得到原问题的解
>
> **2、自底向上先解最小问题**
>
> ​		逐个问题击破，并将结果存储在表格里，求解大问题时通过查表得到小问题的解
>
> **3、往往用递推实现**
>
> ​		可以先列出状态转移递推式子

> **1、能解决的问题：**
>
> ​		**1、最优子结构**  大问题的解包含子问题的解
>
> ​		**2、无后效性**    子问题的求解只与当前状态有关，不可与大问题的状态有关
>
> ​		**3、重复子问题**  子问题只计算一次，后答案一直保存。

> **2、解决问题的步骤**
>
> ​		**1、寻找子问题**：拆分成若干个问题
>
> ​		**2、定义状态**：	与子问题有关的各个变量的一组取值称为一个状态
>
> ​		**3、状态转移**：	列出状态转移的递推公式
>
> ​		**4、确认边界条件**：确认递推的终止和边界条件

**3、滚动数组**

​		多维情况下，若第`i`行只取决于前第`i-k`行，则只保留**必要的行**。

**4、C(m,n)的计算**		

```cpp
int C(int n,int m){
    if(m==0 || n==m) return 1;
    if(m>n/2) m = n-m ;
    long long ans = 1 ;
    for(int i=n-m+1,j=1;i<=n;i++,j++){
        ans = ans*i/j ;
    }
}
//分子：n-m+1~n
//分母：1~m
```

#### 5、最大子数组

> **最大子数组和**
>
> ```cpp
> int maxSubArray(vector<int>& nums) {
>     int res = INT_MIN ;
>     int cur = INT_MIN+1e5  ;
>     for(int& i:nums){
>         cur = max(i,cur+i);		//cur:现在重开吗？不重开就加上
>         res = max(res,cur);		//res:所有的最大值
>     }
>     return res;
> }
> ```

>
>  **最大子数组乘积**
>
> ```cpp
> class Solution {
> public:
>     int maxProduct(vector<int>& nums) {
>         int  cur1 = nums[0] , cur2 = nums[0] , res = nums[0] ;
>         for(int i=1;i<nums.size();i++){
>             cur1 *= nums[i] ;
>             cur2 *= nums[i] ;
>             int maxval = max(max(nums[i],cur1),cur2);
>             int minval = min(min(nums[i],cur1),cur2);
>             cur1 = maxval;
>             cur2 = minval;
>             res = max(cur1,res);
>         }
>         return res;
>     }
> };
> 
> 因为minval很容易就能变成maxval，只需要一个乘上负数的契机。
> 所以一直保存minval（当都是正数的时候，也没啥存在的必要，但当又是正数又是负数的时候，很容易minval就变成maxval了，同时maxval也很容易就变成minval了）
> 
> 假如输入 2,-2,3,-4,5,0,-6,7, -8 则
> cur1 cur2
>  2    2
>  -2  -4
>  3   -12
>  48  -12
>  240 -60
>  0    0
>  0   -6
>  7   -42
>  336 -56
> ```
>



#### 6、子集生成

**可以生成类似**

> **1、子集**
>
> ```cpp
> {}
> {a}
> {a,b}
> {a,b,c}
> {a,c}
> {b}
> {b,c}
> {c}
> ```
>

> **2、YN合集**
>
> ```cpp
> NNN
> NNY
> NYN
> NYY
> YNN
> YNY
> YYN
> YYY
> ```
>

> 以下为**二进制转换代码**
>
> ```cpp
> void solve(){
>     int n;
>     cin>>n;
>     for(int i=0;i<pow(2,n);i++){
>         int tmp = i ;
>         for(int j=n-1;j>=0;j--){
>             if(tmp/(1<<j)) cout<<"Y";	// 5/4?
>             else cout<<"N";
>             tmp %= (1<<j);				//5%=4
>         }
>         cout<<endl;
>     }
> }
> ```
>





## （四）字符串匹配



#### 1、模式匹配

> 在目标串中寻找模式串中出现的首位置

#### 2、朴素模式匹配算法

> ###### 逐步蠕动，每位匹配
>
> **时间复杂度分析：**
>
> ​		平均比较次数：`≤2n`
>
> ​		最坏比较次数：`n*m`
>
> ```cpp
> s = "aaaaaaaaaaaaaaaa"
> p = "aaaaab"
> ```
>
> ​		多次匹配复杂度较大
>
> ​		字集越大，时间越接近线性，字符集越小，越接近最坏情况
>
> ```cpp
> int strStr(string& s,string& p){
> 	int n = s.size(),m = p.size();
> 	for(int i=0;i<=n-m;i++){
> 		int j = 0 ;
> 		while(j<m && s[i+j]==p[j]){
> 			j++;
> 		}
> 		if(j==m) return i;
> 	}
>     return -1 ;
> }
> ```

#### 3、KMP

##### 1、动机：

匹配失败后，是否可以移动多几位？跳过重复比较的部分？

指针`i`是否可以不回退？指针`j`是否也能不回退？

**我们可以利用模式串子串的重复性，加速匹配过程**

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251216140851257.png" alt="image-20251216140851257" style="zoom: 50%;" /><img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251216140926196.png" alt="image-20251216140926196" style="zoom: 50%;" />



##### 2、原理：

在匹配失败时，找**最长相等前后缀**

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251216142229557.png" alt="image-20251216142229557" style="zoom:50%;" />

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251216142322904.png" alt="image-20251216142322904" style="zoom:67%;" />

**意思是如果x匹配失败，则会跳转到红色的b后一位，也就是a继续开始匹配**

**匹配失败时，模式串右移距离为：`len - nxt[len-1]`**

#### 3、代码

`len`增加次数不会超过m次，每次+1，且`len`减少次数也不会超过增加次数，所以关键运算次数`<=2*m`，时间复杂度为`O(m)`

```cpp
int kmp(const string &s, const string &p){
    int n = s.size(), m = p.size();
    vector<int> nxt(m, 0);
    for(int i = 1, len = 0; i < m; i++){
        while(len > 0 && p[i] != p[len]) len = nxt[len-1];
        if(p[i] == p[len]) len++;
        nxt[i] = len;
    } 
    for(int i = 0, len = 0; i < n; i++){
        while(len > 0 && s[i] != p[len]) len = nxt[len-1];
        if(s[i] == p[len]) len++;
        if(len == m) return i - m + 1; // 找到匹配
    }
    return -1;
}
```

**若希望多次匹配，则可以在匹配成功后，假装失配，`len = len[len-1]`**

#### 4、KMP的神必用法

> **1、最长相等前后缀长度`next[n]`**
>
> **2、第二长相等前后缀长度`next[next[n-1]-1]`**
>
> ```cpp
>     int x = n;
>     int cnt = 0;
>     while(x && cnt<2){
>         x = nxt[x-1];
>         cnt++;
>     }
> ```
>
> 

> **3、添加前缀，成为回文**
>
> 本质上其实是求最长回文前缀（也就是前缀到哪开始不回文）
>
> ```cpp
> string shortestPalindrome(string s) {
>     string s1 = s;
>     int n = s.size();
>     reverse(s1.begin(),s1.end());			//获取倒转的字符串s1
>     vector<int> nxt(n);
>     for(int i=1,l=0;i<n;i++){
>         while(l>0 && s[i]!=s[l]) l = nxt[l-1] ;
>         if(s[i]==s[l]) l++;
>         nxt[i] = l ;
>     }
>     int len = 0 ;
>     for(int i=0,l=0;i<n;i++){
>         while(l>0 && s1[i]!=s[l]) l = nxt[l-1];
>         if(s1[i]==s[l]) l++;
>         if(i==n-1){
>             len = n-l ;     			//当最后一次匹配时（i到达终点），返回未匹配的长度
>         }							//这个未匹配长度就是我们要加的长度了
>     }
>     string extra;
>     for(int i=n-1;i>=n-len;i--){
>         extra.push_back(s[i]);
>     }
>     return extra+s;
> }
> ```

> **4、循环节**
>
> 如果一个字符串S由最小子串重复多次形成，则P为S的循环节。
>
> ```cpp
> class Solution {
> public:
>     bool repeatedSubstringPattern(string s) {
>         int n = s.size();
>         vector<int> nxt(n, 0);
>         for(int i = 1, len = 0; i < n; i++){
>             while(len > 0 && s[i] != s[len]) len = nxt[len-1];
>             if(s[i] == s[len]) len++;
>             nxt[i] = len;
>         } 
>         if(nxt[n-1]!=0 && n%(n-nxt[n-1])==0) return true;
>         return false;
>     }
> };
> ```
>
> 字符串的最小循环节长度就是`n-nxt[n-1]`了

#### 5、`nextval`函数

**目标：当比较失败时，只用next函数可能会导致在一个地方，回退`next[next[len-1]-1]`多次，多次比较**

**从而达到改进常数的目标**

```cpp
vector<int> nxt(n, 0), nxtval(n, 0);
for (int i = 1, len = 0; i < n; i++) {
    while (len > 0 && p[i] != p[len])
        len = nxt[len - 1];
    if (p[i] == p[len]) len++;
    nxt[i] = len;
    	
    if (i + 1 < n && p[i + 1] == p[len]) {
        nxtval[i] = nxtval[len - 1];
    } else {
        nxtval[i] = len;
    }
}

//用法
if(s1[i]!=s2[l]) len = nxtval[len-1];
```



# 树

## （五）树与二叉树

#### 1、概念

**有序树**：关心孩子的顺序的树（例如二叉树关心左儿子和有儿子）

**首元素**：树的根节点，没有前驱元素

**末元素**：树的叶子节点，没有后继元素

**中间元素**：有一个前驱，多个后继

****

**一个点的度**：子节点的数目

**一棵树的度**：树上度最多的节点的度

**叶节点**：度为0的节点

**分支节点**：度大于0的节点

**边**：树上节点的连线

****

**节点层数/深度**：根节点在第`0`层

**树的高度与深度**：树上结点的最大深度

**结点的高度**：以该节点为根的子树的高度

****

**路径：**从一个结点到另一个节点的路径**（注意，PPT上要求路径一定要是向下的，不能出现`子->父`）**

**路径长度**：路径经过的边数`k`为路径长度。

**结点的层数**：根节点到某个结点的路径长度。

**子孙祖先节点**：存在a到b的路径，则a为b的祖先，b为a的子孙。

#### 2、二叉树的定义

**结点的有限集合，可能可以是空集**

**每个节点最多有2个子结点，分左右子树**

**有`n`个节点的二叉树有$T(n)  = \frac{1}{n+1}\binom{2n}{n}$种形态**



#### 3、二叉树的性质

> ##### 引理：
>
> **1、二叉树第$i$层至多有$2^i$个节点，$i≥0$**
>
> **2、高度为$k$的二叉树至多有$2^{k+1}-1  $($k≥0$)个节点**
>
> **3、在第`n`个结点构成的二叉树中，若叶子节点个数为$n_0$，度为$2$的节点的个数为$n_2$，则有$n_0=n_2+1$**
>
> **（本质：边数为1的，后面接着叶子的，那这个边数为1的有和没有没啥区别，只有边数为2的才会实际造成影响）**

#### 4、满二叉树

> ##### <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251216183923306.png" alt="image-20251216183923306" style="zoom:50%;" />定义：
>
> **高度为k的满二叉树，有$2^{k+1}-1$个结点**
>
> ##### 特点：
>
> **1、叶子节点都在最后一层**
>
> **2、没有度为1的节点**
>
> **3、叶子节点的个数为非叶子节点的个数+1，用$n_0=n_2+1$**

#### 5、完全二叉树

> ##### <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251216183642980.png" alt="image-20251216183642980" style="zoom: 50%;" />定义：
>
> **层序遍历时，遇到空节点时，未来将不会再遇到节点**
>
> ##### 特点：
>
> **1、除最后一层外，其他层是满的，最后一层节点从左到右出现**
>
> **2、只有最下面两层的节点的度小于2,**
>
> **3、叶节点只在最下面两层出现**
>
> **4、按层次顺序编号，仅编号最大的非叶节点可以没有右儿子**
>
> **5、高度为k的完全二叉树最少有$2^k$个节点，最多有$2^{k+1}-1$个节点**
>
> ##### 引理：
>
> **1、1-逻辑的层序遍历中，结点为$i$的父亲是$\lfloor \frac{i}{2} \rfloor$，左右儿子分别为$2*i$与$2*i+1$**
>
> **2、具有$n$个节点的完全二叉树，非叶节点个数为$\lfloor \frac{n}{2} \rfloor$，叶子节点为$\lceil \frac{n}{2} \rceil$个，用$n_0=n_2+1$**
>
> **（可从满二叉树中摘除/添加节点从而推导，每添加俩，上一层少一个叶子，多一个非叶子节点，下一层多两个叶子）**
>
> **3、$n$个结点的完全二叉树高度为$\lfloor{log_{2}n}\rfloor$ （因为正好完美二叉树的时候，层数才会+1）**
>
> **4、二叉树的第$i$层恰好有$k$个节点，则完全二叉树的节点个数最少为$2^n+k-1$，最多为$2^{n+2}-2k-1$**

#### 6、二叉树存储结构

**1、顺序存储**

> **顺序结构：**层序遍历 ——非完全二叉树时会浪费
>
> **链接结构**：类似链表 ——二叉链表/三叉链表
>
> ```cpp
> struct Node{
>     Node* left ; Node* right ; Node* father ;
>     int val ;
> };
> ```

#### 7、二叉树的遍历

> ###### 先根遍历：
>
> ```cpp
> void Preorder(Node* root){
>     if(!root) return;
>     visit(root);
>     Preorder(root->left);
>     Preorder(root->right);
> }
> ```

> ###### 中根遍历：
>
> ```cpp
> void Inorder(Node* root){
>     if(!root) return;
>     Inorder(root->left);
>     visit(root);
>     Inorder(root->right);
> };
> ```
>
> ###### 冷知识：将中序倒转之后，可生成左右倒转的子树

> ###### 后序遍历：
>
> ```cpp
> void Postorder(Node* root){
>     if(!root) return;
>     Postorder(root->left);
>     Postorder(root->right);
>     visit(root);
> }
> ```
>
> ###### 冷知识：前后序遍历倒转过来之后，可生成左右倒转的子树

> ###### 前两个冷知识的实践：中根+前根，倒转之后可用中根+后根来构建镜面翻转树
>
> ```cpp
> #include<bits/stdc++.h>
> using namespace std;
> #define td return
> int n;
> struct Node{
> 	int val,l=0,r=0;
> };
> 
> vector<Node> g;      // g[1..n]，存所有节点
> vector<int> in;      // 中序序列
> vector<int> post;    // 后序序列
> 
> //in:7 6 5 4 3 2 1
> //post:7 5 6 2 3 1 4
> 
> // 构建树，返回根节点下标
> int build(int inL, int inR, int postL, int postR){
>     if(inL > inR) return 0; // 空子树返回0
>     int rootVal = post[postR];   // 后序最后一个是根
>     int k;
>     for(k = inL; k <= inR; k++){
>         if(in[k] == rootVal) break;
>     }
>     
>     k -= inL;
>     // 构建左子树
>     g[rootVal].l = build(inL, inL+k-1, postL, postL + k - 1);
>     // 构建右子树
>     g[rootVal].r = build(inL+k+1, inR, postL + k, postR - 1);
> 
>     return rootVal;
> }
> 
> 
> void solve(){
> 	cin>>n;
> 	g.resize(31);
>     in.resize(n+10);
>     post.resize(n+10);
> 	for(int i=1;i<=30;i++) g[i].val = i;
> 	for(int i=n-1;i>=0;i--) cin>>in[i];
> 	for(int i=n-1;i>=0;i--) cin>>post[i];
>     int root = build(0, n-1, 0, n-1);
>     queue<int> q;
>     q.push(root);
>     bool first = true;
>     while(!q.empty()) {
>         int idx = q.front(); q.pop();
>         if(!first) cout << " ";
>         cout << g[idx].val;
>         first = false;
>         if(g[idx].l) q.push(g[idx].l);
>         if(g[idx].r) q.push(g[idx].r);
>     }
> }
> int main(){
> 	ios::sync_with_stdio(false);
> 	cin.tie(0);
> 	int t=1;
> 	// cin>>t;
> 	while(t--) solve();
> 	td 0;
> }	
> 
> ```
>
> 

> ###### 层序遍历：
>
> ```cpp 
> void LevelOrder(Node* root){
>     queue<Node*> q;
>     q.push(root);
>     while(!q.empty()){
>         Node* p = q.front();
>     	visit(p);
>         if(p->left) q.push(p->left);
>         if(p->right) q.push(p->right);
>     }
> }
> ```
>
> **注意：以下情况仅限于完全二叉树！！**
>
> **完全二叉树，队列最大规模为所有叶节点的个数，也就是$\lceil n/2 \rceil$**
>
> **最大规模可能会出现两次（当有度为1的节点的时候）**

#### 8、二叉树的操作

> **搜索并返回某个结点的父节点**
>
> ```cpp
> Node* Find(Node* root,Node* p){
> 	if(!root || p==root) return NULL;
> 	if(root->left==p || root->right==p) return root;
>     Node* ans = Find(root->left,p);
>     if(ans) return ans;
>     return Find(root->right,p);
> }
> ```

> **子树结点个数**
>
> ```cpp
> int count(Node* root){
>     if(!root) return 0;
>     return count(root->left)+count(root->right)+1;
> }
> ```

> **二叉树高度**
>
> ```cpp
> int depth(Node* root){
> 	if(!root) return -1 ;
> 	return max(depth(root->left),depth(root->right))+1;
> }
> ```

> **删除二叉树**
>
> ```cpp
> void del(Node*& root){
>     if(!root) return;
>     del(root->left);
>     del(root->right);
>     //delete root ;
>     root = NULL;
> }
> ```
>
> **删除子树**
>
> ```cpp
> bool delsub(Node*& root , Node* p){
>     if(!root || !p) return false;
>     if(p==root){
>         del(root);
>         return true;
>     }
>     if(delsub(root->left,p)) return true;
>     return delsub(root->right,p);
> }
> ```

> **创建二叉树**
>
> **1、增强先根**
>
> ```cpp
> Node* Creat(){
>  char c; cin>>c;
>  if(c=='#') return NULL;
>  Node* root = new Node;
>  root->data = c ;
>  root->left = Creat();
>  root->right = Creat();
>  return root;
> }
> ```
>
> **2、增强后根**
>
> ```cpp
> string s;
> reverse(s.begin(),s.end());
> int index = 0 ;
> Node* creat(){
> 	char c = s[index++];
>     if(c=='#') return NULL;
>     Node* root = new Node(c);
>     root->right = Creat();
>     root->left = Creat();
>     return root;
> }
> ```
>
> **3、复制二叉树**
>
> ```cpp
> Node* cpy(Node* root){
>  if(!root) return NULL;
>  Node* l = cpy(root->left);
>  Node* r = cpy(root->right);
>  Node* newr = new Node;
>  newr -> data = root->data ;
>  newr -> left = l ;
>  newr -> right = r ;
>  return newr;
> }
> ```

> **二叉树中，中根，先根，后根序列的首末节点**
>
> |              | **中根序列**                | **先根序列**                                                 | **后根序列**                                                 |
> | ------------ | --------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
> | 第一个节点   | `while(p->left) p = left`   | `root`                                                       | `while(1){if(p->right) p = p -> right ; else if(p->left) p = p->left ; else return p ;}` |
> | 最后一个节点 | `while(p->right) p = right` | `while(1){if(p->right) p = p -> right ; else if(p->left) p = p->left ; else return p ;}` | `return root`                                                |
>
> **总而言之，就是：中根都是最左或最右，先根后根都是能左就左，无左再右，下图便是一个很好的区分的例子**<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251216194031269.png" alt="image-20251216194031269" style="zoom:50%;" />

#### 9、二叉树的反序列化

> **！！！中根+其他遍历可唯一确定一棵二叉树**
>
> **！！！层次+中遍历可唯一确定一棵二叉树**
>
> **先根+中根 -> 后根**
>
> ```cpp
> void dfs(string mid,string fnt){
>     if(!mid.empty()){
>         int k = mid.find(fnt[0]);
>         dfs(mid.substr(0,k),fnt.substr(1,k));
>         dfs(mid.substr(k+1),fnt.substr(k+1));
>         cout<<root;
>     }
> }
> ```
>
> **中根+后根 -> 先根**
>
> ```cpp
> void dfs(string mid,string bck){
> 	if(!mid.empty()){
> 		cout<<bck.back();
> 		int k = mid.find(bck.back());
> 		dfs(mid.substr(0,k),bck.substr(0,k));
> 		dfs(mid.substr(k+1),bck.substr(k,mid.size()-k-1));
> 	}
> }
> ```
>
> **先根+中根建树**
>
> ```cpp
> //先根：1~mid,mid+1~r
> //中根：0~mid-1,mid+1~r
> Node* build(string pre,string mid,int pl,int pr,int ml,int mr){
>     if(pl>pr) return NULL;
>     Node* root = new Node;
>     root->data = pre[pl];
>     int k = mid.find(pre[pl]) ;
>     k -= ml ;
>     root->left = build(pre,mid,pl+1,pl+k,ml,ml+k-1);
>     root->right = build(pre,mid,pl+k+1,pr,ml+k+1,mr);
>     return root;
> }
> ```
>
> **中根+层次**
>
> ```cpp
> Node* build(string& mid, string& level, int midl, int midr) {
>     if (midl > midr) return nullptr;
>     Node* root = new Node(level[0]);  // level的第一个节点是当前子树的根
> 
>     // 在中序中找到根的位置
>     int k = mid.find(root->val, midl);  // 从midl开始查找
>     if (k == string::npos) return nullptr;  // 安全保护
>     
>     // 构建左子树节点集合
>     unordered_set<char> leftSet;
>     for (int i = midl; i < k; i++) {
>         leftSet.insert(mid[i]);
>     }
>     
>     // 提取左右子树的层次遍历序列（从level[1]开始，跳过根）
>     string leftLevel, rightLevel;
>     for (int i = 1; i < level.size(); i++) {
>         char ch = level[i];
>         if (leftSet.count(ch)) {
>             leftLevel.push_back(ch);
>         } else{
>             rightLevel.push_back(ch);
>         }
>     }
>     
>     root->left = build(mid, leftLevel, midl, k - 1);
>     root->right = build(mid, rightLevel, k + 1, mid);
>     
>     return root;
> }
> ```
>
> **完全二叉树+先根/中根/后根/层序**
>
> ```cpp
> void Prebuild(int pos){
>     if(pos>n) return;
>     cin>>a[pos];
>     Prebuild(pos<<1);
>     Prebuild((pos<<1)+1);
> }
> 
> void Inbuild(int pos){
>     if(pos>n) return;
>     Inbuild(pos<<1);
>     cin>>a[pos];
>     Inbuild((pos<<1)+1);
> }
> 
> void Postbuild(int pos){
>     if(pos>n) return;
>     Postbuild(pos<<1);
>     Postbuild((pos<<1)+1);
>     cin>>a[pos];
> }
> 
> void Levelbuild(){
>     for(int i=1;i<=n;i++) cin>>a[i];
> }
> ```
>
> 

#### 10、二叉树序列的非递归写法

> **先根序列**
>
> ```cpp
> 
> int build(){
>    	stack<pair<int,bool>> s;
>     int root;
>     cin>>root;
>     s.push({root,1});	//1代表右子树
>     s.push({root,0});	//0代表左子树
>     while(!s.empty()){
>         int u = s.top().first();
>         bool f = s.top().second();
>         int v;
>         cin>>v;
>         if(!f){
>             g[u].l = v;
>         }else{
>             g[u].r = v;
>         }
>         if(y!=-1){
>             s.push({v,1});
>             s.push({v,0});
>         }
>     }
> }
> 
> pre.push({x,0});
> while(!pre.empty()){
>     int t = pre.top().first();
>     int f = pre.top().second();
>     if(!f){
>         cout<<t;
>         pre.push({t,1});
>         if(g[t].l!=-1) pre.push({g[t].l,0}); 
>     }else{
>         if(g[t].r!=-1) pre.push({g[t].r,0});
>     }
> }
> ```
>
> **中根序列**
>
> ```cpp
> mid.push({x,0});
> while(!mid.empty()){
>     int t = mid.top().first;
>     bool f = mid.top().second;
>     mid.pop();
>     if(!f){
>         mid.push({t,1});				//第一次访问：转向左侧节点
>         if(g[t].l!=-1) mid.push({g[t].l,0});
>     }else{							//第二次访问：访问该点，并转向其右侧节点
>         cout<<t;
>         if(g[t].r!=-1) mid.push({g[t].r,0});
>     }
> }
> ```
>
> **后根序列**
>
> ```cpp
> vector<int> input;
> index = input.size()-1;
> 
> build(){
>     stack<pair<int,bool>> s;
>     root = input[index--];
> 	s.push({root,0});
>     s.push({root,1});
>     while(!s.empty()){
>         int u = s.top().first();
>         bool f = s.top().second();
>         s.pop();
>         int v = input[index--];
>         if(!f){
>             g[u].l = v;
>         }else{
>             g[u].r = v;
>         }
>         if(v==-1){
>             s.push({v,0});
>             s.push({v,1});
>         }
>     }
> }
> 
> bck.push({x,0});
> while(!bck.empty()){
>     int t = bck.top().first;
>     int f = bck.top().second;
>     bck.pop();
>     if(!f){
>         bck.push({t,1});					//第一次出栈：找左侧
>         if(g[t].l!=-1) bck.push({g[t].l,0});
>     }else if(f==1){
>         bck.push({t,2});					//第二次出栈：找右侧
>         if(g[t].r!=-1) bck.push({g[t].r,0});
>     }else{
>         cout<<t;							//第三次出栈：访问自己。
>     }
> }
> ```
>
> 

#### 11、二叉树的计数

> **由$n$个节点可构成多少个二叉树？**
>
> 不妨先用先根序列来编号，设先根序列为`1,2,3,4...n`，中根序列总数为$T(n)  = \frac{1}{n+1}\binom{2n}{n}$
>
> （本质是因为：先根在入栈的时候访问节点，中根在出栈的时候访问节点，而先根和中根在入栈和出栈的操作并无区别，只是先根在入栈的时候进行了访问，而中根在出栈的时候进行了访问，因此中根序列总数是$T(n)  = \frac{1}{n+1}\binom{2n}{n}$）

## （六）线索二叉树

#### 1、动机

**求一个二叉树的中根后继节点**

```cpp
if(p->right){
    p = p->right;
    while(p->left) p = p->left;
    return p;
}
while(p->fa){
    if(p->fa->left==p){
        return p->fa;
    }
    p = p->fa;
}
return NULL;
```

很明显，找**先中根后继需要较长的时间**，另外，二叉树的非满节点存在不少**空指针**，因此，我们可以建立**线索二叉树**

#### 2、线索二叉树

> **有孩子时，Left / Right 指向儿子  `Thread = 0`**	
>
> **无儿子时，Left / Right 指向某种遍历的前驱 / 后继 `Thread = 1`**
>
> 因此，叶子结点就是`Lthread == 0 && Rthread == 0`
>
> ```cpp
> Node*{
>     Node* left; Node* right;
>     int Data;
>     bool LThread ; bool RThread;
> };
> ```



**另外，在中序遍历中，中根序列第一个节点必定没有左孩子，但`LThread`依旧为1，最后一个节点也必定没有右孩子，同理。**

#### 3、中序线索二叉树操作

> **找第一个节点**（走到最左侧）
>
> ```cpp
> Node* FIO(Node* root){
> 	while(root->LThread==0)
> 		root = root->left;
> 	return p;
> }
> ```

> **找最后一个节点**（走到最右侧）
>
> ```cpp
> Node* LIO(Node* root){
> 	while(root->LThread==0)
> 		root = root->right;
> 	return p;
> }
> ```

> **中序遍历前驱**
>
> ```cpp
> Node* PIO(Node* p){
>     return (p->Lthread)? p->left : LIO(p->left);
> }
> ```
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217110712019.png" alt="image-20251217110712019" style="zoom:50%;" />

> **中序遍历后继**
>
> ```cpp
> Node* NIO(Node* p){
> 	return (p->Rthread)? p->right : LIO(p->right );
> }
> ```
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217110705019.png" alt="image-20251217110705019" style="zoom:50%;" />

> **中序遍历**
>
> ```cpp
> void IO(Node* root){
> 	for(Node* p = FIO(root);p;p=NIO(p)) visit(p)
> }
> ```

#### 4、中序线索化

**本质：用pre来存前驱，之后正常中序遍历即可**

```cpp
Node* pre = NULL;
void IT(Node* p){
    if(!p) return;
    IT(p->left);
    if(p->left) p->LThread = 0;
    else{
        p->LThread = 1 ; p->left = pre;
    }
   	if(!pre){
        if(!pre->right){
            pre->RThread = 1 ;
            pre->right = p ;
        }else pre->Rthread = 0 ;
    } 
    pre = p ;
    IT(p->right);
}
if(pre) pre->Rthread = 1;
```

#### 5、问题与拓展

**前后序线索二叉树的问题**

1、若节点没有**父指针**，前序线索二叉树不能高效查询**前根前驱**

2、若节点没有**父指针**，后序线索二叉树不能高效查询**后根后继**

**拓展的线索二叉树**

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217113937999.png" alt="image-20251217113937999" style="zoom:50%;" />

​		**Pred指向前驱，Succ指向后继，空间换时间**



## （七）树

#### 1、树↔二叉树

> ##### 树→二叉树
>
> **使用左儿子，右兄弟的建树方法**（二叉树的左节点是儿子，二叉树的右节点是兄弟）
>
> ![image-20251217114324783](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217114324783.png)
>
> **如果是森林**
>
> **1、建立一个虚拟节点，建成二叉树之后删去虚拟节点即可**
>
> **2、将每个树变成二叉树，之后以第一个二叉树的根为总根，其他二叉树依次为上一个二叉树根节点的右孩子即可（因为并列，右兄弟）**<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217114756275.png" alt="image-20251217114756275" style="zoom:50%;" />
>
> 

> ##### 二叉树→树
>
> **若右子树为空，则可转换为一棵树，否则是森林**
>
> **反向左儿子右兄弟**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217114934993.png" alt="image-20251217114934993" style="zoom: 50%;" />

#### 2、树的存储结构

> ###### 顺序存储——双亲表示法
>
> **编号后，记录每个节点的父亲即可**

> ###### 链接存储——多叉链表
>
> **按孩子最多的节点为准，但容易有很多空指针**

> ###### 链接存储——左孩子，右兄弟
>
> **用二叉树的算法框架完成树的操作**

#### 3、树的基本操作

> ###### 先根遍历
>
> 与其对应的二叉树**先根序列**相同

> ###### 后根遍历
>
> 与其对应的二叉树的**中根序列**相同

> ###### 遍历
>
> ```cpp
> Node* Search(Node* root,int k){
> 	if(!root) return NULL;
>     if(root->data == k) return root;
>     Node* res = Search(root->left,k);
>     if(res) return res;
>     return Search(root->right,k);
> }
> ```

> ###### 找一个节点的所有孩子
>
> ```cpp
> vector<Node*> Child(Node* root){
>     vector<Node*> res;
>     for(Node* p = root->left;p;p = p->right) res.push_back(p);
> }
> ```

#### 4、树的反序列化

**1、树的先根序列+结点度**（栈逻辑，从左往右）

**2、树的后根序列+结点度**（栈逻辑，从右往左）

**3、树的层次序列+结点度**（队列逻辑）

## （八）树与二叉树的应用

#### 1、压缩

> **数据压缩**的过程叫做**编码**，也就是字符转成唯一的二进制串
>
> **数据解压**的过程叫做**解码**，也就是二进制转换为字符

**不等长编码：**

> **1、熵编码**：不等长编码，压缩时，可使出现**频率**较少的字符用**较短**的编码，从而使得**整体文件编码更短**
>
> **2、前缀编码：**字符串中任何编码都**不能是其他字符的前缀**



> #### 扩充二叉树
>
> ###### 定义：
>
> **在二叉树空指针位置，增加特殊节点，由此生成的二叉树**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217155903261.png" alt="image-20251217155903261" style="zoom:50%;" />
>
> 圆形的为**内节点**，方形的为**外节点**。每个内节点都有两个儿子，外节点没有孩子。
>
> **空二叉树的拓展二叉树只有一个外节点**
>
> ###### 加权路径长度：
>
> $WPL = \sum_{i=1}^{n} w_i L_i$
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217160248498.png" alt="image-20251217160248498" style="zoom:50%;" />
>
> **最优二叉树**：n个带权外节点构成的所有扩充二叉树中，$WPL$值最小的二叉树。
>
> ###### 文件编码与扩充二叉树
>
> | **文件编码**      | =**扩充二叉树=** |
> | ----------------- | ---------------- |
> | 字符$a_i$         | 外节点$i$        |
> | 字符出现次数$c_i$ | 外节点权值$w_i$  |
> | 字符编码长度$l_i$ | 外节点深度$L_i$  |
> | 文件编码总长度    | $WPL$            |
>
> 因此可将文件编码问题转换为构建最优二叉树的问题了。

**选读：Shannon-Fano算法**

> **递归重复做：**将字符集分成两部分，使两部分的频率之和尽可能相等。
>
> **并非最优解！！！**

#### 2、Huffman树

> 树值构建n棵二叉树，每棵二叉树只有一个顶点，权值为$w_i$**
>
> **2、选出权值最小的两个根节点，合并成一棵二叉树，生成的一个新节点为这两个节点的父亲，权值为这两个节点的和**
>
> **3、重复2，直到只剩一棵二叉树为止**
>
> ###### Huffman编码：
>
> **在树上：左分支标记0，右分支标记1**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251217161422652.png" alt="image-20251217161422652" style="zoom:33%;" />
>
> n的编码是00001
>
> s的编码是00000
>
> p的编码是11
>
> **最小编码**
>
> ```cpp
>  priority_queue<int,vector<int>,greater<>> pq;
>  while(n--){
>      int x;
>      cin>>x;
>      pq.push(x);
>  }
>  int WPL = 0;
>  while(pq.size()>1){
>      int u = pq.top();pq.pop();
>      int v = pq.top();pq.pop();
>      pq.push(u+v);
>      WPL += u+v;
>  }
> ```
>
> ###### 二子性
>
> Huffman树上不包含度为1的节点，因此必定有n个叶子节点和n-1个非叶子节点，总共2n-1个结点、
>
> ###### 同权不同构
>
> Huffman树形态不唯一，编码不唯一
>
> 左右子树互换后，WPL长度依旧不变

#### 3、Huffman算法实现

**1、建点**

```cpp
vector<Node*> H;
void CreatHuffmanNode(string ch,vector<int> freq,int n){
    for(int i=0;i<n;i++){
        H[i] = new HuffmanNode;
        H[i] -> data = ch[i];
        H[i] -> weight = freq[i];
        H[i]->left=H[i]->right=NULL;
    }
    sort(H,n);
}
```

**2、建树**

**数组暴力建树**

```cpp
Node* BuildTree(vector<Node*> H,int n){
	for(int i=0;i<n;i++){
        Node* t = new Node;
        t->left = H[i];
        t->right = H[i+1];
        t->weight = t->left->weight + t->right->weight;
        int j = i+2;
        //左侧节点废除两个，这边重复利用i+1
        while(j<n && H[j]->weight<t->weight){
            H[j-1]=H[j];
            j++;	//最后j会停留在一个比t大的位置，而j-1==j-2，因此后面覆盖j-1
        }
        H[j-1] = t;
    }
    return H[n-1];
}
```

**单调队列**

排序后，所有元素放入队列1，队列1是**单调递增**队列

随后，生成的新元素放到队列2，**因为生成的元素只会越来越大**，所以队列二是**单调递增**队列。

因此，新的元素一定会从队列1与队列2的队首产生。

```cpp
sort(H);
for(Node* H){
	queue1.push(H);
}

while(queue1.size()+queue2.size()>1){
	int u,v;	
	if(queue1.empty()){
		u = queue2.front();
        queue2.pop();
	}else if(queue2.empty()){
        u = queue1.front();
        queue1.pop();
    }else if(queue1.front()<queue2.front()){
        u = queue1.front();
        queue1.pop();
    }else{
        u = queue2.front();
        queue2.pop();
    }
    
    if(queue1.empty()){
		v = queue2.front();
        queue2.pop();
	}else if(queue2.empty()){
        v = queue1.front();
        queue1.pop();
    }else if(queue1.front()<queue2.front()){
        v = queue1.front();
        queue1.pop();
    }else{
        v = queue2.front();
        queue2.pop();
    }
    
    Node* t = new Node;
    t->left = u ;
    t->right = v;
    t->weight = u->val+v->val;
    queue2.push(t);
    
}
```

**优先队列最小堆**

```cpp
每次取堆顶，结果放堆顶并让他下沉
```

> **3、解码**
>
> 依次读入01字符串，若是为**0**，则往**左**子树走，若是为**1**，则往**右**子树走
>
> 每走一个点都**检查是否为叶子**，如果为叶子，那么就说明已经结束这段路程了，解码成功



#### 4、表达式树

> ###### 特性
>
> **叶子结点：操作数**
>
> **非叶子节点：运算符**
>
> **中根序列：中缀表达式**（可以使用中缀表达式转后缀表达式的栈的方式，从而完成建树，也就是操作数栈和运算符栈，运算符栈需要是单调栈，优先级单调递增）
>
> **后根序列：后缀表达式**（所以可以将后缀表达式翻转过来，获得了先根表达式，之后颠倒左右子树，即可获得对应的表达式树）
>
> 也可以用栈来存操作数，if运算符，则取俩操作数，放回一个运算符。

> ###### 运算
>
> 通过 **后根遍历**表达式二叉树，计算左子树表达式为ans1，右子树为ans2，结果放在根上即可
>
> ```cpp
> int Calc(Node* t){
>     if(!t->left) return t->data;
>     return Calc(t->left) op Calc(t->right);
> }
> ```

#### 5、并查集

> **make_set** 创建集合，唯一元素是x
>
> **find** 找到x所在代表元
>
> **union** 合并x，y所在的集合（x的根的父节点指向y的根）
>
> **等价关系：**反身性、对称性、传递性 => 等价类 == 并查集
>
> （**注意：当题目有要求当前A<B时，那么就规定了合并次序，此时就不能按秩合并了**）

> ###### 路径压缩
>
> ```cpp
> int find(int x){
>     return fa[x]==x?x:fa[x]=find(fa[x]);
> }
> ```

> ###### 按秩合并
>
> **秩**：以该节点为根的子树的高度的 **上界**
>
> 若**秩不相同**：选秩大的做父节点
>
> 若**秩相同**：随便选一个做父节点，**秩++**
>
> ```cpp
> // 按秩合并的并查集 UNION 操作
> void UNION(int x, int y) {
>     int fx = FIND(x);   // x 所在集合的根
>     int fy = FIND(y);   // y 所在集合的根
>     // 若已经在同一集合中，直接返回
>     if (fx == fy) return;
> 
>     // 按秩合并
>     if (rank[fx] > rank[fy]) {
>         Parent[fy] = fx;        // fx 的秩更大，作为父节点
>     } 
>     else if (rank[fx] < rank[fy]) {
>         Parent[fx] = fy;        // fy 的秩更大，作为父节点
>     } 
>     else {
>         Parent[fx] = fy;        // 秩相同，任选一个
>         rank[fy]++;             // 新根的秩加 1
>     }
> }
> 
> ```

> **单独使用路径压缩与按秩合并：`O(logn)`**
>
> **同时使用两种优化：均摊时间复杂度接近`O(1)`**

****

# 图

## （九）图的概念与存储结构

#### 1、概念

> 由边，点组成
>
> ###### 有向图：
>
> 两个顶点有序对：**弧，起点是弧尾，终点是弧头**
>
> ###### 无向图：
>
> u,v右边→uv互为 **邻接顶点**，u邻接到v，v邻接自u
>
> ###### 度：
>
> 无向图：边数
>
> 有向图：
>
> ​		出度：出边数
>
> ​		入度：入边数
>
> ​		度：出度+入度
>
> 度总数 = 边总数*2
>
> ###### 路径：
>
> 路径长度，路径长度、简单路径（没有相同顶点），简单回路（简单路径，起点与终点相同）
>
> ###### 子图：
>
> 边与点都属于母图，分别为母子图的关系，若点相同，则为支撑子图
>
> ###### 连通性：
>
> 有路径 = 可联通
>
> 无向图中两两可达 → 连通图
>
> 有向图中两两可达 → 强连通图
>
> （强）联通子图
>
> 连通分量：极大（强）连通子图
>
> ###### 带权图：
>
> G为权图
>
> 若u==v，则边为0
>
> 若u无法到v，则边为无穷大
>
> 路径长度：路径上权值和![image-20251218120733691](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251218120733691.png)

****

#### 2、存储结构

> ###### 邻接矩阵
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251218120909833.png" alt="image-20251218120909833" style="zoom:50%;" />
>
> **无向图的度：一行中非0个数**
>
> **无向图的度：一行+一列中非0的个数**
>
> 
>
> **空间：$O(n^2)$**
>
> **是否有边：$O(1)$**
>
> **点的邻接点$O(n)$**
>
> 
>
> **稀疏矩阵浪费时空**

> ###### 邻接表：
>
> **顺序存储顶点表，每个顶点一个链表**![image-20251218121220458](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251218121220458.png)
>
> ![image-20251218121410080](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251218121410080.png)
>
> （左侧：表头）
>
> （右侧：结点）
>
> `Veradj`：邻接顶点在表中下标
>
> `link`：下一个结点的指针
>
> `cost`：权值
>
> **统计顶点入度：**
>
> ```cpp
> void getInDegree(Vertex Head[],int n, int InDegree[]) {
>     for(int i=0;i<n;i++) InDegree[i]=0;
>     for(int i=0;i<n;i++)//用i扫描每个顶点
>         for(Edge* p=Head[i].adjacent; p!=NULL; p=p->link)
>             int k = p->VerAdj;
>             InDegree[k]++;
>         }
> }
> ```
>
> **空间：**$O(n+e)$
>
> **找边：**$O(d_i)$
>
> **删边：**$O(d_i)$
>
> **找邻接点：**$O(d_i)$

****

## （十）图的遍历与应用

#### 1、深度优先搜索

> ###### 深度优先支撑树：
>
> 将深度优先走过的边生成的树
>
> 时间复杂度$O(n+e)$
>
> 非连通图需要多次DFS
>
> **非递归写法**
>
> ​		visit = 0 ，v0 压栈
>
> ​		栈空->结束
>
> ​		loop:弹出顶点->visit = 1，将v未访问过的所有顶点弹栈->loop
>
> ```cpp
> void dfs(int v){
>     stack<int> s;
>     for(int i=0;i<n;i++) vis[i] = 0 ;
>    	s.push(v);
>     while(!s.empty()){
>         v = s.top();
>         s.pop();
>         if(vis[v]) continue;
>         vis[v] = 1;
>         visit(v);
>         for(int& i:g[v]){
>             if(!vis[i])
>                 s.push(i);
>         }
>     }
> }
> ```
>
> 

#### 2、广度优先搜索

> ```cpp
> queue<int> q;
> q.push(u);
> for(int i=0;i<n;i++) vis[i] = 0 ;
> while(!q.empty()){
> 	u = q.front();
> 	q.pop();
> 	for(int& v:q.front()){
> 		if(vis[v]) continue;
> 		vis[v] = 1;
> 		visit(v);
> 		q.push(v);
> 	}
> }
> ```
>
> **都推荐在入队/栈时访问，效率更高**

****

#### 3、图遍历的应用

**1、判断连通性** 并查集&DFS

**2、图中a到b的所有长度为L的简单路径**

思想：DFS，不会走回头路（也就是访问过的节点不会再D了，但回溯之后（dfs结束之后）会将vis置0,）在遇到b的时候，如果恰好长度为L，则放入PathList中，pathcnt++，否则就当没遇到过（且不会继续让b继续D下去）

另外，如果当前长度len大于L，则也不会继续dfs下去（因为也没有意义了）

> **2020年期末真题**
>
> 一个带权图G以邻接表作为存储结构，顶点编号为0至n-1，边权可正可负。请设计一个算法，找出从
>
> 指定顶点u出发的、不经过顶点v(vu)的、包含总顶点数不超过m (m≤2)的、长度等于L的所有简单路
>
> 径，并将每条路径保存在一个单链表中，所有单链表的头指针存入一个指针数组。即实现如下函数：
>
> int FindPath(Vertex Head[ ], int n, int u, int v, int L, int m, ListNode* PathList[ ])
>
> 其中Head为图G的顶点表，n、u、v、L、m含义如题目所述，PathList为存储各路径链表头指针的数
>
> 组，函数返回值为满足条件的路径条数。
>
> ```cpp
> int FindPath(Vertex Head[],int n,int u,int v,int L,int m,ListNode* PathList[]){
>     vector<int> vis(n);
>     int pathcnt = 0;
>     vector<int> path;
>     
>     vis[u] = 1; 				
>     vis[v] = 1; 			//设为访问过，那么后面dfs的时候就不会再访问了
>     path.push_back(u);
>     dfs(vis,pathcnt,u,1,m,0,L,path);
>     return pathcnt;
> }
> 
> void dfs(vector<int>& vis,int& pathcnt,int pos,int pointcnt,const int m, int len,const int L,vector<int>& path){
>     int u = pos;
> 	for(ListNode* tmp = Head[u].link;tmp;tmp = tmp->link){
>         int v = tmp->data;
>         int w = tmp->cost;
>         if(vis[v]) continue;
>         
>         vis[v] = 1 ;									//完成加点操作，并检查加点操作
>         path.push_back(v);
>         if(len+w==L){
>             ListNode* cur = new ListNode; 
>             PathList[pathcnt++] = cur;
>             for(int i:path){
>                 ListNode* newp = new ListNode ;
>                 newp->data = i ;
>                 newp->next = NULL;
>                 cur->next = newp;
>                 cur = newp;
>             }
>         }
>         if(pointcnt+1<m) dfs(vis,pathcnt,v,pointcnt+1,m,len+w,L,path);	//如果还能加点...
>     	path.pop_back();							//回溯
>        	vis[v] = 0 ;
>     }
>     return;
> }
> ```
>

**3、判断无向图是否有环**

​	1、DFS是否会访问到之前访问过的点

​	2、并查集，每读入一条边，看看Find(x)是否与Find(y)相同

**4、判断有向图是否有环**

​	1、`vis[i]`分为三种状态，分别是：0未被访问，1在栈中，2未在栈中（因此访问结束后，并非置0，而是置2

​		置1,2的都不会重复访问，若访问到置1的，则直接返回true

****

## （十一）拓扑排序&关键路径

#### 1、拓扑排序

**目的：子任务A在子任务B达成后才能进行工作时，可用拓扑排序来决定任务完成的先后次序**

**AOV网：顶点代表活动，有向边表示次序，无回路**

> **步骤：不停删0入度的点，可用栈和队列实现**
>
> 判断是否拓扑序：逐个点判断1、判断入度是否为为0 2、删点。
>
> **DFS拓扑**
>
> ```cpp
> void DFS_TopoSort(Vertex* Head, int v, int visited[], vector<int>& topo) {
>     visited[v] = 1;
>     for (Edge* p = Head[v].adjacent; p != nullptr; p = p->link) {
>         int u = p->VerAdj;
>         if (!visited[u])
>             DFS_TopoSort(Head, u, visited, topo);    //先访问最终的汇点，之后再回溯，
>     }
>     topo.push_back(v)；
> }
> ```
>
> 原理：先输出的点一定需要更多条件去触发，那么条件将一定会在这个点的“未来”给出

****

#### 2、关键路径

**AOV网：顶点表示任务**

**AOE网：有向边表示任务**

**AOV可以将顶点上的点权往后推成它发出的边权，从而变成AOE网，就是最后还需要一个虚拟汇点，从而解决原汇点的点权**

> ###### 关键路径：
>
> 完成整个工程所需的**最短时间**，取决于源点到汇点的**最长路径长度**，这条路径就是**关键路径**了
>
> ###### 变量
>
> **事件最早发生时间`ve(j)`**：最长路径长度，完成任务所需最短时间
>
> **事件最晚发生时间`vl(j)`**：一个事件允许最迟开始的时间（也就是需要和平行的并齐进度）——从汇点反过来求
>
> **活动最早发生时间`e(i)`**：最早允许开启这个事件的时间，与`ve(j)`相同
>
> **活动最晚发生时间`l(i)`**：最晚允许开启这个事件的时间，应该为`l(u) = vl(v)-weight(u,v)`
>
> **关键活动：`e(i)==l(i)`**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251218194939817.png" alt="image-20251218194939817" style="zoom: 80%;" />
>
> 

****

## （十二）最短路问题

#### 1、无权图最短路径

**BFS，dist记录距离，pre记录前驱，只有dis==INT_MAX的点才会被更新**

****

####  2、Dijkstra算法

> **能处理非负权图，不能处理负权图，但可以**
>
> `dist[i]`记录u到i最短距离
>
> `pre[i]`前驱，同时也可以存源点到其他点的最短路
>
> `S[i]`顶点i是否进入集合（进入集合则无需更新）
>
> 每次都需要从`S[i]==0`的顶点集合中，寻找一个最小的点放入`S[i]`中。因此为`O(n²+e)`的算法，n²来源于找最小的点，e来自遍历图

按照最短距离递增，依次把顶点加入到集合S中，另外使用斐波那契堆，复杂度为`O(nlogn+e)`

****

#### 3、A*算法

启发式搜索，以代价函数为基准进行Dij

****

#### 4、Floyd算法

> **目标：求每对顶点之间的最短距离，允许负边权，不允许负权环**
>
> `G`邻接矩阵
>
> `n`图的顶点个数
>
> `D[i][j]`顶点`i`到`j`的最短距离，初值等于邻接矩阵
>
> `path[i][j]`，`i`到`j`的最短路径上，下一个顶点的编号
>
> ```cpp
> for(int k=1;k<=n;k++){
>     for(int i=1;i<=n;i++){
> 		if(dis[i][k]==INF) continue;
>         for(int j=1;j<=n;j++){
>             if(dis[i][k]+dis[k][j]<d[i][j]){	//因为不能被自己更新，所以用<而不不可以用<=
>                 dis[i][j] = dis[i][k]+dis[k][j];
>                 path[i][j] = path[i][k];
>             }
>         }
>     }
> }
> ```
>
> **如果想求最长路，且如果恰好能保证没有正权环，可以`dis[i][j] = max(dis[i][j], dis[i][k] + dis[k][j]);`，也可以将所有元素取反**
>
> 
>
> **当然也能做到可及性，从而构建可及矩阵**
>
> **Warshall算法**
>
> ```cpp
> for(int i=1;i<=n;i++)
> 	for(int j=1;j<=n;j++)
> 		reach[i][j] = g[i][j]==INT_MAX?0:1;
> for(int k=1;k<=n;k++)
> 	for(int i=1;i<=n;i++){
> 		if(reach[i][k]==0) continue;
> 		for(int j=1;j<=n;j++){
> 			reach[i][j]|= reach[k][j];
> 		}
> 	}
> ```
>
> 

****

#### 5、满足约束的最短路径

> ###### 简单路径版K 短路：
>
> 集合`vector<Path>Known_Path`存放已知的最短路
>
> 集合`pq<Path>`存探索过的最短路
>
> **1、获取一个最短路**
>
> **2、逐个点遍历（除了终点），设该点为偏离点，在当前路径上，偏离点指出去到偏离点下一个点的那个路径被ban了，之后根据偏离点到终点求一次最短路，求完放到pq里面**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219000752447.png" alt="image-20251219000752447" style="zoom:50%;" />
>
> **3、从pq里取一个最短路，放入`Known_Path`中，之后将这条路径进行逐个点遍历，但注意：如果存在已知路径的前缀与这个路径的前缀相同，则所有已知路径上，这个偏离点到下一个点（所有已知路径上的）的边都被ban掉。之后将获取的路径放入pq中<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219000849069.png" alt="image-20251219000849069" style="zoom:67%;" />**
>
> **4、一直重复步骤3，直到`vector<Path>Known_path`的大小等于K为止**
>
> **5、时空复杂度：**
>
> 求一次最短路`O(nlogn)`，每多个次短路，就需要`n`次求最短路，因此有`O(kn²logn)`的复杂度



> ###### 可有重复点的k短路
>
> **修改dij，允许一个点出队k次，`priority_queue<pair<int,int>>`，记录顶点`v`第`k`次出队时，`dis[v][k]`的大小**



> ###### 满足条件的最短路：
>
> **1、若条件简单，可直接在图上修改来求**
>
> **2、若条件较为复杂，则可以求k短路，求的时候看这条路径是否满足需求**

****

## （十三）最小生成树&图的应用

#### 1、最小支撑树概念

> ###### 支撑树：
>
> 包含 n 个顶点与 n-1 条边构成的连通子图
>
> ###### 最小支撑树：
>
> 边权之和最小的支撑树，应用有设计通信网络、交通网络...
>
> ###### 跨集合边：
>
> 连通集合A与连通集合B中，任取两点连的边
>
> **性质：最小跨边一定在某棵最小支撑树上**：一条边是随意两个集合中的跨集合边，那么一定有最小支撑树包含这条边 <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219093315209.png" alt="image-20251219093315209" style="zoom:50%;" />

****

#### 2、Prim算法

> ###### 步骤：
>
> **1、任选一个点作为起点，放入集合`S`**
>
> **2、一直找集合`S`与集合`V-S`的最小跨边，将对应的点放入集合中**
>
> **3、重复2，直到`V`=`S`**
>
> ###### 运算时使用的数组：
>
> `vector<int> pre`：每个新加的点的父亲，MST中的边就是`{pre[v],v}`
>
> `vector<int> lowcost`：当前情况下，某`S-V`中的点到`V`的最短距离
>
> 更合适稠密图

****

#### 3、Kruskal算法

> ###### 步骤：
>
> **在G中选择权值最小的边，从G将删除。若该边加入T后不产生环，则采纳该边（T的连通分量-1）**
>
> 因此存图只用存边即可，复杂度`O(eloge)`，更适合稀疏图（边少点多）

> **若图中边权各异，其MST一定唯一**：
>
> ​		证明：如果不唯一，那肯定要先成环，成环之后再把原来的点给替换掉，但很明显，如果要成环并替换原来的边，则一定不会更优。
>
> 若**强制一定用某条边**，则可先将这条边加入到边集合中，再跑Kruskal
>
> **最大生成树：**Kruskal，但每次选边权最大的边
>
> **最小乘积支撑树（正权）**：因为乘积在对数呈加法关系，因此正常跑最小生成树即可
>
> **已有MST，此时往G加边，求新MST**：设边为e = (u,v)，则求MST上，u到v路径上的最长边，与`e`相比较即可。

Kruskal还能完成用户聚类，图像颜色分割等功能（类似的边权小）

****

#### 4、SCC强联通分量

> ###### 求法
>
> 1、Warshall求可到达矩阵
>
> 2、遍历每个点，若该点`u`未在任一个SCC内，则新建SCC给他作为代表，之后再遍历所有点，若`r[u][v]==1 && r[v][u]==1`，则两者可在同一个联通分量里面。
>
> 3、因此，每遍历一个点，就能找到一个SCC。

> ###### 缩点
>
> 将SCC缩成一个点，且保持SCC之间的可达性

****

# 排序

## （十四）平方阶排序算法

#### 1、排序概念：

> **文件**：数据对象
>
> **关键词：**属性域中，作为排序的依据
>
> **排序**：按照特定的顺序，以关键词为依据，给文件的记录进行排列的过程
>
> **稳定性：**如果$R_j$与$R_i$的关键词相同，那么排序前后，若他们的相对位置未发生改变，则称这个算法是稳定的。
>
> ###### 分类：
>
> **存储设备角度**：
>
> ​		**内排序**：所有数据元素都在内存中
>
> ​		**外排序**：排序借助外部存储来完成
>
> **关键词操作：**
>
> ​		**基于关键词比较**：基于关键词比较
>
> ​		**分布排序：**基于元素的分布规律
>
> **时间复杂度：**
>
> ​		**平方阶排序**：容易实现，平均时间复杂度`O(n²)`
>
> ​		**线性对数阶**：相对复杂，平均时间复杂度`O(nlogn)`
>
> ​		**线性算法：**不依靠关键词比较，但需要有已知元素的分布规律

****

#### 2、插入排序

**分为已排序区和未排序区：**

**每次从未排序区中找一个元素，插入到已排序区的正确位置 **

```cpp
void InsertSort(vector<int>& a,int n){
   	for(int i=2;i<=n;i++){
        int k = a[i],j = i-1;
        while(j>=1 && a[j]>k){
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = k ;
    }
}
```

```c
运行过程：假如 2 7 9 5，现在处理5

那么k = 5 , j指向9，之后变成2 7 9 9，发现依旧比5大，继续

之后变成2 7 7 9 发现依旧比5大，继续

之后变成2 2 7 9 发现比5小了，那么5就插在2后面
最终：2 5 7 9
```

> **最好时间复杂度：`O(n)`**
>
> **最坏时间复杂度：`O(n²)`**
>
> **平均时间复杂度：`O(n²)`**
>
> **空间复杂度：`O(1)`**
>
> **稳定**

****

#### 3、冒泡排序

**从左到右扫描数组，如果遇到反序对，则交换，如果一次扫描都没遇到则结束 **

改进方法：每次冒泡过程中，如果`t`是最后一次元素交换的位置，则说明`a[t+1]~a[n]`已经排序，因此下次只需排序到位置`t`即可。

```cpp
void BubbleSort(vector<int>& a,int n){
    int bound = n ;
    while(bound>0){
        int t = 0 ;
        for(int i=1;i<bound;i++){
            if(a[i]>a[i+1]){
                swap(a[i],a[i+1]);
                t = i ;
            }
            bound = t;
        }
    }
}
```

>  **最好时间复杂度：`O(n)`**
>
> **最坏时间复杂度：`O(n²)`**
>
> **平均时间复杂度：`O(n²)`**
>
> **空间复杂度：`O(1)`**
>
> **稳定**

#### 4、直接选择排序

**在前`n`个元素中找最大元素，通过交换的方式，放到第`n`位**

**在前`n-1`个元素中找最大元素，通过交换的方式，放到第`n-1`位**

**在前`n-2`个元素中找最大元素，通过交换的方式，放到第`n-2`位**

**.......**

**因为使用的是交换的方式，所以可能会导致稳定性被破坏**

``` cpp
void SelectSort(vector<int>& a,int n){
    for(int i=n;i>=1;i--){
        int maxpos = 1 ;
        for(int j=2;j<=i;j++){
            if(a[j]>a[maxpos]) max = j ;
        }
        swap(a[maxpos],a[i]);
    }
}
```

> **最好时间复杂度：`O(n)`**
>
> **最坏时间复杂度：`O(n²)`**
>
> **平均时间复杂度：`O(n²)`**
>
> **空间复杂度：`O(1)`**
>
> **不稳定**

#### 5、希尔排序

**直接插入排序的升级版**

> **1、把文件按照下标分组**  
>
> 插入排序在“短文件”或者“待排序文件基本有序”的时候速度快，因此可以利用这个特点
>
> **2、分组方法**![image-20251219114334353](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219114334353.png)
>
> ​		**①分为`d`组**
>
> ​		**②每组使用插入排序**
>
> ​		**③把`d`减小，重复执行①②，直到`d`减少到`1` **
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219114535362.png" alt="image-20251219114535362" style="zoom:50%;" />
>
> 两两比较并交换
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219114547995.png" alt="image-20251219114547995" style="zoom:50%;" />
>
> 
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219114556233.png" alt="image-20251219114556233" style="zoom:50%;" />
>
> 五五比较并交换
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219114605462.png" alt="image-20251219114605462" style="zoom:50%;" />
>
> **原理：开始时增量较大，插入速度也快**
>
> **后面增量较小，但大多数都基本有序，因此插入也很快**
>
> ```cpp
> void ShellSort(vector<int>& a,int n){
>     for(int d = n>>1;d>0;d>>=1){
>         //选组
> 		for(int i=d+1;i<=n;i++){
>             int k = a[i],j=i-d;
>             //组内排序
>             while(j>0 && a[j]>k){
>                 a[j+d]=a[j];
>                 j-=d;
>             }
>             a[j+d]=k;
>         }
>     }
> }
> ```
>
> **最坏时间复杂度：`O(n²)`**
>
> **平均时间复杂度：`O(n²)~O(nlogn)`**
>
> **不稳定**

## （十五）线性对数阶排序

#### 1、堆排序

> ###### 锦标赛排序——胜者树
>
> **叶子结点：**放置关键词
>
> **非叶子节点**：放置关键词两两比较后的结果。$fa = max(son1,son2)$
>
> 因此： **第一大数**就在最顶端，取出后，调整一下fa（原来的子节点变成负无穷）
>
> 之后，**第二大数**自然就到最顶端了
>
> 
>
> **构建方法**
>
> **1、用长度为2n-1的数组存树**
>
> **2、把n个元素放在后n个位置**
>
> **3、从下往上推**
>
> **关键词比较复杂度：`O(logn)`**
>
> **总时间复杂度：`O(n+nlogn)`**

> ###### 二叉堆：
>
> **完全二叉树，要求父子满足统一的大于等于/小于等于关系**

> ###### 上浮/下沉:
>
> **结点变大：上浮——一直检查自己的父亲与自己的关系，决定是否交换**
>
> ```cpp
> void shiftup(vector<int>& tree,int i){
>     while(i>1 && tree[i]>tree[i>>1]){
>         swap(tree[i],tree[i>>1]);
>         i>>=1;
>     }
> }
> ```
>
> **结点变小：下沉——一直与自己儿子比较，决定是否交换**
>
> ```cpp
> void shiftdown(vector<int>& tree, int n, int i){
>     while(i <= n/2){
>         int l = i<<1, r = i<<1|1;
>         int maxchd = i;
>         if(l <= n && tree[l] > tree[maxchd]) maxchd = l;
>         if(r <= n && tree[r] > tree[maxchd]) maxchd = r;
>         if(maxchd != i){
>             swap(tree[i], tree[maxchd]);
>             i = maxchd;
>         } else {
>             break;   
>         }
>     }
> }
> 
> ```

> ###### 建堆
>
> **从最后一个非叶子节点开始，依次下沉**
>
> ```cpp
> void BuildHeap(vector<int>& tree,int n){
>     for(int i=n>>1;i>=1;i--){
>         Shiftdown(tree,n,i);
>     }
> }
> ```
>
> **最坏时间复杂度：`O(n)`**(虽然高层的shiftdown可能较多，但高层的也会较少)![
>
> ](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219132255630.png)

> ###### 堆排序
>
> **建成大根堆**
>
> **`tree[1]`肯定最大，`tree[n]`应该较小，因此交换两者（当做`tree[1]`被删除），之后调整堆结构（让`tree[1]`下沉）**
>
> **继续操作，不过`tree[n]`变成了`tree[n-1]`**
>
> .......
>
> ```cpp
> void HeapSort(vector<int>& tree,int n){
>     //建堆
>     for(int i=n/2;i>=1;i--){
>         Shiftdown(tree,n,i);
>     }
>     //排序
>     for(int i=n;i>1;i--){
>         swap(tree[1],tree[i]);
>         Shiftdown(tree,i-1,1);
>     }
> }
> ```
>
> **最好时间复杂度：`O(nlogn)`**
>
> **最坏时间复杂度：`O(nlogn)`**
>
> **平均时间复杂度：`O(nlogn)`**
>
> **空间复杂度：`O(1)`**
>
> **不稳定**

****

#### 2、快速排序

> **思想：随便选择一个数，之后对于别的数，比它大的放左边，比它小的放右边，之后递归处理**![image-20251219142434558](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219142434558.png)
>
> ```cpp
> int Partition(vector<int>& a,int m,int n){
> 	int k = a[m], l = m+1, r = n ;	//a[m]是基准,这里选取了第一个元素为基准
>     while(l<=r){
>         while(l<=n && a[l]<=k) l++;
>         while(a[r]>k) r--;
>         //此时l,r都停在了“不合适”的区域
>         if(l<r){
>             swap(a[l],a[r]);
>             l++,r--;
>         }
>     }
>     //最后 r 会停在l之前。那个是第一个较小的数的位置。
>     swap(a[m],a[r]);
>     return r;
> }
> 
> void QuickSort(vector<int>& a,int m,int n){
>     if(m<n){
>         int k = Partition(R,m,n);
>         QuickSort(R,m,k-1);
>         QuickSort(R,k+1,n);
>     }
> }
> ```
>
> **最好时间复杂度`O(nlogn)`**
>
> **平均时间复杂度`O(nlogn)`**
>
> **空间复杂度`O(logn)`**
>
> **最坏时间复杂度：`O(n²)`**		(选中的数刚好是最大/最小的)
>
> **最坏空间复杂度：`O(n)`**
>
> **不稳定**（排5的时候，如果遇到5，该“扔左边”还是“扔右边”）
>
> 

> **如果需要把正负数/奇偶数分别放到数组两侧**
>
> ```cpp
> void ReArrange(vector<int>& a,int n){
>     int i = 1 , j = n ; 
>     while(i<j){
>         while(i<=n && a[i]该放在左边) i++;
>         while(j>=1 && a[j]该放在右边) j--;
>         if(i<j) swap(a[i],a[j]);
>     }
>     总之就是定位到两者都不合法的位置，但交换之后就合法的位置，之后交换即可 
> }
> ```

> ###### 优化策略：
>
> 1、排序元素比较少时，快速排序可能没有插入排序快，因此可以 **子数组≤16时，采用插入排序**
>
> 2、 **子数组≤16时，退出，最后再统一进行插入排序**
>
> 3、 **基准数**随机选择得到，能降低最坏情况发生的概率
>
> 4、三数取中选基准元素：`R[m]`，`R[(n+m)/2]`，`R[n]`三者的中位数作为基准
>
> 5、尾递归转为循环：递归处理左区间，循环处理右区间，能减少栈空间
>
> ```cpp
> void QuickSort(vectort<int>& a,int m,int n){
>     if(m<n){
>         int k = Partition(R,m,n);
>         QuickSort(R,m,k-1);
>         m = k+1;
>     }
> }
> ```
>
> .....
>
> 6、栈消递归
>
> ```cpp
> void QuickSort(vector<int>& a,int m,int n){
>     Stack<pair<int,int>> s;
>     s.push({m,n});
>     while(!s.empty()){
>         m = s.top().first;
>         n = s.top().second;
>     	int k = Partition(a,m,n);
>         s.push({k+1,n});
>         s.push({m,k-1});
>     }
> }
> ```
>
> 7、递归深度较大时转为堆排序
>
> **8、重复元素较多时，采用三路分化**：较小的放左边，较大的放右边，相等的统一放中间，递归时只对 **不等于k**的进行递归即可
>
> 可用三个指针`i,j,k`，`i`：把他小的元素范围，`j`扫描用，`k`比它大的元素范围，
>
> 若相同：`j++`
>
> 若较小：`swap,i++,j++`
>
> 若较大：`swap,k--`
>
> 算法结束后，`i≤x≤k`的区域都是相同的了

> **2020年期末真题**
>
> 设有一个整数序列$a1, a2,…, an$存放于一个整型数组$A$中，给定两个整数x和y ($y > x$)，请设计一个时间和空间上尽可能高效的算法，重排该序列，使序列中**所有比x小的元素都集中到数组的左侧，所有比y大的元素都集中到数组的右侧，介于x和y之间（含等于x或y）的元素置于数组的中间。**
>
> ```cpp
> void sort(vector<int>& a,int x,int y){
>     n = a.size()-1;
>     int i = 1 , j = 1 , k = n ;
>     while(j<=k){
>         if(a[j]<x){
>             swap(a[i],a[j]);  //因为 i ≤ j ，所以i到j之间的一定是在x到y之间的
>             i++,j++;
>         }else if(a[j]>y){
>             swap(a[j],a[k]);
>             k--;
>         }else{
>             j++;
>         }
>     }
> }
> ```
>
> 

> **快速排序是平均情况下最快的，nlogn的常数更小（1.386），并倾向于访问物理上相邻的数据，cache命中率高**

#### 3、归并排序

**思想：两个有序的数组合成一个大的有序的数组**

> **合成过程**
>
> ```cpp
> void Merge(vector<int>& a,int l,int mid,int r){
>     int i = l , j = mid+1;
>     vector<int>& tmp;
>     while(i<=mid && j<=r){
>         if(a[i]<a[j]) tmp.push_back(a[i++]);
>         else tmp.push_back(a[j++]);
>     }
>     while(i<=mid) tmp.push_back(a[i++]);
>     while(j<=r) tmp.push_back(a[j++]);
>     
>     for(int k=l;k<=r;k++){
>         a[k] = tmp[k-l];
>     }
> }
> ```
>
> **递归合并**
>
> ```cpp
> void MergeSort(vector<int>& a,int l,int r){
>     if(l>=r) return;
>     int mid = (l+r)>>1;
>     //先让小的有序
>     MergeSort(a,l,mid);
>     MergeSort(a,mid+1,r);
>     //再把两个有序的合并
>     Merge(a,l,mid,r);
> }
> ```
>
> **时间复杂度：`O(nlogn)`**
>
> **空间复杂度：`O(n)`**

****

> **非递归合并**
>
> ```cpp
> void MergeSort(vector<int>& a,int n){
>     //确定组长度（从小到大）
>     for(int d=1;d<n;d<<=1){
>         int i ;
>         //所有组内进行合并
>         for(i=1;i+2*d-1<=n;i+=2*d)
>             Merge(a,i,i+d-1;i+2*d-1);
>         //多余的，不能被整除的部分
>         if(i+d-1<n)
>             Merge(a,i,i+d-1,n);
>     }
> }
> ```
>
> **最好时间复杂度：`O(nlogn)`**
>
> **最坏时间复杂度：`O(nlogn)`**
>
> **平均时间复杂度：`O(nlogn)`**
>
> **空间复杂度：`O(n)`**
>
> **稳定**
>
> **最快的稳定排序算法**

****

> **优化策略：**
>
> 数据量较小时，无需采用分治，可直接插入排序
>
> 数组赋值可改为链表指针移动
>
> **21级期末真题**
>
> 给定一个包含哨位结点的单链表，请设计一个时空效率尽可能高效的算法，对该链表进行递增排序，n为链表长度。

****

> **逆序对计算**
>
> 归并的时候，$cnt+=mid-i+1$
>
> ```cpp
> void Merge(vector<int>& a,int l,int mid,int r){
>     int i = l , j = mid+1;
>     vector<int>& tmp;
>     while(i<=mid && j<=r){
>         if(a[i]<a[j]) tmp.push_back(a[i++]);
>         else{
>             ans+=mid-i+1;
>             tmp[k++]=record[j++];			//←这里
>         }
>     }
>     while(i<=mid) tmp.push_back(a[i++]);
>     while(j<=r) tmp.push_back(a[j++]);
>     
>     for(int k=l;k<=r;k++){
>         a[k] = tmp[k-l];
>     }
> }
> ```
>
> 

**基于分治的排序算法**

​		**快速排序：侧重在“分”**

​		**归并排序：侧重在“合”**

| 排序算法     | 最好复杂度 | 平均复杂度 | 最坏复杂度 | 空间复杂度  | 稳定性     |
| ------------ | ---------- | ---------- | ---------- | ----------- | ---------- |
| 直接插入     | `O(n)`     | `O(n²)`    | `O(n²)`    | `O(1)`      | **稳定**   |
| 冒泡排序     | `O(n)`     | `O(n²)`    | `O(n²)`    | `O(1)`      | **稳定**   |
| 直接插入排序 | `O(n²)`    | `O(n²)`    | `O(n²)`    | `O(1)`      | **不稳定** |
| 堆排序       | `O(nlogn)` | `O(nlogn)` | `O(nlogn)` | `O(1)`      | **不稳定** |
| 快速排序     | `O(nlogn)` | `O(nlogn)` | `O(n²)`    | `O(logn~n)` | **不稳定** |
| 归并排序     | `O(nlogn)` | `O(nlogn)` | `O(nlogn)` | `O(n)`      | **稳定**   |

**当需要比较多个元素时，比如需要满足条件1之后，再对相同的内容进行条件2的排序，那这时候就需要有 ==稳定性==了**



#### 4、时间下界

三个元素的排序判定树，高度是排序算法在最坏情况下关键词的比较次数。有：**高度为h的二叉树最多有$2^h$个叶子节点，n个元素的排列组合有$n!$种，因此$log(n!)＝Ω(nlogn)$**因此，基于比较的排序算法平均时间复杂度的下限是$Ω(nlogn)$

## （十六）分布排序

#### 1、桶排序

**对于所有已知元素，设置多个桶（队列结构），将元素依次放入桶中并依次取出**

**$O(n+m)$，稳定<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219182236890.png" alt="image-20251219182236890" style="zoom:50%;" />**

#### 2、计数排序

**用`cnt`数组记录每个元素出现的个数，之后求前缀和。那么`sum[i]`就反映了元素`i`的排名了,但因为知道的是最后一个的排名，因此从右到左倒着放即可。**

```cpp
for(int i=1;i<=n;i++) cnt[a[i]]++;
for(int i=1;i<m;i++) cnt[i]+=cnt[i-1];
for(int i=n;i>=1;i--) B[cnt[a[i]]--] = a[i];
```

`O(m+n)`，**稳定**（因为靠后的元素编码较大，倒着放入的时候也会优先放入）

#### 3、基数排序

**元素关键词由多个域组成，即$K_d$，$K_{d-1}$，...，$K_2$，$K_1$，从$K_1$到$K_d$依次进行稳定排序。**

**因此，若都为数据，则可以每次都使用0~9的计数排序，先按个位排序，再按十位排序...**

```cpp
void RadixSort(vector<int>& a,int n,int d,int r){//每个元素有d位，每位有r个元素
    vector<int> b(n+1),cnt(r),K(n+1);
    for(int k=1,base=1;k<=d;k++,base*=r){//对第k位进行排序
    	for(int i=0;i<r;i++) cnt[i] = 0 ;
        for(int i=1;i<=n;i++) K[i] = (a[i]/base)%r;
        for(int i=1;i<=n;i++) cnt[K[i]]++;
        for(int i=1;i<r;i++) cnt[i] += cnt[i-1];
        for(int i=n;i>=1;i--) b[cnt[K[i]]--] = a[i];
        for(int i=1;i<=n;i++) a[i] = b[i];
    }
}
```

**$O(d(n+r))$稳定**

| 排序算法 | 最好复杂度  | 平均复杂度  | 最坏复杂度  | 空间复杂度 | 稳定性 |
| -------- | ----------- | ----------- | ----------- | ---------- | ------ |
| 桶排序   | $O(n+m)$    | $O(n+m)$    | $O(n+m)$    | $O(n+m)$   | 稳定   |
| 计数排序 | $O(n+m)$    | $O(n+m)$    | $O(n+m)$    | $O(n+m)$   | 稳定   |
| 基数排序 | $O(d(n+r))$ | $O(d(n+r))$ | $O(d(n+r))$ | $O(n+r)$   | 稳定   |

**假如从0~999排序**

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219194034157.png" alt="image-20251219194034157" style="zoom:67%;" />

## （十七）线性结构查找

#### 1、顺序查找

**遍历，逐个找**

#### 2、对半查找

**二分查找，对于有序的序列有效。**

```cpp
int BinarySearch(vector<int>& a,int n,int k){
    int l = 1 , r = n , mid ;
    while(l<=r){
        mid = (l+r)>>1;
        if(k<a[mid]) r = mid - 1 ;
        else if(k>a[mid]) l = mid + 1 ;
        else return mid ;
    }
    return -1 ;
}
```

**可用于插入排序加速，但因为元素移动也是`O(n)`，不过能降低常数**

> ###### 二叉判定树：
>
> **本质：扩充查找树，注意：结点值是数组下标，也就是比较的位置**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219211556832.png" alt="image-20251219211556832" style="zoom: 50%;" />
>
> 第一层：$(1+10)/2=5$
>
> 第二层：$(1+4)/2 = 2$，$(6+10)/2 = 8 $。注意上下界...
>
> 成功查找 → 内节点 。深度越高，比较次数越多。
>
> 查找失败 → 查找到外结点，深度也是内节点数。
>
> **ASL**
>
> 查找成功的平均查找长度：$内节点选中概率*depth$，【这里深度从1开始计算】
>
> 例如上图就是$(1*1+2*2+4*3+3*4)/10$，10来源于一共有10个点，中间的是每层有多少个节点*这层的深度。
>
> 查找失败的平均查找长度长度：$∑外节点层数*该层外节点个数/外节点个数$，【这里深度从0开始计算，更准确地说，其实不是外节点层数，而是外节点所属的内节点的层数】
>
> 例如上图$ASL_{unsucc}=\frac{1}{2}*(5*3+6*4)=3.5$ （第三层伸出来五个节点，第四层伸出来六个节点）
>
> **顺序查找的二叉查找树**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219212638072.png" alt="image-20251219212638072" style="zoom:67%;" />
>
> 

#### 3、斐波那契查找

> **本质：黄金分割点处进行划分**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219213258184.png" alt="image-20251219213258184" style="zoom:67%;" />
>
> 假设数组元素个数为$F_k-1$，则第一次查找的位置是$F_{k-1}$，此时数组被分为了三部分，分别是中间$F_{k-1}$，左侧共$F_{k-1}-1$个数，右侧共$F_{k-2}-1$个数。

> **mid计算**
>
> ```cpp
> 	int mid = l + F[k-1] - 1 ;
> ```
>
> **左侧计算**
>
> ```cpp
> r = mid - 1 ;
> k --;
> ```
>
> **右侧计算**
>
> ```cpp
> l = mid + 1 ;
> k -= 2 ;
> ```

> 
>
> ```cpp
> int FibSearch(vector<int>& a,int n,int aim,const vector<int>& Fib,int k){
>         int l = 1 ,r = n ;
>         while(l<=r){
>             //mid 用的Fib
>             int mid = l+Fib[k-1]-1;
>                //左侧降一阶
>             if(aim<a[mid]){
>                 r = mid - 1 ;
>                 k-- ;
>             }
>             //右侧降两阶
>             else if(aim>a[mid]){
>                 l = mid + 1 ;
>                 k -= 2; 
>             }
>             else return mid ;
>         }
>         return -1 ;
> }
> ```
>
> 复杂度$O(log_2n)$，时间略快于对半查找，算法不涉及乘除法。
>
> 左区间更长，因此转向右区间的比较次数就会减少了（k-=2)

#### 4、插值查找

**若R中元素均匀分布，迭代时，通过线性插值预测K的期望位置mid**

> **mid计算**
>
> ```cpp
> 	int mid = l + (mid-a[l]) * (l-r) / a[l] - a[r] ;
> ```
>
> **左侧计算**
>
> ```cpp
> r = mid - 1 ;
> ```
>
> **右侧计算**
>
> ```cpp
> l = mid + 1 ;
> ```

```cpp
int InterpolationSearch(vector<int>& a,int n,int aim){
    int l = 1  ,r = n ,mid ;
    //之所以这样判定，是因为不满足这个判定的都属于“没找到”的情况
   	while(l<=r && aim>=a[l] && aim<=a[r]){
        if(a[l]==a[r]) return l ;
        mid = l + (aim-a[l])*(l-r)/(a[r]-a[l]);
        if(aim<a[mid]) r = mid-1;
        else if(aim>a[mid]) l = mid+1;
        else return mid;
    }
    return -1 ;
}
```

**平均时间复杂度$O(loglogn)$**

**最坏时间复杂度**$O(n)$

**引入乘除法运算，元素分布需均匀**

**实际中，可以通过插值法快速缩小查找范围，之后再进行对半/顺序查找**

#### 5、分块查找

**将大数组分成多块，需要块`i`中所有元素比块`j`小（但块内无要求）。**

**通过对半查找找到关键词所属块，随后在块内顺序查找 **

# 	复杂结构

## （十八）二叉查找树

> 二叉树，结点**关键字各异**，**中根序列按照关键词递增排序**，结点P的**左儿子一定小于P，右儿子一定大于P。** 

**结构：**

```cpp
struct BST{
	int key;
	BST* left;
	BST* right;
	BST(int k){key = k;left=right=NULL;}
};
```

> **由n个节点组成的二叉查找树个数** 假如选择k为根结点（k种可能），则有k-1种左子树的选法，有n-k种右子树的选法...一直递推下去。因此有$T(n) = C_n = \frac{1}{n+1}\binom{2n}{n}$

#### 核心操作：

###### 1、查找

> 在二叉树中查找关键词为`K`的节点
>

```cpp
    TreeNode* searchBST(TreeNode* root, int val) {
        TreeNode* p = root;
        while(p){
            if(val<p->val) p = p->left;
            else if(val>p->val) p = p->right;
            else return p;
        }
        return NULL;
    }
```

###### 2、插入

> 将关键词为`K`的节点插入二叉查找树，插入后仍为二叉查找树，若`K`已在树上，则不插入。
>
> **步骤1**：查找`K`
>
> **步骤2**：在查找失败处插入`K`

```cpp
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* p = root;
        while(p){
            if(val>p->val){					//尝试去左侧看
                if(p->right) p = p->right;
                else{						//若不存在，则补上
                    TreeNode* q = new TreeNode(val);
                    p->right = q;
                    return root;
                }
            }else if(val<p->val){			//尝试去右侧看
                if(p->left) p = p->left;
                else{						//若不存在，则补上
                    TreeNode* q = new TreeNode(val);
                    p->left = q;
                    return root;
                }
            }else return root;
        }
        return root = new TreeNode(val);
    }
```

###### 3、删除



> 删除关键词为`K`的节点，删除后仍为二叉查找树
>
> ​	若`K`无孩子：直接删除
>
> ​	若`K`只有一个孩子：让子节点替换`K`
>
> ​	若`K`有两个孩子： 找右子树中最小的节点（能保证有少于一个孩子）来代替`K`
>

```cpp
void remove(BST*& root , int k){
	BST** cur = &root;		//这里的cur一直都是删除节点的父亲的左/右指针
    while(*cur && (*cur)->val!=k){
        if(k>(*cur)->val) cur = &(*cur)->right;
        else cur = &(*cur)->left;
    }
    if(!*cur) return;
    BST* node = *cur;		//node才是需要删除的节点
    //如果有两个儿子,则在右子树处找最小节点（肯定在最左侧）
    if(node->left && node->right){
        BST** minpoint = &(node->right);
        while((*minpoint)->left)
            minpoint = &((*minpoint)->left);
        //现在minpoint是minpoint父亲的左节点
        //minp是minpoint的真实节点
        BST* minp = *minpoint;
        *minpoint = minp->right;		//继承最小值的右子树
        minp->left = node->left;		//接下来三步让最小值代替删除值
        minp->right = node->right;
        *cur = minp						
    }else{							//只有0到1个儿子
        *cur = node->left ? node->left:node->right;
    }
    delete node ;
    return;
}
```

## （十九）高度平衡树

> AVL树是一颗满足：**任意节点的左子树和右子树高度相差≤1**的二叉查找树。
>
> 任意节点p的**平衡系数**：p的**左子树高度-右子树高度**
>
> **高度**：logn
>
> **插入、删除、查找时间复杂度**：`O(logn)`
>
> **每次删除均摊旋转**：`O(1)`
>
> **最坏插入删除旋转复杂度**:`O(logn)`



**实现**

```cpp
struct AVL{
	int val ;
	int height ;
	AVL* left,*right;
	AVL(int k){key = k; height = 0; left = right = NULL;}
};

int Height(AVL* node){
	return (node==NULL)?-1:node->height;
}
void UpdateHeight(AVL* node){
	node->height = max(Height(t->left),Height(t->right))+1;
}
```

#### 核心操作：

**掌握程度：需要知道操作，无需知道代码**

###### 1、查找

与二叉查找树一致

###### 2、旋转

**LL旋转：左子树的左子树高度超高了->不改变无关节点相关位置，但让B做父亲**

> 【A↔B】（让B做父亲） 【右转】
>
> 调整AB位置，使得B为父亲且插入的子树与B相连

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251214124739805.png" alt="image-20251214124739805"  />

```cpp
void LL(AVL*& A){
    AVL* B = A->left;
    A->left = B->right;
    B->right = A:
    UpdateH(A);
    UpdateH(B);
    A = B;
}
```

**RR旋转：**

> 【A↔B】（让B做父亲）【左转】
>
> 调整AB位置，使得B为父亲且插入的子树与B相连

![image-20251214125716363](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251214125716363.png)

```cpp
void RR(AVL*& A){
	AVL* B = A->right;
	A->right = B->left;
	B->left = A;
	UpdateH(A);
	UpdateH(B);
}
```

**LR旋转：A的左子树的右子树超高了**

> 【B↔C，A↔C】（一步步让C做父亲） 【先左转再右转】
>
> 调整ABC位置，使得C做父亲，AB为其儿子，并调整所拥有的子树（不改变其相对位置）

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251214130549405.png" alt="image-20251214130549405" style="zoom:80%;" />

**RL旋转：A的右子树的左子树超高了**

> 【B↔C】【A↔C】（一步步让C做父亲）【先左转再右转】
>
> 调整ABC位置，使得C做父亲，AB为其儿子，并调整其拥有的子树（不改变其相对位置）

<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251214130529352.png" alt="image-20251214130529352" style="zoom:80%;" />

###### 3、插入

> 查看插入节点后是否失衡，应调整失衡的最小子树，也就是**最靠下的失衡节点。**
>
> 【向下递归找插入点，向上回溯找第一个非平衡节点】
>
> 旋转后，**平衡系数为0，子树高度与原来相同**

```cpp
void Insert(AVL*& root , int k){
	if(!root) root = new AVL(k);
	else if(k<root->key)   insert(root->left,k);
	else if(k>root->key)   insert(root->right,k);
	ReBalance(root);
}

void ReBalance(AVL*& root){
	if(!root) return;
	if(Height(root->left)-H(root->right)==2){
		if(Height(root->left->left)>=Height(root->left->right)){
			LL(root);
		}else{
         	 LR(root);
         }
	}else if(Height(root->right)-Height(root->left)==2){
        if(Height(root->right->right)>=Height(root->right->left)){
            RR(root);
        }else{
            RL(root);
        }
    }
    UpdateH(root);
}
```

## （二十）多叉查找树

#### 1、B树

> ###### 目标：
>
> 查找树的 **节点可能会存储到外存**，此时指针域就要拓宽到外部了，此时就要尽可能减少 **外存访问次数**， 也就是 **查找树高度**。因此我们需要尽可能降低 **查找树高度**

> ###### 结构：
>
> **孩子 = 关键词 + 1 **
>
> **孩子最多为m** 
>
> ```cpp
> struct Node{
>     vector<int> KeyWords ; //有 j 个关键词，从1 ~ j
>     vector<int> Nodes ; //有j+1个指针，从0 ~ j
> };
> ```
>
> ###### m阶B树：
>
> **1、每个节点最多有$m$个孩子**
>
> **2、除了根节点外，每个节点有$\lceil\frac{m}{2}\rceil 到 m$个孩子**
>
> **3、若根节点不是叶节点，则有$2 到 m$个孩子（根可以较少）**
>
> **4、有$k$个孩子的节点刚好包含$k-1$个递增有序的关键词**
>
> **5、所有的叶节点都在同一层且不包含任何信息**
>
> **假如7阶B树，则关键词数量最多只能有6个，能有7个区间，最少只能有3个，能有4个区间**
>
> ![image-20251219221050933](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219221050933.png)
>
> **指向叶子结点的指针其实是空指针**

> ###### 查找：
>
> **1、若在该节点的关键词中找到K（可用对半查找），则查找成功**
>
> **2、若没找到K，则确认关键词在$K_i$到$K_{i+1}$之间，那么就在指针$p_i$处继续查找K，如果$p_i$为空，则查找失败**

> ###### 插入：
>
> **1、先查找，在查找失败时插入**
>
> **2、若插入后，关键词个数$≤m$，则直接插入，并添加叶子指针**
>
> ![image-20251219221853828](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219221853828.png)
>
> **3、若插入后，节点包含关键词超过$m-1$个，则进行分裂，关键词$K_{\lceil\frac{m}{2}\rceil}$提升到上一层节点中（二分裂），之后下面分裂成两个**![image-20251219221928291](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219221928291.png)
>
> **从而让上一层的节点变多...直到根节点（冷知识：根节点也能分裂，分裂出一个新的根节点）**
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219222518280.png" alt="image-20251219222518280" style="zoom: 50%;" />
>
> <img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219222530684.png" alt="image-20251219222530684" style="zoom: 50%;" />

> ###### 删除：
>
> **1、查找要删除的关键词K**
>
> **2、若K不在最底层，则需要将K下放到最底层之后再进行删除（下放时，需要做的是将其与其右子树的最小的节点（也就是进入右侧子树之后一直向左找），这是一次交换过程，而不是多轮交换往下放，而是一下子直接和最小节点直接换）![image-20251219222743959](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219222743959.png)**
>
> **3、下溢：关键词数少于$\lceil\frac{m}{2}\rceil-1$个，此时需要向左右兄弟借节点。（优先往左侧借），当然如果直接借，就会打破父节点的大小关系，因此我们需要通过父节点中转，此时子树也会一起被借过来**![image-20251219223052532](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219223052532.png)
>
> **4、下溢·合并：如果兄弟节点关键词数等于$\lceil\frac{m}{2}\rceil-1$个，因为这俩节点加起来不会超，因此可以进行合并，照样是优先往左找（下放父亲），总共$\lceil\frac{m}{2}\rceil-1(左侧)+\lceil\frac{m}{2}\rceil-2(右侧)+1(父亲)=\lceil\frac{m}{2}\rceil*2-2$个关键词（若m=7，则共有6个关键词，若m=8，则有6个关键词，均合法）**
>
> **5、冷知识：根也能合并**<img src="C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219223738314.png" alt="image-20251219223738314" style="zoom:50%;" />![image-20251219223743724](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219223743724.png)

> ###### **B树高度**
>
> 总之就是$O(log_mn)$
>
> ###### **m多大合适**
>
> 一般$m$采用$200$~$300$，若$n=2*10^{10}$，`k`最多是5，最坏情况下，依次查找要5次外存访存。如果是二叉树，则要35次，很明显能减少很多访存时间
>
> ###### **分裂频率**
>
> 每插入$\lceil\frac{m}{2}\rceil-1$个关键词就分裂一次。（根节点只包含一个关键词，其他节点都要满了的时候）

#### 2、B+树

![](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219231540572.png)

![image-20251219231603376](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219231603376.png)

## （二十一）散列 Hash

#### 1、散列定义

**直接根据关键词定位到该元素的存储地址**

> ###### 散列函数 $h('a')=1$
>
> **自变量K：关键词**
>
> **函数值h(K)：元素在散列表中的存储地址**
>
> **作用：将关键词值映射到地址中**
>
> 但存在冲突——同一个关键词，但指向的是不同的内容

#### 2、散列函数

> ###### $h(Key)=Adress$ $of$ $Hash$ $Table$
>
> ###### **选取原则：**
>
> ​		1、便于快速计算
>
> ​		2、极少出现冲突，散列函数值尽可能不同
>
> ​		也就是：函数值域在散列表长以内，且在各位置的概率尽可能相等。
>
> ###### **除法取余法：**
>
> ​		**$h(k)=K \% M$**
>
> ​		1、理想的随机序列：M无所谓
>
> ​		2、类似a+d，a+2d，a+3d的序列，应尽可能让$GCD(d,M)=1$
>
> ###### **MAD法**
>
> ​	$h(k)=(a*K+b)\%M$
>
> ​	其中M为质数，且$a>1,b>0,M不整除a$
>
> ###### **乘法散列函数**
>
> ###### **$h(K)=\lfloor M(kθ mod1)\rfloor$，其中mod1指取小数部分，M为表长，θ一般为黄金分割点** 
>
> ###### **平方取中法**
>
> 取一个数的平方值的中间的若干位
>
> ![image-20251219233217277](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219233217277.png)
>
> ###### **压缩法**
>
> **将关键词/其二进制串分割为等宽的子串，并按照某种方式合并**
>
> ![image-20251219233302708](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219233302708.png)
>
> ###### **抽取 / 数学分析法**
>
> ![image-20251219233352073](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219233352073.png)

#### 3、冲突处理方法

> ##### （1）开散列法——拉链法
>
> **本质：用链表来存储相同的hash值**
>
> ![image-20251219233432975](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219233432975.png)

> ##### （2）闭散列法

> ###### 【1】线性探查
>
> **思想**：当发生冲突时，以**固定的次序**查找表中的记录，直到找到一个关键词为K的结点或者**找到一个空位置**，路径是**取模+1**
>
> ​		因检查相邻元素，cache命中率高
>
> **装填因子：**填入表中元素个数 / 散列表长度。一般为0.5~0.8最佳
>
> ****
>
> ###### ASL
>
> **成功平均查找长度：**
>
> （查找成功：查找的元素在表中）
>
> ​		一查就查到：1
>
> ​		**需要往后找，最终为包括首尾点的距离**
>
> ![image-20251219234150754](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219234150754.png)
>
> $ASL_{成功}=\frac{1+1+1+1+3+1+1+3}{8}$
>
> （因为只有8种会成功的元素）
>
> ****
>
> **失败查找长度**
>
> 一直查直到**查到空** / 查完**所有元素**为止
>
> ![image-20251219234801532](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219234801532.png)
>
> $ASL_{失败}=\frac{6+5+4+3+2+1+4+3+2+1}{10}$
>
> （因为有10种可能的输入，与有效内容有关，与HT长度无关）

> ###### 【2】二次探查
>
> **探查公式：**$h_i=(h(K)±i^2)\%M$，其中$i$从1到$(M-1)/2$
>
> ​	比如 $x=h(K)$，则为**$x,x+1^2,x-1^2,x+2^2,x-2^2...$**
>
> ​	能有效避免**冲突聚集**
>
> 

> ###### 【3】双重探查
>
> 寻找空地址时，走的**步长与K相关**
>
> ![image-20251219235826903](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219235826903.png)
>
> ![image-20251219235849985](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251219235849985.png)
>
> 

#### 4、删除某点

> ###### **拉链法：**
>
> 链表的删除
>
> ###### **闭散列法**：
>
> 元素因为可能存在冲突，因此不能直接删掉，不然查的时候会发生问题。
>
> ###### **懒惰删除**——将这个节点标记为“已删除
>
> 查找：跳过“已删除“
>
> 插入：可插入到“已删除”
>
> 缺点：探查所需的探查次数较多
>
> ###### **实时删除**——
>
> 本质：当删除的节点在查找路径上时，才会产生影响，因此在删除之后，考察位置`j+1`到下一个空位之前的每一个位置`i`，看是否有影响`T[i]`的探查路径。若影响了，则将`T[i]`往前移动到空位上
>
> 路径阻断有两种情况：`a->删->b`和`...->b a->删->...`
>
> ```cpp
> void hashRemove(vector<int>& T,int j){
>     T[j] = 空 ;
>     for(int i=j+1;T[i]!=空;i=(i+1)%M){
>         r = h(T[i]);
>         if(路径被阻断){
>             T[j] = T[i];
>             T[i] = 空;
>             j = i ;
>         }
>     }
> }
> ```
>
> 最坏时间复杂度：$O(n)$
>
> 但当装填因子≤2/3时，平均时间复杂度为$O(1)$
>
> ###### **延迟删除——**
>
> 平时Lazy删除，每一段时间执行真正删除，同时保存每个元素访问次数，按照访问次数重新插入散列表。

#### 5、性能分析

![image-20251220003055131](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251220003055131.png)

![image-20251220003118364](C:\Users\long1\AppData\Roaming\Typora\typora-user-images\image-20251220003118364.png)

**散列表VS线性表/树形查找**

平均情况，散列表更快

最坏情况，时间可到O(n)

散列表占的空间大（要用控制装载因子，用空间换时间）

散列表查找失败后，只能知道不在表内，不能知道upperbound什么的。

散列表不能维护数据有序信息。

## （二十二）堆与优先队列

#### 1、堆的插入与删除

> ###### 插入到堆：
>
> 插入到**堆尾**，再进行**上浮操作**，堆中元素个数++；
>
> ```cpp
> void Insert(vector<int>& a,int& n,int x){
>     a[++n] = x ;
>     Shiftup(a,n,n);
> }
> ```
>
> **时间复杂度：**$O(logn)$

> ###### 删除堆顶：
>
> **把堆顶与堆尾进行交换**，再进行 **下沉**操作
>
> ```cpp
> int DelMax(vector<int>& a,int &n){
>     int MaxKey = a[1] ;
>     a[1] = R[n--] ;
>     ShiftDown(R,n,1);
>     return MaxKey;
> }
> ```
>
> **时间复杂度：**$O(logn)$

#### 2、优先队列

> ###### 优先队列：
>
> ```cpp
> const int maxn=1e5+10;
> Template<class T>
> class MinPQ{
> public:
>     void Insert(int v, T key);
>     int DelMin();
>     bool Empty();
> ……
> private:
>     void ShiftUp(int i);
>     void ShiftDown(int i); 
>     int R[maxn]; //存堆元素
>     T dist[maxn]; //存关键词
>     int n; //堆的元素个数
> ……
> };
> ```



> ###### 优先队列优化Huffman算法
>
> ```cpp
> for (int i=0; i<n-1; i++){
>     HuffmanNode *t = new HuffmanNode; 
>     t->left = pq.DelMin(); //取出权值最小的结点
>     t->right= pq.DelMin(); //取出权值最小的结点
>     t->weight = t->left->weight + t->right->weight;
>     pq.Insert(t); //新创建的结点插入堆
> }
> ```

> ###### 堆优化的Dijkstra算法
>
> ```cpp
> void Dijkstra(Vertex* head,int n, int start,vector<int>& dis){
>    	vector<int> vis(N);
>     priority_queue<pair<int,int>> pq ;
>     for(int i=1;i<=n;i++) dis[i] = (i==start)?0:INT_MAX;
>     pq.insert(start);
>     while(!q.empty()){
>         int u = pq.top();pq.pop();
>         vis[u] = 1 ;
>         for(Edge* p = Head[u].adjacent;p;p=p->link){
>             int w = p->cost;
>             int v = p->VerAdj;
>             if(!vis[v] && dis[u]+w<dis[v]){
>                 dis[v] = dis[u] + w ;
>                 pq.push({dis[v],v})  //这一步如果是自己实现的堆的话，可以使用Decrease(v,dis[v])
>                     	//也就是手动修改顶点v的值，减少为dis[v]，并使其上浮。
>             }
>         }
>     }
> }
> ```
>
> 斐波那契堆可以将堆的插入与元素修改复杂度优化为$O(1)$

> ###### TOP K 问题
>
> 选择数组中最大的$k$个元素
>
> 可以通过建立由`k`个元素的小根堆（前k个元素），之后依次扫描剩余元素，如果这个元素x大于堆顶，则用x替换堆顶，并执行下沉操作。这样就能保证堆内的元素总是最大的k个元素了，且复杂度会降低到`O(nlogk)`



# 三、无关紧要的小算法

## （一）单链表

#### 1、链表操作：

1.查找

​		找第k个节点，找值为k的节点，找某个节点的前驱

2.插入

​		在p右侧 【new s，s->next = p->next，p->next = s】

3.创建

​		头查法：【new s, s->next = head->next，head->next =s】

4.删除

​		删除p的后继节点【q = p->next，p->next = q->next，delete q】

​		删除p【后继赋给p，之后p->next跳过后继即可】

循环链表操作：

包含哨兵节点，末尾元素总是指向哨兵节点。【last->next = head】

双向链表操作：

删除节点s【s->prev->next = s->next，s->next->prev = s->prev，delete s】

#### 2、链表双指针法：

1、找倒数第k个节点（一个指针先走k次）

2、找中间节点（快慢指针法）

3、反转单链表【换头法：带着原来的头走到最后，遇到一个新的节点就把他扔到头那里】

```cpp
    ListNode* reverseList(ListNode* head) {
        if(head==NULL) return head;
        ListNode* p = head , *q = head->next;
        while(q){
            p->next = q->next;
            q->next = head;
            head = q;
            q=p->next;
        }
        return head;
    }
```

4、链表交叉问题【双指针轮流跑】

5、单链表判环问题【快慢指针相交】

```cpp
    bool hasCycle(ListNode *head) {
        ListNode* fast = head ,*slow = head ;
        while(fast && fast->next && fast!=slow){
            fast = fast->next->next;
            slow = slow->next;        
            if(fast==slow) return true;
        }
        return false;
    }
```

6、判断单链表是否回文

```cpp
    bool isPalindrome(ListNode* head) {
        ListNode* fast = head,*slow = head;
        while(fast && fast->next){
            fast = fast->next->next;
            slow = slow->next;
        }
        fast = slow;
        ListNode* mid = fast;
        fast = fast->next;
        while(fast){
            slow->next = fast->next;
            fast->next = mid;
            mid = fast;
            fast = slow->next;
        }
        slow = head;
        fast = mid;
        while(fast){
            if(fast->val!=slow->val){
                return false;
            }
            fast = fast->next;
            slow = slow->next;
        }
        return true;
    }
```

7、重排链表结点

```cpp
    void reorderList(ListNode* head) {
        if (head == nullptr) {
            return;
        }
        ListNode* mid = middleNode(head);
        ListNode* l1 = head;
        ListNode* l2 = mid->next;
        mid->next = nullptr;
        l2 = reverseList(l2);
        mergeList(l1, l2);
    }

    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while (fast->next != nullptr && fast->next->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }

    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        while (curr != nullptr) {
            ListNode* nextTemp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = nextTemp;
        }
        return prev;
    }

    void mergeList(ListNode* l1, ListNode* l2) {
        ListNode* l1_tmp;
        ListNode* l2_tmp;
        while (l1 != nullptr && l2 != nullptr) {
            l1_tmp = l1->next;
            l2_tmp = l2->next;

            l1->next = l2;
            l1 = l1_tmp;

            l2->next = l1;
            l2 = l2_tmp;
        }
    }
```

