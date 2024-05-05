from urllib.parse import quote,urlencode
from urllib import request
import string,json,traceback
postdict={}
postdict['file_path'] = '/mnt/sdb/nyz/nyz_flask/app/static/5.jpg'
# postdict['num2'] = 21
print(urlencode(postdict).encode(encoding='UTF8'))
req = request.Request('http://localhost:8018/predict?filename=/mnt/sdb/nyz/nyz_flask/app/static/5.jpg') # , data=urlencode(postdict).encode(encoding='UTF8')
jsondata = request.urlopen(req,timeout=10).read()
dict_str = json.loads(jsondata)
print(dict_str)