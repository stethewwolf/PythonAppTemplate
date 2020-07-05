# PythonAppTemplate

## Introduction

Often happens that you have to implement a command line application very 
quickly, the following is an example of a base code.

## Template
In general, a command line application needs:

* a main in which to initialize all components
* a logger to be able to debug any problems
* a parser to interpret parameters from the command line
* a pattern to manage all the options you have in mind to implement

This template tries to answer all the previous points.

## Structure
Files present in the project

```
$ tree
.
├── app # this file contains the main of the application
├── app_modules
│ ├── commands
│ │ ├── commandline_parser.py # command line parser
│ │ ├── command.py # base class for handling commands
│ │ ├── __init__.py
│ │ ├── runner
│ │ │ ├── __init__.py
│ │ │ └── run_version.py # example of command that prints the version
│ │ └── setter
│ │ ├── __init__.py
│ │ ├── set_conf.py
│ │ └── set_env.py
│ ├── core
│ │ ├── config.py
│ │ ├── constants.py
│ │ ├── __init__.py
│ │ └── mlogger.py
│ └── __init__.py
├── build.sh
├── LICENSE
├── README.md
└── requirements.txt

5 directories, 18 files
```

## Class flow chart

During execution the application will follow the following steps:

1. the app class starts running and prepares the logger
2. the app class instantiates the commandline_parser class
3. the commandline_parser class initializes all commands
4. the commandline_parser class analyzes the arguments passed by line and builds
 the list of commands to be executed
5. the commandline_parse class returns the command list to the app class
6. the app class executes all the commands managing any exceptions

## Extend the template

To extend the template you will first need to enter the application specific 
codes into the `app_modules` folder, and then start creating the new commands.

Commands are distinguished in:

* setter: commands used to pass values ​​to the application

* runner: commands used to specify which action to perform

### Example of a new command

Suppose we want to create the `--say-hello option`, 
we will have to create the file:

`app_modules/commands/runner/sey_hello.py`

```
from app_modules.core import LoggerFactory
from app_modules.core import SingleConfig
from app_modules.core import AppConstants
from app_modules.commands.command import Command

class Say_hello (Command):
    short_arg = None
    long_arg = 'say-hello'
    cmd_help = 'print hello world'
    cmd_type = None
    cmd_action = 'store_true'

    def __init __ (self, param = None):
        super () .__ init __ ()
        self.logger = LoggerFactory.getLogger (str (self .__ class__))

    def run (self):
        print ('hello world')

```

then you need to update the file:

`app_modules/commands/runner/__init__.py`



```
__all__ = [
    'Run_version',
    'Say_hello'
    ]

# deprecated to keep older scripts who import this from breaking
from app_modules.commands.runner.run_version import Run_version
from app_modules.commands.runner.say_hello import Say_hello
```

At this point it is necessary to register the new command in the parser:

```
# file app_modules / commands / commandline_parser.py
# line 38

        self.rcl = [
            Run_version,
            Say_hello
            ]
```

Finally you can try the new command:

```
$ python app -h
usage: App [-h] [--version] [--say-hello] [--conf CONF]

A sample python app

optional arguments:
  -h, --help show this help message and exit
  --version, -V print version
  --say-hello print hello world
  --conf CONF, -c CONF pass to configuration file
 
$ python app --say-hello
hello world
```
