from urllib2 import urlopen, urlparse
from urllib import urlencode

# Base URL being accessed
url = 'http://httpbin.org/get'

# Dicitonary of query parameters (if any)
parms = {
    'name1' : 'value1',
    'name2' : 'value2'
}

# Encode the query string
querystring = urlencode(parms)
# Make a GET request and read the response
u = urlopen(url+'?' + querystring)
resp = u.read()

print resp