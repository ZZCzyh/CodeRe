from backends.rawcri_preprocess.interfaces import preprocess
import backends.personal_info.interfaces as pi
import backends.code_recommend.interfaces as cr
import backends.license_info.interface as li

def get_search_result(scriteria, license):

    '''
    :param scriteria: the search criteria
    :return: An HTTP response
    '''
    conditions = preprocess(scriteria)
    search_result = cr.search_result(conditions, license)
    search_result_dict = []
    valid_license = li.get_valid_license(license)
    print('valid: ' + str(valid_license))
    for i in range(len(search_result['valid'])):
        the_name = search_result['valid'][i]
        the_license = li.get_pkg_license(the_name.split('.')[0])
        the_flag = False
        the_synopsis = search_result['synopsis'][i]
        if str(the_license) in valid_license:
            the_flag = True
        search_result_dict.append(
            {
                'name': the_name,
                'license': the_license,
                'valid': the_flag,
                'synopsis': the_synopsis
            }
        )
    print(search_result_dict)
    '''
    search_result_dict是更新后的返回值 结构如下：
    [{
	'name': 'matplotlib.pyplot.cm.ScalarMappable.get_array',
	'license': 'matplotlib',
	'valid': False,
	'synopsis': 'Return the array'
	}, 
	{
	'name': 'numpy.linalg.tests.test_deprecations.np.matrixlib.defmatrix.N.arrayprint.np.full_like',
	'license': 'numpy',
	'valid': False,
	'synopsis': 'Return a full array with the same shape and type as a given array.'
	}]
    '''
    search_result_json={
        're':search_result_dict
    }
    return search_result_json

def get_detail_result(name):
    '''

    :param name: 具体接口的名称
    :return: 接口详细信息
    '''
    result=cr.detail_conn_mongo(name)
    return result
def regist(username, password):
    return pi.regist(username, password)

def login(username, password):
    return pi.login(username, password)

