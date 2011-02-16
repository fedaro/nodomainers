from ConfigParser import RawConfigParser
import pdb

try:
    configParser = RawConfigParser()
    configParser.read('tools.cfg')
    TWITTER_URL = configParser.get('twitter', 'url')
    TWITTER_Q_VAR = configParser.get('twitter', 'query_var')
    TWITTER_QUERY = configParser.get('twitter', 'query')
    TWITTER_OFFSET = configParser.get('twitter', 'offset') 

except Exception, x:
    print "Unhandled Exception: " + str(x)
    TWITTER_URL = None
    print "Could not find twitter URL, ignoring."

