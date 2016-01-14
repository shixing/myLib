import subprocess as sp

def demo():
  cmd = "carmel -sliOk 20 eword-epron3.fst epron-pinyin-reg.fst.trained pinyin-reg-pinyin.fst"
  carmel = sp.Popen(cmd.split(),stdout=sp.PIPE,stdin=sp.PIPE)
  cmd = ["echo",'"'+word+'"']
  echo =sp.Popen(cmd,stdout=sp.PIPE)
  echoout,echoerr = echo.communicate()
  output,err = carmel.communicate(input=echoout)
  
  #directly call a command
  sp.call(["ls", "-l"])