import json


def get_valid_license(input_license):
    if input_license == 'Mozilla  Public License 2.0':
        return['Mozilla  Public License 2.0', 'Apache License 2.0', 'BSD license', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'GNU General Public License':
        return['GNU General Public License', 'Apache License 2.0', 'BSD license', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'Apache License 2.0':
        return['Apache License 2.0', 'BSD license', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'BSD License':
        return['BSD License', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'GNU Lesser General Public License':
        return['BSD License', 'GNU Lesser General Public License', 'MIT License']
    elif input_license == 'MIT License':
        return['MIT License']
    elif input_license == 'None':
        return['Mozilla  Public License 2.0', 'Apache License 2.0', 'BSD license', 'GNU Lesser General Public License',
               'MIT License', 'GNU General Public License', 'PSF License']



license_info = open('E:/srtp/CodeRe/backends/license_info/pkg_license.txt', 'r').read()
# license_info = open('./pkg_license.txt', 'r')

def get_pkg_license(pkg_name):
    li = json.loads(license_info)
    return li[pkg_name]


if __name__ == '__main__':
    print(get_pkg_license('nltk'))
