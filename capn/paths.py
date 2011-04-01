import os, operator

from capn import configuration, default_type

def path_in_path(parent, child):
    '''
    Example:
       parent - ~/projects
       child  - ~/projects/myproject/foo
    Would return True
    '''
    parent = parent
    child = child
    prefix = os.path.commonprefix([parent, child])
    return parent == prefix

def get_parents(child):
    '''
    Find all parents that are of type 'tree'
    '''
    parents = []
    # for all hooked paths
    for hook in configuration['hooks']:
        # get path's type or default
        path = hook['path']
        pathtype = hook.get('type', default_type)
        # append parent if type is tree
        if pathtype == 'tree' and path_in_path(path, child):
            parents.append(hook)
    parents.sort(key=operator.itemgetter('path'))
    return parents


