import urllib
import urllib2

def calculate(calc):
    data = {}
    data["c"] = calc
    urlencoded = urllib.urlencode(data)
    response = urllib2.urlopen('https://www.calcatraz.com/calculator/api?' + urlencoded)
    result = response.read()

    return result
