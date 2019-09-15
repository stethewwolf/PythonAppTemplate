# Author : stefano prina 
#
# MIT License
# 
# Copyright (c) 2017 Stefano Prina <stethewwolf@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without sestriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
#     The above copyright notice and this permission notice shall be included in all
#     copies or substantial portions of the Software.
# 
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#     FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#     AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#     OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#     SOFTWARE.

import configparser, os

__instance = None

def getConfig():
    __APP_HOME = '.app'
    __CONF_FILE = 'conf.ini'
    __DATA_FILE = 'data.sqlite3'
    __DB_CREATE_TABLE_APP = 'CREATE TABLE `app` ( `id` INTEGER PRIMARY KEY AUTOINCREMENT, `data` INTEGER UNIQUE, `example` TEXT )'
    global __instance

    if not __instance :
        __instance = configparser.ConfigParser()
        __instance['private'] = {
                'home' : os.path.join( os.environ['HOME'], __APP_HOME),
                'conf' : os.path.join( os.environ['HOME'], __APP_HOME, __CONF_FILE ),
                'data' : os.path.join( os.environ['HOME'], __APP_HOME, __DATA_FILE ),
                'db_create_table_app' : __DB_CREATE_TABLE_APP ,
            }  

        if os.path.exists(
            __instance['private']['conf'] 
        ) :
            __instance.read( __instance['private']['conf'] )
    return __instance

def loadConfig( path ):
    global __instance
    if not __instance:
        getConfig()

    __instance.read( path )


def save( cfg ):
    with open( cfg['private']['conf'], 'w') as file:
        cfg.write(file)
