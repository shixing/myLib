# Supported type : float,int,bool,string,numpy.float64
# Supported feature : '#' comments
#

import numpy 

def get_config(fn):
    config = {}
    f = open(fn)
    for line in f:
        if line.strip().startswith('#'):
            continue
        fields = line.strip().split('=')
        if len(fields)<3:
            continue

        t = fields[0]
        key = fields[1]
        value = fields[2]
        if t == 'i': #int
            config[key] = int(value)
        elif t== 'f': #float
            config[key] = float(value)
        elif t=='s': # string
            config[key] = value
        elif t=='b': # bool
            if value == 'True':
                config[key]= True
            elif value == 'False':
                config[key]=False
    return config


def write_config(config,fn):
    f = open(fn,'w')
    temp  = []
    for key in config:
        value = config[key]
        type_str = ''
        if type(value) == type(' '):
            type_str = 's'
        elif type(value) == type(1):
            type_str = 'i'
        elif type(value) == float or type(value) == numpy.float64:
            type_str = 'f'
        elif type(value) == type(True):
            type_str = 'b'
        value = str(value)
        temp.append([type_str,key,value])

    temp = ['='.join(x) for x in temp]
    temp = sorted(temp)
    temp_str = '\n'.join(temp)
    f.write(temp_str)
    f.close()

def demo():
    path = './train.config'
    config = get_config(path)
    write_config(config,path)

