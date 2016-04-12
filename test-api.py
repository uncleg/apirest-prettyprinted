import urllib2
import json

"""
url="https://api.locu.com/v1_0/venue/search/?has_menu=false&locality=Buenos%20Aires&street_address=Rivadavia&api_key=12df9787a95a8a4173300b5fbd6e2900cdd88349"

json_obj = urllib2.urlopen(url)
data = json.load(json_obj)


print data
"""
data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
print 'DATA:', repr(data)

data_string = json.dumps(data)
print 'JSON:', data_string

decoded = json.loads(data_string)
print 'DECODED:', decoded
