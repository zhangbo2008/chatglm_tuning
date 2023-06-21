#include<stdio.h>

int get_num(int);

/*
返回值为函数指针的函数：
  1.先看 (*get_fun()) ，可知它是一个函数，
函数名为get_fun,没有参数，返回值是一个指针，
该指针指向什么类型的数据呢？
  2.去掉函数名部分，剩下的部分：int (*)(int)，
容易看出它就是一个函数指针，该指针指向的函数：
有一个int型参数，返回值为int型
*/
int (*get_fun())(int);  

int (*get_fun())(int){
    return get_num;
}
int get_num(int num){
    return num;
}

int main(){
    int (*fp)(int)=get_fun();
    printf("get num is : %d\n",fp(2));
    return 0;
}