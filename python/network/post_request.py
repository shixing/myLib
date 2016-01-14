import urllib2

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
register_openers()

def upload_file(fileObj):
    # fileObj = open('1.mp3','rb')
    # return media_id
    access_token = Token.get_token()
    url = 'http://file.api.weixin.qq.com/cgi-bin/media/upload?access_token={}&type=voice'.format(access_token)
    datagen, headers = multipart_encode({"media": fileObj})
    request = urllib2.Request(url,datagen,headers)
    json_str = urllib2.urlopen(request).read()
    json_obj = json.loads(json_str)
    return json_obj['media_id']
