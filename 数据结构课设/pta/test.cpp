#include<iostream>
#include<stdlib.h>
#include<math.h>
using namespace std;

struct AVLnode{
    int key; //关键词
    int height; //以该结点为根的子树高度
    AVLnode *left, *right;
    AVLnode(int K){ key=K; height=0; left=right=NULL; }
};

int Height(AVLnode *t){ return(t==NULL)?-1:t->height; }
int max(int a, int b){ return (a>b)? a:b; }

void UpdateHeight(AVLnode *t){
t->height = max(Height(t->left),Height(t->right))+1;
}

void LL(AVLnode* &A)
{
    AVLnode *B = A->left;
    A->left = B->right;
    B->right = A;
    UpdateHeight(A);
    UpdateHeight(B);
    A = B;
}

void RR(AVLnode* &A)
{
    AVLnode *B = A->right;
    A->right = B->left;
    B->left = A;
    UpdateHeight(A);
    UpdateHeight(B);
    A = B;
}

void LR(AVLnode* &A){
    RR(A->left);
    LL(A);
}

void RL(AVLnode* &A){
    LL(A->right);
    RR(A);
}

void ReBalance(AVLnode* &t)
{
    if(t==NULL)
        return;
    if(Height(t->left) - Height(t->right)==2)
    {
        if(Height(t->left->left) >= Height(t->left->right))
            LL(t);
        else
            LR(t);
    }
    else if(Height(t->right) - Height(t->left)==2)
    {
        if(Height(t->right->right) >= Height(t->right->left))
            RR(t);
        else
            RL(t);
    }
    UpdateHeight(t);
}

void remove(AVLnode* &root, int K)
{
    if(root==NULL) 
        return;
    if(K<root->key) 
        remove(root->left, K); //在左子树删K
    else if(K>root->key)
        remove(root->right, K); //在右子树删K
    else if(root->left!=NULL && root->right!=NULL)
    {
        AVLnode *s=root->right;
        while(s->left!=NULL)
            s=s->left;
        root->key=s->key; //s为t右子树中根序列第一个结点
        remove(root->right, s->key);
    }
    else
    {
        AVLnode* oldroot=root;
        root=(root->left!=NULL)? root->left:root->right;
        delete oldroot;
    }
    ReBalance(root);
}

void Insert(AVLnode* &root, int K)
{
    if(root==nullptr) 
        root=new AVLnode(K);
    else if(K < root->key) //在左子树插入
        Insert(root->left, K);
    else if(K > root->key) //在右子树插入
        Insert(root->right, K);
    ReBalance(root);
}