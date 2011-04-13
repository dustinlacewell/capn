capn
====

capn is a package that provides hooks when the current-working-directory changes.

### Installation

    $ sudo pip install capn
    $ touch ~/.capnhooks

### Configuration

capn uses a simple YAML file for specifying paths and their hooks. As a quick example, consider the following:


     settings:
       default_type: path
       external_hooks:
         - ~/.otherhooks
     hooks:
      - path: /home
        type: tree
        enter: 
          - echo entering /home
        exit: 
          - echo exiting /home
          - echo /home waves goodbye

      - path: ~/
        enter: 
          - echo entering ~/
        exit: 
          - echo exiting ~/

The above establish enter and exit hooks for the two listed directories. As you change directories you should see output indicating each hook's execution. You'll notice that the */home* path has a **type** key with the value **tree**. There are two types of hooks; **path**, which is the default, only triggers for that absolute path. **tree** hooks will trigger when you enter or leave the tree below the specified path. Moving between child-paths below the tree does _not_ trigger the hooks. For example, moving from */ -> /home* would trigger the *enter* hook. Moving from */home -> ~/* would not trigger the exit hook. 

Generally the commands specified in the hooks will be the names of shell scripts not single shell commands.

The first section of the configuration currently has two available settings:

* **default_type**: either **path** or **tree**. If setting is not specified, **path** will be used.
* **external_hooks**: a list of paths to other YAML files containing additional hooks. Such files should resemble the **'hooks'** section of the above example configuration.

### Usage

After installing capn you will need to source:

    $ source capn

If you no longer wish to have the hooks activated:

    $ unhook

### API

    add_external_hook(filename, path, hooktype=DEFAULT_TYPE, 
                      enter=[], exit=[]):


Currently capn has a minimal API with a single function that is used to manage programmatically generated external hook files. See the example below:

    >>>from capn.config import add_external_hook
    >>>filename = "~/.otherhooks"
    >>>path = ~/projects/foo/bar
    >>>hooktype = 'tree'
    >>>enter = ['source ~/projects/foo/bar/bin/activate']
    >>>exit = ['deactivate']
    >>>add_external_hook(filename, path, hooktype=hooktype,
    ...                  enter=enter, exit=exit)
    >>>

The above will add a hook to auto de/activate the python-virtualenv whenever the shell is inside the project directory to the file *"~/.otherhooks"*. You will then need to add the filename to the **external_hooks** list in the *"~/.capnhooks"* configuration file.