# Author : stefano prina 
#
# MIT License
# 
# Copyright (c) 2019 Stefano Prina
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

class APP :
    NAME            = "App",
    DESCRIPTION     = "A sample python app"
    VERSION         = "0.0.0"


class COMMANDS:
    class CMD:
        SHORT_ARG   = None
        LONG_ARG    = None
        HELP        = "this is a command"
        TYPE        = None
        ACTION      = 'store_true'


    class RUN_VERSION:
        SHORT_ARG   = "V"
        LONG_ARG    = "version"
        HELP        = "print the version"
        TYPE        = None
        ACTION      = 'store_true'


    class SET_DB:
        SHORT_ARG   = "c"
        LONG_ARG    = "conf"
        HELP        = "pass a configuration file"
        TYPE        = str
        ACTION      = None


    class SET_ENV:
        SHORT_ARG   = None
        LONG_ARG    = None
        HELP        = None
        TYPE        = None
        ACTION      = None



