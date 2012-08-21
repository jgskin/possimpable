"""module to handle twitter data"""

import urllib, urllib2, json

class Twit:
    """A single twit entry"""

    def __init__(self, content, lat, long):
        """init the required values"""

        self.lat = lat
        self.long = long
        self.content = content

def search_twits(lat, long, radius):
    """Find twits by region"""

    #configure the parameters
    params = {"geocode": ",".join([lat, long, radius])}

    #do the search and save return
    search_return = json.load(urllib2.urlopen("http://search.twitter.com/search.json?" + urllib.urlencode(params)))

    return [Twit(result["text"], lat, long) for result in search_return["results"]]