import json
import os


def regist(username, pwd):
    retval = {
        'status': None,
        'username': None
    }

    f1 = open("./backends/account_file/account_info.txt", 'r')
    # f1 = open("../account_file/account_info.txt", 'r')
    acc_info = json.loads(f1.read())
    f1.close()
    '''
    检测是否有重复的账号
    '''
    for acc in acc_info:
        if acc['username'] == username:
            retval['status'] = False
            return retval
        else:
            continue
    retval['status'] = True
    retval['username'] = username
    '''
    将new user插入到数据库中
    '''
    newuser = {
        'username': username,
        'password': pwd
    }
    acc_info.append(newuser)

    f2 = open("./backends/account_file/account_info.txt", 'w')
    # f2 = open("../account_file/account_info.txt", 'w')
    f2.write(json.dumps(acc_info))
    print(acc_info)
    f3 = open("./backends/account_file/history/" + str(username) + ".txt", 'a')
    # f3 = open("../account_file/history/" + str(username) + ".txt", 'a')
    f3.close()
    return retval

def login(username, pwd):
    retval = {
        'status': None,
        'username': None
    }
    # print(os.path.abspath('.'))
    # print(os.getcwd())
    f1 = open("./backends/account_file/account_info.txt", 'r')
    # f1 = open("../account_file/account_info.txt", 'r')
    acc_info = json.loads(f1.read())
    f1.close()
    for i in acc_info:
        print(0)
        if(username == i['username']):
            if(pwd == i['password']):
                print(1)
                retval['status'] = True
                retval['username'] = username
            else:
                print(2)
                retval['status'] = False
                retval['username'] = username

    return retval


def get_his(username):
    f = open("./backends/account_file/history/" + str(username) + ".txt", 'r')
    history = []
    for i in f.readlines():
        history.append(i)
    f.close()
    return history

def his_storage(username, content):
    f = open("../../backends/account_file/history/" + str(username) + ".txt", 'r')
    history = []
    for i in f.readlines():
        history.append(i)
    f.close()
    history.append(str(content) + '\n')
    if(len(history) > 10):
        history.remove(history[0])
    f1 = open("../../backends/account_file/history/jyl1.txt", 'w')
    for i in history:
        f1.writelines(i)
    return True


if(__name__ == "__main__"):
    print(regist('zyhtest1', 'pwdzyh'))
