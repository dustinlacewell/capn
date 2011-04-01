from capn import configuration, default_type
from capn.paths import *

# capn's shell wrappers use eval to execute
# the python codepath. The handlers below
# simply use print to provide the commands
# specfified in the configuration directly
# to the shell

def hooks_for_path(path):
    return [hook for hook in configuration['hooks'] if hook['path'] == path]

def handle_exit_cwd(old):
    hooks = hooks_for_path(old)
    for hook in hooks:
        pathtype = hook.get('type', default_type)
        if pathtype == 'path':
            commands = hook.get('exit', [])
            for command in commands:
                command = command.format(old=old)
                print command

def handle_exit(old, new):
    # handle old path first
    handle_exit_cwd(old)
    # handle parents bottom-up
    parents = get_parents(old)
    parents.reverse()
    for hook in parents:
        path = hook['path']
        commands = hook.get('exit', [])
        if not path_in_path(path, new):
            for command in commands:
                command = command.format(old=old)
                print command

def handle_enter_cwd(old, new):
    hooks = hooks_for_path(new)
    for hook in hooks:
        pathtype = hook.get('type', default_type)
        if pathtype == 'path':
            commands = hook.get('enter', [])
            for command in commands:
                command = command.format(old=old, new=new)
                print command

def handle_enter(old, new):
    # handle parents top-down
    parents = get_parents(new)
    for hook in parents:
        path = hook['path']
        commands = hook.get('enter', [])
        if not path_in_path(path, old):
            for command in commands:
                command = command.format(old=old, new=new)
                print command
    # handle new path last
    handle_enter_cwd(old, new)


