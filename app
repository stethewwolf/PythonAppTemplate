#!/usr/bin/env python3
#
# Author : stefano prina <stethewwolf@null.net>  stefano-prina@outlook.it
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
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#   
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

from app_modules.commands import CommandLine_Parser
from app_modules.core import LoggerFactory

if __name__ == "__main__":
    # setup logging service
    logger = LoggerFactory.getLogger('app')

    # the app starts
    logger.debug('app start')

    clp = CommandLine_Parser()

    command_list = clp.parse()

    logger.debug('start run commands')
    for cmd in command_list :
        logger.debug('running command ' + str(cmd.__class__) )
        cmd.run()
    
    # the app ends
    logger.debug('app end')
