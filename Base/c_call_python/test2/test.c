#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "python2.6/Python.h"

void getcurrent()
{
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");
    return;
}

void test1()
{
    Py_Initialize();//初始化python
    PyRun_SimpleString("print 'hello python'");//直接运行python代码
    Py_Finalize(); //释放python
    return;
}

void test2()
{
    Py_Initialize(); 
    if(!Py_IsInitialized())
    {
        printf("初始化失败");
        return;
    }
    getcurrent();

    PyObject *pModule = NULL, *pFunc = NULL, *pArg = NULL;  
    pModule = PyImport_ImportModule("demo"); 
    pFunc = PyObject_GetAttrString(pModule, "print_arg"); //参数类型转换，传递一个字符串。将c/c++类型的字符串转换为python类型 
    pArg = Py_BuildValue("(s)", "hello_python");   //调用直接获得的函数， 并传递参数
    PyEval_CallObject(pFunc, pArg); 
    Py_Finalize();
    return;
}

void test3()
{
    Py_Initialize(); 
    if(!Py_IsInitialized())
    {
        printf("初始化失败");
        return;
    }
    getcurrent();

    PyObject *pModule=NULL, *pDict=NULL, *pClass=NULL, *pInstance=NULL, *result=NULL;
    pModule = PyImport_ImportModule("demo");

    pDict = PyModule_GetDict(pModule);  //获取模块字典属性
    pClass = PyDict_GetItemString(pDict, "Class_A");   //通过字典属性获取模块中的类
    pInstance = PyInstance_New(pClass, NULL, NULL);   //对获取的类进行实例化
    result = PyObject_CallMethod(pInstance, "fun", "(s)", "python_000");   //调用类的方法
    char *name=NULL;
    PyArg_Parse(result, "s", &name);   //将python类型的返回值转换为c/c++类型
    printf("%s\n", name);
    Py_Finalize();
    
    return;
}

void test4()
{
    Py_Initialize();
    if(!Py_IsInitialized())
    {
        printf("初始化失败");
        return;
    }
    getcurrent();

    PyObject *pModule=NULL, *pDict=NULL, *pClass=NULL, *pInstance=NULL, *result=NULL;
    pModule = PyImport_ImportModule("demo");

    pDict = PyModule_GetDict(pModule);
    pClass = PyDict_GetItemString(pDict, "dedecms_get_webshell");
    pInstance = PyInstance_New(pClass, NULL, NULL);
    result = PyObject_CallMethod(pInstance, "check", "(s,i)", "www.baidu.com", 80);
    
    int flag;
    char *content = NULL;
    PyObject *obj_content = PyDict_GetItemString(result, "content");
    content = PyString_AsString(obj_content);

    PyObject *obj_flag = PyDict_GetItemString(result, "flag");
    flag = PyInt_AsLong(obj_flag);
    
    printf("content: %s,  flag: %d\n", content, flag);
   
    Py_Finalize();
}

int main(int argc, char *argv[])
{
    test1();
    test2();
    test3();     //调用模块中的一个类
    test4();
    return 0;  
}
