/*
cJSON API 函数封装
*/
#include "cJsonHead.h"

//读JSON文件，获取JSON结构体 
cJSON *FileToJsonObject(char *filename, cJSON *json)
{
    long len;
    char* pContent;
    int tmp;
    FILE* fp = fopen(filename, "rb+");
    if(!fp)
    {
        return NULL;
    }
    fseek(fp,0,SEEK_END);
    len=ftell(fp);
    if(0 == len)
    {
        return NULL;
    }

    fseek(fp,0,SEEK_SET);
    pContent = (char*) malloc (sizeof(char)*len);
    tmp = fread(pContent,1,len,fp);

    fclose(fp);
    json=cJSON_Parse(pContent);
    if (!json)
    {
        return NULL;
    }
    free(pContent);
    return json;
}

//JSON字符串转换为JSON结构体
static cJSON *StrToJsonObject(char *str)
{
    cJSON *json;

    if(str == NULL)
    {
        return NULL; 
    }
    json = cJSON_Parse(str);
//    if (!json) {return JSON_ERROR;}
//    else
        return json;
}


/*
//打印type的值
void PrintType(char *key,int type)
{
    switch(type)
    {
        case 0:
        case 1:
           ELOG(INFO,"Key[%s]对应的位置存放的是 bool 类型", key);
           break;
        case 2:
           ELOG(INFO,"Key[%s]对应的位置未存放数据", key);
           break;
        case 3:
           ELOG(INFO,"Key[%s]对应的位置存放的是 int 类型", key);
           break;
        case 4:
           ELOG(INFO,"Key[%s]对应的位置存放的是 char 类型", key);
           break;
    }

}
*/

/* 一层对象的json解析 */
int GetIntFromJson1(char *JsonStr, char *key, int *iNum)
{
    cJSON *root, *cJsonkey;

    root = StrToJsonObject(JsonStr);

    if(root)
    {
        cJsonkey = cJSON_GetObjectItem(root, key);
        if(NULL == cJsonkey)
        {
            cJSON_Delete(root);
            return KEY_ERROR;
        }
        if(cJsonkey->type == 3)
            *iNum = cJsonkey->valueint;
        else{
            cJSON_Delete(root);
            return FORMAT_ERROR;
            }
    }
    else
    {
        return ROOT_ERROR;
    }

    cJSON_Delete(root);
    return 0;
}

int GetDoubleFromJson1(char *JsonStr, char *key, double *DouNum)
{
    cJSON *root, *cJsonkey;

    root = StrToJsonObject(JsonStr);

    if(root)
    {
        cJsonkey = cJSON_GetObjectItem(root, key);
        if(NULL == cJsonkey)
        {
            cJSON_Delete(root);
            return KEY_ERROR;
        }
        if(cJsonkey->type == 3)
            *DouNum = cJsonkey->valuedouble;
        else{
            cJSON_Delete(root);
            return FORMAT_ERROR;
            }
    }
    else
    {
        return ROOT_ERROR;
    }

    cJSON_Delete(root);
    return 0;
}


int GetStrFromJson1(char *JsonStr, char *key, char *GetStr)
{
    cJSON *root, *cJsonkey;
    root = StrToJsonObject(JsonStr);

    if(root)
    {
        cJsonkey = cJSON_GetObjectItem(root, key);
        if(NULL == cJsonkey)
        {
            cJSON_Delete(root);
            return KEY_ERROR;
        }
        if(cJsonkey->type == 4)
        {
            strcpy(GetStr, cJsonkey->valuestring);
        }
        else{
            cJSON_Delete(root);
            return FORMAT_ERROR;
            }
    }
    else
    {
        return ROOT_ERROR;
    }
    cJSON_Delete(root);
    return 0;
}

int GetBoolFromJson1(char *JsonStr, char *key, int *GetBool)
{
    cJSON *root, *cJsonkey;

    root = StrToJsonObject(JsonStr);

    if(root)
    {
        cJsonkey = cJSON_GetObjectItem(root, key);
        if(NULL == cJsonkey)
        {
            cJSON_Delete(root);
            return KEY_ERROR;
        }
        if(cJsonkey->type == 0 || cJsonkey->type == 1)
            *GetBool = cJsonkey->valueint;
        else{
            cJSON_Delete(root);
            return FORMAT_ERROR;
            }
    }
    else
    {
        return ROOT_ERROR;
    }

    cJSON_Delete(root);
    return 0;

}

/*两层对象的json解析*/
int GetIntFromJson2(char *JsonStr, char *ObjectItem, char *key, int *iNum)
{
    cJSON *root, *cJsonItem, *cJsonkey;

    root = StrToJsonObject(JsonStr);

    if(root)
    {
        cJsonItem = cJSON_GetObjectItem(root, ObjectItem);
        if(cJsonItem)
        {
            cJsonkey = cJSON_GetObjectItem(cJsonItem, key);
            if(NULL == cJsonkey)
            {
                cJSON_Delete(root);
                return KEY_ERROR;
            }
            if(cJsonkey->type == 3)
                *iNum = cJsonkey->valueint;
            else{
                cJSON_Delete(root);
                return FORMAT_ERROR;
            }
        }
        else
        {
           cJSON_Delete(root);
           return OBJECT_ERROR;
        }

    }
    else
    {
        return ROOT_ERROR;
    }

    cJSON_Delete(root);
    return 0;
}

int GetDoubleFromJson2(char *JsonStr, char *ObjectItem, char *key, double *DouNum)
{
    cJSON *root, *cJsonItem, *cJsonkey;

    root = StrToJsonObject(JsonStr);

    if(root)
    {
        cJsonItem = cJSON_GetObjectItem(root, ObjectItem);
        if(cJsonItem)
        {
            cJsonkey = cJSON_GetObjectItem(cJsonItem, key);
            if(NULL == cJsonkey)
            {
                cJSON_Delete(root);
                return KEY_ERROR;
            }
            if(cJsonkey->type == 3)
                *DouNum = cJsonkey->valuedouble;
            else{
                cJSON_Delete(root);
                return FORMAT_ERROR;
            }
        }
        else
        {
           cJSON_Delete(root);
           return OBJECT_ERROR;
        }
    }
    else
    {
        return ROOT_ERROR;
    }

    cJSON_Delete(root);
    return 0;
}

int GetStrFromJson2(char *JsonStr, char *ObjectItem, char *key, char *GetStr)
{
    cJSON *root, *cJsonItem, *cJsonkey;

    root = StrToJsonObject(JsonStr);

    if(root)
    {
        cJsonItem = cJSON_GetObjectItem(root, ObjectItem);
        if(cJsonItem)
        {
            cJsonkey = cJSON_GetObjectItem(cJsonItem, key);
            if(NULL == cJsonkey)
            {
                cJSON_Delete(root);
                return KEY_ERROR;
            }
            if(cJsonkey->type == 4)
                strcpy(GetStr, cJsonkey->valuestring);
            else{
                cJSON_Delete(root);
                return FORMAT_ERROR;
            }
        }
        else
        {
           cJSON_Delete(root);
           return OBJECT_ERROR;
        }

    }
    else
    {
        return ROOT_ERROR;
    }

    cJSON_Delete(root);
    return 0;
}


int GetBoolFromJson2(char *JsonStr, char *ObjectItem, char *key, int *GetBool)
{
    cJSON *root, *cJsonItem, *cJsonkey;

    root = StrToJsonObject(JsonStr);

    if(root)
    {
        cJsonItem = cJSON_GetObjectItem(root, ObjectItem);
        if(cJsonItem)
        {
            cJsonkey = cJSON_GetObjectItem(cJsonItem, key);
            if(NULL == cJsonkey)
            {
                cJSON_Delete(root);
                return KEY_ERROR;
            }
            if(cJsonkey->type == 0 || cJsonkey->type == 1)
                *GetBool = cJsonkey->valueint;
            else{
                cJSON_Delete(root);
                return FORMAT_ERROR;
            }
        }
        else
        {
           cJSON_Delete(root);
           return OBJECT_ERROR;
        }

    }
    else
    {
        return ROOT_ERROR;
    }
    cJSON_Delete(root);
    return 0;
}
