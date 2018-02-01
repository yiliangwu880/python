#find use enum def proto variable
#use method: change your search path in target_path.

import os,sys
import re

def FindFileByExt(base_path, extend_name):
    '''
    find file
    @para base_path  path name
    @para extend_name  file extend name, or file name
    ex FindFileByExt("E:/test/python/prj/protocol", ".proto")
    '''
    fileresult = []
    cur_list = os.listdir(base_path)
    for item in cur_list:
        full_path = os.path.join(base_path, item)
        if os.path.isdir(full_path):
            fileresult += FindFileByExt(full_path, extend_name)
        #if os.path:
        if full_path.endswith(extend_name):
            fileresult.append(full_path)
    return fileresult

def ReFile(path, regular_str):
    '''
    regular a file, return result list.
    '''
    re_file=open(path,'r')
    fileread=re_file.read()
    data=re.findall(regular_str,fileread)
    re_file.close()
    return data

def ReAllFile(base_path, extend_name, regular_str):
    '''
    regular all file in path
    @para base_path  path name
    @para extend_name  file extend name, or file name
    @return result list
    ex ReAllFile("E:/test/python/prj/protocol", ".proto", "fun.*abc")
    '''
    all_ret = []
    for file_path in FindFileByExt(base_path, extend_name):
        ret = ReFile(file_path, regular_str)
        for v in ret:
            all_ret.append(v)    
    return all_ret

def WriteFile(path, str):
    '''将字符串 写入文件'''

    f = file(path, 'w')
    f.write(str+"\n")
    f.close()

if __name__ == '__main__':
    target_path = "E:/test/python/prj"            
    r = ReAllFile(target_path, "txt", "EquipConfMgr.*")
    for result in r:
        print(result)
