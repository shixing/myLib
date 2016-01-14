import os,sys

def demo():
    # list folder
    l = os.listdir('./') # will list every file and folder in ./
    # path concatenate
    new_path = os.path.join('./','text.py')
    # check whether dir or file
    os.path.isdir('./') # True
    os.path.isfile('./text.py') # True
    #get the file name from a path
    os.path.basename('./shixing/123.txt') # 123.txt
    # get the file name and deepest folder from a path
    os.path.split('./shixing/dingna/123.txt') # ['./shixing/dingna/','123.txt'] 
    