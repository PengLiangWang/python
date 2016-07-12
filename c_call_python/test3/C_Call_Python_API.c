#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "python2.6/Python.h"
#include "cJsonHead.h"

#define SQLNOTFOUND 1
#define DATABASEERROR -1
#define TTS_SUCCESS 0 

void getcurrent()
{
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append('./')");
    return;
}

/*
PyObject* BusinessDataBaseOpen()
{
    PyObject *connt=NULL;
    Py_Initialize();
    if(!Py_IsInitialized())
    {
        printf("初始化失败");
    }
    getcurrent();
    PyObject *pModule=NULL, *pFunction=NULL, *pFun=NULL;
    pModule = PyImport_ImportModule("py_oracle_connect");
    pFunction = PyObject_GetAttrString(pModule, "DB_connect");
    connt = PyEval_CallObject(pFunction, NULL);
    printf("connt: %d\n", connt->ob_refcnt);
    Py_Finalize();
    return connt;
}

int BusinessDataBaseClose(PyObject *conn)
{
    printf("conn->ob_refcnt: %d\n", conn->ob_refcnt);
    Py_Initialize();
    if(!Py_IsInitialized())
    {
        printf("初始化失败");
        return -1;
    }
    getcurrent();
    PyObject *pModule=NULL,*pFunction=NULL, *pArg=NULL;
    pModule = PyImport_ImportModule("py_oracle_connect");
    pFunction = PyObject_GetAttrString(pModule, "DB_close");
    PyEval_CallObject(pFunction, conn);
    Py_Finalize();
    return 0;
}
*/

int DB_Read_PayJnls_By_LocalDate_LocalLogNo(char *localdate, char *locallogno, char *JsonStr)
{
    Py_Initialize();
    if(!Py_IsInitialized())
    {
        printf("初始化失败");
        return -1;
    }
    getcurrent();
    PyObject *pModule=NULL, *pArg=NULL, *pFunction=NULL, *result = NULL;
    pModule = PyImport_ImportModule("py_oracle_read");
    pFunction = PyObject_GetAttrString(pModule, "DB_connect");
    pArg = Py_BuildValue("(ss)",localdate, locallogno); 
    result =  PyEval_CallObject(pFunction, pArg);
    char  *str = NULL;
    PyArg_Parse(result, "s", &str);
    strcpy(JsonStr, str);
    Py_Finalize();
    if(strcmp(JsonStr, "NoneSQL") == 0)
        return SQLNOTFOUND;
    else if(strcmp(JsonStr, "DatabaseError") == 0)
        return DATABASEERROR;
    else
        return TTS_SUCCESS;
}

int main()
{
    int res;
    char json[1024]={'\0'}, date[10]={'\0'};

/*
    PyObject *connt=NULL;
    connt = BusinessDataBaseOpen();
    printf("connt->ob_refcnt: %d\n", connt->ob_refcnt);

    BusinessDataBaseClose(connt);
*/

    res = DB_Read_PayJnls_By_LocalDate_LocalLogNo("20150211", "F15332", json); 
    if(res != TTS_SUCCESS && res != SQLNOTFOUND)
    {
        printf("Read 表 PayJnls 失败, ERR: %d\n", res);
        return res;
    }
    if(res == SQLNOTFOUND)
    {
        printf("未查到任何数据\n");
        return res;
    }

    printf("json: %s\n", json);

    GetStrFromJson1(json, "localdate", date);
    printf("localdate: %s\n", date); 
   
    return 0;

}
