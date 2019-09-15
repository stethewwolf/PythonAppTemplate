#  Author : stefano prina <stethewwolf@gmail.com>
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

from app_modules.core import LoggerFactory
from app_modules.core import SingleConfig
from app_modules.core import AppConstants
from app_modules.commands.command import Command

class RunVersion ( Command ):
    short_arg   = AppConstants.COMMANDS.RUN_VERSION.SHORT_ARG
    long_arg    = AppConstants.COMMANDS.RUN_VERSION.LONG_ARG
    cmd_help    = AppConstants.COMMANDS.RUN_VERSION.HELP
    cmd_type    = AppConstants.COMMANDS.RUN_VERSION.TYPE
    cmd_action  = AppConstants.COMMANDS.RUN_VERSION.ACTION

    def __init__( self, param = None ):
        super().__init__()
        self.logger = LoggerFactory.getLogger( str( self.__class__ ))

    def run( self ):
        print(AppConstants.APP.NAME, " - ", AppConstants.APP.VERSION)
