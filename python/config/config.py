import configparser

def demo():
    config_fn = './train.cfg'
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read(config_fn)
    
    # get str
    # get(session_name,field_name)
    config.get('path','reference')
    
    # get int
    config.getint('decoding','nthread')
    
    # set value
    # set(session_name,field_name,value_str)
    # value should always be strings
    weight = 0.4
    config.set('weights','wlm',str(weight))
