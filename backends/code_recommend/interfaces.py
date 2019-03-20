from .inside_function import *

def search_result(conditions, license):
    '''

    :param conditions: 一个list，包含了搜索条件的所有词和它们的近义词
    :param license: 许可证
    :return:
        'valid': 有效的top10
        'invalid': 无效的top5
    '''

    #re_synopsis=[]
    #f=open('dict2.txt','r',encoding='utf-8')
    #a = f.read()
    #dict = eval(a)
    #for item in data_process(conditions):
        #re_synopsis.append(dict[item])
    valid = data_process(conditions)
    syn = conn_mongo(valid)
    retval = {
        'valid': valid,
        'invalid': [],
        'synopsis': syn,
    }
    return retval
def detail_search_result(conditions):
    return detail_conn_mongo(conditions)

def get_valid_license(input_license):
    if input_license == 'Mozilla  Public License 2.0':
        return['Mozilla  Public License 2.0', 'Apache License 2.0', 'BSD license', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'GNU General Public License':
        return['GNU General Public License', 'Apache License 2.0', 'BSD license', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'Apache License 2.0':
        return['Apache License 2.0''BSD license', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'BSD License':
        return['BSD License', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'GNU Lesser General Public License':
        return['BSD License', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'MIT License':
        return['MIT License']

