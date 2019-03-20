from pymongo import MongoClient

def get_dbconn(ip_address, uid, pwd):
    conn = MongoClient(ip_address, 27017)
    db_auth = conn.admin
    try:
        print(db_auth.authenticate(uid, pwd))
    except BaseException as e:
        print(e)
        return False
    else:
        return conn

# conn = get_dbconn('196.168.0.1', 'zyh', 'pwd')
# db = conn.python_dbs

def get_interface_info(name):
    content = name.split('.')
    col = db[content[0]]
    doc = col.find({'Name': name})
    if len(doc) != 0:
        return doc[0]
    else:
        return False


