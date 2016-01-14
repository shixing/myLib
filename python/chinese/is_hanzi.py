def is_hanzi(n):
  return (0x3400 <= n and n <= 0x9fff) or (0xf900 <= n and n <= 0xfaff)

def demo():
  a = u'实'
  n = ord(a)
  is_hanzi(n) # True
  a = '实'
  ua = a.decode('utf8')
  n = ord(ua)
  is_hanzi(n) # True