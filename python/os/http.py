import urllib
import urllib2

def main():
    # dict to urlencode
    fields = {}
    fields['key'] = 'AIzaSyADlrkxuZ47AGABAmqk8JsIHPkU_3WS4Wg'
    fields['format'] = 'text'
    fields['target'] = target
    fields['source'] = source
    fields['q'] = text
    query = urllib.urlencode(fields)
    url = 'https://www.googleapis.com/language/translate/v2?'+query
    # http GET
    json_str = urllib2.urlopen(url).read()
    