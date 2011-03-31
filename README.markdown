capn
====

capn is a package that provides hooks when the current-working-directory changes.

### Installation

    $ sudo python setup.py install
    $ touch ~/.capnhooks

### Configuration

capn uses a simple YAML file for specifying paths and their hooks. As a quick example, consider the following:


     settings:
       default_type: path
       /:
         enter: echo hello from /
         exit: goodbye from /
      /home:
         enter: echo hello from /home
         exit: goodbye from /home
      ~/:
         type: tree
         enter: echo hello from ~/
         exit: echo goodbye from ~/

The above establishes enter and exit hooks for the listed directories. As you change directories you should see messages output indicating each hook executing. You'll notice that the last entry for the user's home directory has an extra attribute called **type** with a value of **tree**. Currently there are two path types, **tree** and **path**. **path** hooks only execute for that single directory, **tree** hooks execute anytime you leave the entire tree below the specificed path. For example traversing from ~/ to ~/projects would not invoke either hooks.

### Usage

After installing capn you will need to source:

    $ source capn

If you no longer wish to have the hooks activated:

    $ unhook

Generally the commands specified in the hooks will be the names of shell scripts not single shell commands.