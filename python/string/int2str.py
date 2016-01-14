#### str <=> int ####
int('3c16',16) # 15382

# int to 10-base string
str(15382) # '15382'

# int to hex string
hex(15382) # '0x3c16'

#### unicode/char <=> int
# unicode 65535 and char 256
chr(63) # '?'
unichr(23454) # u'\u5b9e' : 实
ord('?') # 63
ord(u'实') # 23454

#### unicode <=> ASCII #### 
# in python, str is ASCII, unicode is utf8
# every str is just byte char
a = '实' # '\xe5\xae\x9e'
type(a) # str
len(a) # 3
ua = a.decode('utf8') #  u'\u5b9e'
len(ua) # 1
type(ua) # unicode
a = ua.encode('utf8') # convert unicode to str (byte chars)

#### json dump as unicode ####
a = {}
a['a'] = u'实行'
json_str = json.dumps(a) # json will escapes all the utf code
# json_str =  '{"a": "\\u5b9e\\u884c"}'
json_str = json.dumps(a, ensure_ascii=False)
# json_str = {"a": "实行"}



