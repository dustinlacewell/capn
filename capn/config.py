import os

from yaml import load, dump
try:
    from yaml import CLoader as Loader
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from capn.util import expand

CONFIG_NAME = ".capnhooks"
DEFAULT_TYPE = 'path'
DEFAULT_CONFIG = {'settings':{'default_type': DEFAULT_TYPE}, 'hooks':[]}

def expand_config(config):
    for hook in config['hooks']:
        hook['path'] = expand(hook['path'])
    return config

def load_yaml(path):
    config_file = open(expand(path), 'r+')
    config = load(config_file, Loader=Loader)
    config_file.close()
    return expand_config(config)

def save_yaml(path, config):
    config = expand_config(config)
    config_file = open(expand(path), 'w')
    config_file.write(dump(config, default_flow_style=False))
    config_file.close()

def get_configuration():
    config = DEFAULT_CONFIG
    configpath = expand(os.path.join("~", CONFIG_NAME))
    if os.path.isfile(configpath):
        config.update(load_yaml(os.path.join("~", CONFIG_NAME)))
        external_configs = config['settings'].get('external_hooks', [])
        for conf in external_configs:
            if os.path.isfile(expand(conf)):
                config['hooks'].extend(load_yaml(conf)['hooks'])
    return config

def add_external_hook(filename, path, hooktype=DEFAULT_TYPE, 
                      enter=[], exit=[], unique=False):
    '''
    Will add an external hook to the YAML specfified
    YAML file.
    '''
    if os.path.isfile(expand(filename)):
        config = load_yaml(filename)
    else:
        config = {'hooks': []}
    if unique:
        removed = []
        for hook in config['hooks']:
            if hook['path'] == path:
                removed.append(hook)
        for hook in removed:
            config['hooks'].remove(hook)
    hook = {'path': path, 'type': hooktype}
    if enter:
        hook['enter'] = enter
    if exit:
        hook['exit'] = exit
    config['hooks'].append(hook)
    save_yaml(filename, config)

def remove_external_hook(filename, path):
    '''
    Removes all hooks for a given path.
    '''
    if os.path.isfile(expand(filename)):
        config = load_yaml(filename)
        config['hooks'] = [h for h in config['hooks'] if h['path'] != path]
        save_yaml(filename, config)
        
        
        

        
