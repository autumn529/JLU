#include<iostream>
#include<stack>
#include<string>
using namespace std;

//数组实现
#define size 100000
int num[size];

int top=-1;

void push(int x){
    num[++top]=x;
}

int pop(){
    return num[top--];
}

int peek(){
    return num[top];
}

void clear(){
    top=-1;
}

bool isEmpty(){
    return top==-1;
}


//链表实现
struct node{
    node* next;
    int val;
};


node* head=nullptr;

void push(int x){
    node* temp=new node;
    temp->val=x;
    temp->next=head;
    head=temp;
}

void pop2(){
    node* temp=head;
    head=head->next;
    delete temp;
}

node* peek2(){
    return head;
}

void clear2(){
    while(head)
    {
        node* tmp=head;
        head=head->next;
        delete tmp;
    }
}


int main(void)
{
    string str;
    cin>>str;

    stack<char> a;
    
    

    return 0;
}
